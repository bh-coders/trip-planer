import logging

from sqlalchemy.orm import Session

from src.attraction.interfaces.repository import Repository
from src.attraction.schemas import AttractionSchema, AttractionsImages
from src.core.cloudstorage import CloudStorage

logger = logging.getLogger(__name__)
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
            self, db: Session, attraction_id: int, updated_attraction: AttractionSchema
    ):
        attraction = self.get_attraction_by_id(db, attraction_id)
        if attraction is None:
            return False
        return self._repository.update(db, attraction, updated_attraction)

    def delete_attraction(self, db: Session, attraction_id: int):
        attraction = self.get_attraction_by_id(db, attraction_id)
        if attraction is None:
            return False
        return self._repository.delete(db, attraction)

    def get_attraction_images(self, db: Session, attraction_id: int) -> AttractionsImages:
        cloud_storage = CloudStorage()
        attraction = self.get_attraction_by_id(db, attraction_id)

        if attraction is None:
            return AttractionsImages(id=None)

        bucket_name = 'attractions'
        default_path = f"{bucket_name}/default.jpg"
        prefix_bucket = f"{attraction.id}/"

        try:
            objects = cloud_storage.list_bucket_objects(bucket_name, prefix_bucket)
        except Exception as e:
            logger.error("Error retrieving objects from cloud server: %s " % e)
            return AttractionsImages(id=attraction.id, image_urls=[default_path])

        result = AttractionsImages(id=attraction.id, image_urls=[default_path])

        for obj in objects:
            if default_path in result.image_urls:
                result.image_urls.remove(default_path)
            result.image_urls.append(f"{bucket_name}/{obj.object_name}")

        return result
