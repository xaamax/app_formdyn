from app.core.exceptions import NotFoundException

from .models import OptionAnswer
from .repository import OptionAnswerRepository
from .schemas import OptionAnswerPartial, OptionAnswerSchema


class OptionAnswerService:
    def __init__(self, repository: OptionAnswerRepository):
        self.repository = repository

    def _get_or_404(self, id: int) -> OptionAnswer:
        model = self.repository.get_by_id(id)
        if not model:
            raise NotFoundException('Opção de Resposta não encontrada')
        return model

    def create(self, data: OptionAnswerSchema) -> OptionAnswer:
        model = OptionAnswer(**data.model_dump())
        return self.repository.create(model)

    def list(self):
        return self.repository.list()

    def get(self, id: int) -> OptionAnswer:
        return self._get_or_404(id)

    def update(self, id: int, data: OptionAnswerSchema) -> OptionAnswer:
        model = self._get_or_404(id)

        update_data = data.model_dump()

        for attr, value in update_data.items():
            setattr(model, attr, value)

        return self.repository.create(model)

    def patch(self, id: int, data: OptionAnswerPartial) -> OptionAnswer:
        model = self._get_or_404(id)

        update_data = data.model_dump(exclude_unset=True)

        for attr, value in update_data.items():
            setattr(model, attr, value)

        return self.repository.create(model)

    def delete(self, id: int):
        model = self._get_or_404(id)
        self.repository.delete(model)
