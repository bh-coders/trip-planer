from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def get_all(self, db):
        pass

    @abstractmethod
    def get_by_id(self, db, attraction_id):
        pass

    @abstractmethod
    def create(self, db, attraction):
        pass

    def update(self, db, db_attraction, updated_attraction):
        pass

    def delete(self, db, attraction):
        pass

    def search(self, db, name, country, state, city):
        pass
