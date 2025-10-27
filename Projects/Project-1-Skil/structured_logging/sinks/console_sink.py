from structured_logging.sinks.i_sink import ISink
import json

class ConsoleSink(ISink):
    def sink_data(self, data):
        print(json.dumps(data, indent=2, ensure_ascii=False), flush=True)
