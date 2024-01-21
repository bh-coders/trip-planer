from src.auth.interfaces.repository import Repository


class AuthService:
    def __init__(self, repository: Repository):
        self._repository = repository