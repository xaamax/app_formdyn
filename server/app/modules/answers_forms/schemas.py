from typing import Optional

from pydantic import BaseModel

from app.shared.pagination import PaginatedResponse


class AnswerFormSchema(BaseModel):
    description: str
    legend: str
    order: int
    only_legend: bool = False
    color: Optional[str] = None
    background: Optional[str] = None


class AnswerFormPartial(BaseModel):
    description: Optional[str] = None
    legend: Optional[str] = None
    order: Optional[int] = None
    only_legend: Optional[bool] = None
    color: Optional[str] = None
    background: Optional[str] = None


class AnswerFormPublic(BaseModel):
    id: int
    description: str
    legend: str
    order: int
    only_legend: bool
    color: Optional[str] = None
    background: Optional[str] = None
    @classmethod
    def from_model(cls, model):
        return cls.model_validate(model.__dict__)

AnswerFormPaginated = PaginatedResponse[AnswerFormPublic]
