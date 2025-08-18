from logger import Logger

class ConsoleLogger(Logger):
    def log_error(self, message: str, exception: Exception) -> None:
        print(f"error: {message}, exception: {exception}")
    
    def log_info(self, message: str) -> None:
        print(f"info: {message}")
    
    def log_warning(self, message: str) -> None:
        print(f"warning: {message}")
        
logger = ConsoleLogger()

logger.log_info("this is an info message")
logger.log_warning("this is a warning")
logger.log_error("this is an error", Exception("some weird exception"))