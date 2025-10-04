from client.infrastructure.settings.settings import Settings
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger_creation.logger_config_builder import LoggerConfigBuilder


def create_logger_config(settings: Settings, builder: LoggerConfigBuilder) -> LoggerConfig:
    raise NotImplementedError()
