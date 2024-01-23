import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.users.repositories import UserRepository, repo
from src.users.schemas import (
    ChangeEmailSchema,
    ChangePasswordSchema,
    UserCreateSchema,
    UserListSchema,
    UserSchema,
    UserUpdateSchema,
)


class UserService:
    def __init__(self):
        self.repo: UserRepository = repo

    def get_all_users(self, db: Session) -> UserListSchema | None:
        return self.repo.get_all(db)

    def get_user_by_id(self, db: Session, user_id: uuid.UUID) -> UserSchema | None:
        return self.repo.get_by_id(db, user_id)

    def create_user(self, db: Session, user: UserCreateSchema) -> bool:
        return self.repo.create(db, user)

    def update_user(
        self, db: Session, user_id: uuid.UUID, update_user: UserUpdateSchema
    ) -> UserSchema | None:
        user = self.repo.get_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return self.repo.update(db, user, update_user)

    def delete_user(self, db: Session, user_id: uuid.UUID) -> bool:
        user = self.repo.get_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return self.repo.delete(db, user)

    def change_email(
        self, db: Session, user_id: uuid.UUID, user_data: ChangeEmailSchema
    ) -> bool:
        user = self.repo.get_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return self.repo.change_email(db, user, user_data)

    def change_password(
        self, db: Session, user_id: uuid.UUID, user_data: ChangePasswordSchema
    ) -> bool:
        user = self.repo.get_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return self.repo.change_password(db, user, user_data)
