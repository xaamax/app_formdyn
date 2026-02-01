from app.core.exceptions import NotFoundException

from .models import FormAnswer
from .repository import FormAnswerRepository
from .schemas import FormAnswerPartial, FormAnswerSchema


class FormAnswerService:
    def __init__(self, repository: FormAnswerRepository):
        self.repository = repository

    def _get_or_404(self, id: int) -> FormAnswer:
        model = self.repository.get_by_id(id)
        if not model:
            raise NotFoundException('Resposta de Formulário não encontrada')
        return model

    def create(self, data: FormAnswerSchema) -> FormAnswer:
        model = FormAnswer(**data.model_dump())
        return self.repository.create(model)

    def list(self):
        return self.repository.list()

    def get(self, id: int) -> FormAnswer:
        return self._get_or_404(id)

    def update(self, id: int, data: FormAnswerSchema) -> FormAnswer:
        model = self._get_or_404(id)

        update_data = data.model_dump()

        for attr, value in update_data.items():
            setattr(model, attr, value)

        return self.repository.create(model)

    def patch(self, id: int, data: FormAnswerPartial) -> FormAnswer:
        model = self._get_or_404(id)

        update_data = data.model_dump(exclude_unset=True)

        for attr, value in update_data.items():
            setattr(model, attr, value)

        return self.repository.create(model)

    def delete(self, id: int):
        model = self._get_or_404(id)
        self.repository.delete(model)
