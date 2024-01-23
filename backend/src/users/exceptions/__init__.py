class UserCreationError(Exception):
    pass


class UserUpdateError(Exception):
    pass


class UserDeleteError(Exception):
    pass


__all__ = [
    "UserCreationError",
    "UserUpdateError",
    "UserDeleteError",
]
