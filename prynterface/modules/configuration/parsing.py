from .base import ConfigParser


class ParsingConfig(ConfigParser):
    """Handles the config for the parser module.
    Config must have the following structure:
    {
        "identifier": {
            "detector": {...},
            "extractor": {...},
            "parser": {...}
        }
    }
    """

    # @todo add tests
    # tests for init, parser_config, detector_config, extractor_config

    # @todo Add input validation
    def __init__(self) -> None:
        super().__init__(config_fn="parsing.json")
        self.parser_cfg = {}
        self.detector_cfg = {}
        self.extractor_cfg = {}
        for key in self.config:
            self.parser_cfg[key] = self.config[key]["parser"]
            self.detector_cfg[key] = self.config[key]["detector"]
            self.extractor_cfg[key] = self.config[key]["extractor"]

    def parser(self) -> dict:
        return self.parser_cfg

    def detector(self) -> dict:
        return self.detector_cfg

    def extractor(self) -> dict:
        return self.extractor_cfg
