from client.infrastructure.settings.settings import Settings, LoggingType

from client.infrastructure.logging.masking_processor import MaskingProcessor

from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger_creation.logger_config_builder import LoggerConfigBuilder
from structured_logging.processors.timestamp_processor import TimestampProcessor


def create_logger_config(settings: Settings, builder: LoggerConfigBuilder) -> LoggerConfig:
    builder = LoggerConfigBuilder()

    if settings.logging_is_async:
        builder.as_async(settings.logging_async_delay)
    
    match settings.logging_type:
        case LoggingType.CONSOLE:
            builder.with_console_sink()
        case LoggingType.FILE:
            builder.with_file_sink(settings.logging_file_path)
    
    if settings.masked_keys:
        builder.add_processor(MaskingProcessor(settings.masked_keys))

    if settings.environment is not None:
        builder.add_environment(settings.environment)

    builder.add_processor(TimestampProcessor())

    return builder.build()
