from pydantic import BaseModel


class MessageSchema(BaseModel):
    message: str
