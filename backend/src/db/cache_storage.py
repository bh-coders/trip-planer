import json
import logging
import time
from enum import Enum
from typing import Any, Awaitable, Optional, Union

from redis import Redis

from src.core.configs import (
    CACHE_STORAGE_EXP,
    CACHE_STORAGE_HOST,
    CACHE_STORAGE_PASSWORD,
    CACHE_STORAGE_PORT,
)
from src.db.interfaces import CacheStorage, ICacheHandler

logger = logging.getLogger(__name__)
ResponseT = Union[Awaitable, Any]


class CacheKeys(Enum):
    THREAD = "thread:"
    COMMENT = "thread-comment:"
    ATTRACTION = "attraction:"
    USER = "user:"
    ATTRACTION_IMAGES = "attraction-images:"


class RedisStorage(CacheStorage):
    def __init__(self):
        """
        Initialize the RedisStorage class by connecting to the Redis server.

        Raises:
            ValueError: If connection to the Redis server fails.
        """
        self.expiration_time: int = CACHE_STORAGE_EXP
        try:
            self.cache = Redis(
                host=CACHE_STORAGE_HOST,
                port=CACHE_STORAGE_PORT,
                password=CACHE_STORAGE_PASSWORD,
                decode_responses=True,
            )
        except Exception as e:
            logger.error("Could not connect to redis server: %s" % e)
            raise ValueError(f"Could not connect to redis server: {e}")

        self.pubsub = self.cache.pubsub()

    def set_value(self, key: Any, value: Any, expiration: Optional[int] = None) -> None:
        """
        Set a key-value pair in the cache with an optional expiration time.

        Args:
            key (Any): The key to set in the cache.
            value (Any): The value to set in the cache.
            expiration (Optional[int]): The expiration time in seconds (default is None).

        Returns:
            None
        """
        if expiration:
            self.cache.set(key, value, expiration)
        else:
            self.cache.set(key, value, self.expiration_time)

    def get_value(self, key: Any) -> Optional[Awaitable]:
        """
        Get the value associated with the given key from the cache.

        Args:
            key (Any): The key to retrieve the value for.

        Returns:
            Optional[Awaitable]: The value associated with the key, or None if key is not found.
        """
        value = self.cache.get(key)
        if value is not None:
            return value
        return None

    def delete_value(self, key: Any) -> None:
        """
        Delete the key-value pair from the cache.

        Args:
            key (Any): The key to delete from the cache.

        Returns:
            None
        """
        self.cache.delete(key)

    def publish_signal(
        self,
        pattern: bytes | str | memoryview,
        serialized_data: bytes | memoryview | str | int | float,
    ) -> Awaitable:
        """
        Publish a signal to a channel in the cache.

        Args:
            pattern (bytes | str | memoryview): The channel to publish the signal to.
            serialized_data (bytes | memoryview | str | int | float): The data to publish.

        Returns:
            Awaitable
        """
        return self.cache.publish(channel=pattern, message=serialized_data)

    def subscribe_signal(
        self,
        pattern: list,
    ) -> None:
        """
        Subscribe to one or more channels to receive signals.

        Args:
            pattern (list): List of channels to subscribe to.

        Returns:
            None
        """
        self.pubsub.subscribe(*pattern)

    def unsubscribe_signal(
        self,
        pattern: list,
    ) -> None:
        """
        Unsubscribe from one or more channels.

        Args:
            pattern (list): List of channels to unsubscribe from.

        Returns:
            None
        """
        self.pubsub.unsubscribe(*pattern)

    def get_signal(self) -> Optional[Union[None, dict[str, Union[None, str, bytes]]]]:
        """
        Get the next signal message from the subscribed channels.

        Returns:
            Optional[Union[None, dict[str, Union[None, str, bytes]]]]
        """
        while message := self.pubsub.get_message():
            if message and message["type"] == "message":
                return message
            time.sleep(0.2)
        return None


class CacheHandler(ICacheHandler):
    def __init__(self, redis: RedisStorage):
        """
        Initialize the CacheHandler with the provided RedisStorage instance.

        Args:
            redis (RedisStorage): The RedisStorage instance to use for caching.
        """
        self.redis = redis

    def publish_event(self, pattern: str, data: dict) -> None:
        """
        Publish an event with the specified pattern and data.

        Args:
            pattern (str): The pattern to publish the event under.
            data (dict): The data to be published.

        Returns:
            None
        """
        serialized_data = json.dumps(data)
        self.redis.publish_signal(
            pattern=pattern,
            serialized_data=serialized_data,
        )
        logger.info("Published event: %s" % data)

    def subscribe_event(self, pattern: str | list[str]) -> None:
        """
        Subscribe to events with the specified pattern(s).

        Args:
            pattern (str | list[str]): The pattern(s) to subscribe to.

        Returns:
            None
        """
        if isinstance(pattern, str):
            pattern = [pattern]

            self.redis.subscribe_signal(pattern=pattern)

        logger.info("Subscribed to events: %s" % pattern)

    def unsubscribe_event(self, pattern: str | list[str]) -> None:
        """
        Unsubscribe from events with the specified pattern(s).

        Args:
            pattern (str | list[str]): The pattern(s) to unsubscribe from.

        Returns:
            None
        """
        if isinstance(pattern, str):
            pattern = [pattern]

            self.redis.unsubscribe_signal(pattern=pattern)

        logger.info("Unsubscribed from events: %s" % pattern)

    def get_event(self) -> Optional[dict]:
        """
        Get the next event from the cache.

        Returns:
            Optional[dict]
        """
        if msg := self.redis.get_signal():
            deserialized_data = json.loads(msg["data"])
            logger.info("Received event: %s" % deserialized_data)
            return deserialized_data

        return None
