from ..interfaces.repository import Repository


class InMemoryRepository(Repository):
    def __init__(self):
        self._data_source = [
            {
                "id": "919eaf51-41eb-408b-86d8-fba661e2f755",
                "name": "Test attraction",
                "latitude": 12.4567,
                "longitude": 24.8909,
                "opening_hours": {
                    "Monday": {
                        "Open": 10,
                        "Close": 18
                    },
                    "Tuesday": {
                        "Open": 10,
                        "Close": 18
                    },
                    "Wednesday": {
                        "Open": 10,
                        "Close": 18
                    },
                    "Thursday": {
                        "Open": 10,
                        "Close": 18
                    }
                },
                "prices": {
                    "Entry fee": {
                        "Normal": 20,
                        "Child": 10,
                        "Dog": 5
                    },
                    "Photos": {
                        "Normal": 10,
                        "Child": 5,
                        "Dog": 2.5
                    }
                }
            },
            {
                "id": "549eaf51-41eb-408b-86d8-fba661e2f755",
                "name": "Test attraction",
                "latitude": 12.4567,
                "longitude": 24.8909,
                "opening_hours": {
                    "Monday": {
                        "Open": 10,
                        "Close": 18
                    },
                    "Tuesday": {
                        "Open": 10,
                        "Close": 18
                    },
                    "Wednesday": {
                        "Open": 10,
                        "Close": 18
                    },
                    "Thursday": {
                        "Open": 10,
                        "Close": 18
                    }
                },
                "prices": {
                    "Entry fee": {
                        "Normal": 20,
                        "Child": 10,
                        "Dog": 5
                    },
                    "Photos": {
                        "Normal": 10,
                        "Child": 5,
                        "Dog": 2.5
                    }
                }
            }
        ]

    def get_all(self):
        return self._data_source

    def get_by_id(self, item_id):
        return next((item for item in self._data_source if item["id"] == item_id), None)

    def create(self, item):
        self._data_source.append(item)
        return item

    def update(self, updated_item):
        index = next((i for i, obj in enumerate(self._data_source) if obj["id"] == str(updated_item.id)), None)
        if index is not None:
            self._data_source[index].update(updated_item)
            return True
        return False

    def delete(self, item_id):
        index = next((i for i, obj in enumerate(self._data_source) if obj["id"] == item_id), None)
        if index is not None:
            self._data_source.pop(index)
            return True
        return False
