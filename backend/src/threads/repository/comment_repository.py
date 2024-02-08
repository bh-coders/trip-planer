import logging
import uuid
from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.threads.models import Comment
from src.threads.schemas.model_schema import (
    CommentSchema,
    CommentUpdate,
)

logger = logging.getLogger(__name__)


class CommentRepository:
    def get_comment_by_id(
        self, comment_id: uuid.UUID, db: Session
    ) -> Optional[Comment]:
        return db.query(Comment).filter(Comment.id == comment_id).first()

    def add_comment_to_review(self, comment: CommentSchema, db: Session) -> bool:
        try:
            with db.begin_nested():
                new_comment = Comment(
                    content=comment.content,
                    user_id=comment.user_id,
                    created_at=comment.created_at,
                    review_id=comment.review_id,
                )
                db.add(new_comment)
            db.commit()
            return True
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error create comment to review: %s", error)
            return False

    def delete_comment(self, db: Session, comment: Comment):
        try:
            with db.begin_nested():
                db.delete(comment)
                db.commit()
            return True
        except SQLAlchemyError as e:
            logger.error("Error delete comment: %s", e)
            return False

    def update_comment(
        self, db: Session, db_comment: Comment, updated_comment: CommentUpdate
    ) -> Optional[Comment]:
        try:
            # we using begin_nested, because we already used session to get db_item
            with db.begin_nested():
                update_data = updated_comment.model_dump(exclude_unset=True)
                for key, value in update_data.items():
                    setattr(db_comment, key, value)

                db.add(db_comment)
                db.commit()
            return db_comment
        except Exception as e:
            logger.error("Error update review: %s", e)
            return None  # For now I will return False
