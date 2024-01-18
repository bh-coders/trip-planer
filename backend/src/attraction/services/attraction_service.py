from uuid import uuid4
from sqlalchemy.orm import Session
from attraction.schemas import AttractionSchema
from attraction.interfaces.repository import Repository


class AttractionService:
    def __init__(self, repository: Repository):
        self._repository = repository

    def get_all_attractions(self, db: Session):
        return self._repository.get_all(db)

    def get_attraction_by_id(self, db: Session, attraction_id: int):
        return self._repository.get_by_id(db, attraction_id)

    def create_attraction(self, db: Session, attraction: AttractionSchema):
        return self._repository.create(db, attraction)

    def update_attraction(
        self, db: Session, id: int, updated_attraction: AttractionSchema
    ):
        attraction = self.get_attraction_by_id(db, id)
        if attraction is None:
            return False
        return self._repository.update(db, attraction, updated_attraction)

    def delete_attraction(self, db: Session, attraction_id: int):
        attraction = self.get_attraction_by_id(db, attraction_id)
        if attraction is None:
            return False
        return self._repository.delete(db, attraction)
