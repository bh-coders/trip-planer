from sqlalchemy.orm import Session

from src.attraction.interfaces.repository import Repository
from src.attraction.models import Attraction
from src.attraction.schemas import AttractionSchema


class AttractionRepository(Repository):
    def get_all(self, db: Session) -> list[Attraction]:
        attractions = db.query(Attraction).all()
        return attractions

    def get_by_id(self, db: Session, attraction_id: int):
        attraction = db.query(Attraction).filter(Attraction.id == attraction_id).first()
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
        self, db: Session, db_attraction: Attraction, updated_attraction: AttractionSchema
    ) -> Attraction:
        try:
            # we using begin_nested, because we already used session to get db_item
            with db.begin_nested():
                update_data = updated_attraction.model_dump(exclude_unset=True)
                for key, value in update_data.items():
                    setattr(db_attraction, key, value)

                db.add(db_attraction)
                db.commit()
            return db_attraction
        except Exception as e:
            print(f"Error during update: {e}")
            return False  # For now I will return False

    def delete(self, db: Session, attraction: Attraction):
        try:
            with db.begin_nested():
                db.delete(attraction)
                db.commit()
            return True
        except Exception as e:
            print(f"Error during delete: {e}")
            return False  # For now I will return False
