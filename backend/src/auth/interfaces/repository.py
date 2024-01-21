from abc import ABC


class Repository(ABC):
    def register(self, db, user):
        pass

    def sign_in(self, db, sign_in_user):
        pass