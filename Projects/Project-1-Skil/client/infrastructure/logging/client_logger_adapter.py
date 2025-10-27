from dataclasses import asdict

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

    def __create_data(self, data: str | object) -> dict:
        if isinstance(data, str):
            return {"message":data}
        return {"data": asdict(data)}

    def __add_level(self, data: dict, lvl:str) -> None:
        data["level"] = lvl

    def __add_exception(self, data: dict, exception: Exception) -> None:
        if exception is not None:
            data["error"] = str(exception)


    def info(self, data):
        data = self.__create_data(data)
        self.__add_level(data, "info")
        self.__log(data)

    def warning(self, data, exception = None):
        data = self.__create_data(data)
        self.__add_level(data, "warning")
        self.__add_exception(data, exception)
        self.__log(data)

    def error(self, data, exception = None):
        data = self.__create_data(data)
        self.__add_level("error")
        self.__add_exception(data, exception)
        self.__log(data)
