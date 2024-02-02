import uuid
from abc import ABC, abstractmethod
from typing import List, Optional

from sqlalchemy.orm import Session as SessionType

from src.threads.models import (
    Comment,
    Review,
)

# Załóżmy, że te modele są zdefiniowane gdzie indziej
from src.threads.schemas.model_schema import (
    CommentSchema,
    ReviewSchema,
)


class Repository(ABC):
    @abstractmethod
    def get_review_by_id(
        self, review_id: uuid.UUID, db: SessionType
    ) -> Optional[Review]:
        pass

    @abstractmethod
    def get_reviews_filtered_sorted(
        self,
        db: SessionType,
        attraction_id: int,
        sort_by: Optional[str] = None,
        rating: Optional[int] = None,
        price: Optional[int] = None,
        time_spent: Optional[int] = None,
    ) -> List[Review]:
        pass

    @abstractmethod
    def create_review(self, review: ReviewSchema, db: SessionType) -> Review:
        pass

    @abstractmethod
    def add_comment_to_review(self, comment: CommentSchema, db: SessionType) -> Comment:
        pass
