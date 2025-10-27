from structured_logging.processors.abstract_processor import AbstractProcessor

class NullProcessor(AbstractProcessor):
    def _process_data(self, data):
        # Do nothing
        return