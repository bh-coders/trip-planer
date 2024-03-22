from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, TypeVar
from uuid import UUID

from sqlalchemy.orm import Session as SessionType

from src.users.schemas.user import CreateUserSchema

if TYPE_CHECKING:
    from src.users.models.user_model import User

    UserType = TypeVar("UserType", bound=User)


class IUserRepository(ABC):
    @abstractmethod
    def get_by_id(
        self,
        user_id: UUID,
        db: SessionType,
    ) -> Optional["UserType"]:
        pass

    @abstractmethod
    def get_by_username(
        self,
        username: str,
        db: SessionType,
    ) -> Optional["UserType"]:
        pass

    @abstractmethod
    def get_by_email(
        self,
        email: str,
        db: SessionType,
    ) -> Optional["UserType"]:
        pass

    @abstractmethod
    def create_user(
        self,
        user_schema: CreateUserSchema,
        db: SessionType,
    ) -> Optional["UserType"]:
        pass

    @abstractmethod
    def set_is_active(
        self,
        user_obj: "UserType",
        db: SessionType,
    ) -> bool:
        pass

    @abstractmethod
    def update_email(
        self,
        new_email: str,
        user_obj: "UserType",
        db: SessionType,
    ) -> bool:
        pass

    @abstractmethod
    def update_password(
        self,
        new_password: str,
        user_obj: "UserType",
        db: SessionType,
    ) -> bool:
        pass

    @abstractmethod
    def delete_user(
        self,
        user_obj: "UserType",
        db: SessionType,
    ) -> bool:
        pass
