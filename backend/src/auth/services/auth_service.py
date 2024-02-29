from typing import Optional

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.auth.schemas import (
    LoginEndpoint,
    LoginUserModel,
    RefreshTokenEndpoint,
    RegisterEndpoint,
    RegisterUserModel,
)
from src.auth.utils import (
    encode_jwt_token,
    hash_password,
    verify_passwords,
)
from src.common.exceptions import (
    NotAuthenticated,
)
from src.common.utils import publish_handler_event
from src.core.interceptors.auth_interceptor import verify_user_id
from src.users.exceptions import (
    EmailTaken,
    InvalidPassword,
    InvalidUserData,
    RegisterFailed,
    TokenDoesNotExist,
    UserDoesNotExist,
    UsernameTaken,
)
from src.users.models.user_model import User
from src.users.repositories import UserRepository
from src.users.schemas.profile import CreateProfileModel
from src.users.schemas.user import CreateUserModel


class AuthService:
    def __init__(
        self,
        repository: UserRepository,
    ):
        self.repository = repository

    def authenticate_user(
        self, username: str, password: str, db: Session
    ) -> Optional[User]:
        """
        Authenticates a user by checking the provided username and password against the database.

        Args:
        - username: The username of the user to authenticate.
        - password: The password of the user to authenticate.
        - db: The database session.

        Returns:
        - The authenticated user.
        """
        # Get user from the database by username
        user = self.repository.get_by_username(username=username, db=db)

        # If user does not exist, raise UserDoesNotExist exception
        if not user:
            raise UserDoesNotExist

        # If the provided password does not match the user's password, raise InvalidPassword exception
        if not verify_passwords(password, user.password):
            raise InvalidPassword

        # Return the authenticated user
        return user

    def create_user(self, user: CreateUserModel, db: Session):
        """
        Creates a new user in the database.

        Args:
            user (CreateUserModel): The user model to be created.
            db (Session): The database session.

        Returns:
            CreateUserModel: The created user model.

        Raises:
            HTTPException: If the user already exists in the database.
        """
        # Hash the user's password
        user.password = hash_password(user.password)

        try:
            # Create the user in the database
            user = self.repository.create_user(user=user, db=db)
        except Exception:
            # If the user already exists, raise an HTTPException
            raise HTTPException(status_code=400, detail="User already exists")

        return user

    @staticmethod
    def publish_user_created_event(
        user_id: str, user: CreateUserModel, profile: CreateProfileModel
    ) -> None:
        """
        Publishes a user created event to the cache handler.

        Args:
            user_id (str): The ID of the user.
            user (CreateUserModel): The user object containing user details.
            profile (CreateProfileModel): The profile object containing profile details.
        """
        # Publish user created event to the cache handler
        publish_handler_event(
            pattern="user_created",
            data={
                "id": user_id,
                "email": user.email,
                "username": user.username,
                "profile": {
                    "name": profile.name,
                    "surname": profile.surname,
                    "image_url": profile.image_url,
                },
            },
        )

    def register(self, user: RegisterUserModel, db: Session) -> Optional[JSONResponse]:
        """
        Registers a new user and returns a JSONResponse.

        Args:
            user (RegisterUserModel): The user to register.
            db (Session): The database session.

        Returns:
            Optional[JSONResponse]: The JSONResponse with the registration status.
        """
        # Check if the username is already taken
        if self.repository.get_by_username(user.username, db):
            raise UsernameTaken
        # Check if the email is already taken
        elif self.repository.get_by_email(user.email, db):
            raise EmailTaken

        try:
            # Create the user in the database
            user_db = self.create_user(user=user, db=db)
            # Check if the user creation was successful
            if not user_db:
                raise InvalidUserData

            # Publish user created event
            self.publish_user_created_event(
                user_id=str(user_db.id), user=user, profile=user.profile
            )

            # Return successful registration message
            return JSONResponse(
                content=RegisterEndpoint(
                    message="User registered successfully"
                ).model_dump(),
                status_code=201,
            )
        except Exception:
            raise RegisterFailed

    def login(self, user: LoginUserModel, db: Session) -> Optional[JSONResponse]:
        """
        Logs in the user and returns a JSONResponse with authentication token.

        Args:
        - user: LoginUserModel object containing username and password
        - db: database session

        Returns:
        - Optional[JSONResponse]: JSONResponse object with authentication token
        """
        # Authenticate the user
        auth_user = self.authenticate_user(
            username=user.username,
            password=user.password,
            db=db,
        )
        if not auth_user:
            raise NotAuthenticated

        # Set user as active
        self.repository.set_is_active(auth_user, db)

        # Generate JWT token and return JSONResponse
        token = encode_jwt_token(username=auth_user.username, user_id=auth_user.id)
        return JSONResponse(
            content=LoginEndpoint(**token).model_dump(),
            status_code=200,
        )

    def refresh_credentials(self, token: str, db: Session) -> Optional[JSONResponse]:
        """
        Refresh user credentials based on the provided token.

        Args:
        token (str): The user token.
        db (Session): The database session.

        Returns:
        Optional[JSONResponse]: The JSON response containing the refreshed token.
        """
        # Check if token exists
        if not token:
            raise TokenDoesNotExist

        # Get user id from token
        user_id = verify_user_id(get_token=token)

        # Get user from database
        user = self.repository.get_by_id(user_id=user_id, db=db)
        if not user:
            raise UserDoesNotExist

        # Generate new token and return JSONResponse
        token = encode_jwt_token(username=user.username, user_id=user.id)
        return JSONResponse(
            content=RefreshTokenEndpoint(**token).model_dump(),
            status_code=200,
        )
