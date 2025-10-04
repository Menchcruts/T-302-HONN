
from injector import Module

from structured_logging.configuration.logger_config import LoggerConfig


class AppModule(Module):
    def __init__(self, logger_config: LoggerConfig) -> None:
        self.__logger_config = logger_config
