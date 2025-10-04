from abc import ABC, abstractmethod


class ISink(ABC):
    @abstractmethod
    def sink_data(self, data: dict):
        pass
