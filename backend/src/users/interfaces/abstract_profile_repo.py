from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, TypeVar
from uuid import UUID

from sqlalchemy.orm import Session as SessionType

if TYPE_CHECKING:
    from src.users.models import Profile
    from src.users.models.user_model import User
    from src.users.schemas.profile import UpdateProfileModel

    UserType = TypeVar("UserType", bound=User)
    ProfileType = TypeVar("ProfileType", bound=Profile)
    UpdateProfileModelType = TypeVar(
        "UpdateProfileModelType",
        bound=UpdateProfileModel,
    )


class AbstractProfileRepository(ABC):
    @abstractmethod
    def get_by_id(
        self,
        profile_id: UUID,
        db: SessionType,
    ) -> None:
        pass

    @abstractmethod
    def create_profile(
        self,
        name: str,
        surname: str,
        user_id: UUID,
        db: SessionType,
    ) -> None:
        pass

    @abstractmethod
    def get_profile_by_user_id(
        self,
        user_id: UUID,
        db: SessionType,
    ) -> None:
        pass

    @abstractmethod
    def update_profile(
        self,
        profile: "ProfileType",
        profile_update: "UpdateProfileModelType",
        db: SessionType,
    ) -> None:
        pass

    @abstractmethod
    def delete_profile(
        self,
        profile_id: UUID,
        db: SessionType,
    ) -> None:
        pass
