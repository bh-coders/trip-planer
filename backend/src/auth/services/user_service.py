from typing import Optional

from sqlalchemy.orm import Session

from src.auth.exceptions import (
    DeleteFailed,
    EmailChangeFailed,
    InvalidNewOldEmail,
    InvalidNewOrRewritePassword,
    InvalidOldEmail,
    InvalidOldPassword,
    PasswordChangeFailed,
)
from src.auth.models import User
from src.auth.repositories import UserRepository
from src.auth.schemas import (
    DeleteResponse,
    EmailChangeResponse,
    PasswordChangeResponse,
)
from src.auth.utils import verify_passwords


class UserService:
    def __init__(self, repository: UserRepository):
        self.user_repository = repository

    def change_email(
        self,
        user: User,
        new_email: str,
        old_email: str,
        db: Session,
    ) -> Optional[EmailChangeResponse]:
        if old_email != user.email:
            raise InvalidOldEmail

        if new_email == old_email:
            raise InvalidNewOldEmail
        try:
            self.user_repository.update_email(new_email, user, db)
            return EmailChangeResponse(
                message="Email changed successfully",
            )
        except Exception:
            raise EmailChangeFailed

    def change_password(
        self,
        user: User,
        old_password,
        new_password,
        rewrite_password,
        db: Session,
    ) -> Optional[PasswordChangeResponse]:
        if new_password != rewrite_password:
            raise InvalidNewOrRewritePassword

        if not verify_passwords(old_password, user.password):
            raise InvalidOldPassword
        try:
            self.user_repository.update_password(new_password, user, db)
            return PasswordChangeResponse(
                message="Password changed successfully",
            )
        except Exception:
            raise PasswordChangeFailed

    def delete_user(self, user: User, db: Session) -> Optional[DeleteResponse]:
        try:
            self.user_repository.delete_model(user, db)
            return DeleteResponse(
                message="User deleted successfully",
            )
        except Exception:
            raise DeleteFailed
