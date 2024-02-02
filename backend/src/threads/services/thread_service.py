import uuid
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from fastapi import HTTPException, Request
from sqlalchemy.orm import Session

from src.auth.utils import get_user_id_from_request
# from src.threads.models import Review
from src.threads.repository.thread_repository import ThreadsRepository
from src.threads.schemas.model_schema import (
    CommentCreate,
    CommentSchema,
    CommentUpdate,
    ReviewCreate,
    ReviewSchema,
    ReviewUpdate,
)

if TYPE_CHECKING:
    from src.threads.models import Review


class ThreadsService:
    def __init__(self, repository: ThreadsRepository):
        self.repository = repository

    def create(self, request: Request, thread: ReviewCreate, db: Session) -> bool:
        user_id = get_user_id_from_request(request)
        if not user_id:
            raise HTTPException(
                status_code=401, detail="Cannot find user_id in token payload."
            )
        new_review = ReviewSchema(
            user_id=user_id,
            attraction_id=thread.attraction_id,
            rating=thread.rating,
            price=thread.price,
            time_spent=thread.time_spent,
            title=thread.title,
            description=thread.description,
        )
        return self.repository.create_review(new_review, db)

    def get_thread_by_id(
            self, thread_id: uuid.UUID, db: Session
    ) -> Optional[ReviewSchema]:
        review = self.repository.get_review_by_id(thread_id, db)
        if not review:
            raise HTTPException(
                status_code=404, detail=f"Cannot find review with review_id={thread_id}"
            )
        return ReviewSchema(**review.as_dict())

    def get_threads_attraction_filtered_sorted(
            self,
            db: Session,
            attraction_id: str | int,
            sort_by: Optional[str] = None,
            rating: Optional[int] = None,
            price: Optional[int] = None,
            time_spent: Optional[int] = None,
    ) -> List[ReviewSchema]:
        reviews: Optional[List[Review]] = self.repository.get_reviews_filtered_sorted(
            db, attraction_id, sort_by, rating, price, time_spent
        )
        if not reviews:
            raise HTTPException(
                status_code=404,
                detail=f"Cannot find reviews for attraction_id={attraction_id}",
            )

        review_schemas = [ReviewSchema(**review.as_dict()) for review in reviews]

        return review_schemas

    def comment_thread(
            self, request: Request, comment: CommentCreate, db: Session
    ) -> bool:
        user_id = get_user_id_from_request(request)
        if not user_id:
            raise HTTPException(
                status_code=401, detail="Cannot find user_id in token payload."
            )
        new_comment = CommentSchema(
            review_id=comment.review_id,
            user_id=user_id,
            content=comment.content,
            created_at=datetime.utcnow(),
        )
        return self.repository.add_comment_to_review(new_comment, db)

    def delete_thread(self, db: Session, review_id: uuid.UUID):
        thread = self.repository.get_review_by_id(review_id, db)
        if thread is None:
            raise HTTPException(
                status_code=404, detail=f"Not found review_id={review_id}."
            )
        return self.repository.delete(db, thread)

    def delete_comment(self, db: Session, comment_id: uuid.UUID):
        comment = self.repository.get_comment_by_id(comment_id, db)
        if comment is None:
            raise HTTPException(
                status_code=404, detail=f"Not found comment_id={comment_id}."
            )
        return self.repository.delete_comment(db, comment)

    def update_thread(
            self, db: Session, review_id: uuid.UUID, updated_review: ReviewUpdate
    ) -> ReviewSchema:
        thread = self.repository.get_review_by_id(review_id, db)
        if thread is None:
            raise HTTPException(
                status_code=404, detail=f"Not found review_id={review_id}."
            )
        updated = self.repository.update_review(db, thread, updated_review)
        return ReviewSchema(**updated.as_dict())

    def update_comment(
            self, db: Session, comment_id: uuid.UUID, updated_comment: CommentUpdate
    ):
        comment = self.repository.get_comment_by_id(comment_id, db)
        if comment is None:
            raise HTTPException(
                status_code=404, detail=f"Not found comment_id={comment_id}."
            )
        updated = self.repository.update_comment(db, comment, updated_comment)

        return CommentSchema(**updated.as_dict())
