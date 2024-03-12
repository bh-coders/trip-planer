import json
import uuid
from typing import TYPE_CHECKING, List, Optional

import orjson
from fastapi import HTTPException, Response
from sqlalchemy.orm import Session

from src.db.cache_storage import CacheKeys
from src.db.interfaces.cache_storage import ICacheStorage
from src.threads.repository.review_repository import ReviewRepository
from src.threads.schemas.model_schema import (
    ReviewCreate,
    ReviewSchema,
    ReviewUpdate,
)

if TYPE_CHECKING:
    from src.threads.models import Review


class ReviewService:
    def __init__(self, repository: ReviewRepository, cache: ICacheStorage):
        self.repository = repository
        self.cache = cache

    def create(
        self,
        user_id: uuid.UUID,
        thread: ReviewCreate,
        db: Session,
    ) -> Response:
        new_review = ReviewSchema(
            user_id=user_id,
            attraction_id=thread.attraction_id,
            rating=thread.rating,
            price=thread.price,
            time_spent=thread.time_spent,
            title=thread.title,
            description=thread.description,
        )
        if not self.repository.create_review(new_review, db):
            raise HTTPException(status_code=400, detail="Review could not be created.")
        return Response(status_code=201, content="Review successfully created.")

    def get_thread_by_id(self, thread_id: uuid.UUID, db: Session) -> ReviewSchema:
        cache_key = CacheKeys.THREAD.value + str(thread_id)
        cache_review = self.cache.get_value(cache_key)
        if cache_review:
            review_data = json.loads(cache_review)
            return ReviewSchema(**review_data)

        review = self.repository.get_review_by_id(thread_id, db)
        if not review:
            raise HTTPException(
                status_code=404, detail=f"Cannot find review with review_id={thread_id}"
            )

        self.cache.set_value(cache_key, orjson.dumps(review.as_dict()))
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

    def delete_thread(self, db: Session, review_id: uuid.UUID) -> Response:
        cache_key = CacheKeys.THREAD.value + str(review_id)
        thread = self.repository.get_review_by_id(review_id, db)
        if thread is None:
            raise HTTPException(
                status_code=404, detail=f"Not found review_id={review_id}."
            )
        if not self.repository.delete(db, thread):
            raise HTTPException(status_code=400, detail="Review could not be deleted.")
        self.cache.delete_value(cache_key)
        return Response(status_code=200, content="Review deleted")

    def update_thread(
        self, db: Session, review_id: uuid.UUID, updated_review: ReviewUpdate
    ) -> ReviewSchema:
        cache_key = CacheKeys.THREAD.value + str(review_id)
        thread = self.repository.get_review_by_id(review_id, db)
        if thread is None:
            raise HTTPException(
                status_code=404, detail=f"Not found review_id={review_id}."
            )
        updated = self.repository.update_review(db, thread, updated_review)
        if not updated:
            raise HTTPException(status_code=402, detail="Cannot update review.")
        self.cache.set_value(cache_key, orjson.dumps(updated.as_dict()))
        return ReviewSchema(**updated.as_dict())
