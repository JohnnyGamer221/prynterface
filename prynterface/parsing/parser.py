import asyncio
from typing import Protocol, Any, AsyncGenerator


class PipelineModule(Protocol):
    data: Any
    yield_condition: asyncio.Condition

    def __init__(self, config: dict[str, Any]) -> None:
        ...

    async def _func(self) -> None:
        ...

    async def _add_data(self, data: str) -> None:
        ...

    async def generator(self) -> AsyncGenerator:
        ...


class BasePipelineModule:
    config: dict[str, Any]
    yield_condition: asyncio.Condition
    data: Any
    out: list[Any]

    def __init__(self, config: dict[str, Any]) -> None:
        self.config = config
        self.yield_condition = asyncio.Condition()
        self.data = None
        self.out = []

    async def _func(self, data: Any) -> bool:
        ...
        if len(self.out) > 0:
            return True
        return False

    async def _add_data(self, data: str) -> None:
        async with self.yield_condition:
            if self._func(data):
                self.yield_condition.notify_all()

    async def generator(self) -> AsyncGenerator:
        while True:
            async with self.yield_condition:
                while self.out is None:
                    await self.yield_condition.wait()
                for data in self.out:
                    yield data


class PipelineStep(Protocol):
    stepid: str
    module: PipelineModule
    input_generator: AsyncGenerator
    output_generator: AsyncGenerator

    def __init__(self, stepid, module: PipelineModule) -> None:
        ...

    def setup(self, generator: AsyncGenerator) -> AsyncGenerator:
        """Set up input and output generators"""
        ...


class BasePipelineStep:
    def __init__(self, stepid, module: PipelineModule) -> None:
        self.stepid = stepid
        self.module = module

    def setup(self, generator: AsyncGenerator) -> AsyncGenerator:
        self.generator = generator

        async def _setup_add() -> None:
            async for data in generator:
                await self.module._add_data(data)

        asyncio.create_task(_setup_add())
        return self.module.generator()


class Pipeline:
    def __init__(self, steps: list[PipelineStep]) -> None:
        self.steps = steps
        self.generator = None

    def _setup(self, generator: AsyncGenerator) -> None:
        self.generator = generator
        for step in self.steps:
            step.setup(generator)
