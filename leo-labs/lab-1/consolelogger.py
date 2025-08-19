from logger import Logger

#2.2 Console Logger (25 points)

#1. (Total points: 20) Implement the concrete class ConsoleLogger
#• The class should be stored in a file named consolelogger.py
#• ConsoleLogger implements the Logger interface
#• log_info, log_warning and log_error log to the console

class ConsoleLogger(Logger):
    def log_error(self, message: str, exception: Exception) -> None:
        print(f"error: {message}, exception: {exception}")
    
    def log_info(self, message: str) -> None:
        print(f"info: {message}")
    
    def log_warning(self, message: str) -> None:
        print(f"warning: {message}")
        

#2. (Total points: 5) Try to alter the name of the log_warning function to log_waarning in the ConsoleLogger
#class and try to initalize the ConsoleLogger, specify the error message you get.

# logger = ConsoleLogger()
# Initializing the console logger after changing the name of log_warning to log_waarning give me this error:
#TypeError: Can't instantiate abstract class ConsoleLogger
# without an implementation for abstract method 'log_warning'


