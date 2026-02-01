from app.core.exceptions import BadRequestException, NotFoundException

from .enums import FormTypeEnum
from .models import Form
from .repository import FormRepository
from .schemas import FormPartial, FormSchema


class FormService:
    def __init__(self, repository: FormRepository):
        self.repository = repository

    def create(self, data: FormSchema) -> Form:
        try:
            form_type = FormTypeEnum(data.type)
        except ValueError:
            raise BadRequestException(
                f'{data.type} não é um tipo válido'
            )

        form = Form(name=data.name, type=form_type)
        return self.repository.create(form)

    def list(self):
        return self.repository.list()

    def get(self, form_id: int) -> Form:
        form = self.repository.get_by_id(form_id)
        if not form:
            raise NotFoundException('Formulário não encontrado')
        return form

    def update(self, form_id: int, data: FormSchema) -> Form:
        form = self.get(form_id)

        try:
            form.type = FormTypeEnum(data.type)
        except ValueError:
            raise BadRequestException(
                f'{data.type} não é um tipo válido'
            )

        form.name = data.name
        return self.repository.create(form)

    def patch(self, form_id: int, data: FormPartial) -> Form:
        form = self.get(form_id)

        if data.name is not None:
            form.name = data.name

        if data.type is not None:
            try:
                form.type = FormTypeEnum(data.type)
            except ValueError:
                raise BadRequestException(
                    f'{data.type} não é um tipo válido'
                )

        return self.repository.create(form)

    def delete(self, form_id: int):
        form = self.get(form_id)
        self.repository.delete(form)
