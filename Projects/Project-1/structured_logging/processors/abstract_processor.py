from structured_logging.processors.i_processor import IProcessor

class AbstractProcessor(IProcessor):
    __next: IProcessor

    def set_next(self, processor):
        self.__next = processor