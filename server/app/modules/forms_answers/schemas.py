from typing import Optional

from pydantic import BaseModel

from app.shared.pagination import PaginatedResponse


class FormAnswerSchema(BaseModel):
    form_id: int
    answer_id: int
    value: Optional[str] = None


class FormAnswerPartial(BaseModel):
    form_id: Optional[int] = None
    answer_id: Optional[int] = None
    value: Optional[str] = None


class FormAnswerPublic(BaseModel):
    id: int
    form_id: int
    answer_id: int
    value: str | None

    @classmethod
    def from_model(cls, model):
        return cls.model_validate(model.__dict__)


FormAnswerListPaginated = PaginatedResponse[FormAnswerPublic]
