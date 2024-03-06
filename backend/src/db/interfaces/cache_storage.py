from abc import ABC, abstractmethod


class ICacheStorage(ABC):
    @abstractmethod
    def set_value(self, key, value, expiration=None):
        """Set a value in the cache with an optional expiration."""
        pass

    @abstractmethod
    def get_value(self, key):
        """Get a value from the cache."""
        pass

    @abstractmethod
    def delete_value(self, key):
        """Delete a value from the cache."""
        pass

    @abstractmethod
    def publish_signal(self, event_type, serialized_data):
        """Publish a signal to a channel in the cache."""
        pass

    @abstractmethod
    def subscribe_signal(self, event_type):
        """Subscribe to a channel to receive signals."""
        pass

    @abstractmethod
    def unsubscribe_signal(self, event_type):
        """Unsubscribe from a channel."""
        pass

    @abstractmethod
    def get_signal(self):
        """Get the next signal message from the subscribed channels."""
        pass
