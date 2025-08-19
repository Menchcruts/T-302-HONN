from abc import ABC, abstractmethod

#2.1 Logger interface (15 stig)

#1. (Total points: 12.5) implement the Logger interface, the interface should be stored in a file with the
#name logger.py and this interface will have all the operations specified on the diagram above.

class Logger(ABC):
    @abstractmethod
    def log_error(self, message: str, exception: Exception) -> None:
        pass
    @abstractmethod
    def log_info(self, message: str) -> None:
        pass
    @abstractmethod
    def log_warning(self, message: str) -> None:
        pass
        
#2. (Total points: 2.5) Try to initalize the Logger interface and specify what error message you get.
#(what is meant by initalize is simply to try and create an instance of the class)

# logger = Logger() 
# Initializing the logger give me this error:
# TypeError: 
# Can't instantiate abstract class Logger without an implementation for abstract method 'log_error'


