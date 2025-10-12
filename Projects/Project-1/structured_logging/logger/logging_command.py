from structured_logging.command_queue.command import Command
from sinks.i_sink import ISink

class LoggerCommand(Command):
    def __init__(self, sink: ISink, data: dict):
        self.sink = sink
        self.data = data

    def execute(self):
        self.sink.sink_data(self.data)
        
