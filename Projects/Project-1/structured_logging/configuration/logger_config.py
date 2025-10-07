from structured_logging.processors.i_processor import IProcessor
from structured_logging.sinks.i_sink import ISink
from pydantic import (BaseSettings)

from structured_logging.sinks.console_sink import ConsoleSink
from structured_logging.processors.null_processor import NullProcessor


class LoggerConfig(BaseSettings):
    sink: ISink                         = ConsoleSink()
    processor: IProcessor               = NullProcessor()
    is_async: bool                      = False
    async_wait_delay_in_seconds: int    = 0
