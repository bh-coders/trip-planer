from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    email: str
    password: str


class SignInSchema(BaseModel):
    username: str
    password: str
