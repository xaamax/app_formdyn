import pytest

from app.modules.forms.enums import FormTypeEnum


@pytest.mark.parametrize(
    "enum_value,expected_label",
    [
        (
            FormTypeEnum.FORMULARIO_ENSINO_FUNDAMENTAL,
            "Formulário Ensino Fundamental",
        ),
        (
            FormTypeEnum.FORMULARIO_ENSINO_MEDIO,
            "Formulário Ensino Médio",
        ),
        (
            FormTypeEnum.FORMULARIO_EJA,
            "Formulário EJA",
        ),
    ],
)
def test_form_type_enum_label(enum_value, expected_label):
    assert enum_value.label == expected_label
