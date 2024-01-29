import uuid
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, TypeVar

from sqlalchemy.orm import Session as SessionType

from src.auth.schemas import UserCreate
from src.auth.schemas.model_schema import UserModel

if TYPE_CHECKING:
    from src.auth.models import User

    UserType = TypeVar("UserType", bound=User)


class Repository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: uuid.UUID, db: SessionType) -> Optional["UserType"]:
        raise NotImplementedError

    @abstractmethod
    def get_by_username(self, username: str, db: SessionType) -> Optional["UserType"]:
        raise NotImplementedError

    @abstractmethod
    def get_by_email(self, email: str, db: SessionType) -> Optional["UserType"]:
        raise NotImplementedError

    @abstractmethod
    def create_user(self, user: UserCreate, db: SessionType) -> bool:
        raise NotImplementedError

    @abstractmethod
    def set_is_active(self, user: UserModel, db: SessionType) -> bool:
        raise NotImplementedError
