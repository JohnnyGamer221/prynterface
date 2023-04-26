from typing import Any
from ..baseclass import PipelineModuleABC


class Extractor(PipelineModuleABC):
    """Extract match groups from Detector and yield them with line info, start/end positions and group names"""

    def name(self) -> str:
        return "extractor"

    def setup_module(self) -> None:
        ...

    def add_data(self, data: str) -> bool:
        ...


def get_module() -> Any:
    return Extractor
