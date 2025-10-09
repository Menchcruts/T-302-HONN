from structured_logging.processors.abstract_processor import AbstractProcessor
from datetime import datetime

class TimestampProcessor(AbstractProcessor):
    def _process_data(self, data):
        timestamp = datetime.now()
        data.setdefault("timestamp", timestamp.strftime("%d/%m/%Y %H:%M:%S"))