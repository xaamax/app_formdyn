import pytest
from pydantic import ValidationError

from app.modules.forms.enums import FormTypeEnum
from app.modules.forms.models import Form
from app.modules.forms.schemas import FormPublic, FormSchema


def test_form_schema_valid_minimal():
    schema = FormSchema(
        name='Formulário Teste',
        type=FormTypeEnum.FORMULARIO_ENSINO_FUNDAMENTAL.value,
    )

    assert schema.name == 'Formulário Teste'
    assert schema.type == FormTypeEnum.FORMULARIO_ENSINO_FUNDAMENTAL.value


def test_form_schema_missing_required_forms():
    with pytest.raises(ValidationError):
        FormSchema(name='Formulário Teste')


def test_form_public_from_model_basic():
    form = Form(
        id=1,
        name='Formulário Teste',
        type=FormTypeEnum.FORMULARIO_ENSINO_FUNDAMENTAL.value,
    )

    public = FormPublic.from_model(form)

    assert public.id == 1
    assert public.name == 'Formulário Teste'
    assert public.type == FormTypeEnum.FORMULARIO_ENSINO_FUNDAMENTAL.label
