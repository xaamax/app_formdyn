from app.modules.forms.enums import FormTypeEnum
from app.modules.forms.schemas import FormPublic


class FakeForm:
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type


def test_form_public_from_model_with_type():
    model = FakeForm(
        id=1,
        name='Form Teste',
        type=FormTypeEnum.FORMULARIO_ENSINO_FUNDAMENTAL.value,
    )

    dto = FormPublic.from_model(model)

    assert dto.id == 1
    assert dto.name == 'Form Teste'
    assert dto.type == 'Formulário Ensino Fundamental'


def test_form_public_from_model_without_type():
    model = FakeForm(
        id=2,
        name='Form Sem Tipo',
        type=None,
    )

    dto = FormPublic.from_model(model)

    assert dto.id == 2
    assert dto.name == 'Form Sem Tipo'
    assert dto.type is None
