import logging
import threading
from functools import wraps

logger = logging.getLogger(__name__)


def start_listening_if_supported(service: object) -> None:
    if hasattr(service, "event_handler"):
        logger.info("Start event handler")
        service.event_handler()
    else:
        logger.error("Service does not support listening")


def start_events(services: list[object]) -> None:
    for service in services:
        start_listening_if_supported(
            service=service,
        )


def start_listening(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        logger.info("Start listening for events")
        return thread

    return wrapper
