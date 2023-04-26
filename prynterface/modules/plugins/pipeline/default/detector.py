from typing import Any
from ..baseclass import PipelineModuleABC


class Detector(PipelineModuleABC):
    """Buffer data from PreProcessor, do the initial detection and yield matches with line info and start/end positions"""

    def name(self) -> str:
        return "detector"

    def setup_module(self) -> None:
        ...

    def add_data(self, data: str) -> bool:
        ...


def get_module() -> Any:
    return Detector
