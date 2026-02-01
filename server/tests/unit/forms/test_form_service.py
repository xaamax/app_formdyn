import pytest

from app.core.exceptions import BadRequestException, NotFoundException
from app.modules.forms.models import Form
from app.modules.forms.schemas import FormPartial, FormSchema
from app.modules.forms.service import FormService


class FakeFormRepository:
    def __init__(self):
        self.data = {}
        self.counter = 1

    def list(self):
        return list(self.data.values())

    def create(self, form: Form) -> Form:
        if not getattr(form, 'id', None):
            form.id = self.counter
            self.counter += 1
        self.data[form.id] = form
        return form

    def get_by_id(self, form_id: int) -> Form | None:
        return self.data.get(form_id)

    def delete(self, form: Form):
        self.data.pop(form.id, None)


# ---------- LIST ----------


def test_form_service_list():
    repo = FakeFormRepository()
    service = FormService(repo)

    service.create(FormSchema(name='Form A', type=1))
    service.create(FormSchema(name='Form B', type=2))

    result = service.list()

    assert len(result) == 2
    assert result[0].name == 'Form A'
    assert result[1].name == 'Form B'


# ---------- CREATE ----------


def test_form_service_create():
    repo = FakeFormRepository()
    service = FormService(repo)

    form = service.create(FormSchema(name='Form A', type=1))

    assert form.id == 1
    assert form.name == 'Form A'
    assert form.type == 1


def test_form_service_create_invalid_type():
    repo = FakeFormRepository()
    service = FormService(repo)

    with pytest.raises(
        BadRequestException, match='0 não é um tipo válido'
    ):
        service.create(FormSchema(name='Invalid', type=0))


# ---------- GET ----------


def test_form_service_get_success():
    repo = FakeFormRepository()
    service = FormService(repo)

    created = service.create(FormSchema(name='Form A', type=1))

    fetched = service.get(created.id)

    assert fetched.id == created.id
    assert fetched.name == 'Form A'


def test_form_service_get_not_found():
    repo = FakeFormRepository()
    service = FormService(repo)

    with pytest.raises(NotFoundException, match='Formulário não encontrado'):
        service.get(999)


# ---------- UPDATE ----------


def test_form_service_update():
    repo = FakeFormRepository()
    service = FormService(repo)

    created = service.create(FormSchema(name='Original', type=1))

    updated = service.update(created.id, FormSchema(name='Updated', type=2))

    assert updated.id == created.id
    assert updated.name == 'Updated'
    assert updated.type == 2


def test_form_service_update_not_found():
    repo = FakeFormRepository()
    service = FormService(repo)

    with pytest.raises(NotFoundException, match='Formulário não encontrado'):
        service.update(999, FormSchema(name='X', type=1))


def test_form_service_update_invalid_type():
    repo = FakeFormRepository()
    service = FormService(repo)

    created = service.create(FormSchema(name='Original', type=1))

    with pytest.raises(
        BadRequestException, match='0 não é um tipo válido'
    ):
        service.update(created.id, FormSchema(name='Updated', type=0))


# ---------- PATCH ----------


def test_form_service_patch():
    repo = FakeFormRepository()
    service = FormService(repo)

    created = service.create(FormSchema(name='Original', type=1))

    patched = service.patch(created.id, FormPartial(name='Patched'))

    assert patched.name == 'Patched'
    assert patched.type == 1


def test_form_service_patch_invalid_type():
    repo = FakeFormRepository()
    service = FormService(repo)

    created = service.create(FormSchema(name='Original', type=1))

    with pytest.raises(
        BadRequestException, match='0 não é um tipo válido'
    ):
        service.patch(created.id, FormPartial(type=0))


def test_form_service_patch_not_found():
    repo = FakeFormRepository()
    service = FormService(repo)

    with pytest.raises(NotFoundException, match='Formulário não encontrado'):
        service.patch(999, FormPartial(name='X'))


# ---------- DELETE ----------


def test_form_service_delete():
    repo = FakeFormRepository()
    service = FormService(repo)

    created = service.create(FormSchema(name='Form A', type=1))

    service.delete(created.id)

    with pytest.raises(NotFoundException, match='Formulário não encontrado'):
        service.get(created.id)


def test_form_service_delete_not_found():
    repo = FakeFormRepository()
    service = FormService(repo)

    with pytest.raises(NotFoundException, match='Formulário não encontrado'):
        service.delete(999)
