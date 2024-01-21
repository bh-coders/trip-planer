from sqlalchemy.orm import Session

from src.auth.interfaces.repository import Repository
from src.auth.schemas import UserSchema, SignInSchema


class AuthService:
    def __init__(self, repository: Repository):
        self._repository = repository

    def register_user(self, db: Session, user: UserSchema):
        return self._repository.register(db, user)

    def sign_in_user(self, db: Session, sign_in_user: SignInSchema):
        return self._repository.sign_in(db, sign_in_user)
