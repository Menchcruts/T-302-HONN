from typing import Any, Iterable
from structured_logging.command_queue.queue import Queue
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger.logging_command import LoggerCommand

class Logger:
    def __init__(self, logger_config: LoggerConfig, logging_queue: Queue):
        self.__logger_config = logger_config
        self.__logging_queue = logging_queue
        self.__logging_queue.start()

    def log(self, **kwargs: Iterable[Any]):
        data = kwargs
        processor = self.__logger_config.processor
        processor.handle(data)

        logger_command = LoggerCommand(self.__logger_config.sink, data)

        if (self.__logger_config.is_async):
            self.__logging_queue.add(logger_command)
        else:
            logger_command.execute()

    def close(self):
        self.__logging_queue.join()