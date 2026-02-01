import pytest

from app.core.exceptions import BadRequestException, NotFoundException
from app.modules.fields.models import Field
from app.modules.fields.schemas import FieldPartial, FieldSchema
from app.modules.fields.service import FieldService


class FakeFieldRepository:
    def __init__(self):
        self.data = {}
        self.counter = 1

    def list(self):
        return list(self.data.values())

    def create(self, field: Field) -> Field:
        if not getattr(field, 'id', None):
            field.id = self.counter
            self.counter += 1
        self.data[field.id] = field
        return field

    def get_by_id(self, field_id: int) -> Field | None:
        return self.data.get(field_id)

    def delete(self, field: Field):
        self.data.pop(field.id, None)


def valid_field_schema(**overrides):
    data = {
        'form_id': 1,
        'slug': 'field_slug',
        'name': 'field_name',
        'label': 'Field Label',
        'type': 1,
        'order': 1,
        'readonly': False,
        'observation': None,
        'optional': None,
        'grid': None,
        'size': None,
        'mask': None,
        'placeholder': None,
    }
    data.update(overrides)
    return FieldSchema(**data)


def test_field_service_list():
    repo = FakeFieldRepository()
    service = FieldService(repo)

    service.create(valid_field_schema(label='Field A'))
    service.create(valid_field_schema(label='Field B', slug='field_b'))

    result = service.list()

    assert len(result) == 2
    assert result[0].label == 'Field A'
    assert result[1].label == 'Field B'


def test_field_service_create():
    repo = FakeFieldRepository()
    service = FieldService(repo)

    field = service.create(valid_field_schema())

    assert field.id == 1
    assert field.label == 'Field Label'
    assert field.type == 1


def test_field_service_create_invalid_type():
    repo = FakeFieldRepository()
    service = FieldService(repo)

    with pytest.raises(BadRequestException, match='0 não é um tipo válido'):
        service.create(valid_field_schema(type=0))


def test_field_service_get_success():
    repo = FakeFieldRepository()
    service = FieldService(repo)

    created = service.create(valid_field_schema())

    fetched = service.get(created.id)

    assert fetched.id == created.id
    assert fetched.label == 'Field Label'


def test_field_service_get_not_found():
    repo = FakeFieldRepository()
    service = FieldService(repo)

    with pytest.raises(NotFoundException, match='Campo não encontrado'):
        service.get(999)


def test_field_service_update():
    repo = FakeFieldRepository()
    service = FieldService(repo)

    created = service.create(valid_field_schema())

    updated = service.update(
        created.id,
        valid_field_schema(label='Updated', type=2),
    )

    assert updated.id == created.id
    assert updated.label == 'Updated'
    assert updated.type == 2


def test_field_service_update_invalid_type():
    repo = FakeFieldRepository()
    service = FieldService(repo)

    created = service.create(valid_field_schema())

    with pytest.raises(BadRequestException, match='0 não é um tipo válido'):
        service.update(created.id, valid_field_schema(type=0))


def test_field_service_update_not_found():
    repo = FakeFieldRepository()
    service = FieldService(repo)

    with pytest.raises(NotFoundException, match='Campo não encontrado'):
        service.update(999, valid_field_schema())


def test_field_service_patch_name_only():
    repo = FakeFieldRepository()
    service = FieldService(repo)

    created = service.create(valid_field_schema())

    patched = service.patch(created.id, FieldPartial(label='Patched Label'))

    assert patched.label == 'Patched Label'
    assert patched.type == 1


def test_field_service_patch_type_only():
    repo = FakeFieldRepository()
    service = FieldService(repo)

    created = service.create(valid_field_schema())

    patched = service.patch(created.id, FieldPartial(type=2))

    assert patched.type == 2


def test_field_service_patch_invalid_type():
    repo = FakeFieldRepository()
    service = FieldService(repo)

    created = service.create(valid_field_schema())

    with pytest.raises(BadRequestException, match='0 não é um tipo válido'):
        service.patch(created.id, FieldPartial(type=0))


def test_field_service_patch_not_found():
    repo = FakeFieldRepository()
    service = FieldService(repo)

    with pytest.raises(NotFoundException, match='Campo não encontrado'):
        service.patch(999, FieldPartial(label='X'))


def test_field_service_delete():
    repo = FakeFieldRepository()
    service = FieldService(repo)

    created = service.create(valid_field_schema())

    service.delete(created.id)

    with pytest.raises(NotFoundException, match='Campo não encontrado'):
        service.get(created.id)


def test_field_service_delete_not_found():
    repo = FakeFieldRepository()
    service = FieldService(repo)

    with pytest.raises(NotFoundException, match='Campo não encontrado'):
        service.delete(999)
