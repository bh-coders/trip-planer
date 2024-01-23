import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.users.exceptions import UserCreationError, UserDeleteError, UserUpdateError
from src.users.interfaces import RepositoryInterface
from src.users.models import User
from src.users.schemas import (
    ChangeEmailSchema,
    ChangePasswordSchema,
    UserCreateSchema,
    UserListSchema,
    UserSchema,
    UserUpdateSchema,
)


class UserRepository(RepositoryInterface):
    def __init__(self, *args, **kwargs):
        self.model = User
        super().__init__(*args, **kwargs)

    def get_by_id(self, db: Session, user_id: uuid.UUID) -> UserSchema | None:
        user = db.query(self.model).filter(self.model.id == user_id).first()
        return user

    def get_all(self, db: Session) -> UserListSchema | None:
        users = db.query(self.model).all()
        return users

    def create(
        self,
        db: Session,
        user: UserCreateSchema,
    ) -> bool:
        if user.password != user.second_password:
            raise ValueError("Passwords don't match")
        try:
            with db.begin():
                new_user = User(
                    name=user.name,
                    surname=user.surname,
                    email=user.email,
                    password=user.password,
                    username=user.username,
                )
                db.add(new_user)
                return True
        except UserCreationError:
            raise HTTPException(status_code=400, detail="Can't create user")

    def update(
        self,
        db: Session,
        user: UserSchema,
        update_user: UserUpdateSchema,
    ) -> UserSchema:
        try:
            with db.begin_nested():
                update_data = update_user.model_dump(exclude_unset=True)
                for key, value in update_data.items():
                    setattr(user, key, value)
                db.add(user)
                db.commit()
                db.refresh(user)
                return user
        except UserUpdateError:
            raise HTTPException(status_code=400, detail="Can't update user")

    def delete(self, db: Session, user: UserSchema) -> bool:
        try:
            with db.begin_nested():
                db.delete(user)
                db.commit()
            return True
        except UserDeleteError:
            raise HTTPException(status_code=400, detail="Can't delete user")

    def change_email(
        self,
        db: Session,
        user: UserSchema,
        user_data: ChangeEmailSchema,
    ) -> bool:
        if user_data.new_email == user.email:
            raise ValueError("New email is the same as old one")
        try:
            user = (
                db.query(self.model)
                .filter(
                    self.model.email == user_data.new_email,
                    self.model.password == user_data.password,
                )
                .first()
            )
            user.email = user.new_email
            db.add(user)
            db.commit()
            return True
        except UserUpdateError:
            raise HTTPException(status_code=400, detail="Wrong email")

    def change_password(
        self, db: Session, user: UserSchema, user_data: ChangePasswordSchema
    ) -> bool:
        if user_data.new_password != user_data.second_new_password:
            raise HTTPException(status_code=400, detail="Passwords don't match")
        if user.password != user_data.old_password:
            raise HTTPException(status_code=400, detail="Wrong old password")
        user.password = user_data.new_password
        db.add(user)
        db.commit()
        return True
