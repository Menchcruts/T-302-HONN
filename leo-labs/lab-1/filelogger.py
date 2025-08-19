from logger import Logger

#2.3 File Logger (20 points)
#1. (Total points: 20) Implement the concrete class FileLogger
#• The class should be in a file named filelogger.py
#• FileLogger implements the Logger interface
#• log_info, log_warning og log_error log to a file with path ./logging.log
#• If no logging.log file exists then the logger creates one
#• The logger appends to the file if it already exists

class FileLogger(Logger):
    def log_error(self, message: str, exception: Exception) -> None:
        with open('./logging.log', 'a') as file:
            file.write(f"error: {message}, exception: {exception}\n")
    
    def log_info(self, message: str) -> None:
        with open('./logging.log', 'a') as file:
            file.write(f"info: {message} \n")
    
    def log_warning(self, message: str) -> None:
        with open('./logging.log', 'a') as file:
            file.write(f"warning: {message} \n")

