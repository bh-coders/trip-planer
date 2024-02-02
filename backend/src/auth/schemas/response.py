from src.auth.schemas.endpoint import Message, Token


# register_view
class RegisterResponse(Message):
    model_config = {
        "json_schema_extra": {
            "title": "User",
            "description": "User model",
            "example": {
                "message": "User registered successfully",
            },
        },
    }


# login_view
class LoginResponse(Token):
    pass


# refresh_view
class RefreshTokenResponse(Token):
    pass


# email_change_view
class EmailChangeResponse(Message):
    model_config = {
        "json_schema_extra": {
            "title": "User",
            "description": "User model",
            "example": {
                "message": "Email changed successfully",
            },
        },
    }


# password_change_view
class PasswordChangeResponse(Message):
    model_config = {
        "json_schema_extra": {
            "title": "User",
            "description": "User model",
            "example": {
                "message": "Password changed successfully",
            },
        },
    }


# delete_view
class DeleteResponse(Message):
    model_config = {
        "json_schema_extra": {
            "title": "User",
            "description": "User model",
            "example": {
                "message": "User deleted successfully",
            },
        },
    }
