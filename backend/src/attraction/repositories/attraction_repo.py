import logging
from typing import Optional

from geoalchemy2 import Geography
from sqlalchemy import desc, func
from sqlalchemy.orm import Session

from src.attraction.interfaces.repository import Repository
from src.attraction.models import Attraction
from src.attraction.schemas import (
    AttractionFilters,
    AttractionSchema,
    AttractionSortedBy,
)
from src.common.schemas.common_schema import SortDirection

logger = logging.getLogger(__name__)


class AttractionRepository(Repository):
    def get_all(self, db: Session) -> list[Attraction]:
        return db.query(Attraction).all()

    def get_by_filters(
        self, db: Session, filters: AttractionFilters
    ) -> list[Attraction]:
        query = db.query(Attraction)

        filter_operations = {
            "city": lambda value: Attraction.city == value,
            "country": lambda value: Attraction.country == value,
            "category": lambda value: Attraction.category == value,
        }

        for filter_name, operation in filter_operations.items():
            filter_value = getattr(filters, filter_name, None)
            if filter_value:
                query = query.filter(operation(filter_value))

        if (
            filters.radius is not None
            and filters.longitude is not None
            and filters.latitude is not None
        ):
            point = func.ST_SetSRID(
                func.ST_MakePoint(filters.longitude, filters.latitude), 4326
            ).cast(Geography)
            attraction_point = func.ST_SetSRID(
                func.ST_MakePoint(Attraction.longitude, Attraction.latitude), 4326
            ).cast(Geography)
            query = query.filter(
                func.ST_DWithin(attraction_point, point, filters.radius)
            )

        # sorting
        if filters.sort_by == AttractionSortedBy.TopRated:
            if filters.sort_direction == SortDirection.Desc:
                query = query.order_by(desc(Attraction.rating))
            else:
                query = query.order_by(Attraction.rating)
        elif filters.sort_by == AttractionSortedBy.MostRated:
            if filters.sort_direction == SortDirection.Desc:
                query = query.order_by(desc(Attraction.visits))
            else:
                query = query.order_by(Attraction.visits)

        return query.all()

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
