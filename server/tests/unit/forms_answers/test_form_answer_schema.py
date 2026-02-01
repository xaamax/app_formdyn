import pytest
from pydantic import ValidationError

from app.modules.forms_answers.schemas import (
    FormAnswerPartial,
    FormAnswerPublic,
    FormAnswerSchema,
)


class FakeFormAnswerModel:
    def __init__(
        self,
        id: int,
        form_id: int,
        answer_id: int,
        value: str | None,
    ):
        self.id = id
        self.form_id = form_id
        self.answer_id = answer_id
        self.value = value


def test_form_answer_schema_valid_minimal():
    schema = FormAnswerSchema(
        form_id=1,
        answer_id=2,
    )

    assert schema.form_id == 1
    assert schema.answer_id == 2
    assert schema.value is None


def test_form_answer_schema_with_value():
    schema = FormAnswerSchema(
        form_id=1,
        answer_id=2,
        value='Teste',
    )

    assert schema.value == 'Teste'


def test_form_answer_schema_missing_required_fields():
    with pytest.raises(ValidationError):
        FormAnswerSchema(
            form_id=1,
        )


def test_form_answer_partial_empty():
    partial = FormAnswerPartial()

    assert partial.form_id is None
    assert partial.answer_id is None
    assert partial.value is None


def test_form_answer_partial_with_some_fields():
    partial = FormAnswerPartial(
        value='Patch',
    )

    assert partial.value == 'Patch'
    assert partial.form_id is None
    assert partial.answer_id is None


def test_form_answer_partial_with_all_fields():
    partial = FormAnswerPartial(
        form_id=10,
        answer_id=20,
        value='Completo',
    )

    assert partial.form_id == 10
    assert partial.answer_id == 20
    assert partial.value == 'Completo'


def test_form_answer_public_from_model_basic():
    model = FakeFormAnswerModel(
        id=1,
        form_id=1,
        answer_id=2,
        value='Teste',
    )

    public = FormAnswerPublic.from_model(model)

    assert public.id == 1
    assert public.form_id == 1
    assert public.answer_id == 2
    assert public.value == 'Teste'


def test_form_answer_public_from_model_with_none_value():
    model = FakeFormAnswerModel(
        id=2,
        form_id=3,
        answer_id=4,
        value=None,
    )

    public = FormAnswerPublic.from_model(model)

    assert public.id == 2
    assert public.form_id == 3
    assert public.answer_id == 4
    assert public.value is None
