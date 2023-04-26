from abc import abstractmethod, ABC
import asyncio
from typing import Any, AsyncGenerator


class PipelineModule(ABC):
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

    @abstractmethod
    def _setup_module(self) -> None:
        """Needs to do everything neccesary for the module to work"""
        ...

    @abstractmethod
    async def _func(self, data: Any) -> bool:
        """Needs to add data, do its conversions and return True if data is ready to be yielded"""
        ...

    async def _add_data(self, data: str) -> None:
        async with self._yield_condition:
            if self._func(data):
                self._yield_condition.notify_all()

    async def generator(self) -> AsyncGenerator:
        while True:
            async with self._yield_condition:
                while len(self._out) == 0:
                    await self._yield_condition.wait()
                for data in self._out:
                    data = self._out.pop(0)
                    yield data


class PipelineStep(ABC):
    stepid: str
    module: PipelineModule
    input_generator: AsyncGenerator
    output_generator: AsyncGenerator

    def __init__(self, stepid, module: PipelineModule) -> None:
        self.stepid = stepid
        self.module = module

    def setup(self, generator: AsyncGenerator) -> AsyncGenerator:
        self.input_generator = generator

        async def _setup_add() -> None:
            async for data in generator:
                await self.module._add_data(data)

        asyncio.create_task(_setup_add())
        self.output_generator = self.module.generator()
        return self.output_generator


class BasePipeline:
    def __init__(self, steps: list[PipelineStep]) -> None:
        self.steps = steps
        self.generator = None

    def _setup(self, generator: AsyncGenerator) -> None:
        self.generator = generator
        for step in self.steps:
            step.setup(generator)
