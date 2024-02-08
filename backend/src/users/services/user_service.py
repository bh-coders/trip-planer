import uuid
from typing import Optional

from sqlalchemy.orm import Session

from src.auth.utils import verify_passwords
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
    def __init__(self, repository: UserRepository):
        self.user_repository = repository

    def change_email(
        self,
        user_id: uuid.UUID,
        new_email: str,
        old_email: str,
        db: Session,
    ) -> Optional[EmailChangeEndpoint]:
        user = self.user_repository.get_by_id(user_id=user_id, db=db)
        if not user:
            raise UserDoesNotExist
        if old_email != user.email:
            raise InvalidOldEmail

        if new_email == old_email:
            raise InvalidNewOldEmail
        try:
            self.user_repository.update_email(new_email, user, db)
            return EmailChangeEndpoint(
                message="Email changed successfully",
            )
        except Exception:
            raise EmailChangeFailed

    def change_password(
        self,
        user_id: uuid.UUID,
        old_password,
        new_password,
        rewrite_password,
        db: Session,
    ) -> Optional[PasswordChangeEndpoint]:
        user = self.user_repository.get_by_id(user_id=user_id, db=db)
        if not user:
            raise UserDoesNotExist
        if new_password != rewrite_password:
            raise InvalidNewOrRewritePassword

        if not verify_passwords(old_password, user.password):
            raise InvalidOldPassword
        try:
            self.user_repository.update_password(new_password, user, db)
            return PasswordChangeEndpoint(
                message="Password changed successfully",
            )
        except Exception:
            raise PasswordChangeFailed

    def delete_user(
        self,
        user_id: uuid.UUID,
        db: Session,
    ) -> Optional[DeleteEndpoint]:
        user = self.user_repository.get_by_id(user_id=user_id, db=db)
        if not user:
            raise UserDoesNotExist
        try:
            self.user_repository.delete_model(user, db)
            return DeleteEndpoint(
                message="User deleted successfully",
            )
        except Exception:
            raise DeleteFailed
