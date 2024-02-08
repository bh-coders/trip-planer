import uuid
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, TypeVar

from sqlalchemy.orm import Session as SessionType

from src.users.schemas.user import CreateUserModel

if TYPE_CHECKING:
    from src.users.models.user_model import User

    UserType = TypeVar("UserType", bound=User)


class AbstractUserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: uuid.UUID, db: SessionType) -> None:
        pass

    @abstractmethod
    def get_by_username(self, username: str, db: SessionType) -> None:
        pass

    @abstractmethod
    def get_by_email(self, email: str, db: SessionType) -> None:
        pass

    @abstractmethod
    def create_model(self, user: CreateUserModel, db: SessionType) -> None:
        pass

    @abstractmethod
    def set_is_active(self, user: "UserType", db: SessionType) -> None:
        pass

    @abstractmethod
    def update_email(self, new_email: str, user: "UserType", db: SessionType) -> None:
        pass

    @abstractmethod
    def update_password(
        self, new_password: str, user: "UserType", db: SessionType
    ) -> None:
        pass

    @abstractmethod
    def delete_model(self, user: "UserType", db: SessionType) -> None:
        pass
