from injector import Module

from client.infrastructure.settings.settings import Settings

class AppModule(Module):
    def __init__(self, settings: Settings) -> None:
        self.__settings = settings
