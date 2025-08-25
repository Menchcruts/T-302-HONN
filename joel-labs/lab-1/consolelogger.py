from logger import Logger

class ConsoleLogger(Logger):
    def log_info(self, message):
        print(f"info: {message}")
        return super().log_info(message)

    def log_warning(self, message):
        print(f"warning: {message}")
        return super().log_warning(message)
    
    def log_error(self, message, exception):
        print(f"error: {message}, exception: {exception}")
        return super().log_error(message, exception)
    