from structured_logging.configuration.environment import Environment
from structured_logging.configuration.logger_config import LoggerConfig

from structured_logging.processors.i_processor import IProcessor
from structured_logging.processors.null_processor import NullProcessor

from structured_logging.sinks.i_sink import ISink
from structured_logging.sinks.file_sink import FileSink
from structured_logging.sinks.console_sink import ConsoleSink



class LoggerConfigBuilder:
    __sink: ISink
    __processors: list[IProcessor]
    __is_async: bool
    __async_wait_delay_in_seconds: float
    __environment: Environment

    def __init__(self):
        self._clear()

    def with_custom_sink(self, sink: ISink) -> 'LoggerConfigBuilder':
        assert isinstance(sink, ISink)
        self.__sink = sink
        return self
        
    def with_file_sink(self, file_path: str) -> 'LoggerConfigBuilder':
        self.__sink = FileSink(file_path)
        return self

    def with_console_sink(self) -> 'LoggerConfigBuilder':
        self.__sink = ConsoleSink()
        return self

    def as_async(self, wait_delay_in_seconds: float) -> 'LoggerConfigBuilder':
        self.__is_async = True
        self.__async_wait_delay_in_seconds = wait_delay_in_seconds
        return self

    def add_environment(self, environment: Environment) -> 'LoggerConfigBuilder':
        assert isinstance(environment, Environment)
        self.__environment = environment
        return self

    def add_processor(self, processor: IProcessor) -> 'LoggerConfigBuilder':
        assert isinstance(processor, IProcessor)
        self.__processors.append(processor)
        return self

    def _clear(self):
        self.__sink = ConsoleSink()
        self.__processors = [NullProcessor()]
        self.__is_async = False
        self.__async_wait_delay_in_seconds = 0
        self.__environment = None   # Used for what?

    def __build_processor(self) -> IProcessor:
        last: IProcessor = None
        for processor in self.__processors[::-1]:
            if last is not None:
                processor.set_next(last)
            last = processor
        return last

    def build(self) -> LoggerConfig:
        config = LoggerConfig(
            sink=self.__sink, 
            processor=self.__build_processor(), 
            is_async=self.__is_async, 
            async_wait_delay_in_seconds=self.__async_wait_delay_in_seconds
        )
        return config
