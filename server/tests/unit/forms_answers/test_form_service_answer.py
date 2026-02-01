import pytest

from app.core.exceptions import NotFoundException
from app.modules.forms_answers.models import FormAnswer
from app.modules.forms_answers.schemas import (
    FormAnswerPartial,
    FormAnswerSchema,
)
from app.modules.forms_answers.service import FormAnswerService


class FakeFormAnswerRepository:
    def __init__(self):
        self.data = {}
        self.counter = 1

    def list(self):
        return list(self.data.values())

    def create(self, model: FormAnswer) -> FormAnswer:
        # cria ou "atualiza"
        if not getattr(model, 'id', None):
            model.id = self.counter
            self.counter += 1
        self.data[model.id] = model
        return model

    def get_by_id(self, model_id: int) -> FormAnswer | None:
        return self.data.get(model_id)

    def delete(self, model: FormAnswer):
        self.data.pop(model.id, None)


def valid_form_answer_schema(**overrides):
    data = {
        'form_id': 1,
        'answer_id': 1,
        'value': 'Teste',
    }
    data.update(overrides)
    return FormAnswerSchema(**data)


# ---------- INTERNAL (_get_or_404) ----------


def test_form_answer_service_get_or_404_success():
    repo = FakeFormAnswerRepository()
    service = FormAnswerService(repo)

    created = service.create(valid_form_answer_schema())

    fetched = service._get_or_404(created.id)

    assert fetched.id == created.id
    assert fetched.value == 'Teste'


def test_form_answer_service_get_or_404_not_found():
    repo = FakeFormAnswerRepository()
    service = FormAnswerService(repo)

    with pytest.raises(
        NotFoundException, match='Resposta de Formulário não encontrada'
    ):
        service._get_or_404(999)


# ---------- CREATE / LIST / GET ----------


def test_form_answer_service_create():
    repo = FakeFormAnswerRepository()
    service = FormAnswerService(repo)

    created = service.create(
        valid_form_answer_schema(form_id=10, answer_id=20)
    )

    assert created.id == 1
    assert created.form_id == 10
    assert created.answer_id == 20
    assert created.value == 'Teste'


def test_form_answer_service_list():
    repo = FakeFormAnswerRepository()
    service = FormAnswerService(repo)

    service.create(valid_form_answer_schema(value='A'))
    service.create(valid_form_answer_schema(value='B', answer_id=2))

    items = service.list()

    assert len(items) == 2
    assert items[0].value == 'A'
    assert items[1].value == 'B'


def test_form_answer_service_get_success():
    repo = FakeFormAnswerRepository()
    service = FormAnswerService(repo)

    created = service.create(valid_form_answer_schema(value='Get'))

    fetched = service.get(created.id)

    assert fetched.id == created.id
    assert fetched.value == 'Get'


def test_form_answer_service_get_not_found():
    repo = FakeFormAnswerRepository()
    service = FormAnswerService(repo)

    with pytest.raises(
        NotFoundException, match='Resposta de Formulário não encontrada'
    ):
        service.get(999)


# ---------- UPDATE ----------


def test_form_answer_service_update_success_updates_all_fields():
    repo = FakeFormAnswerRepository()
    service = FormAnswerService(repo)

    created = service.create(
        valid_form_answer_schema(form_id=1, answer_id=1, value='Old')
    )

    updated = service.update(
        created.id,
        valid_form_answer_schema(form_id=2, answer_id=3, value='New'),
    )

    assert updated.id == created.id
    assert updated.form_id == 2
    assert updated.answer_id == 3
    assert updated.value == 'New'


def test_form_answer_service_update_not_found():
    repo = FakeFormAnswerRepository()
    service = FormAnswerService(repo)

    with pytest.raises(
        NotFoundException, match='Resposta de Formulário não encontrada'
    ):
        service.update(999, valid_form_answer_schema())


# ---------- PATCH ----------


def test_form_answer_service_patch_empty_payload_no_changes():
    """
    Garante que o caminho do exclude_unset=True com payload vazio
    não executa loop e não quebra (cobre branch do loop "vazio").
    """
    repo = FakeFormAnswerRepository()
    service = FormAnswerService(repo)

    created = service.create(
        valid_form_answer_schema(form_id=1, answer_id=1, value='Keep')
    )

    patched = service.patch(created.id, FormAnswerPartial())

    assert patched.id == created.id
    assert patched.form_id == 1
    assert patched.answer_id == 1
    assert patched.value == 'Keep'


def test_form_answer_service_patch_partial_updates_only_sent_fields():
    repo = FakeFormAnswerRepository()
    service = FormAnswerService(repo)

    created = service.create(
        valid_form_answer_schema(form_id=1, answer_id=1, value='Old')
    )

    patched = service.patch(
        created.id,
        FormAnswerPartial(value='Patched'),
    )

    assert patched.id == created.id
    assert patched.form_id == 1
    assert patched.answer_id == 1
    assert patched.value == 'Patched'


def test_form_answer_service_patch_multiple_fields():
    repo = FakeFormAnswerRepository()
    service = FormAnswerService(repo)

    created = service.create(
        valid_form_answer_schema(form_id=1, answer_id=1, value='Old')
    )

    patched = service.patch(
        created.id,
        FormAnswerPartial(form_id=9, answer_id=8, value='X'),
    )

    assert patched.form_id == 9
    assert patched.answer_id == 8
    assert patched.value == 'X'


def test_form_answer_service_patch_not_found():
    repo = FakeFormAnswerRepository()
    service = FormAnswerService(repo)

    with pytest.raises(
        NotFoundException, match='Resposta de Formulário não encontrada'
    ):
        service.patch(999, FormAnswerPartial(value='X'))


# ---------- DELETE ----------


def test_form_answer_service_delete_success():
    repo = FakeFormAnswerRepository()
    service = FormAnswerService(repo)

    created = service.create(valid_form_answer_schema())

    service.delete(created.id)

    with pytest.raises(
        NotFoundException, match='Resposta de Formulário não encontrada'
    ):
        service.get(created.id)


def test_form_answer_service_delete_not_found():
    repo = FakeFormAnswerRepository()
    service = FormAnswerService(repo)

    with pytest.raises(
        NotFoundException, match='Resposta de Formulário não encontrada'
    ):
        service.delete(999)
