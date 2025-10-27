from typing import Type, TypeVar

from injector import Injector

from common.infrastructure.app_module import AppModule
from common.infrastructure.settings import Settings

settings = Settings("./.env")
T = TypeVar('T')
injector = Injector(AppModule(settings))

def get_service(cls: Type[T]):
    def dependency() -> T:
        return injector.get(cls)
    return dependency