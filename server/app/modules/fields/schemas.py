from typing import Optional

from pydantic import BaseModel

from app.shared.pagination import PaginatedResponse

from .enums import FieldTypeEnum


class FieldSchema(BaseModel):
    form_id: int
    slug: str
    label: str
    type: int
    order: int
    readonly: bool
    observation: Optional[str] = None
    optional: Optional[str] = None
    grid: Optional[str] = None
    size: Optional[int] = None
    mask: Optional[str] = None
    placeholder: Optional[str] = None


class FieldPartial(BaseModel):
    slug: Optional[str] = None
    label: Optional[str] = None
    type: Optional[int] = None
    order: Optional[int] = None
    readonly: Optional[bool] = None
    observation: Optional[str] = None
    optional: Optional[str] = None
    grid: Optional[str] = None
    size: Optional[int] = None
    mask: Optional[str] = None
    placeholder: Optional[str] = None


class FieldPublic(BaseModel):
    id: int
    slug: str
    label: str
    type: str
    order: int
    readonly: bool
    observation: str | None
    optional: str | None
    grid: str | None
    size: int | None
    mask: str | None
    placeholder: str | None

    @classmethod
    def from_model(cls, model):
        data = {
            **model.__dict__,
            'type': (
                FieldTypeEnum(model.type).label
                if model.type is not None
                else None
            ),
        }
        return cls.model_validate(data)


FieldPaginated = PaginatedResponse[FieldPublic]
