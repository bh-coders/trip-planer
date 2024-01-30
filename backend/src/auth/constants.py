class ErrorCode:
    USERNAME_TAKEN = "Username is already taken."
    EMAIL_TAKEN = "Email is already taken."
    INVALID_PASSWORD = "Invalid password."
    USERNAME_DOES_NOT_EXIST = "Username does not exist."
    USER_DOES_NOT_EXIST = "User does not exist."
    TOKEN_DOES_NOT_EXIST = "Token does not exist."

    AUTHENTICATION_REQUIRED = "Authentication required."
    AUTHORIZATION_FAILED = "Authorization failed. User has no access."
    INVALID_TOKEN = "Invalid token."
    INVALID_CREDENTIALS = "Invalid credentials."
    REFRESH_TOKEN_NOT_VALID = "Refresh token is not valid."
    REFRESH_TOKEN_REQUIRED = "Refresh token is required either in the body or cookie."
