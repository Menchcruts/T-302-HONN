from enum import Enum
from pydantic import BaseSettings


class ContainerSettingEnum(Enum):
    def get(self, *argv):
        return self.value


class LoggingType(ContainerSettingEnum):
    CONSOLE = 'console'
    FILE = 'file'


class Environment(ContainerSettingEnum):
    DEVELOPMENT = 'development'
    STAGING = 'staging'
    PRODUCTION = 'production'


class Settings(BaseSettings):
    order_file_path: str
    should_payment_succeed: bool
    logging_type: LoggingType
    logging_file_path: str
    logging_is_async: bool
    logging_async_delay: int
    environment: Environment

    class Config:
        env_file = "./client/infrastructure/settings/.env"
        env_file_encoding = 'utf-8'
