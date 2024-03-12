from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from src.file.models.schemas import MediaRead


class CommentBase(BaseModel):
    review_id: UUID
    content: str

    class Config:
        from_attributes = True


class CommentCreate(CommentBase):
    pass


class CommentUpdate(CommentBase):
    pass


class CommentSchema(CommentBase):
    id: Optional[UUID] = None
    user_id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    media: list[
        MediaRead
    ] = []  # Something to think about is whether we need so much data


class ReviewBase(BaseModel):
    attraction_id: int
    rating: int = Field(gt=0, lt=6)  # Range from 1 to 5
    price: int = Field(gt=0, lt=6)  # (1 $, 2 $-$$, 3 $$, 4 $$-$$$, 5 $$$)
    time_spent: int
    title: str
    description: str

    class Config:
        from_attributes = True


class ReviewUpdate(ReviewBase):
    pass


class ReviewCreate(ReviewBase):
    pass


class ReviewSchema(ReviewCreate):
    id: Optional[UUID] = None
    user_id: Optional[UUID] = None
    comments: list[CommentSchema] = []
    media: list[
        MediaRead
    ] = []  # Something to think about is whether we need so much data
