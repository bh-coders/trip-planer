import json
import logging
import time
from enum import Enum
from typing import Optional
from uuid import UUID

from redis import Redis

from src.core.configs import (
    CACHE_STORAGE_EXP,
    CACHE_STORAGE_HOST,
    CACHE_STORAGE_PASSWORD,
    CACHE_STORAGE_PORT,
)
from src.db.database import Base

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
        self.pubsub = self.cache.pubsub()
        self.client = self.RedisPubSub(
            redis=self.cache,
            client=self.pubsub,
        )

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

    class RedisPubSub:
        def __init__(self, redis, client):
            self.redis = redis
            self.client = client

        def publish(
            self,
            pattern: str,
            data: Optional[int | str | dict | float] = None,
            suffix: Optional[str] = None,
        ):
            try:
                pattern = f"{pattern}:{suffix}" if suffix else pattern
                if isinstance(data, dict):
                    data = json.dumps(data)
                self.redis.publish(pattern, data)
                logger.info(f"Published signal: {data} to pattern: {pattern}")
                return True
            except Exception as e:
                logger.error("Could not publish signal: %s" % e)
                return False

        def subscribe(
            self,
            channel: str,
            suffix: Optional[str] = None,
        ):
            full_channel = f"{channel}:{suffix}" if suffix else channel
            self.client.subscribe(full_channel)
            logger.info("Subscribed to channel: %s", full_channel)

        def unsubscribe(self, channel: str, suffix: Optional[str] = None):
            full_channel = f"{channel}:{suffix}" if suffix else channel
            self.client.unsubscribe(full_channel)
            logger.info("Unsubscribed from channel: %s", full_channel)

        def message(self):
            message = self.client.get_message()
            if message is not None:
                message_type = message["type"]
                if message_type == "message":
                    message_data = message["data"]
                    if isinstance(
                        message_data,
                        str,
                    ):
                        try:
                            message_data = json.loads(message_data)
                        except json.decoder.JSONDecodeError:
                            pass

                    logger.info("Received message: %s", message_data)
                    return message_data

                elif message_type == "subscribe":
                    if message.get("pattern") is not None:
                        logger.info("Subscribed to pattern: %s", message["pattern"])
                    else:
                        logger.info("Subscribed")
                elif message_type == "unsubscribe":
                    logger.info("Unsubscribed from pattern: %s", message["pattern"])
                else:
                    logger.warning(
                        "Received unhandled message type: %s. Message data: %s",
                        message_type,
                        message.get("data"),
                    )
            return None


class CacheModel:
    cache = CacheStorage()

    def add(
        self,
        model: Base,
        data: dict | str | int | float,
        model_id: Optional[int | str | UUID] = None,
    ):
        if model_id is not None:
            model_id = str(model_id)
        self.cache.client.publish(
            pattern=model.__tablename__,
            suffix=model_id,
            data=data,
        )

    def connect(
        self,
        model: Base,
        model_id: Optional[int | str | UUID] = None,
        many: Optional[bool] = False,
    ):
        if model_id is not None:
            model_id = str(model_id)
        suffix = model_id
        if many:
            suffix = "*"
        self.cache.client.subscribe(
            channel=model.__tablename__,
            suffix=suffix,
        )

    def disconnect(
        self,
        model: Base,
        model_id: Optional[int | str | UUID] = None,
    ):
        self.cache.client.unsubscribe(model.__tablename__, model_id)

    def get(self):
        while True:
            message = self.cache.client.message()
            if message:
                return message
            time.sleep(0.1)
