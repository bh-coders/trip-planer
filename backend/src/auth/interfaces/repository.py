from abc import ABC


class Repository(ABC):
    def register(self, user, db):
        pass

    def sign_in(self, sign_in_user, db):
        pass
