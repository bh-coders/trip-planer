import logging
import threading
from typing import Callable

from sqlalchemy.orm import Session

from src.common.utils import delay_time
from src.db.interfaces.cache_handler import ICacheHandler

logger = logging.getLogger(__name__)


def publish_handler_event(
    event_type: str,
    data: dict,
    cache_handler: ICacheHandler,
) -> None:
    try:
        logger.info("Start cache storage for publish")
        cache_handler.publish_event(
            event_type=event_type,
            data=data,
        )
        logger.info(
            "Cache storage for published to event_type %s data %s", event_type, data
        )
    except Exception as e:
        logger.error("Failed to handle publish event: %s", e)


def make_thread(func, *args, **kwargs):
    thread = threading.Thread(target=func, args=args, kwargs=kwargs)
    thread.start()
    return thread


def add_task(
    func,
    *args,
    delay=None,
    **kwargs,
):
    def delayed_task():
        if delay:
            delay_time(delay)
        func(*args, **kwargs)

    make_thread(delayed_task)


def run_handler_thread(
    method: Callable,
    event_type: str,
    cache_handler: ICacheHandler,
    db: Session = None,
    *args,
    **kwargs,
) -> None:
    if method:
        if db:
            args += (db,)
        make_thread(lambda: method(event_type, cache_handler, *args, **kwargs))

    else:
        logger.error("No cache storage for subscribe %s", method.__name__)
