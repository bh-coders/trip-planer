import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.users.models.user_model import User
from src.users.repositories import ProfileRepository
from src.users.schemas.profile import CreateProfileModel


class ProfileService:
    def __init__(self, repository: ProfileRepository):
        self.profile_repository = repository

    def get_profile_by_user_id(self, user_id: uuid.UUID, db: Session):
        return self.profile_repository.get_profile_by_user_id(user_id, db)
