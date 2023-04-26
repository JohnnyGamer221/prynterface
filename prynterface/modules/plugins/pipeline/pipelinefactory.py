import asyncio
from dataclasses import dataclass
from importlib import import_module, util
from typing import Callable, AsyncGenerator, Union
from baseclass import PipelineModuleABC
from ...configuration.plugins import PluginConfig


class PipelineStep:
    stepid: str
    module: PipelineModuleABC
    input_gen: AsyncGenerator
    output_gen: AsyncGenerator

    def __init__(self, stepid, module: PipelineModuleABC) -> None:
        self.stepid = stepid
        self.module = module

    def setup(self, generator: AsyncGenerator) -> AsyncGenerator:
        self.input_gen = generator

        async def _setup_add() -> None:
            async for data in generator:
                await self.module.add_async(data)

        asyncio.create_task(_setup_add())
        self.output_gen = self.module.generator()
        return self.output_gen


class Pipeline:
    identifier: str
    steps: list[PipelineStep]
    input_generator: AsyncGenerator
    output_generator: AsyncGenerator

    def __init__(self, identifier: str, step_list: list[PipelineStep]) -> None:
        self.identifier = identifier
        self.steps = step_list

    def setup(self, input_generator: AsyncGenerator) -> AsyncGenerator:
        self.input_generator = input_generator
        for step in self.steps:
            input_generator = step.setup(input_generator)
        self.output_generator = input_generator
        return self.output_generator


@dataclass
class PipelinePlugin:
    default: bool
    name: str

    @property
    def import_path(self):
        p = "prynterface.plugins.pipeline."
        if self.default:
            p += "default."
        else:
            p += "user."
        p += self.name
        return p

    @property
    def module(self) -> Callable:
        return import_module(self.import_path).get_module()

    @property
    def path_exists(self):
        return util.find_spec(self.import_path) is not None


class PipelineFactory:
    plugins: dict[str, Callable]

    def __init__(self, config: Union[PluginConfig, None]) -> None:
        if config is None:
            config = PluginConfig()
        self.available_plugins = config.plugins["pipeline"]
        self.plugins = {}

    def add_plugin(self, plugin: str) -> None:
        if plugin not in self.available_plugins:
            raise ValueError(f"Pipeline plugin {plugin} is not available")
        plugin_obj = PipelinePlugin(default=False, name=plugin)
        if not plugin_obj.path_exists:
            plugin_obj = PipelinePlugin(default=True, name=plugin)
        if not plugin_obj.path_exists:
            raise ValueError(f"Pipeline plugin {plugin_obj.name} does not exist")
        if plugin_obj.name in self.plugins:
            raise ValueError(f"Pipeline plugin {plugin_obj.name} already exists")
        self.plugins[plugin_obj.name] = plugin_obj.module

    def get_pipeline(
        self,
        identifier: str,
        use_preprocessor: bool,
        steps: list[dict[str, Union[str, dict]]],
    ) -> Pipeline:
        if use_preprocessor:
            if "preprocessor" not in self.plugins:
                raise ValueError("Preprocessor plugin does not exist or is not enabled")
            steps.insert(0, {"name": "preprocessor", "config": {}})
        step_objs = []
        for step in steps:
            if not isinstance(step, dict):
                raise ValueError("Pipeline step is not a dict")
            if "name" not in step:
                raise ValueError("Pipeline step does not have a name")
            stepid = step["name"]
            plugin = step["name"]
            if "config" in step:
                config = step["config"]
            else:
                config = {}
            if plugin not in self.plugins:
                raise ValueError(f"Pipeline plugin {plugin} does not exist")
            plugin_obj = self.plugins[plugin]
            module = plugin_obj(config)
            step_obj = PipelineStep(stepid, module)
            step_objs.append(step_obj)
        pipeline = Pipeline(identifier, step_objs)
        return pipeline
