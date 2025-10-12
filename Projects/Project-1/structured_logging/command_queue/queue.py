import threading
import time
from typing import List
from structured_logging.command_queue.command import Command


class Queue:
    def __init__(self, wait_delay: float = 0):
        self.commands: List[Command] = []
        self.__async_wait_delay = wait_delay
        self.__thread = threading.Thread(target=self.__process)
        self.__thread.daemon = True
        self.__thread.start()

    def add(self, command: Command):
        self.commands.append(command)

    def __process(self):
        while True:
            if len(self.commands) > 0:
                command = self.commands.pop(0)
                command.execute()
            else:
                if self.__async_wait_delay > 0:
                    time.sleep(self.__async_wait_delay)