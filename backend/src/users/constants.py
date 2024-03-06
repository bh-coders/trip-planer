class ErrorCode:
    # invalid
    INVALID_PASSWORD = "Invalid password."
    INVALID_OLD_EMAIL = "Invalid old email."
    INVALID_NEW_EMAIL = "Invalid new email."
    INVALID_NEW_OLD_EMAIL = "New email cannot be the same as old email."
    INVALID_TOKEN = "Invalid token."
    INVALID_CREDENTIALS = "Invalid credentials."
    INVALID_OLD_PASSWORD = "Invalid old password."
    INVALID_NEW_OR_REWRITE_PASSWORD = "New password cannot be the same as old password."
    INVALID_PROFILE_DATA = "Invalid profile data."
    INVALID_USER_DATA = "Invalid user data."

    # taken
    USERNAME_TAKEN = "Username is already taken."
    EMAIL_TAKEN = "Email is already taken."
    USER_ALREADY_EXISTS = "User already exists."

    # not found
    USERNAME_DOES_NOT_EXIST = "Username does not exist."
    USER_DOES_NOT_EXIST = "User does not exist."
    TOKEN_DOES_NOT_EXIST = "Token does not exist."

    # expired
    TOKEN_EXPIRED = "Token expired."

    # failed
    EMAIL_CHANGE_FAILED = "Email change failed."
    PASSWORD_CHANGE_FAILED = "Password change failed."
    DELETE_FAILED = "Delete failed"
    REGISTER_FAILED = "Register failed"
    AUTHORIZATION_FAILED = "Authorization failed. User has no access."
    PROFILE_CREATION_FAILED = "Profile creation failed."

    # other
    AUTHENTICATION_REQUIRED = "Authentication required."
    REFRESH_TOKEN_REQUIRED = "Refresh token is required either in the body or cookie."
    REFRESH_TOKEN_NOT_VALID = "Refresh token is not valid."
