from typing import Optional
from uuid import UUID

from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.auth.utils import verify_passwords
from src.common.utils import publish_handler_event
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
from src.users.repositories import UserRepository
from src.users.schemas.user import (
    DeleteEndpoint,
    EmailChangeEndpoint,
    PasswordChangeEndpoint,
)


class UserService:
    def __init__(
        self,
        repository: UserRepository,
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
        user = self.repository.get_by_id(user_id=user_id, db=db)
        if not user:
            raise UserDoesNotExist
        if not verify_passwords(password, user.password):
            raise InvalidOldPassword
        if old_email != user.email:
            raise InvalidOldEmail

        if new_email == old_email:
            raise InvalidNewOldEmail
        try:
            self.repository.update_email(new_email, user, db)
            return JSONResponse(
                content=EmailChangeEndpoint(
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
        user = self.repository.get_by_id(user_id=user_id, db=db)
        if not user:
            raise UserDoesNotExist
        if new_password != rewrite_password:
            raise InvalidNewOrRewritePassword

        if not verify_passwords(old_password, user.password):
            raise InvalidOldPassword
        try:
            self.repository.update_password(new_password, user, db)
            return JSONResponse(
                content=PasswordChangeEndpoint(
                    message="Password changed successfully",
                ).model_dump(),
                status_code=200,
            )
        except Exception:
            raise PasswordChangeFailed

    @staticmethod
    def publish_user_deleted_event(user_id: str) -> None:
        publish_handler_event(
            pattern="user_deleted",
            data={
                "id": user_id,
            },
        )

    def delete_user(
        self,
        user_id: UUID,
        db: Session,
    ) -> Optional[JSONResponse]:
        user_db = self.repository.get_by_id(user_id=user_id, db=db)
        if not user_db:
            raise UserDoesNotExist
        try:
            self.publish_user_deleted_event(str(user_db.id))
            self.repository.delete_user(user_db, db)

            return JSONResponse(
                content=DeleteEndpoint(
                    message="User deleted successfully",
                ).model_dump(),
                status_code=200,
            )
        except Exception:
            raise DeleteFailed
