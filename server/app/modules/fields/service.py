from app.core.exceptions import BadRequestException, NotFoundException

from .enums import FieldTypeEnum
from .models import Field
from .repository import FieldRepository
from .schemas import FieldPartial, FieldSchema


def _validate_type(value: int) -> FieldTypeEnum:
    try:
        return FieldTypeEnum(value)
    except ValueError:
        raise BadRequestException(f'{value} não é um tipo válido')


class FieldService:
    def __init__(self, repository: FieldRepository):
        self.repository = repository

    def _get_or_404(self, field_id: int) -> Field:
        model = self.repository.get_by_id(field_id)
        if not model:
            raise NotFoundException('Campo não encontrado')
        return model

    def create(self, data: FieldSchema) -> Field:
        model = Field(**{
            **data.model_dump(exclude={'type'}),
            'type': _validate_type(data.type),
        })
        return self.repository.create(model)

    def list(self):
        return self.repository.list()

    def get(self, id: int) -> Field:
        return self._get_or_404(id)

    def update(self, id: int, data: FieldSchema) -> Field:
        model = self._get_or_404(id)

        update_data = data.model_dump()

        if 'type' in update_data:
            update_data['type'] = _validate_type(update_data['type'])

        for attr, value in update_data.items():
            setattr(model, attr, value)

        return self.repository.create(model)

    def patch(self, id: int, data: FieldPartial) -> Field:
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
