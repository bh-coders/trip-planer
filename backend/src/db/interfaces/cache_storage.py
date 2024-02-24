from abc import ABC, abstractmethod
from typing import Any


class CacheStorage(ABC):
    @abstractmethod
    def set_value(self, key: Any, value: Any, expiration=None) -> None:
        pass

    @abstractmethod
    def get_value(self, key: Any) -> None:
        pass

    @abstractmethod
    def delete_value(self, key: Any) -> None:
        pass
