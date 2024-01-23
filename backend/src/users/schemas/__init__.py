from typing import List, Type

from src.users.schemas.model import (
    ChangeEmailSchema,
    ChangePasswordSchema,
    UserCreateSchema,
    UserSchema,
    UserUpdateSchema,
)

UserListSchema = List[Type[UserSchema]]

__all__ = [
    "UserSchema",
    "UserUpdateSchema",
    "ChangePasswordSchema",
    "ChangeEmailSchema",
    "UserCreateSchema",
    "UserListSchema",
]
