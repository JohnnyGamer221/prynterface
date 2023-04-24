from time import time
from dataclasses import dataclass
from ..configuration.parsing import ParsingConfig
from .helpers import LineWithInfo
from .matcher import Detector, Extractor


@dataclass
class MatchWithLineInfo:
    matched_string: str
    start_index: int
    end_index: int
    key_name: str
    lines: list[LineWithInfo]


@dataclass
class MatchWithExtractedData:
    matched_string: str
    start_index: int
    end_index: int
    key_name: str
    lines: list[LineWithInfo]
    extracted_data: dict


@dataclass
class MatchWithConvertedData:
    matched_string: str
    start_index: int
    end_index: int
    key_name: str
    lines: list[LineWithInfo]
    extracted_data: dict
    converted_data: dict


class Converter:
    """
    @todo Implement Parser Helper class
    - converts regex match groups to dict
    - data types and annotations etc are defined in config
    - return parsed data to Parser Controller
    """

    def __init__(self, parser_config: dict) -> None:
        self.config = parser_config

    def convert(self, data: dict, key: str) -> dict:
        pass


class Parser:
    """
    @todo Implement Parser Controller class
    - set up detector, extractor, parser
    - manage pipeline
    - return parsed data to UI Controller
    """

    def __init__(self, configuration: ParsingConfig) -> None:
        self._config = configuration
        self._linebuffer = []
        self._detector = Detector(self._config.detectorcfg())
        self.detector_output = []
        self._extractor = Extractor(self._config.extractorcfg())
        self.extractor_output = []
        self._converter = Converter(self._config.parsercfg())
        self.converter_output = []
        self._total_lines = 0
        self._total_chars = 0

    def add_line(self, line: bytes) -> None:
        linewinfo = LineWithInfo(
            line,
            self._total_lines,
            time(),
            self._total_chars,
            self._total_chars + len(line),
        )
        self._linebuffer.append(linewinfo)
        self._total_lines += 1
        self._total_chars += len(line)

    def detect(self) -> None:
        constructed_string = "".join([line.line.decode() for line in self._linebuffer])
        self._detector.set_data(constructed_string)
        matches = self._detector.get_matches()
        for m in matches:
            match_start = m.start_index + self._linebuffer[0].start_str_index
            match_end = m.end_index + self._linebuffer[0].start_str_index
            match_with_line_info = MatchWithLineInfo(
                m.matched_string, m.start_index, m.end_index, m.key_name, []
            )
            for line in self._linebuffer:
                if line.start_str_index >= match_start:
                    match_with_line_info.lines.append(line)
                    self._linebuffer.remove(line)
                if line.end_str_index >= match_end:
                    break
            self.detector_output.append(match_with_line_info)

    def extract(self) -> None:
        for match in self.detector_output:
            extracted_data = self._extractor.extract(
                match.matched_string, match.key_name
            )
            match_with_extracted_data = MatchWithExtractedData(
                match.matched_string,
                match.start_index,
                match.end_index,
                match.key_name,
                match.lines,
                extracted_data,
            )
            self.extractor_output.append(match_with_extracted_data)

    def convert(self) -> None:
        for match in self.extractor_output:
            converted_data = self._converter.convert(
                match.extracted_data, match.key_name
            )
            match_with_converted_data = MatchWithConvertedData(
                match.matched_string,
                match.start_index,
                match.end_index,
                match.key_name,
                match.lines,
                match.extracted_data,
                converted_data,
            )
            self.converter_output.append(match_with_converted_data)

    def parse(self) -> None:
        self.detect()
        self.extract()
        self.convert()


if __name__ == "__main__":
    pass
