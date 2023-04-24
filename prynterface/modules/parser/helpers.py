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
