from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, TypeVar

if TYPE_CHECKING:
    from src.db.interfaces import ICacheStorage

    ICacheStorageType = TypeVar("ICacheStorageType", bound=ICacheStorage)


class ICacheHandler(ABC):
    @abstractmethod
    def __init__(self, pool_storage: "ICacheStorageType"):
        pass

    @abstractmethod
    def publish_event(self, event_type: str, data: dict) -> None:
        pass

    @abstractmethod
    def subscribe_event(self, event_type: str | list[str]) -> None:
        pass

    @abstractmethod
    def unsubscribe_event(self, event_type: str | list[str]) -> None:
        pass

    @abstractmethod
    def get_event(self) -> Any:
        pass
