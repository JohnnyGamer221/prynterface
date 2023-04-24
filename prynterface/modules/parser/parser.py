from time import time
from ..configuration.parsing import ParsingConfig
from .helpers import LineWithInfo
from .matcher import Detector, Extractor


class Converter:
    """
    @todo Implement Parser Helper class
    - converts regex match groups to dict
    - data types and annotations etc are defined in config
    - return parsed data to Parser Controller
    """

    def __init__(self, parser_config: dict) -> None:
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
        self._detector = Detector(self._config.detectorcfg())
        self._extractor = Extractor(self._config.extractorcfg())
        self._converter = Converter(self._config.parsercfg())
        self._linebuffer = []
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

    def parse(self) -> None:
        constructed_string = "".join([line.line.decode() for line in self._linebuffer])
        self._detector.set_data(constructed_string)
        matches = self._detector.get_matches()
        print(matches)


if __name__ == "__main__":
    pass
