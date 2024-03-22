import json


class SerializerMixin:
    def __init__(self, data):
        for field in self.__table__.columns:
            if getattr(field, "name"):
                setattr(self, field.name, data[field.name])

    def to_dict(self) -> dict:
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
