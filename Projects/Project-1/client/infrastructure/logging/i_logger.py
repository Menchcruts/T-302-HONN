from abc import ABC, abstractmethod


class ILogger(ABC):
    @abstractmethod
    def error(self, message: str, exception: Exception = None):
        pass

    @abstractmethod
    def warning(self, message: str, exception: Exception = None):
        pass

    @abstractmethod
    def info(self, message: str):
        pass
