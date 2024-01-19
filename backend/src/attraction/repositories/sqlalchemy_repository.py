from src.attraction.interfaces.repository import Repository
from src.attraction.models import Attraction
from sqlalchemy.orm import Session
from src.attraction.schemas import AttractionSchema


class SQLAlchemyRepository(Repository):
    def get_all(self, db: Session) -> list[Attraction]:
        attractions = db.query(Attraction).all()
        return attractions

    def get_by_id(self, db: Session, id: int):
        attraction = db.query(Attraction).filter(Attraction.id == id).first()
        return attraction

    def create(self, db: Session, attraction: AttractionSchema):
        try:
            with db.begin():
                new_attraction = Attraction(
                    name=attraction.name,
                    description=attraction.description,
                    longitude=attraction.longitude,
                    latitude=attraction.latitude,
                )
                db.add(new_attraction)
            return True
        except Exception as e:
            print(f"Error kurwa: {e}")
        return False

    def update(
        self, db: Session, db_item: Attraction, updatedItem: AttractionSchema
    ) -> Attraction:
        try:
            # we using begin_nested, because we already used session to get db_item
            with db.begin_nested():
                update_data = updatedItem.model_dump(exclude_unset=True)
                for key, value in update_data.items():
                    setattr(db_item, key, value)

                db.add(db_item)
            return db_item
        except Exception as e:
            print(f"Error during update: {e}")
            return False  # For now I will return False

    def delete(self, db: Session, item: Attraction):
        try:
            with db.begin_nested():
                db.delete(item)
            return True
        except Exception as e:
            print(f"Error during delete: {e}")
            return False  # For now I will return False
