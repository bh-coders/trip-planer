from enum import Enum

from pydantic import BaseModel


class QueryParams(BaseModel):
    page: int = 1
    per_page: int = 25

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.per_page

    @property
    def limit(self) -> int:
        return self.per_page


class SortDirection(str, Enum):
    Asc = "asc"
    Desc = "desc"
