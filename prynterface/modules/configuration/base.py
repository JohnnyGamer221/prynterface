import json
import os
from typing import Union

# Path: prynterface/src/parser/parseconfig.py
# Config: prynterface/config/default/{config_fn}.json as default
#         prynterface/config/{config_fn}.json if it exists

# Path to the config directory relative to the root of the project.
DEFAULT_CONFIG_DIR = "prynterface/config"


class UninitializedConfigException(Exception):
    """Raised when a config file is not loaded."""

    pass


def json_regex_decode(string: str):
    """Decode a regex string from json.
    The json library encodes regex strings with double backslashes.
    This function replaces the double backslashes with single backslashes.
    """
    decoded = string.replace("\\\\", "\\")
    # convert to raw string
    return r"{}".format(decoded)


def fix_double_backslash(json_data: dict) -> dict:
    """Traverses a dict of arbitrary many dicts and fixs the double backslash
    For whatever reason the default json library reads a double backslash
    as two backslashes which is *** because it needs to be escaped to be valid json.
    """
    for k, v in json_data.items():
        if isinstance(json_data[k], dict):
            json_data[k] = fix_double_backslash(json_data[k])
        elif k == "expression" and isinstance(json_data[k], str):
            original = v
            fixed = json_regex_decode(original)
            json_data[k] = fixed
    return json_data


class ConfigParser:
    """Base class for handling loading and storing of config files."""

    def __init__(
        self, config_fn: Union[str, None] = None, config_dir: Union[str, None] = None
    ) -> None:
        """
        Args:
                config (str):   File name of the config file with extension.
                                If not supplied it needs to be set with set_file.
                                Must be json. e.g. "parsing.json", "serial.json" etc.
        """
        self.config_dir = config_dir if config_dir is not None else DEFAULT_CONFIG_DIR
        self.config_type = "user"
        self.config_fn = config_fn
        self.is_loaded = False
        if self.config_fn is None:
            return
        self.set_file(self.config_fn)
        self.load_selected()

    def _check_file(self, config_fn: str) -> str:
        """Checks the config directory for default/user config files with the given name.
                If the user config is invalid or missing the default will be returned.

        Args:
                fn (str): Filename of the config file. "something.json"

        Returns:
                str: Absolute path of the config file.

        Raises:
                FileNotFoundError: If both the default and user config file are missing.
                ValueError: If the supplied filename is invalid.
        """
        if not config_fn.endswith(".json"):
            raise ValueError(f"Config file '{config_fn}' is not a json file.")

        if self.config_type == "default":
            path = os.path.join(self.config_dir, "default", config_fn)
            abs_path = os.path.abspath(path)
            if not os.path.isfile(abs_path):
                raise FileNotFoundError(
                    (
                        f"Config files for '{config_fn}' not found.\n"
                        f"Default config file should be at\n'{abs_path}'.\n"
                        f"Please create your own config file at\n{os.path.join(self.config_dir, config_fn)}\n"
                        f"or copy the default config file to the config directory."
                    )
                )
            return abs_path

        path = os.path.join(self.config_dir, config_fn)
        abs_path = os.path.abspath(path)
        if not os.path.isfile(abs_path):
            self.config_type = "default"
            return self._check_file(config_fn)
        return abs_path

    def _load_file(self, path: str) -> None:
        """Loads a config file from a given path.

        Args:
                path (str): (Absolute) path to the config file.

        Raises:
                json.decoder.JSONDecodeError: If the file is not a valid json file.
        """
        try:
            with open(path, "rb") as f:
                data = f.read()
                self.config = fix_double_backslash(json.loads(data))
                print("debug")
        except json.decoder.JSONDecodeError as e:
            raise json.decoder.JSONDecodeError(
                (
                    f"Config file '{path}' is not a valid json file.\n"
                    f"Decoder Error:\n{e.msg}\n"
                ),
                e.doc,
                e.pos,
            )
        except Exception as e:
            raise e
        self.is_loaded = True

    def set_file(self, config_fn: str) -> None:
        """Sets the config file to be used. and loads it.

        Args:
                config_fn (str): Filename of the config file. "something.json"
        """
        self.config_type = "user"
        self.config_fn = config_fn
        self.config_path = self._check_file(config_fn)

    def load_selected(self) -> None:
        """Loads the currently selected config file."""
        if self.config_fn is None:
            raise UninitializedConfigException("No config file selected.")
        try:
            self._load_file(self.config_path)
        except json.decoder.JSONDecodeError as e:
            print(e)
            print("Using default config file.")
            self.config_type = "default"
            self.config_path = self._check_file(self.config_fn)
        finally:
            self._load_file(self.config_path)

    def get_key(self, key: str) -> dict:
        """Gets a value from the config file.

        Args:
                key (str): Key of the value to be retrieved.

        Returns:
                dict: Value of the key.

        Raises:
                UnititializedConfigError: If the config file is not loaded.
                KeyError: If the key is not found in the config file.
        """
        if not self.is_loaded:
            raise UninitializedConfigException("Config file not loaded.")
        try:
            return self.config[key]
        except KeyError:
            raise KeyError(f"Key '{key}' not found in config.")

    def get_all(self) -> dict:
        """Gets the entire config file.

        Returns:
                dict: The entire config file.

        Raises:
                UnititializedConfigError: If the config file is not loaded.
        """
        if not self.is_loaded:
            raise UninitializedConfigException("Config file not loaded.")
        return self.config

    def set_key(self, key: str, value: dict) -> None:
        """Sets a value in the config file.

        Args:
                key (str): Key of the value to be set.
                value (dict): Value to be set.

        Raises:
                UnititializedConfigError: If the config file is not loaded.
                KeyError: If the key is not found in the config file.
        """
        if not self.is_loaded:
            raise UninitializedConfigException("Config file not loaded.")
        if key not in self.config:
            raise KeyError(f"Key '{key}' not found in config.")

    def set_all(self, config: dict) -> None:
        """Sets the entire config file.

        Args:
                config (dict): The entire config file.
        """
        self.config = config
        self.is_loaded = True

    def save(self) -> None:
        """Saves the config file to the user config directory."""
        if not self.is_loaded or self.config_fn is None:
            raise ValueError("Config file not loaded.")
        path = os.path.join(self.config_dir, self.config_fn)
        with open(path, "w") as f:
            json.dump(self.config, f, indent=4)

    def reload(self) -> None:
        """Reloads the config file."""
        self.config_type = "user"
        self.load_selected()
