from structured_logging.command_queue.command import Command
from structured_logging.sinks.i_sink import ISink

class LoggingCommand(Command):
    __sink: ISink
    __data: dict
    
    def __init__(self, sink: ISink, data: dict):
        super().__init__()
        self.__sink = sink
        self.__data = data

    def execute(self):
        self.__sink.sink_data(self.__data)