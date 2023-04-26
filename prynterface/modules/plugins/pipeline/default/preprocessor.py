from typing import Any
from ..baseclass import PipelineModuleABC


class PreProcessor(PipelineModuleABC):
    """Receives raw data, splits it into lines, adds line numbers and timestamp and yields it back"""

    def name(self) -> str:
        return "preprocessor"

    def setup_module(self) -> None:
        pass

    def add_data(self, data: str) -> Any:
        return "False"


def get_module() -> Any:
    return PreProcessor
