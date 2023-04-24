if __name__ == "__main__":
    # @todo this is fucked but i cant get it to run the tests and main otherwise
    from modules.configuration.parsing import ParsingConfig
    from modules.configuration.printer import PrinterConfig
    from modules.parser.parser import Parser
    from modules.sinterface.sinterface import SerialIO
    from modules.ui.ui import UserInterface
else:
    from .context import ParsingConfig, PrinterConfig, Parser, SerialIO, UserInterface

__TEST_DATA = """This is some test data we are going to parse.
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
TestOne: 45 TestTwo:46 TestThree: 69420
"""


def import_test():
    print(ParsingConfig, PrinterConfig, Parser, SerialIO)


# @todo implement main loop [implement]
def main():
    parser_config = ParsingConfig()
    parser = Parser(parser_config)
    lines = __TEST_DATA.splitlines()
    for line in lines:
        parser.add_line(line.encode() + b"\n")
    out = parser.parse()
    print(out)


if __name__ == "__main__":
    main()
