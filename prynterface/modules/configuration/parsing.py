from typing import Union
from base import ConfigParser


class ParsingConfig(ConfigParser):
    """Handles the config for the parser module.
    Config must have the following structure:
    {
        "value name 1": {
            "preprocessor": "true" | "false",
            "pipeline plugin 1": {...},
            ...,
            "pipeline plugin n": {...}
        },
        ...,
        "value name n": {...}
    }
    """

    # @todo add tests
    # tests for init

    # @todo Add input validation
    def __init__(
        self,
        config_fn: Union[str, None] = "parsing.json",
        config_dir: Union[str, None] = "prynterface/config",
    ) -> None:
        super().__init__(config_fn, config_dir)
