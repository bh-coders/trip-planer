import time

from backend.src.attraction.repositories.in_memory_repo import InMemoryRepository
from backend.src.attraction.models import Attraction
from typing import TypedDict


class AttractionService:
    def __init__(self, repository):
        self._repository = repository

    def get_all_items(self):
        return self._repository.get_all()

    def get_item_by_id(self, item_id):
        return self._repository.get_by_id(item_id)

    def create_item(self, attraction) :
        item = attraction
        return self._repository.create(item)

    def update_item(self, item_id, name):
        item = self._repository.get_by_id(item_id)
        if item is None:
            return False
        item.name = name
        return self._repository.update(item)

    def delete_item(self, item_id):
        return self._repository.delete(item_id)


# client code
in_memory_repository = InMemoryRepository()
item_service = AttractionService(in_memory_repository)

item_service.create_item(Attraction(
            id=1,
            name="Attraction 1",
            latitude=15.1234,
            longitude=25.1234,
            opening_hours={
                'Monday': '10:00-11:00'
            },
            prices={
                'Normal': 15.0
            },
        )
)

item_service.create_item(Attraction(
            id=2,
            name="Attraction 1",
            latitude=15.1234,
            longitude=25.1234,
            opening_hours={
                'Monday': '10:00-11:00'
            },
            prices={
                'Normal': 15.0
            },
        ))

items = item_service.get_all_items()
print(items)

time.sleep(2)

item = item_service.get_item_by_id(1)
print(item)

time.sleep(2)

item_service.update_item(2, 'Second attraction updated')
items = item_service.get_all_items()
print(items)

time.sleep(2)

item_service.delete_item(1)
items = item_service.get_all_items()
print(items)
