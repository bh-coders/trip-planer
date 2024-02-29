import uuid
from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, model_validator


class MediaBase(BaseModel):
    id: Optional[uuid.UUID] = None
    bucket_name: Optional[str] = None
    file_name: Optional[str] = None
    file_type: Optional[str] = None
    attraction_id: Optional[int] = None
    review_id: Optional[uuid.UUID] = None
    comment_id: Optional[uuid.UUID] = None


class MediaFile(BaseModel):
    file_name: str
    bucket_name: str
    id_object: int | str | uuid.UUID | None = None


class MediaCreate(MediaBase):
    pass

    @model_validator(mode="after")
    def check_one_of_ids_is_present(self):
        attraction_id, review_id, comment_id = (
            self.attraction_id,
            self.review_id,
            self.comment_id,
        )
        if not any([attraction_id, review_id, comment_id]):
            raise ValueError(
                "At least one of attraction_id, review_id, or comment_id must be provided."
            )
        return self


class MediaUpdate(MediaBase):
    updated_at: datetime = datetime.utcnow()


class MediaRead(MediaBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    bucket_name: str
    file_name: str
    file_type: str


class MediaReference(BaseModel):
    attraction_id: Optional[int] = None
    comment_id: Optional[Union[str, uuid.UUID]] = None
    review_id: Optional[Union[str, uuid.UUID]] = None
