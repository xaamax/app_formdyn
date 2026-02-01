from server.app.core.exceptions import AppException

from .models import Field
from .repository import FieldRepository
from .schemas import FieldPartial, FieldSchema


class FieldService:
    def __init__(self, repository: FieldRepository):
        self.repository = repository

    def create(self, data: FieldSchema) -> Field:
        form = Field(**data.model_dump())
        return self.repository.create(form)

    def list(self):
        return self.repository.list()

    def get(self, form_id: int) -> Field:
        form = self.repository.get_by_id(form_id)
        if not form:
            raise AppException()
        return form

    def update(self, form_id: int, data: FieldSchema) -> Field:
        form = self.get(form_id)
        for attr, value in data.model_dump().items():
            setattr(form, attr, value)
        return self.repository.create(form)

    def patch(self, form_id: int, data: FieldPartial) -> Field:
        form = self.get(form_id)
        for attr, value in data.model_dump(exclude_unset=True).items():
            setattr(form, attr, value)
        return self.repository.create(form)

    def delete(self, form_id: int):
        form = self.get(form_id)
        self.repository.delete(form)
