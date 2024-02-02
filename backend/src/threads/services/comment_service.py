import uuid
from datetime import datetime

from fastapi import HTTPException, Request
from sqlalchemy.orm import Session

from src.auth.utils import get_user_id_from_request
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

    def delete_comment(self, db: Session, comment_id: uuid.UUID):
        comment = self.repository.get_comment_by_id(comment_id, db)
        if comment is None:
            raise HTTPException(
                status_code=404, detail=f"Not found comment_id={comment_id}."
            )
        return self.repository.delete_comment(db, comment)

    def update_comment(
            self, db: Session, comment_id: uuid.UUID, updated_comment: CommentUpdate
    ):
        comment = self.repository.get_comment_by_id(comment_id, db)
        if comment is None:
            raise HTTPException(
                status_code=404, detail=f"Not found comment_id={comment_id}."
            )
        updated = self.repository.update_comment(db, comment, updated_comment)
        if not updated:
            raise HTTPException(
                status_code=402, detail=f"Cannot update comment."
            )
        return CommentSchema(**updated.as_dict())
