from src.auth.routes.auth_router import router as auth_router
from src.auth.routes.user_router import router as user_router

__all__ = [
    "auth_router",
    "user_router",
]
