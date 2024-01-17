from uuid import uuid4


class AttractionService:
    def __init__(self, repository):
        self._repository = repository

    def get_all_items(self):
        return self._repository.get_all()

    def get_item_by_id(self, item_id):
        return self._repository.get_by_id(item_id)

    def create_item(self, attraction):
        item = attraction
        if item.id is None:
            item.id = uuid4()
        return self._repository.create(item)

    def update_item(self, item_id):
        item = self._repository.get_by_id(item_id)
        if item is None:
            return False
        return self._repository.update(item)

    def delete_item(self, item_id):
        return self._repository.delete(item_id)