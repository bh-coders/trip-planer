import logging
from typing import Optional

from sqlalchemy.orm import Session

from src.attraction.interfaces.repository import Repository
from src.attraction.models import Attraction
from src.attraction.schemas import AttractionSchema

logger = logging.getLogger(__name__)


class AttractionRepository(Repository):
    def get_all(self, db: Session) -> list[Attraction]:
        return db.query(Attraction).all()

    def get_by_id(self, db: Session, attraction_id: int) -> Optional[Attraction]:
        return db.query(Attraction).filter(Attraction.id == attraction_id).first()

    def create(self, db: Session, attraction: AttractionSchema) -> bool:
        try:
            with db.begin():
                new_attraction = Attraction(
                    name=attraction.name,
                    description=attraction.description,
                    longitude=attraction.longitude,
                    latitude=attraction.latitude,
                    open_hours=attraction.open_hours,
                )
                db.add(new_attraction)
            return True
        except Exception as e:
            logger.error("Error: %s" % e)
        return False

    def update(
        self,
        db: Session,
        db_attraction: Attraction,
        updated_attraction: AttractionSchema,
    ) -> Optional[Attraction]:
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
            logger.error("Error during update: %s" % e)
            return None

    def delete(self, db: Session, attraction: Attraction):
        try:
            with db.begin_nested():
                db.delete(attraction)
                db.commit()
            return True
        except Exception as e:
            logger.error("Error during delete: %s" % e)
            return False
