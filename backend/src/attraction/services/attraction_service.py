import json
import logging

import orjson
from fastapi import HTTPException, Response
from sqlalchemy.orm import Session

from src.attraction.interfaces.repository import Repository
from src.attraction.schemas import AttractionFilters, AttractionImages, AttractionSchema
from src.attraction.services.geocoding_service import MapsCoService
from src.db.cache_storage import CacheKeys
from src.db.cloud_storage import BucketNames
from src.db.interfaces.cache_storage import ICacheStorage
from src.db.interfaces.cloud_storage import ICloudStorage

logger = logging.getLogger(__name__)


class AttractionService:
    def __init__(
            self,
            repository: Repository,
            cache: ICacheStorage,
            cloud_storage: ICloudStorage,
            geo_service: MapsCoService,
    ):
        self._repository = repository
        self.cache = cache
        self.cloud_storage = cloud_storage
        self.geo_service = geo_service

    def get_all_attractions(self, db: Session) -> list[AttractionSchema]:
        attractions = self._repository.get_all(db)
        return [AttractionSchema(**attraction.as_dict()) for attraction in attractions]

    def get_attractions(
            self, db: Session, filters: AttractionFilters
    ) -> list[AttractionSchema]:
        if not filters.country and filters.longitude and filters.latitude:
            try:
                result = self.geo_service.reverse_geocode(
                    filters.latitude, filters.longitude
                )
                if "country" in result["address"] and not filters.country:
                    filters.country = result["address"]["country"]
            except Exception as e:
                logger.error("Error during reverse geocoding: %s" % e)

        attractions = self._repository.get_by_filters(db, filters)
        return [AttractionSchema(**attraction.as_dict()) for attraction in attractions]

    def get_attraction_by_id(self, db: Session, attraction_id: int) -> AttractionSchema:
        cache_key = CacheKeys.ATTRACTION.value + str(attraction_id)
        cache_attraction = self.cache.get_value(cache_key)
        if cache_attraction:
            attraction = json.loads(cache_attraction)
            return AttractionSchema(**attraction)
        attraction = self._repository.get_by_id(db, attraction_id)
        if not attraction:
            raise HTTPException(status_code=404, detail="Attraction does not exist")
        self.cache.set_value(
            cache_key,
            orjson.dumps(attraction.as_dict()),
        )
        return AttractionSchema(**attraction.as_dict())

    def create_attraction(self, db: Session, attraction: AttractionSchema):
        if not self._repository.create(db, attraction):
            raise HTTPException(
                status_code=400, detail="Attraction could not be created."
            )
        return Response(status_code=201, content="Attraction successfully created.")

    def update_attraction(
            self, db: Session, attraction_id: int, updated_attraction: AttractionSchema
    ) -> AttractionSchema:
        cache_key = CacheKeys.ATTRACTION.value + str(attraction_id)
        attraction = self._repository.get_by_id(db, attraction_id)
        if attraction is None:
            raise HTTPException(status_code=404, detail="Cannot found attraction.")
        updated = self._repository.update(db, attraction, updated_attraction)
        if not updated:
            raise HTTPException(status_code=402, detail="Cannot update attraction.")
        self.cache.set_value(cache_key, updated.as_dict())
        return AttractionSchema(**updated.as_dict())

    def delete_attraction(self, db: Session, attraction_id: int):
        cache_key = CacheKeys.ATTRACTION.value + str(attraction_id)
        attraction = self._repository.get_by_id(db, attraction_id)
        if attraction is None:
            return False
        self.cache.delete_value(cache_key)
        if not self._repository.delete(db, attraction):
            raise HTTPException(
                status_code=400, detail="Attraction could not be deleted."
            )
        return Response(status_code=200, content="Attraction successfully deleted.")

    def get_attraction_images(
            self, db: Session, attraction_id: int
    ) -> AttractionImages:
        cache_key = CacheKeys.ATTRACTION_IMAGES.value + str(attraction_id)
        cache_attraction_images = self.cache.get_value(cache_key)
        if cache_attraction_images:
            attraction_images = json.loads(cache_attraction_images)
            return AttractionImages(**attraction_images)

        attraction = self.get_attraction_by_id(db, attraction_id)

        bucket_name = BucketNames.ATTRACTIONS.value
        default_path = f"{bucket_name}/default.jpg"
        prefix_bucket = f"{attraction.id}/"

        try:
            objects = self.cloud_storage.list_bucket_objects(bucket_name, prefix_bucket)
        except Exception as e:
            logger.error("Error retrieving objects from cloud server: %s " % e)
            return AttractionImages(id=attraction.id, image_urls=[default_path])

        result = AttractionImages(id=attraction.id, image_urls=[default_path])

        for obj in objects:
            if default_path in result.image_urls:
                result.image_urls.remove(default_path)
            result.image_urls.append(f"{bucket_name}/{obj.object_name}")
        self.cache.set_value(
            cache_key,
            orjson.dumps(result.model_dump()),
        )
        return result
