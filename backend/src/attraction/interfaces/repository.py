from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def get_all(self, db):
        pass

    @abstractmethod
    def get_by_id(self, db, item_id):
        pass

    @abstractmethod
    def create(self, db, item):
        pass

    def update(self, db, db_item, updated_item):
        pass

    def delete(self, db, item):
        pass
