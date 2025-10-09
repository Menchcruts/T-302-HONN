from structured_logging.configuration.environment import Environment

from structured_logging.processors.null_processor import NullProcessor
from structured_logging.processors.timestamp_processor import TimestampProcessor
from structured_logging.processors.environment_processor import EnvironmentProcessor

from structured_logging.sinks.console_sink import ConsoleSink

if __name__ == "__main__":
    env = Environment.STAGING
    data = {
        "message": "Order started"
    }
    sink = ConsoleSink()
    sink.sink_data(data)
    
    null_processor = NullProcessor()
    ts_processor = TimestampProcessor()
    env_processor = EnvironmentProcessor(env)

    ts_processor.set_next(env_processor)
    null_processor.set_next(ts_processor)
    
    null_processor.handle(data)
    sink.sink_data(data)