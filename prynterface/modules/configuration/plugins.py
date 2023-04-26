from typing import Union
from base import ConfigParser


class PluginConfig(ConfigParser):
    """Handles the config for the plugin module.
    Config must have the following structure:
    {
        "module 1": {
            "plugin 1": {
                "enabled": true | false,
                "settings": {...} (optional)
            },
            ...
            "plugin n": {...}
        },
        ...
        "module n": {...}
    }
    With "module" being the name of the module the plugin belongs to
    and "plugin" being the name of the plugin.
    "settings" is an optional dict containing the settings for the plugin.
    """

    # @todo add tests
    # tests for init and valid config

    # @todo Add input validation
    def __init__(
        self,
        config_fn: Union[str, None] = "plugins.json",
        config_dir: Union[str, None] = "prynterface/config",
    ) -> None:
        super().__init__(config_fn, config_dir)
        self.plugins = {}
        for module, plugin_config in self.config.items():
            plugin_config = [
                plugin
                for plugin, config in plugin_config.items()
                if config["enabled"] == True
            ]
            if len(plugin_config) > 0:
                self.plugins[module] = plugin_config
