from typing import Any
from ..configuration.parsing import ParsingConfig
from ..plugins.pipeline.pipelinefactory import PipelineFactory, Pipeline


class Parser:
    def __init__(self, config: ParsingConfig) -> None:
        self.config = config
        self.pipeline_factory = PipelineFactory(None)

    def _request_pipeline(self, pipeline: dict[str, Any]) -> Pipeline:
        ...

    def request_pipelines(self) -> None:
        ...
