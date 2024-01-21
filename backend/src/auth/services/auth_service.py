from sqlalchemy.orm import Session

from src.auth.interfaces.repository import Repository
from src.auth.schemas import UserSchema


class AuthService:
    def __init__(self, repository: Repository):
        self._repository = repository

    def register_user(self, db: Session, user: UserSchema):
        return self._repository.register(db, user)
