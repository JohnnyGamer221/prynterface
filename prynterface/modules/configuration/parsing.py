from typing import Union
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
    def __init__(
        self,
        config_fn: Union[str, None] = "parsing.json",
        config_dir: Union[str, None] = "prynterface/config",
    ) -> None:
        self.parser_config = {}
        self.detector_cfg = {}
        self.extractor_cfg = {}
        super().__init__(config_fn, config_dir)
        for key in self.config:
            self.parser_config[key] = self.config[key]["parser"]
            self.detector_cfg[key] = self.config[key]["detector"]
            self.extractor_cfg[key] = self.config[key]["extractor"]

    def parsercfg(self) -> dict:
        return self.parser_config

    def detectorcfg(self) -> dict:
        return self.detector_cfg

    def extractorcfg(self) -> dict:
        return self.extractor_cfg
