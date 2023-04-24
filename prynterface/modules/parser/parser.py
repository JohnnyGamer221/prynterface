from time import time
from dataclasses import dataclass
from ..configuration.parsing import ParsingConfig
from .helpers import (
    LineWithInfo,
    MatchWithLineInfo,
    MatchWithExtractedData,
    MatchWithConvertedData,
    convert_to_value,
    ParsedData,
)
from .matcher import Detector, Extractor


class Converter:
    """
    @todo A dict of functions would probably be better than this.
    All different cutsom data types in one file and conversion functions for all of them.
    Then we could have one function that takes a string and a type and returns the converted value.
    -> split helper.py into multiple files
    -> move all conversion functions to a new file
    -> create a dict of functions
    -> create a function that takes a string and a type and returns the converted value
    -> use it in here
    -> profit
    """

    def __init__(self, parser_config: dict) -> None:
        self.config = parser_config

    def convert(self, data: dict, key: str) -> dict:
        # print(data, key)
        # print(self.config[key])
        converted_data = {}
        for name, value in data.items():
            valuetype = self.config[key]["types"][name]
            print(valuetype)
            if valuetype == "value":
                converted_data[name] = convert_to_value(key, value)
            elif valuetype == "int":
                converted_data[name] = int(value)
            elif valuetype == "float":
                converted_data[name] = float(value)
        return converted_data


class Parser:
    """
    @todo Docstrings, tests, error handling,
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
        self.parser_output = []

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
            self.detector_output.remove(match)

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
            self.extractor_output.remove(match)

    def compress(self) -> None:
        for match in self.converter_output:
            parsed = ParsedData(
                name=match.key_name,
                data=match.converted_data,
                timestamp=match.lines[0].rcv_time,
                start=match.start_index,
                end=match.end_index,
            )
            self.parser_output.append(parsed)
            self.converter_output.remove(match)

    def parse(self) -> list[ParsedData]:
        self.detect()
        self.extract()
        self.convert()
        self.compress()
        return self.parser_output
