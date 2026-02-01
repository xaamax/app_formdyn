import pytest

from app.core.exceptions import NotFoundException
from app.modules.answers.models import Answer
from app.modules.answers.schemas import AnswerPartial, AnswerSchema
from app.modules.answers.service import AnswerService


class FakeAnswerRepository:
    def __init__(self):
        self.data = {}
        self.counter = 1

    def list(self):
        return list(self.data.values())

    def create(self, answer: Answer) -> Answer:
        if not getattr(answer, 'id', None):
            answer.id = self.counter
            self.counter += 1
        self.data[answer.id] = answer
        return answer

    def get_by_id(self, answer_id: int) -> Answer | None:
        return self.data.get(answer_id)

    def delete(self, answer: Answer):
        self.data.pop(answer.id, None)


def valid_answer_schema(**overrides):
    data = {
        'description': 'Descrição',
        'legend': 'Legenda',
        'order': 1,
        'only_legend': False,
        'color': None,
        'background': None,
    }
    data.update(overrides)
    return AnswerSchema(**data)


def test_answer_service_list():
    repo = FakeAnswerRepository()
    service = AnswerService(repo)

    service.create(valid_answer_schema(description='A'))
    service.create(valid_answer_schema(description='B', order=2))

    result = service.list()

    assert len(result) == 2
    assert result[0].description == 'A'
    assert result[1].description == 'B'


def test_answer_service_create():
    repo = FakeAnswerRepository()
    service = AnswerService(repo)

    answer = service.create(valid_answer_schema())

    assert answer.id == 1
    assert answer.description == 'Descrição'
    assert answer.legend == 'Legenda'
    assert answer.order == 1
    assert answer.only_legend is False


def test_answer_service_get_success():
    repo = FakeAnswerRepository()
    service = AnswerService(repo)

    created = service.create(valid_answer_schema())

    fetched = service.get(created.id)

    assert fetched.id == created.id
    assert fetched.description == 'Descrição'


def test_answer_service_get_not_found():
    repo = FakeAnswerRepository()
    service = AnswerService(repo)

    with pytest.raises(NotFoundException, match='Resposta não encontrada'):
        service.get(999)


def test_answer_service_update():
    repo = FakeAnswerRepository()
    service = AnswerService(repo)

    created = service.create(valid_answer_schema())

    updated = service.update(
        created.id,
        valid_answer_schema(
            description='Atualizada',
            legend='Nova',
            order=2,
            only_legend=True,
            color='#FFF',
            background='#000',
        ),
    )

    assert updated.id == created.id
    assert updated.description == 'Atualizada'
    assert updated.legend == 'Nova'
    assert updated.order == 2
    assert updated.only_legend is True
    assert updated.color == '#FFF'
    assert updated.background == '#000'


def test_answer_service_update_not_found():
    repo = FakeAnswerRepository()
    service = AnswerService(repo)

    with pytest.raises(NotFoundException, match='Resposta não encontrada'):
        service.update(999, valid_answer_schema())


def test_answer_service_patch_partial():
    repo = FakeAnswerRepository()
    service = AnswerService(repo)

    created = service.create(valid_answer_schema())

    patched = service.patch(
        created.id,
        AnswerPartial(description='Patch'),
    )

    assert patched.description == 'Patch'
    assert patched.legend == 'Legenda'
    assert patched.order == 1


def test_answer_service_patch_multiple_fields():
    repo = FakeAnswerRepository()
    service = AnswerService(repo)

    created = service.create(valid_answer_schema())

    patched = service.patch(
        created.id,
        AnswerPartial(
            legend='Nova Legenda',
            order=10,
            only_legend=True,
        ),
    )

    assert patched.legend == 'Nova Legenda'
    assert patched.order == 10
    assert patched.only_legend is True


def test_answer_service_patch_not_found():
    repo = FakeAnswerRepository()
    service = AnswerService(repo)

    with pytest.raises(NotFoundException, match='Resposta não encontrada'):
        service.patch(999, AnswerPartial(description='X'))


def test_answer_service_delete():
    repo = FakeAnswerRepository()
    service = AnswerService(repo)

    created = service.create(valid_answer_schema())

    service.delete(created.id)

    with pytest.raises(NotFoundException, match='Resposta não encontrada'):
        service.get(created.id)


def test_answer_service_delete_not_found():
    repo = FakeAnswerRepository()
    service = AnswerService(repo)

    with pytest.raises(NotFoundException, match='Resposta não encontrada'):
        service.delete(999)
