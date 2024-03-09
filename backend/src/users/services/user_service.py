from typing import Optional
from uuid import UUID

from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.auth.utils import hash_password, verify_passwords
from src.common.multithreading_utils import (
    publish_handler_event,
)
from src.db.interfaces import ICacheHandler
from src.users.exceptions import (
    DeleteFailed,
    EmailChangeFailed,
    InvalidNewOldEmail,
    InvalidNewOrRewritePassword,
    InvalidOldEmail,
    InvalidOldPassword,
    PasswordChangeFailed,
    UserDoesNotExist,
)
from src.users.interfaces import IUserRepository
from src.users.schemas.user import (
    DeleteSuccessSchema,
    EmailChangeSuccessSchema,
    PasswordChangeSuccessSchema,
)


class UserService:
    def __init__(
        self,
        repository: IUserRepository,
    ):
        self.repository = repository

    def change_email(
        self,
        user_id: UUID,
        new_email: str,
        old_email: str,
        password: str,
        db: Session,
    ) -> Optional[JSONResponse]:
        user = self.repository.get_by_id(
            user_id=user_id,
            db=db,
        )
        if not user:
            raise UserDoesNotExist
        if not verify_passwords(password, user.password):
            raise InvalidOldPassword
        if old_email != user.email:
            raise InvalidOldEmail
        if new_email == old_email:
            raise InvalidNewOldEmail
        try:
            self.repository.update_email(
                new_email=new_email,
                user_obj=user,
                db=db,
            )
            return JSONResponse(
                content=EmailChangeSuccessSchema(
                    message="Email changed successfully",
                ).model_dump(),
                status_code=200,
            )
        except Exception:
            raise EmailChangeFailed

    def change_password(
        self,
        user_id: UUID,
        old_password,
        new_password,
        rewrite_password,
        db: Session,
    ) -> Optional[JSONResponse]:
        user = self.repository.get_by_id(
            user_id=user_id,
            db=db,
        )
        if not user:
            raise UserDoesNotExist
        if new_password != rewrite_password:
            raise InvalidNewOrRewritePassword
        if not verify_passwords(old_password, user.password):
            raise InvalidOldPassword
        try:
            self.repository.update_password(
                new_password=hash_password(new_password),
                user_obj=user,
                db=db,
            )
            return JSONResponse(
                content=PasswordChangeSuccessSchema(
                    message="Password changed successfully",
                ).model_dump(),
                status_code=200,
            )
        except Exception:
            raise PasswordChangeFailed

    def delete_user(
        self,
        user_id: UUID,
        db: Session,
        cache_handler: ICacheHandler,
    ) -> Optional[JSONResponse]:
        user_obj_db = self.repository.get_by_id(
            user_id=user_id,
            db=db,
        )
        if not user_obj_db:
            raise UserDoesNotExist
        try:
            publish_handler_event(
                event_type="user_deleted",
                data={
                    "id": str(user_obj_db.id),
                },
                cache_handler=cache_handler,
            )
            self.repository.delete_user(
                user_obj=user_obj_db,
                db=db,
            )
            return JSONResponse(
                content=DeleteSuccessSchema(
                    message="User deleted successfully",
                ).model_dump(),
                status_code=200,
            )
        except Exception:
            raise DeleteFailed
