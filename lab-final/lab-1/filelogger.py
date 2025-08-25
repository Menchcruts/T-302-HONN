from logger import Logger
from pathlib import Path

#2.3 File Logger (20 points)
#1. (Total points: 20) Implement the concrete class FileLogger
#• The class should be in a file named filelogger.py
#• FileLogger implements the Logger interface
#• log_info, log_warning og log_error log to a file with path ./logging.log
#• If no logging.log file exists then the logger creates one
#• The logger appends to the file if it already exists

class FileLogger(Logger):
    def __init__(self):
        super().__init__()
        self.log_file = Path("./logging.log")
    
    def __log(self, message:str) -> None:
        with self.log_file.open("a+") as file:
            file.write(message)
        
    def log_info(self, message):
        self.__log(f"info: {message}\n")
        return super().log_info(message)

    def log_warning(self, message):
        self.__log(f"warning: {message}\n")
        return super().log_warning(message)
    
    def log_error(self, message, exception):
        self.__log(f"warning: {message}, exception: {exception}\n")
        return super().log_error(message, exception)
