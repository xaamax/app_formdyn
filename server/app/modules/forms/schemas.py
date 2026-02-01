from typing import Optional

from pydantic import BaseModel

from app.modules.forms.enums import FormTypeEnum
from app.shared.pagination import PaginatedResponse


class FormSchema(BaseModel):
    name: str
    type: int


class FormPartial(BaseModel):
    name: Optional[str] = None
    type: Optional[int] = None


class FormPublic(BaseModel):
    id: int
    name: str
    type: str

    @classmethod
    def from_model(cls, model):
        return cls(
            id=model.id, name=model.name, type=FormTypeEnum(model.type).label
        )


FormListPaginated = PaginatedResponse
