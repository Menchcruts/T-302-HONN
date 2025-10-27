from structured_logging.processors.abstract_processor import AbstractProcessor
from structured_logging.configuration.environment import Environment

class EnvironmentProcessor(AbstractProcessor):
    __environment: str = ""
    def __init__(self, env: Environment):
        super().__init__()
        self.__environment = env.name.lower()
    
    def _process_data(self, data):
        data.setdefault("environment", self.__environment)