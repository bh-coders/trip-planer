import logging
import logging.handlers
import sys

from pythonjsonlogger import jsonlogger

from src.core.configs import LOGS_DIR, LOGS_FILE_PATH


class LoggerSetup:
    def __init__(self) -> None:
        self.create_logging_dir()
        self.logger = logging.getLogger("")
        self.setup_logging()

    @staticmethod
    def create_logging_dir():
        if not LOGS_DIR.exists():
            LOGS_DIR.mkdir(parents=True, exist_ok=True)
        if not LOGS_FILE_PATH.exists():
            LOGS_FILE_PATH.touch()

    @staticmethod
    def setup_logging():
        # JSON Formatter
        json_formatter = jsonlogger.JsonFormatter(
            "%(asctime)s %(process)s %(levelname)s %(name)s %(module)s %(funcName)s %(lineno)d %(message)s"
        )

        # Console Handler
        console_handler = logging.StreamHandler(sys.stderr)
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(json_formatter)

        # File Handler with JSON formatter
        file_handler = logging.handlers.TimedRotatingFileHandler(
            filename=LOGS_FILE_PATH, when="midnight", backupCount=5
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(json_formatter)

        # Setting up the root logger
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        root_logger.addHandler(console_handler)
        root_logger.addHandler(file_handler)
