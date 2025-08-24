from enum import Enum
from pathlib import Path

class Log:
    class LogLvL(Enum):
        INFO = 1
        DEBUG = 2
        WARNING = 3
        ERROR = 4

    __log_file = Path("./logging2.log")
    # __size = len(max(LogLvL._member_names_, key=lambda x: len(x)))

    def __log(self, lvl: LogLvL, fmt:str, *fmt_args):
        with self.__log_file.open("+a") as file:
            file.write(f"[{lvl.name}]: {fmt.format(*fmt_args)}\n")
    
    def info(self, fmt:str, *fmt_args):
        self.__log(self.LogLvL.INFO, fmt, *fmt_args)
    
    def debug(self, fmt:str, *fmt_args):
        self.__log(self.LogLvL.DEBUG, fmt, *fmt_args)
    
    def warning(self, fmt:str, *fmt_args):
        self.__log(self.LogLvL.WARNING, fmt, *fmt_args)
    
    def error(self, fmt:str, *fmt_args):
        self.__log(self.LogLvL.ERROR, fmt, *fmt_args)
    

if __name__ == "__main__":
    log = Log()
    log.debug("stuff {1:.3f} {0}", "hello", 3.1432543252)
    log.info("some info")
    log.warning("some warning")
    log.error("oops, error")