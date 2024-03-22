import json
import logging
import time
from enum import Enum
from typing import Any, Optional, Union

from redis import Redis

from src.core.configs import (
    CACHE_STORAGE_EXP,
    CACHE_STORAGE_HOST,
    CACHE_STORAGE_PASSWORD,
    CACHE_STORAGE_PORT,
)
from src.db.interfaces.cache_handler import ICacheHandler
from src.db.interfaces.cache_storage import ICacheStorage

logger = logging.getLogger(__name__)


class CacheKeys(Enum):
    THREAD = "thread:"
    COMMENT = "thread-comment:"
    ATTRACTION = "attraction:"
    ATTRACTION_IMAGES = "attraction-images:"


class RedisStorage(ICacheStorage):
    def __init__(self):
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
        if expiration:
            self.cache.set(key, value, expiration)
        else:
            self.cache.set(key, value, self.expiration_time)

    def get_value(self, key: Any) -> Optional[Any]:
        value = self.cache.get(key)
        if value is not None:
            return value
        return None

    def delete_value(self, key: Any) -> None:
        self.cache.delete(key)

    def publish_signal(
        self,
        event_type: bytes | str | memoryview,
        serialized_data: bytes | memoryview | str | int | float,
    ) -> int:
        return self.cache.publish(channel=event_type, message=serialized_data)

    def subscribe_signal(
        self,
        event_type: list,
    ) -> None:
        self.pubsub.subscribe(*event_type)

    def unsubscribe_signal(
        self,
        event_type: list,
    ) -> None:
        self.pubsub.unsubscribe(*event_type)

    def get_signal(self) -> Optional[Union[None, dict[str, Union[None, str, bytes]]]]:
        while message := self.pubsub.get_message():
            if message and message["type"] == "message":
                return message
            time.sleep(0.2)
        return None


class CacheHandler(ICacheHandler):
    def __init__(self, pool_storage: ICacheStorage):
        self.pool = pool_storage

    def publish_event(self, event_type: str, data: dict) -> None:
        serialized_data = json.dumps(data)
        self.pool.publish_signal(
            event_type=event_type,
            serialized_data=serialized_data,
        )
        logger.info("Published event: %s" % data)

    def subscribe_event(self, event_type: str | list[str]) -> None:
        if isinstance(event_type, str):
            event_type = [event_type]

        self.pool.subscribe_signal(event_type=event_type)

        logger.info("Subscribed to events: %s" % event_type)

    def unsubscribe_event(self, event_type: str | list[str]) -> None:
        if isinstance(event_type, str):
            event_type = [event_type]

        self.pool.unsubscribe_signal(event_type=event_type)

        logger.info("Unsubscribed from events: %s" % event_type)

    def get_event(self) -> Optional[dict]:
        msg = self.pool.get_signal()
        if msg:
            deserialized_data = json.loads(msg["data"])
            logger.info("Received event: %s" % deserialized_data)
            return deserialized_data

        return None
