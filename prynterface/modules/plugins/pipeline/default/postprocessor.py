from typing import Any
from ..baseclass import PipelineModuleABC


class PostProcessor(PipelineModuleABC):
    """Buffer data from Extractor, do the final processing and yield the final result"""

    def name(self) -> str:
        return "postprocessor"

    def setup_module(self) -> None:
        ...

    def add_data(self, data: str) -> bool:
        ...


def get_module() -> Any:
    return PostProcessor
