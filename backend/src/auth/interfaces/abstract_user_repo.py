import uuid
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, TypeVar

from sqlalchemy.orm import Session as SessionType

from src.auth.schemas import CreateUserSchema

if TYPE_CHECKING:
    from src.auth.models import User

    UserType = TypeVar("UserType", bound=User)


class AbstractUserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: uuid.UUID, db: SessionType) -> Optional["UserType"]:
        pass

    @abstractmethod
    def get_by_username(self, username: str, db: SessionType) -> Optional["UserType"]:
        pass

    @abstractmethod
    def get_by_email(self, email: str, db: SessionType) -> Optional["UserType"]:
        pass

    @abstractmethod
    def create_model(self, user: CreateUserSchema, db: SessionType) -> bool:
        pass

    @abstractmethod
    def set_is_active(self, user: UserModel, db: SessionType) -> bool:
        pass

    @abstractmethod
    def update_email(self, new_email: str, user: "UserType", db: SessionType) -> bool:
        pass

    @abstractmethod
    def update_password(
        self, new_password: str, user: "UserType", db: SessionType
    ) -> bool:
        pass

    @abstractmethod
    def delete_model(self, user: "UserType", db: SessionType) -> bool:
        pass
