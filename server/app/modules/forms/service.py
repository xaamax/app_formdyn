from app.core.exceptions import BadRequestException, NotFoundException

from .enums import FormTypeEnum
from .models import Form
from .repository import FormRepository
from .schemas import FormPartial, FormSchema


def _validate_type(value: int) -> FormTypeEnum:
    try:
        return FormTypeEnum(value)
    except ValueError:
        raise BadRequestException(f'{value} não é um tipo válido')


class FormService:
    def __init__(self, repository: FormRepository):
        self.repository = repository

    def _get_or_404(self, id: int) -> Form:
        model = self.repository.get_by_id(id)
        if not model:
            raise NotFoundException('Formulário não encontrado')
        return model

    def create(self, data: FormSchema) -> Form:
        model = Form(**{
            **data.model_dump(exclude={'type'}),
            'type': _validate_type(data.type),
        })
        return self.repository.create(model)

    def list(self):
        return self.repository.list()

    def get(self, id: int) -> Form:
        return self._get_or_404(id)

    def update(self, id: int, data: FormSchema) -> Form:
        model = self._get_or_404(id)

        update_data = data.model_dump()

        if 'type' in update_data:
            update_data['type'] = _validate_type(update_data['type'])

        for attr, value in update_data.items():
            setattr(model, attr, value)

        return self.repository.create(model)

    def patch(self, id: int, data: FormPartial) -> Form:
        model = self._get_or_404(id)

        update_data = data.model_dump(exclude_unset=True)

        if 'type' in update_data:
            update_data['type'] = _validate_type(update_data['type'])

        for attr, value in update_data.items():
            setattr(model, attr, value)

        return self.repository.create(model)

    def delete(self, id: int):
        model = self._get_or_404(id)
        self.repository.delete(model)
