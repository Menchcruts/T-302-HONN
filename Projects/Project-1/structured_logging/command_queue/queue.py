import threading
from structured_logging.command_queue.command import Command


class Queue:
    # TODO: we also need to inject the async delay time into the constructor
    def __init__(self):
        raise NotImplementedError()
        self.__thread = threading.Thread(target=self.__process)
        self.__thread.daemon = True
        self.__thread.start()

    def add(self, command: Command):
        raise NotImplementedError()

    def __process(self):
        raise NotImplementedError()
