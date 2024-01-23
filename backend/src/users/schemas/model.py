from pydantic import BaseModel


class UserSchema(BaseModel):
    id: str
    name: str
    surname: str
    email: str
    password: str
    username: str
    is_active: bool
    is_superuser: bool
    attraction: list


class UserCreateSchema(BaseModel):
    name: str
    surname: str
    email: str
    password: str
    second_password: str
    username: str


class UserUpdateSchema(BaseModel):
    name: str
    surname: str
    username: str


class ChangePasswordSchema(BaseModel):
    old_password: str
    new_password: str
    second_new_password: str


class ChangeEmailSchema(BaseModel):
    new_email: str
    password: str
