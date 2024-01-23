from abc import ABC, abstractmethod
from uuid import UUID


class User(object):
    pass


class Repository(ABC):
    @abstractmethod
    def get_by_id(self, db, user_id: UUID) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_all(self, db) -> list[User]:
        raise NotImplementedError

    @abstractmethod
    def create(self, db, user: User) -> bool:
        raise NotImplementedError

    @abstractmethod
    def update(self, db, user: User, update_user: dict) -> User:
        raise NotImplementedError

    @abstractmethod
    def delete(self, db, user: User) -> bool:
        raise NotImplementedError

    @abstractmethod
    def change_password(self, db, user: User, user_data: dict) -> User:
        raise NotImplementedError

    @abstractmethod
    def change_email(self, db, user: User, user_data: dict) -> User:
        raise NotImplementedError
