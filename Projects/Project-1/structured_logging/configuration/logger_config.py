from structured_logging.processors.i_processor import IProcessor
from structured_logging.sinks.i_sink import ISink
from pydantic import (BaseSettings)


class LoggerConfig(BaseSettings):
    sink: ISink
    processor: IProcessor
    is_async: bool
    async_wait_delay_in_seconds: int
