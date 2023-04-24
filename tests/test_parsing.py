import pytest, os
from .context import matcher, parser, parsing


CONFIG_DIR = "tests/configs/parsing"
PARSING_CONFIG_PATH = "simple.json"
TEST_DATA = """This is some test data we are going to parse.
Just for the lols.
TestOne: 42 TestTwo:43 TestThree: 42069
Some more stuff we aint gonna parse.
This is the start of something in a block:
Here are some data points.
But only a little further down to test the block matching.
X: 50 Y:60 Z : 70
Status: FAIL
Mesh:
0 1 2 3 4
5 6 7 8 9
1 2 3 4 5
6 7 8 9 0
Now its finished
ok
Some more lines that arent going to get parsed.
lorem ipsum dolor sit amet.
"""


@pytest.fixture
def configfixture() -> parsing.ParsingConfig:
    return parsing.ParsingConfig(PARSING_CONFIG_PATH, CONFIG_DIR)


@pytest.fixture
def parser_fixture(config: parsing.ParsingConfig) -> parser.Parser:
    return parser_fixture.Parser(configfixture())


def test_simple_parsing():
    test_parser = parser.Parser(configfixture())
    lines = TEST_DATA.splitlines()
    for line in lines:
        test_parser.add_line(line.encode())

    test_parser.detect()
    returned_data = test_parser.get_data()[0]
    assert returned_data["test1"] == {
        "type": "dict-float",
        "line-start": 3,
        "values": {"TestOne": 42, "TestTwo": 43, "TestThree": 42069},
    }
    assert returned_data["test2"] == {
        "type": "some-advanced-data",
        "line-start": 5,
        "values": {
            "mesh": [
                [0, 1, 2, 3, 4],
                [5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 0],
            ],
            "coords": {"X": 50, "Y": 60, "Z": 70},
            "status": False,
        },
    }
