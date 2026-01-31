from typing import Optional

from pydantic import BaseModel

from app.shared.pagination import PaginatedResponse


class OptionAnswerSchema(BaseModel):
    form_id: int
    answer_id: int
    order: int


class OptionAnswerPartial(BaseModel):
    form_id: Optional[int] = None
    answer_id: Optional[int] = None
    order: Optional[int] = None


class OptionAnswerPublic(BaseModel):
    id: int
    form_name: str
    answer_description: str | None

    @classmethod
    def from_model(cls, model):
        data = {
            'id': model.id,
            'order': model.order,
            'form_name': model.form.name,
            'answer_description': (
                model.answer.description if model.answer is not None else None
            ),
        }
        return cls.model_validate(data)


OptionAnswerPaginated = PaginatedResponse[OptionAnswerPublic]
