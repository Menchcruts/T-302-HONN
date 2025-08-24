from logger import Logger
from pathlib import Path

class FileLogger(Logger):
    def __init__(self):
        super().__init__()
        self.log_file = Path("./logging.log")
    
    def log_info(self, message):
        with self.log_file.open("a+") as file:
            file.write(f"info: {message}\n")
        return super().log_info(message)

    def log_warning(self, message):
        with self.log_file.open("a+") as file:
            file.write(f"warning: {message}\n")
        return super().log_warning(message)
    
    def log_error(self, message, exception):
        with self.log_file.open("a+") as file:
            file.write(f"warning: {message}, exception: {exception}\n")
        return super().log_error(message, exception)
