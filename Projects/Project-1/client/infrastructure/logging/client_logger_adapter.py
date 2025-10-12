from client.infrastructure.logging.i_logger import ILogger

from structured_logging.logger.logger import Logger
from structured_logging.logger_creation.logger_config_builder import LoggerConfig
from structured_logging.logger_creation.logger_factory import create_logger

class ClientLoggerAdapter(ILogger):
    __logger: Logger

    def __init__(self, config: LoggerConfig):
        super().__init__()
        self.__logger = create_logger(config)

    def __log(self, data: dict) -> None:
        self.__logger.log(**data)

    def __create_data(self, message:str) -> None:
        return {"message":message}

    def info(self, message):
        data = self.__create_data(message)
        data["level"] = "info"
        self.__log(data)

    def warning(self, message, exception = None):
        data = self.__create_data(message)
        data["level"] = "warning"
        if exception is not None:
            data["error"] = str(exception)
        self.__log(data)

    def error(self, message, exception = None):
        data = self.__create_data(message)
        data["level"] = "error"
        if exception is not None:
            data["error"] = str(exception)
        self.__log(data)