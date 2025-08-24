from typing import List

from consolelogger import ConsoleLogger
from filelogger import FileLogger
from logger import Logger

loggers: List[Logger] = [ConsoleLogger(), FileLogger()]
for logger in loggers:
    logger.log_info('this is an info message')
    logger.log_warning('this is a warning')
    logger.log_error('this is a an error', Exception('some weird exception'))
