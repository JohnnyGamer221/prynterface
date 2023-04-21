from ..configuration.parsing import ParsingConfig
from .matcher import Detector, Extractor

# @todo Parser and Controller classes [implement][tests]
#       - Controller is responsible for configuring and moving data between detector, extractor and parser
#       - Parser is responsible for returning a dict of named values from the match groups extracted by the extractor


class ParserHelper:
    def __init__(self, parser_config: dict) -> None:
        pass


class Parser:
    def __init__(self, configuration: ParsingConfig) -> None:
        self.CONFIG = configuration
        self.detector = Detector(self.CONFIG.detector_config())
        self.extractor = Extractor(self.CONFIG.extractor_config())
        self.parser = ParserHelper(self.CONFIG.parser_config())
