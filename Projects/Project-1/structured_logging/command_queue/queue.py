import threading
import time
from queue import Queue as ThreadQueue, Empty
from structured_logging.command_queue.command import Command


class Queue:
    def __init__(self, wait_delay: float = 0):
        self.__commands = ThreadQueue[Command]()
        self.__stop_event = threading.Event()
        self.__async_wait_delay = wait_delay
        self.__thread = None

    def start(self) -> None:
        if self.__thread is None or not self.__thread.is_alive():
            self.__thread = threading.Thread(target=self.__process, daemon=True)
            self.__thread.start()

    def stop(self) -> None:
        self.__stop_event.set()
        if self.__thread:
            self.__thread.join()

    def add(self, command: Command):
        self.__commands.put(command)

    def __process(self):
        while not self.__stop_event.is_set():
            try:
                command = self.__commands.get()
                if command:
                    command.execute()
                    self.__commands.task_done()
            except Empty as e:
                pass
            except Exception as e:
                print(f"Queue: Error processing command. | {e}", flush=True)

            time.sleep(self.__async_wait_delay)

    def join(self):
        self.__commands.join()
        self.stop()
