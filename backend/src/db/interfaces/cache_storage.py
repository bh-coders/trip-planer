from abc import ABC


class CacheStorage(ABC):
    def set_value(self, key, value, expiration=None):
        pass

    def get_value(self, key):
        pass

    def delete_value(self, key):
        pass
