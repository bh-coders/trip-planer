from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class CommentBase(BaseModel):
    review_id: UUID
    content: str

    class Config:
        from_attributes = True


class CommentCreate(CommentBase):
    review_id: UUID
    content: str


class CommentUpdate(CommentBase):
    review_id: UUID
    content: str


class CommentSchema(CommentBase):
    id: Optional[UUID] = None
    user_id: Optional[UUID] = None
    created_at: Optional[datetime] = None


class ReviewUpdate(BaseModel):
    attraction_id: int
    rating: int = Field(gt=0, lt=6)  # Zakres od 1 do 5
    price: int = Field(gt=0, lt=6)  # Zakres od 1 do 5
    time_spent: int
    title: str
    description: str


class ReviewCreate(BaseModel):
    attraction_id: int
    rating: int = Field(gt=0, lt=6)  # Zakres od 1 do 5
    price: int = Field(gt=0, lt=6)  # Zakres od 1 do 5
    time_spent: int
    title: str
    description: str

    class Config:
        from_attributes = True


class ReviewSchema(ReviewCreate):
    id: Optional[UUID] = None
    user_id: Optional[UUID] = None
    comments: list[CommentSchema] = []
