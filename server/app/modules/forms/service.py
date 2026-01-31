from .exceptions import FormNotFoundError
from .models import Form
from .repository import FormRepository
from .schemas import FormPartial, FormSchema


class FormService:
    def __init__(self, repository: FormRepository):
        self.repository = repository

    def create(self, data: FormSchema) -> Form:
        form = Form(**data.model_dump())
        return self.repository.create(form)

    def list(self):
        return self.repository.list()

    def get(self, form_id: int) -> Form:
        form = self.repository.get_by_id(form_id)
        if not form:
            raise FormNotFoundError()
        return form

    def update(self, form_id: int, data: FormSchema) -> Form:
        form = self.get(form_id)
        for attr, value in data.model_dump().items():
            setattr(form, attr, value)
        return self.repository.create(form)

    def patch(self, form_id: int, data: FormPartial) -> Form:
        form = self.get(form_id)
        for attr, value in data.model_dump(exclude_unset=True).items():
            setattr(form, attr, value)
        return self.repository.create(form)

    def delete(self, form_id: int):
        form = self.get(form_id)
        self.repository.delete(form)
