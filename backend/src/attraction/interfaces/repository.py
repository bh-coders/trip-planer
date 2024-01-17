from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, item_id):
        pass

    @abstractmethod
    def create(self, item):
        pass

    @abstractmethod
    def update(self, item):
        pass

    @abstractmethod
    def delete(self, item_id):
        pass
