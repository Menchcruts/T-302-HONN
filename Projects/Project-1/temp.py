from structured_logging.sinks.console_sink import ConsoleSink
from structured_logging.sinks.file_sink import FileSink

if __name__ == "__main__":
    sink = ConsoleSink()
    sink = FileSink("logs/temp.json")
    sink.sink_data({"hello": "world", "wow": "geggjað"})
    