from injector import Injector
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.infrastructure.app_module import AppModule
from structured_logging.logger.logger import Logger


def create_logger(logger_config: LoggerConfig) -> Logger:
    injector = Injector(AppModule(logger_config))
    return injector.get(Logger)
