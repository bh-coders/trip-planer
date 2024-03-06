import logging
import re
import threading
import time
from typing import Callable

from sqlalchemy.orm import Session

from src.db.interfaces.cache_handler import ICacheHandler

logger = logging.getLogger(__name__)


def publish_handler_event(
    event_type: str,
    data: dict,
    cache_handler: ICacheHandler,
    delay: str,
) -> None:
    try:
        logger.info("Start cache storage for publish")
        if delay:
            delay_time(delay)
        cache_handler.publish_event(
            event_type=event_type,
            data=data,
        )
        logger.info(
            "Cache storage for published to event_type %s data %s", event_type, data
        )
    except Exception as e:
        logger.error("Failed to handle publish event: %s", e)


def publish_handler_thread(
    event_type: str,
    data: dict,
    cache_handler: ICacheHandler,
    delay: str = None,
):
    try:
        thread = threading.Thread(
            target=publish_handler_event,
            args=(event_type, data, cache_handler, delay),
        )
        thread.start()
        logger.info("Handler thread %s started", thread.name)
        return True

    except Exception as e:
        logger.error("Failed to publish handler thread: %s", e)
        return False


def run_handler_thread(
    method: Callable,
    event_type: str,
    cache_handler: ICacheHandler,
    db: Session = None,
) -> None:
    if method:
        if db:
            thread = threading.Thread(
                target=method,
                args=(event_type, cache_handler, db),
            )
        else:
            thread = threading.Thread(
                target=method,
                args=(event_type, cache_handler),
            )
        thread.start()
        logger.info("Handler thread %s started", method.__name__)

    else:
        logger.error("No cache storage for subscribe %s", method.__name__)


def delay_time(time_string="0.2s"):
    units = {"s": 1, "m": 60, "h": 3600, "d": 86400, "y": 31536000}

    match = re.match(r"(\d+)([smhdy])", time_string)
    if match:
        value = int(match.group(1))
        unit = match.group(2)
        total_seconds = value * units[unit]
        time.sleep(total_seconds)
    else:
        logger.error("Invalid time string format: %s", time_string)
        time.sleep(0.2)
