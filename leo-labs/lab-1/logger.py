from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log_error(self, message: str, exception: Exception) -> None:
        pass
    
    def log_info(self, message: str) -> None:
        pass

    def log_warning(self, message: str) -> None:
        pass
        

# logger = Logger() 
# Initializine the logger give me this error:
# TypeError: Can't instantiate abstract class Logger without an implementation for abstract method 'log_error'


