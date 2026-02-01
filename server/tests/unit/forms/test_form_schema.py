import pytest
from pydantic import ValidationError

from app.modules.fields.enums import FieldTypeEnum
from app.modules.fields.models import Field
from app.modules.fields.schemas import FieldPublic, FieldSchema

# -----------------------------
# FieldSchema (input / contrato)
# -----------------------------


def test_field_schema_valid_minimal():
    schema = FieldSchema(
        form_id=1,
        slug='name',
        label='Nome',
        type=FieldTypeEnum.FRASE.value,
        order=1,
        readonly=False,
    )

    assert schema.form_id == 1
    assert schema.slug == 'name'
    assert schema.label == 'Nome'
    assert schema.type == FieldTypeEnum.FRASE.value
    assert schema.readonly is False


def test_field_schema_missing_required_fields():
    """
    Contrato da API:
    Campos obrigatórios NÃO podem faltar
    """
    with pytest.raises(ValidationError):
        FieldSchema(
            label='Nome',
            type=FieldTypeEnum.FRASE.value,
        )


def test_field_schema_accepts_optional_fields():
    schema = FieldSchema(
        form_id=1,
        slug='email',
        label='E-mail',
        type=FieldTypeEnum.TEXTO.value,
        order=2,
        readonly=True,
        observation='Obs',
        optional='Sim',
        grid='col-6',
        size=12,
        mask='###',
        placeholder='Digite aqui',
    )

    assert schema.observation == 'Obs'
    assert schema.grid == 'col-6'
    assert schema.size == 12
    assert schema.placeholder == 'Digite aqui'


# -----------------------------------
# FieldPublic (output / API response)
# -----------------------------------


def test_field_public_from_model_basic():
    field = Field(
        id=1,
        form_id=1,
        slug='name',
        label='Nome',
        type=FieldTypeEnum.FRASE.value,
        order=1,
        readonly=False,
        observation=None,
        optional=None,
        grid=None,
        size=None,
        mask=None,
        placeholder=None,
    )

    public = FieldPublic.from_model(field)

    assert public.id == 1
    assert public.slug == 'name'
    assert public.label == 'Nome'
    assert public.type == FieldTypeEnum.FRASE.label
    assert public.readonly is False


def test_field_public_from_model_with_optional_fields():
    field = Field(
        id=2,
        form_id=1,
        slug='email',
        label='E-mail',
        type=FieldTypeEnum.TEXTO.value,
        order=2,
        readonly=True,
        observation='Obs',
        optional='Sim',
        grid='col-6',
        size=12,
        mask='###',
        placeholder='Digite aqui',
    )

    public = FieldPublic.from_model(field)

    assert public.type == FieldTypeEnum.TEXTO.label
    assert public.observation == 'Obs'
    assert public.optional == 'Sim'
    assert public.grid == 'col-6'
    assert public.size == 12
    assert public.mask == '###'
    assert public.placeholder == 'Digite aqui'
