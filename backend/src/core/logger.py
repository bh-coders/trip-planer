import logging
import logging.handlers
import sys

from pythonjsonlogger import jsonlogger

from src.core.configs import BASE_DIR


class LoggerSetup:
    def __init__(self) -> None:
        self.logger = logging.getLogger("")
        self.setup_logging()

    def setup_logging(self):
        # JSON Formatter
        json_formatter = jsonlogger.JsonFormatter(
            "%(asctime)s %(process)s %(levelname)s %(name)s %(module)s %(funcName)s %(lineno)d %(message)s"
        )

        # Console Handler
        console_handler = logging.StreamHandler(sys.stderr)
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(json_formatter)

        # File Handler with JSON formatter
        log_file = BASE_DIR / "logs/api-logs.log"
        file_handler = logging.handlers.TimedRotatingFileHandler(
            filename=log_file, when="midnight", backupCount=5
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(json_formatter)

        # Setting up the root logger
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        root_logger.addHandler(console_handler)
        root_logger.addHandler(file_handler)
