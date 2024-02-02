import uuid
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.core.interceptors.auth_interceptor import verify_jwt
from src.threads.repository.thread_repository import ThreadsRepository
from src.threads.schemas.model_schema import (
    CommentCreate,
    CommentUpdate,
    ReviewCreate,
    ReviewUpdate,
)
from src.threads.services.thread_service import ThreadsService

threads_router = APIRouter()
threads_repository = ThreadsRepository()
threads_service = ThreadsService(repository=threads_repository)


@threads_router.post("/create")
def create_thread(
    thread: ReviewCreate,
    request: Request,
    db: Annotated[Session, Depends(get_db)],
    is_token_valid: bool = Depends(verify_jwt),
):
    return threads_service.create(request=request, thread=thread, db=db)


@threads_router.get("/{review_id}")
def get_thread(
    review_id: uuid.UUID,
    db: Annotated[Session, Depends(get_db)],
    is_token_valid: bool = Depends(verify_jwt),
):
    return threads_service.get_thread_by_id(thread_id=review_id, db=db)


@threads_router.delete("/{review_id}")
def delete_thread(
    review_id: uuid.UUID,
    db: Annotated[Session, Depends(get_db)],
    is_token_valid: bool = Depends(verify_jwt),
):
    return threads_service.delete_thread(db=db, review_id=review_id)


@threads_router.delete("/comment/{comment_id}")
def delete_comment(
    comment_id: uuid.UUID,
    db: Annotated[Session, Depends(get_db)],
    is_token_valid: bool = Depends(verify_jwt),
):
    return threads_service.delete_comment(db=db, comment_id=comment_id)


@threads_router.patch("/{review_id}")
def update_thread(
    review_id: uuid.UUID,
    review: ReviewUpdate,
    db: Annotated[Session, Depends(get_db)],
    is_token_valid: bool = Depends(verify_jwt),
):
    return threads_service.update_thread(db=db, review_id=review_id, updated_review=review)


@threads_router.patch("/comment/{comment_id}")
def update_comment(
    comment_id: uuid.UUID,
    comment: CommentUpdate,
    db: Annotated[Session, Depends(get_db)],
    is_token_valid: bool = Depends(verify_jwt),
):
    return threads_service.update_comment(db=db, comment_id=comment_id, updated_comment=comment)


@threads_router.get("/attraction/{attraction_id}")
def get_threads_attraction(
    db: Annotated[Session, Depends(get_db)],
    attraction_id: int | str,
    sort_by: Optional[str] = None,  # 'rating', 'price', 'time_spent'
    rating: Optional[int] = None,
    price: Optional[int] = None,
    time_spent: Optional[int] = None,
    is_token_valid: bool = Depends(verify_jwt),
):
    return threads_service.get_threads_attraction_filtered_sorted(
        db=db,
        attraction_id=attraction_id,
        sort_by=sort_by,
        rating=rating,
        price=price,
        time_spent=time_spent,
    )


@threads_router.post("/comment")
def comment_thread(
    request: Request,
    comment: CommentCreate,
    db: Annotated[Session, Depends(get_db)],
    is_token_valid: bool = Depends(verify_jwt),
):
    return threads_service.comment_thread(request=request, comment=comment, db=db)
