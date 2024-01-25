from sqlalchemy.orm import Session

from src.auth.interfaces.repository import Repository
from src.auth.schemas import SignInSchema, UserSchema


class AuthService:
    def __init__(self, repository: Repository):
        self._repository = repository

    def register_user(self, user: UserSchema, db: Session):
        return self._repository.register(user, db)

    def sign_in_user(self, sign_in_user: SignInSchema, db: Session):
        return self._repository.sign_in(sign_in_user, db)
