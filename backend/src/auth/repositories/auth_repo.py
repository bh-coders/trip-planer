from sqlalchemy.orm import Session

from src.auth.interfaces.repository import Repository
from src.auth.models import User
from src.auth.schemas import UserSchema
from src.auth.utils import hash_password


class AuthRepository(Repository):
    def register(self, db: Session, user: UserSchema):
        try:
            with db.begin():
                new_user = User(
                    username=user.username,
                    email=user.email,
                    password=hash_password(user.password),
                )
                db.add(new_user)
            return True
        except Exception as e:
            print(f"Error during user creation: {e}")
            return False
