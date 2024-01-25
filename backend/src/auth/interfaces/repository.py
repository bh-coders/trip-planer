from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id, db):
        pass

    @abstractmethod
    def authenticate(self, username, password, db):
        pass

    @abstractmethod
    def get_user(self, username, db):
        pass

    @abstractmethod
    def register(self, user, db):
        pass
