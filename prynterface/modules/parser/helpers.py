import re
from dataclasses import dataclass


@dataclass
class LineWithInfo:
    line: bytes
    linenumber: int
    rcv_time: float
    start_str_index: int
    end_str_index: int

    def __str__(self) -> str:
        return self.line.decode()

    def __repr__(self) -> str:
        return f"Line number {self.linenumber}:{self.line.decode()}"

    def __len__(self) -> int:
        return len(self.line)


@dataclass
class Match:
    matched_string: str
    start_index: int
    end_index: int
    key_name: str


# @todo This is horrendous, just wanted to get it working without losing any data on the way.
#       Need to find a better way to do this.
#       Clean up [cleanup]
@dataclass
class MatchWithLineInfo:
    matched_string: str
    start_index: int
    end_index: int
    key_name: str
    lines: list[LineWithInfo]


@dataclass
class MatchWithExtractedData:
    matched_string: str
    start_index: int
    end_index: int
    key_name: str
    lines: list[LineWithInfo]
    extracted_data: dict


@dataclass
class MatchWithConvertedData:
    matched_string: str
    start_index: int
    end_index: int
    key_name: str
    lines: list[LineWithInfo]
    extracted_data: dict
    converted_data: dict


@dataclass
class Value:
    name: str | None
    no_value: bool
    sign: str | None
    pre_decimal: int | None
    post_decimal: int | None

    def __str__(self) -> str:
        if self.no_value:
            return "No value"
        if self.sign is None:
            if self.post_decimal is None:
                return f"{self.pre_decimal}"
            return f"{self.pre_decimal}.{self.post_decimal}"
        if self.post_decimal is None:
            return f"{self.sign}{self.pre_decimal}"
        return f"{self.sign}{self.pre_decimal}.{self.post_decimal}"

    def __repr__(self) -> str:
        return f"Value '{self.name}': {self.__str__()}"

    def __len__(self) -> int:
        # Number of significant digits
        if self.no_value:
            return 0
        if self.post_decimal is None:
            return len(str(self.pre_decimal))
        return len(str(self.pre_decimal)) + len(str(self.post_decimal))

    def __eq__(self, __value: object) -> bool:
        return self.__str__() == __value.__str__()

    @property
    def asfloat(self) -> float:
        if self.no_value:
            return float("nan")
        return float(self.__str__())

    @property
    def asint(self) -> int:
        if self.no_value:
            raise ValueError("No value")
        return int(self.asfloat)


def convert_to_value(name: str, value: str) -> Value:
    if value == "":
        return Value(name, True, None, None, None)
    if value[0] == "-":
        sign = "-"
        value = value[1:]
    elif value[0] == "+":
        sign = "+"
        value = value[1:]
    else:
        sign = None
    if "." in value:
        pre_decimal, post_decimal = value.split(".")
    else:
        pre_decimal = value
        post_decimal = None
    # check if everything is a digit or none, if all are none or there are non digits, return no value
    if not all(
        [x.isdigit() if x is not None else True for x in [pre_decimal, post_decimal]]
    ):
        return Value(name, True, None, None, None)
    return Value(
        name, False, sign, int(pre_decimal), int(post_decimal) if post_decimal else None
    )


@dataclass
class ParsedData:
    name: str
    data: dict
    timestamp: float
    start: int
    end: int
