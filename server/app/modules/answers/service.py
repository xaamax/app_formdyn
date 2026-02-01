from app.core.exceptions import NotFoundException

from .models import Answer
from .repository import AnswerRepository
from .schemas import AnswerPartial, AnswerSchema


class AnswerService:
    def __init__(self, repository: AnswerRepository):
        self.repository = repository

    def _get_or_404(self, id: int) -> Answer:
        model = self.repository.get_by_id(id)
        if not model:
            raise NotFoundException('Resposta não encontrada')
        return model

    def create(self, data: AnswerSchema) -> Answer:
        model = Answer(**data.model_dump())
        return self.repository.create(model)

    def list(self):
        return self.repository.list()

    def get(self, id: int) -> Answer:
        return self._get_or_404(id)

    def update(self, id: int, data: AnswerSchema) -> Answer:
        model = self._get_or_404(id)

        update_data = data.model_dump()

        for attr, value in update_data.items():
            setattr(model, attr, value)

        return self.repository.create(model)

    def patch(self, id: int, data: AnswerPartial) -> Answer:
        model = self._get_or_404(id)

        update_data = data.model_dump(exclude_unset=True)

        for attr, value in update_data.items():
            setattr(model, attr, value)

        return self.repository.create(model)

    def delete(self, id: int):
        model = self._get_or_404(id)
        self.repository.delete(model)
