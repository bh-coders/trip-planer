import logging
import uuid
from typing import List, Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from src.threads.models import Review
from src.threads.schemas.model_schema import (
    ReviewSchema,
    ReviewUpdate,
)

logger = logging.getLogger(__name__)


class ReviewRepository:
    def create_review(self, review: ReviewSchema, db: Session) -> bool:
        try:
            with db.begin():
                new_review = Review(
                    user_id=review.user_id,
                    attraction_id=review.attraction_id,
                    rating=review.rating,
                    price=review.price,
                    time_spent=review.time_spent,
                    title=review.title,
                    description=review.description,
                )
                db.add(new_review)
            return True
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error create review: %s", error)
            return False

    def get_review_by_id(self, review_id: uuid.UUID, db: Session) -> Optional[Review]:
        return (
            db.query(Review)
            .options(joinedload(Review.comments))
            .filter(Review.id == review_id)
            .first()
        )

    def get_reviews_filtered_sorted(
        self,
        db: Session,
        attraction_id: str | int,
        sort_by: Optional[str] = None,
        rating: Optional[int] = None,
        price: Optional[int] = None,
        time_spent: Optional[int] = None,
    ) -> Optional[List[Review]]:
        try:
            query = (
                db.query(Review)
                .options(joinedload(Review.comments))
                .filter(Review.attraction_id == attraction_id)
            )

            if rating is not None:
                query = query.filter(Review.rating == rating)
            if price is not None:
                query = query.filter(Review.price == price)
            if time_spent is not None:
                query = query.filter(Review.time_spent == time_spent)

            if sort_by == "rating":
                query = query.order_by(Review.rating.desc())
            elif sort_by == "price":
                query = query.order_by(Review.price.desc())
            elif sort_by == "time_spent":
                query = query.order_by(Review.time_spent.desc())

            return query.all()
        except SQLAlchemyError as error:
            logger.error("Error getting threads for attraction: %s", error)
            return None

    def delete(self, db: Session, review: Review):
        try:
            with db.begin_nested():
                db.delete(review)
                db.commit()
            return True
        except SQLAlchemyError as e:
            logger.error("Error delete review: %s", e)
            return False

    def update_review(
        self, db: Session, db_review: Review, updated_review: ReviewUpdate
    ) -> Optional[Review]:
        try:
            # we using begin_nested, because we already used session to get db_item
            with db.begin_nested():
                update_data = updated_review.model_dump(exclude_unset=True)
                for key, value in update_data.items():
                    setattr(db_review, key, value)

                db.add(db_review)
                db.commit()
            return db_review
        except Exception as e:
            logger.error("Error update review: %s", e)
            return None
