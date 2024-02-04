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

logger = logging.getLogger(__name__)


class CacheKeys(Enum):
    THREAD = "thread:"
    COMMENT = "thread-comment:"
    ATTRACTION = "attraction:"
    ATTRACTION_IMAGES = "attraction-images:"


class CacheStorage:
    def __init__(
        self,
        host: Optional[str] = None,
        port: Optional[str] = None,
        password: Optional[str] = None,
        expiration: Optional[int] = None,
    ):
        self._host = host or CACHE_STORAGE_HOST
        self._port = port or CACHE_STORAGE_PORT
        self._password = password or CACHE_STORAGE_PASSWORD
        self.cache = self._connect_to_data_store()

        self.expiration_time: int = expiration or CACHE_STORAGE_EXP

    def _connect_to_data_store(self) -> Redis:
        try:
            redis = Redis(
                host=self._host,
                port=self._port,
                password=self._password,
                decode_responses=True,
            )
            return redis
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
