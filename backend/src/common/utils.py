import logging
import threading

from src.db.cache_storage import CacheHandler, RedisStorage

logger = logging.getLogger(__name__)


def publish_handler_event(pattern: str, data: dict) -> None:
    """
    Publishes an event to a cache storage system.

    Parameters:
    pattern (str): The pattern of the event.
    data (dict): The data associated with the event.

    Returns:
    None
    """
    cache_handler = CacheHandler(redis=RedisStorage())
    logger.info("Start cache storage for publish")
    cache_handler.publish_event(
        pattern=pattern,
        data=data,
    )
    logger.info("Cache storage for published to pattern %s data %s", pattern, data)


def run_handler_thread(
    cls: object,
    subscribe_name: str = None,
    handler_name: str = None,
) -> None:
    """
    Run a handler method in a separate thread.

    Args:
        cls (object): The class object containing the handler method.
        subscribe_name (str): The name of the subscription. Defaults to None.
        handler_name (str): The name of the handler method to be executed. Defaults to None.

    Returns:
        None

    """
    cache_handler = CacheHandler(redis=RedisStorage())
    if cache_handler:
        logger.info("Start cache storage for subscribe %s", handler_name)
        if handler_name and cls and hasattr(cls, handler_name):
            method = getattr(cls, handler_name, None)
            if method:
                thread = threading.Thread(
                    target=method,
                    args=(cache_handler, subscribe_name),
                )
                thread.start()
                logger.info(
                    "Handler thread %s started for %s",
                    handler_name,
                    cls.__class__.__name__,
                )
