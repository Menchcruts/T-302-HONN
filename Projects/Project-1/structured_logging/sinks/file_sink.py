from structured_logging.sinks.i_sink import ISink
from pathlib import Path
import json

class FileSink(ISink):
    def __init__(self, filepath: Path):
        super().__init__()
        self.path = Path(filepath)

    def get_data(self) -> list[dict]:
        data = []
        with self.path.open("r") as file:
            data = json.load(file)
        return data
    
    def save_data(self, data: list[dict]) -> None:
        with self.path.open("w+") as file:
            json.dump(data, file)

    def sink_data(self, data):
        saved_data = self.get_data()
        saved_data.append(data)