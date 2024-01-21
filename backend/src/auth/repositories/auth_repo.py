from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.auth.interfaces.repository import Repository
from src.auth.models import User
from src.auth.schemas import UserSchema, SignInSchema
from src.auth.utils import hash_password, check_password, return_token




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

                return return_token(new_user)

        except Exception as e:
            print(f"Error during user creation: {e}")
            return False


    def sign_in(self, db, sign_in_user: SignInSchema):
        user = db.query(User).filter_by(username=sign_in_user.username).first()
        if user and check_password(sign_in_user.password, user.password):
            return return_token(user)

        raise HTTPException(status_code=401, detail="Invalid credentials")