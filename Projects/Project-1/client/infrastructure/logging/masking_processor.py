from structured_logging.processors.abstract_processor import AbstractProcessor

class MaskingProcessor(AbstractProcessor):
    __masked_keys: list[str]

    def __init__(self, masked_keys: list[str]):
        super().__init__()
        self.__masked_keys = masked_keys

    def __mask_keys(self, data: dict) -> None:
        for key in data.keys():
            if isinstance(data[key], dict):
                self.__mask_keys(data[key])
            elif isinstance(data[key], list):
                lst: list = data[key]
                if len(lst) <= 0:
                    continue
                if isinstance(lst[0], dict):
                    for item in lst:
                        self.__mask_keys(item)
            else:
                if key in self.__masked_keys:
                    data[key] = "***"

    def _process_data(self, data):
        self.__mask_keys(data)