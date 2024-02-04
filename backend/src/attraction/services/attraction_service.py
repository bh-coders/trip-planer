import json
import logging

from fastapi import HTTPException, Response
from sqlalchemy.orm import Session

from src.attraction.interfaces.repository import Repository
from src.attraction.schemas import AttractionImages, AttractionSchema
from src.core.json_encoder import JSONEncoder
from src.db.cache_storage import CacheStorage
from src.db.cloudstorage import CloudStorage

logger = logging.getLogger(__name__)
cache = CacheStorage()
cloud_storage = CloudStorage()


class AttractionService:
    def __init__(self, repository: Repository):
        self._repository = repository

    def get_all_attractions(self, db: Session) -> list[AttractionSchema]:
        attractions = self._repository.get_all(db)
        return [AttractionSchema(**attraction.as_dict()) for attraction in attractions]

    def get_attraction_by_id(self, db: Session, attraction_id: int) -> AttractionSchema:
        cache_attraction = cache.get_value(f"attraction:{attraction_id}")
        if cache_attraction:
            attraction = json.loads(cache_attraction)
            return AttractionSchema(**attraction)
        attraction = self._repository.get_by_id(db, attraction_id)

        if not attraction:
            raise HTTPException(status_code=404, detail="Attraction does not exist")
        cache.set_value(
            f"attraction:{attraction_id}",
            json.dumps(attraction.as_dict(), cls=JSONEncoder),
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
        attraction = self._repository.get_by_id(db, attraction_id)
        if attraction is None:
            raise HTTPException(status_code=404, detail="Cannot found attraction.")
        updated = self._repository.update(db, attraction, updated_attraction)
        if not updated:
            raise HTTPException(status_code=402, detail="Cannot update attraction.")
        cache.set_value(f"attraction:{attraction_id}", updated.as_dict())
        return AttractionSchema(**updated.as_dict())

    def delete_attraction(self, db: Session, attraction_id: int):
        attraction = self._repository.get_by_id(db, attraction_id)
        if attraction is None:
            return False
        cache.delete_value(f"attraction:{attraction_id}")
        if not self._repository.delete(db, attraction):
            raise HTTPException(
                status_code=400, detail="Attraction could not be deleted."
            )
        return Response(status_code=200, content="Attraction successfully deleted.")

    def get_attraction_images(
        self, db: Session, attraction_id: int
    ) -> AttractionImages:
        cache_attraction_images = cache.get_value(f"attraction_images:{attraction_id}")
        if cache_attraction_images:
            attraction_images = json.loads(cache_attraction_images)
            return AttractionImages(**attraction_images)

        attraction = self.get_attraction_by_id(db, attraction_id)

        bucket_name = "attractions"
        default_path = f"{bucket_name}/default.jpg"
        prefix_bucket = f"{attraction.id}/"

        try:
            objects = cloud_storage.list_bucket_objects(bucket_name, prefix_bucket)
        except Exception as e:
            logger.error("Error retrieving objects from cloud server: %s " % e)
            return AttractionImages(id=attraction.id, image_urls=[default_path])

        result = AttractionImages(id=attraction.id, image_urls=[default_path])

        for obj in objects:
            if default_path in result.image_urls:
                result.image_urls.remove(default_path)
            result.image_urls.append(f"{bucket_name}/{obj.object_name}")
        cache.set_value(
            f"attraction_images:{attraction_id}",
            json.dumps(result.model_dump(), cls=JSONEncoder),
        )
        return result
