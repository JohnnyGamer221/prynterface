from ..configuration.parsing import ParsingConfig
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
        self.config = configuration
        self.detector = Detector(self.config.detectorcfg())
        self.extractor = Extractor(self.config.extractorcfg())
        self.parser = Converter(self.config.parsercfg())
