from abc import abstractmethod
from structured_logging.processors.i_processor import IProcessor

class AbstractProcessor(IProcessor):
    __next: IProcessor = None

    def set_next(self, processor):
        self.__next = processor

    def handle(self, data):
        self._process_data(data)
        if self.__next is not None:
            self.__next.handle(data)

    @abstractmethod
    def _process_data(self, data: dict) -> None: ...