from abc import ABC, abstractmethod
from typing import Any


class ICacheHandler(ABC):
    @abstractmethod
    def publish_event(self, pattern: str, data: dict) -> None:
        pass

    @abstractmethod
    def subscribe_event(self, pattern: str | list[str]) -> None:
        pass

    @abstractmethod
    def unsubscribe_event(self, pattern: str | list[str]) -> None:
        pass

    @abstractmethod
    def get_event(self) -> Any:
        pass
