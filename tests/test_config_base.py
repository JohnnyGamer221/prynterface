import pytest
import json
import os
from contextlib import nullcontext as does_not_raise
from .context import base

UninitConfigExc = base.UninitializedConfigException

CONFIG_DIR = "tests/configs/base"

GOOD_FILE = "default.json"
GOOD_USER_FILE = "user.json"
NONEXISTENT_FILE = "nonexistent.json"
NOT_A_FILE = "directory.json"
WRONG_EXTENSION = "default.txt"
BAD_JSON = "bad.json"
BAD_USER_JSON = "baduser.json"


def config_defaultpath(config_fn):
    return os.path.abspath(os.path.join(CONFIG_DIR, "default", config_fn))


def config_userpath(config_fn):
    return os.path.abspath(os.path.join(CONFIG_DIR, config_fn))


# __init__


@pytest.mark.parametrize(
    "config_fn, expectation",
    [
        (GOOD_FILE, does_not_raise()),
        (GOOD_USER_FILE, does_not_raise()),
        (NONEXISTENT_FILE, pytest.raises(FileNotFoundError)),
        (NOT_A_FILE, pytest.raises(FileNotFoundError)),
        (WRONG_EXTENSION, pytest.raises(ValueError)),
        (BAD_JSON, pytest.raises(json.decoder.JSONDecodeError)),
        (BAD_USER_JSON, does_not_raise()),
    ],
)
def test_init_exceptions(config_fn, expectation):
    """Test that valid files are loaded and invalid files raise exceptions.

    Args:
            config_fn: test file name
            expectation: Expected exception or nullcontext if no exception is expected.
    """
    with expectation:
        base.ConfigParser(config_fn, CONFIG_DIR)


@pytest.mark.parametrize(
    "config_fn, expectation",
    [
        (GOOD_FILE, "default"),
        (GOOD_USER_FILE, "user"),
        (BAD_USER_JSON, "default"),
    ],
)
def test_init_loaded_and_config_type(config_fn, expectation):
    """_summary_

    Args:
            config_fn (_type_): _description_
            expectation (_type_): _description_
    """
    config = base.ConfigParser(config_fn, CONFIG_DIR)
    assert config.is_loaded
    assert config.config_type == expectation


def test_init_no_file():
    config = base.ConfigParser(None, CONFIG_DIR)
    assert not config.is_loaded


# _check_file


@pytest.mark.parametrize(
    "config_fn, config_path",
    [
        (GOOD_FILE, config_defaultpath(GOOD_FILE)),
        (GOOD_USER_FILE, config_userpath(GOOD_USER_FILE)),
        # Bad user json should be selected, detection is done during loading
        (BAD_USER_JSON, config_userpath(BAD_USER_JSON)),
    ],
)
def test_check_file(config_fn, config_path):
    config = base.ConfigParser(None, CONFIG_DIR)
    assert config._check_file(config_fn) == config_path


# _load_file

# set_file

# load_selected

# get

# get_all

# set

# set_all

# save

# reload
