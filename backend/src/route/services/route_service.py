import time

from backend.src.attraction.models import Attraction
from backend.src.attraction.repositories.in_memory_repo import InMemoryRepository
from backend.src.route.models import Route


class RouteService:
    def __init__(self, repository):
        self._repository = repository

    def get_all_items(self):
        return self._repository.get_all()

    def get_item_by_id(self, item_id):
        return self._repository.get_by_id(item_id)

    def create_item(self, route):
        item = route
        return self._repository.create_profile(item)

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
item_service = RouteService(in_memory_repository)

item_service.create_item(Route(
    id=1,
    name="Test Route",
    attractions=[Attraction(
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
    ),
        Attraction(
            id=2,
            name="Attraction 1",
            latitude=95.1234,
            longitude=25.1234,
            opening_hours={
                'Monday': '12:00-11:00'
            },
            prices={
                'Normal': 75.0
            },
        )]
))

item_service.create_item(Route(
    id=2,
    name="Test Route",
    attractions=[Attraction(
        id=3,
        name="Attraction 3",
        latitude=15.1234,
        longitude=25.1234,
        opening_hours={
            'Monday': '10:00-11:00'
        },
        prices={
            'Normal': 15.0
        },
    ),
        Attraction(
            id=4,
            name="Attraction 4",
            latitude=195.1234,
            longitude=625.1234,
            opening_hours={
                'Monday': '22:00-11:00'
            },
            prices={
                'Normal': 95.0
            },
        )]
))

items = item_service.get_all_items()
print(items)

time.sleep(2)

item = item_service.get_item_by_id(1)
print(item)

time.sleep(2)

item_service.update_item(2, 'Second route updated')
items = item_service.get_all_items()
print(items)

time.sleep(2)

item_service.delete_item(1)
items = item_service.get_all_items()
print(items)
