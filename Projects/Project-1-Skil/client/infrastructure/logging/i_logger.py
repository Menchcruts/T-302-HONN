from abc import ABC, abstractmethod


class ILogger(ABC):
    @abstractmethod
    def error(self, data: str | object, exception: Exception = None): ...

    @abstractmethod
    def warning(self, data: str | object, exception: Exception = None): ...

    @abstractmethod
    def info(self, data: str | object): ...
