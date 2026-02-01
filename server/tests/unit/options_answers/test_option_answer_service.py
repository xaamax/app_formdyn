import pytest

from app.core.exceptions import NotFoundException
from app.modules.options_answers.models import OptionAnswer
from app.modules.options_answers.schemas import (
    OptionAnswerPartial,
    OptionAnswerSchema,
)
from app.modules.options_answers.service import OptionAnswerService


class FakeOptionAnswerRepository:
    def __init__(self):
        self.data = {}
        self.counter = 1

    def list(self):
        return list(self.data.values())

    def create(self, model: OptionAnswer) -> OptionAnswer:
        if not getattr(model, 'id', None):
            model.id = self.counter
            self.counter += 1
        self.data[model.id] = model
        return model

    def get_by_id(self, model_id: int) -> OptionAnswer | None:
        return self.data.get(model_id)

    def delete(self, model: OptionAnswer):
        self.data.pop(model.id, None)


def valid_option_answer_schema(**overrides):
    data = {
        'form_id': 1,
        'answer_id': 1,
        'order': 1,
    }
    data.update(overrides)
    return OptionAnswerSchema(**data)


def test_option_answer_service_list():
    repo = FakeOptionAnswerRepository()
    service = OptionAnswerService(repo)

    service.create(valid_option_answer_schema(order=1))
    service.create(valid_option_answer_schema(order=2))

    result = service.list()

    assert len(result) == 2
    assert result[0].order == 1
    assert result[1].order == 2


def test_option_answer_service_create():
    repo = FakeOptionAnswerRepository()
    service = OptionAnswerService(repo)

    option = service.create(valid_option_answer_schema())

    assert option.id == 1
    assert option.form_id == 1
    assert option.answer_id == 1
    assert option.order == 1


def test_option_answer_service_get_success():
    repo = FakeOptionAnswerRepository()
    service = OptionAnswerService(repo)

    created = service.create(valid_option_answer_schema())

    fetched = service.get(created.id)

    assert fetched.id == created.id
    assert fetched.order == 1


def test_option_answer_service_get_not_found():
    repo = FakeOptionAnswerRepository()
    service = OptionAnswerService(repo)

    with pytest.raises(
        NotFoundException, match='Opção de Resposta não encontrada'
    ):
        service.get(999)


def test_option_answer_service_update():
    repo = FakeOptionAnswerRepository()
    service = OptionAnswerService(repo)

    created = service.create(valid_option_answer_schema())

    updated = service.update(
        created.id,
        valid_option_answer_schema(
            form_id=2,
            answer_id=3,
            order=10,
        ),
    )

    assert updated.id == created.id
    assert updated.form_id == 2
    assert updated.answer_id == 3
    assert updated.order == 10


def test_option_answer_service_update_not_found():
    repo = FakeOptionAnswerRepository()
    service = OptionAnswerService(repo)

    with pytest.raises(
        NotFoundException, match='Opção de Resposta não encontrada'
    ):
        service.update(999, valid_option_answer_schema())


def test_option_answer_service_patch_partial():
    repo = FakeOptionAnswerRepository()
    service = OptionAnswerService(repo)

    created = service.create(valid_option_answer_schema())

    patched = service.patch(
        created.id,
        OptionAnswerPartial(order=99),
    )

    assert patched.order == 99
    assert patched.form_id == 1
    assert patched.answer_id == 1


def test_option_answer_service_patch_multiple_fields():
    repo = FakeOptionAnswerRepository()
    service = OptionAnswerService(repo)

    created = service.create(valid_option_answer_schema())

    patched = service.patch(
        created.id,
        OptionAnswerPartial(
            form_id=5,
            answer_id=6,
        ),
    )

    assert patched.form_id == 5
    assert patched.answer_id == 6
    assert patched.order == 1


def test_option_answer_service_patch_not_found():
    repo = FakeOptionAnswerRepository()
    service = OptionAnswerService(repo)

    with pytest.raises(
        NotFoundException, match='Opção de Resposta não encontrada'
    ):
        service.patch(999, OptionAnswerPartial(order=1))


def test_option_answer_service_delete():
    repo = FakeOptionAnswerRepository()
    service = OptionAnswerService(repo)

    created = service.create(valid_option_answer_schema())

    service.delete(created.id)

    with pytest.raises(
        NotFoundException, match='Opção de Resposta não encontrada'
    ):
        service.get(created.id)


def test_option_answer_service_delete_not_found():
    repo = FakeOptionAnswerRepository()
    service = OptionAnswerService(repo)

    with pytest.raises(
        NotFoundException, match='Opção de Resposta não encontrada'
    ):
        service.delete(999)
