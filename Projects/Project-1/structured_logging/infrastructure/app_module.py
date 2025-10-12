from injector import Module, provider

from structured_logging.logger.logger import Logger
from structured_logging.configuration.logger_config import LoggerConfig

from structured_logging.command_queue.queue import Queue


class AppModule(Module):
    def __init__(self, logger_config: LoggerConfig) -> None:
        self.__logger_config = logger_config

    @provider
    def provide_logger(self) -> Logger:
        return Logger(self.__logger_config, Queue(self.__logger_config.async_wait_delay_in_seconds))