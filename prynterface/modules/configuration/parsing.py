from .base import ConfigParser


class Config(ConfigParser):
    """Handles the config for the parser module.
    Config must have the following structure:
    {
        "identifier": {
            "detector": {},
            "extractor": {},
            "parser": {}
        }
    }
    """

    # @todo add tests
    # tests for init, parser_config, detector_config, extractor_config

    # @todo Add input validation
    def __init__(self) -> None:
        super().__init__(config_fn="parsing.json")
        self.parser = {}
        self.detector = {}
        self.extractor = {}
        for key in self.config:
            self.parser[key] = self.config[key]["parser"]
            self.detector[key] = self.config[key]["detector"]
            self.extractor[key] = self.config[key]["extractor"]

    def parser_config(self) -> dict:
        return self.parser

    def detector_config(self) -> dict:
        return self.detector

    def extractor_config(self) -> dict:
        return self.extractor
