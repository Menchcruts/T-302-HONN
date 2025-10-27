from structured_logging.sinks.i_sink import ISink
from pathlib import Path
import json

class FileSink(ISink):
    def __init__(self, filepath: Path):
        super().__init__()
        self.path = Path(filepath)
        if self.path.exists() and not self.path.is_file():
            raise ValueError("FileSink: 'filepath' must be a file.")
        self.path.parent.mkdir(exist_ok=True, parents=True)

    def get_data(self) -> list[dict]:
        if not self.path.exists():
            return []
        try:
            with self.path.open("r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def save_data(self, data: list[dict]) -> None:
        with self.path.open("w+", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def sink_data(self, data):
        saved_data = self.get_data()
        saved_data.append(data)
        self.save_data(saved_data)
