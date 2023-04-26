import asyncio
from abc import abstractmethod, ABC
from typing import Any, AsyncGenerator


class PipelineModuleABC(ABC):
    _config: dict[str, Any]
    _yield_condition: asyncio.Condition
    _data: Any
    _out: list[Any]

    def __init__(self, config: dict[str, Any]) -> None:
        self._config = config
        self._yield_condition = asyncio.Condition()
        self._data = None
        self._out = []
        self._setup_module()

    def _setup_module(self) -> None:
        self.setup_module()

    @abstractmethod
    def name(self) -> str:
        """Needs to return the name of the module"""

    @abstractmethod
    def setup_module(self) -> None:
        """Needs to do everything neccesary for the module to work"""

    @abstractmethod
    def add_data(self, data: Any) -> bool:
        """Needs to add data, do its conversions and return True if data is ready to be yielded
        All converted data needs to be stored in self._out"""

    async def add_async(self, data: Any) -> None:
        async with self._yield_condition:
            if self.add_data(data):
                self._yield_condition.notify_all()

    async def generator(self) -> AsyncGenerator:
        while True:
            async with self._yield_condition:
                while len(self._out) == 0:
                    await self._yield_condition.wait()
                for data in self._out:
                    data = self._out.pop(0)
                    yield data
