import logging
from enum import Enum
from typing import Optional

from redis import Redis

from src.core.configs import (
    CACHE_STORAGE_EXP,
    CACHE_STORAGE_HOST,
    CACHE_STORAGE_PASSWORD,
    CACHE_STORAGE_PORT,
)
from src.db.interfaces.cache_storage import CacheStorage

logger = logging.getLogger(__name__)


class CacheKeys(Enum):
    THREAD = "thread:"
    COMMENT = "thread-comment:"
    ATTRACTION = "attraction:"
    ATTRACTION_IMAGES = "attraction-images:"


class RedisStorage(CacheStorage):
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
            raise Exception(f"Could not connect to redis server: {e}")

    def set_value(self, key, value, expiration: Optional[int] = None):
        if expiration:
            self.cache.set(key, value, expiration)
        else:
            self.cache.set(key, value, self.expiration_time)

    def get_value(self, key):
        value = self.cache.get(key)
        if value is not None:
            return value
        return None

    def delete_value(self, key):
        self.cache.delete(key)
