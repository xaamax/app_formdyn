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
    form_id: int
    answer_id: int
    order: int

    @classmethod
    def from_model(cls, model):
        data = { **model.__dict__, }
        return cls.model_validate(data)

# class OptionAnswerWithFormAndAnswer(BaseModel):
#     id: int
#     form_name: str
#     answer_description: str

#     @classmethod
#     def from_model(cls, model):
#         data = {
#             'id': model.id,
#             'order': model.order,
#             'form': model.form.name,
#             'answer': model.answer.description,
#         }
#         return cls.model_validate(data)


OptionAnswerListPaginated = PaginatedResponse[OptionAnswerPublic]
