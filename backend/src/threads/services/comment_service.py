import uuid
from datetime import datetime

from fastapi import HTTPException, Response
from sqlalchemy.orm import Session

from src.threads.repository.comment_repository import CommentRepository
from src.threads.schemas.model_schema import (
    CommentCreate,
    CommentSchema,
    CommentUpdate,
)


class CommentService:
    def __init__(self, repository: CommentRepository):
        self.repository = repository

    def comment_thread(
        self,
        user_id: uuid.UUID,
        comment: CommentCreate,
        db: Session,
    ) -> Response:
        new_comment = CommentSchema(
            review_id=comment.review_id,
            user_id=user_id,
            content=comment.content,
            created_at=datetime.utcnow(),
        )
        if not self.repository.add_comment_to_review(new_comment, db):
            raise HTTPException(status_code=400, detail="Comment could not be created.")
        return Response(status_code=201, content="Comment created successfully")

    def delete_comment(self, db: Session, comment_id: uuid.UUID) -> Response:
        comment = self.repository.get_comment_by_id(comment_id, db)
        if comment is None:
            raise HTTPException(
                status_code=404, detail=f"Not found comment_id={comment_id}."
            )
        if not self.repository.delete_comment(db, comment):
            raise HTTPException(
                status_code=400, detail="Comment could not be deleted ."
            )
        return Response(status_code=200, content="Comment deleted successfully")

    def update_comment(
        self, db: Session, comment_id: uuid.UUID, updated_comment: CommentUpdate
    ) -> CommentSchema:
        comment = self.repository.get_comment_by_id(comment_id, db)
        if comment is None:
            raise HTTPException(
                status_code=404, detail=f"Not found comment_id={comment_id}."
            )
        updated = self.repository.update_comment(db, comment, updated_comment)
        if not updated:
            raise HTTPException(status_code=402, detail="Cannot update comment.")
        return CommentSchema(**updated.as_dict())
