import pytest
from pydantic import ValidationError

from app.modules.options_answers.schemas import (
    OptionAnswerPartial,
    OptionAnswerPublic,
    OptionAnswerSchema,
)


class FakeForm:
    def __init__(self, name: str):
        self.name = name


class FakeAnswer:
    def __init__(self, description: str):
        self.description = description


class FakeOptionAnswerModel:
    def __init__(
        self, id: int, order: int, form_name: str, answer_description: str
    ):
        self.id = id
        self.order = order
        self.form = FakeForm(form_name)
        self.answer = FakeAnswer(answer_description)


def test_option_answer_schema_valid_minimal():
    schema = OptionAnswerSchema(
        form_id=1,
        answer_id=2,
        order=1,
    )

    assert schema.form_id == 1
    assert schema.answer_id == 2
    assert schema.order == 1


def test_option_answer_schema_missing_required_fields():
    with pytest.raises(ValidationError):
        OptionAnswerSchema(
            form_id=1,
            order=1,
        )


def test_option_answer_partial_empty():
    partial = OptionAnswerPartial()

    assert partial.form_id is None
    assert partial.answer_id is None
    assert partial.order is None


def test_option_answer_partial_with_some_fields():
    partial = OptionAnswerPartial(
        order=10,
    )

    assert partial.order == 10
    assert partial.form_id is None
    assert partial.answer_id is None


def test_option_answer_partial_with_all_fields():
    partial = OptionAnswerPartial(
        form_id=5,
        answer_id=6,
        order=3,
    )

    assert partial.form_id == 5
    assert partial.answer_id == 6
    assert partial.order == 3


def test_option_answer_public_from_model_basic():
    model = FakeOptionAnswerModel(
        id=1,
        order=1,
        form_name='Form Teste',
        answer_description='Resposta Teste',
    )

    public = OptionAnswerPublic.from_model(model)

    assert public.id == 1
    assert public.form_name == 'Form Teste'
    assert public.answer_description == 'Resposta Teste'


def test_option_answer_public_from_model_with_different_values():
    model = FakeOptionAnswerModel(
        id=2,
        order=99,
        form_name='Outro Form',
        answer_description='Outra Resposta',
    )

    public = OptionAnswerPublic.from_model(model)

    assert public.id == 2
    assert public.form_name == 'Outro Form'
    assert public.answer_description == 'Outra Resposta'
