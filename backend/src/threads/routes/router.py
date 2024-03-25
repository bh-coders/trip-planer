import uuid
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from src.core.interceptors.auth_interceptor import get_user_id, verify_jwt
from src.db.cache_storage import RedisStorage
from src.db.database import get_db
from src.threads.repository.comment_repository import CommentRepository
from src.threads.repository.review_repository import ReviewRepository
from src.threads.schemas.model_schema import (
    CommentCreate,
    CommentSchema,
    CommentUpdate,
    ReviewCreate,
    ReviewSchema,
    ReviewUpdate,
)
from src.threads.services.comment_service import CommentService
from src.threads.services.review_service import ReviewService

threads_router = APIRouter()
review_repository = ReviewRepository()
comment_repository = CommentRepository()
cache_storage = RedisStorage()
comment_service = CommentService(repository=comment_repository)
review_service = ReviewService(repository=review_repository, cache=cache_storage)


@threads_router.post("/create")
def create_thread(
    thread: ReviewCreate,
    user_id: Annotated[uuid.UUID, Depends(get_user_id)],
    db: Annotated[Session, Depends(get_db)],
) -> Response:
    return review_service.create(user_id=user_id, thread=thread, db=db)


@threads_router.get("/{review_id}", dependencies=[Depends(verify_jwt)])
def get_thread(
    review_id: uuid.UUID,
    db: Annotated[Session, Depends(get_db)]
) -> ReviewSchema:
    return review_service.get_thread_by_id(thread_id=review_id, db=db)


@threads_router.delete("/{review_id}", dependencies=[Depends(verify_jwt)])
def delete_thread(
    review_id: uuid.UUID,
    db: Annotated[Session, Depends(get_db)]
) -> Response:
    return review_service.delete_thread(db=db, review_id=review_id)


@threads_router.delete("/comment/{comment_id}", dependencies=[Depends(verify_jwt)])
def delete_comment(
    comment_id: uuid.UUID,
    db: Annotated[Session, Depends(get_db)]
) -> Response:
    return comment_service.delete_comment(db=db, comment_id=comment_id)


@threads_router.patch("/{review_id}", dependencies=[Depends(verify_jwt)])
def update_thread(
    review_id: uuid.UUID,
    review: ReviewUpdate,
    db: Annotated[Session, Depends(get_db)]
) -> ReviewSchema:
    return review_service.update_thread(
        db=db, review_id=review_id, updated_review=review
    )


@threads_router.patch("/comment/{comment_id}", dependencies=[Depends(verify_jwt)])
def update_comment(
    comment_id: uuid.UUID,
    comment: CommentUpdate,
    db: Annotated[Session, Depends(get_db)]
) -> CommentSchema:
    return comment_service.update_comment(
        db=db, comment_id=comment_id, updated_comment=comment
    )


@threads_router.get("/attraction/{attraction_id}", dependencies=[Depends(verify_jwt)])
def get_threads_attraction(
    db: Annotated[Session, Depends(get_db)],
    attraction_id: int | str,
    sort_by: Optional[str] = None,  # 'rating', 'price', 'time_spent'
    rating: Optional[int] = None,
    price: Optional[int] = None,
    time_spent: Optional[int] = None
) -> list[ReviewSchema]:
    return review_service.get_threads_attraction_filtered_sorted(
        db=db,
        attraction_id=attraction_id,
        sort_by=sort_by,
        rating=rating,
        price=price,
        time_spent=time_spent,
    )


@threads_router.post("/comment")
def comment_thread(
    comment: CommentCreate,
    user_id: Annotated[uuid.UUID, Depends(get_user_id)],
    db: Annotated[Session, Depends(get_db)],
) -> Response:
    return comment_service.comment_thread(user_id=user_id, comment=comment, db=db)
