import pytest
from pydantic import ValidationError

from app.modules.answers.models import Answer
from app.modules.answers.schemas import (
    AnswerPartial,
    AnswerPublic,
    AnswerSchema,
)


def test_answer_schema_valid_minimal():
    schema = AnswerSchema(
        description='Descrição',
        legend='Legenda',
        order=1,
    )

    assert schema.description == 'Descrição'
    assert schema.legend == 'Legenda'
    assert schema.order == 1
    assert schema.only_legend is False
    assert schema.color is None
    assert schema.background is None


def test_answer_schema_missing_required_fields():
    with pytest.raises(ValidationError):
        AnswerSchema(
            legend='Legenda',
            order=1,
        )


def test_answer_schema_accepts_optional_fields():
    schema = AnswerSchema(
        description='Descrição',
        legend='Legenda',
        order=2,
        only_legend=True,
        color='#FFFFFF',
        background='#000000',
    )

    assert schema.only_legend is True
    assert schema.color == '#FFFFFF'
    assert schema.background == '#000000'


def test_answer_partial_empty():
    partial = AnswerPartial()

    assert partial.description is None
    assert partial.legend is None
    assert partial.order is None
    assert partial.only_legend is None
    assert partial.color is None
    assert partial.background is None


def test_answer_partial_with_some_fields():
    partial = AnswerPartial(
        description='Nova descrição',
        order=10,
    )

    assert partial.description == 'Nova descrição'
    assert partial.order == 10
    assert partial.legend is None


def test_answer_public_from_model_basic():
    answer = Answer(
        id=1,
        description='Descrição',
        legend='Legenda',
        order=1,
        only_legend=False,
        color=None,
        background=None,
    )

    public = AnswerPublic.from_model(answer)

    assert public.id == 1
    assert public.description == 'Descrição'
    assert public.legend == 'Legenda'
    assert public.order == 1
    assert public.only_legend is False
    assert public.color is None
    assert public.background is None


def test_answer_public_from_model_with_optional_fields():
    answer = Answer(
        id=2,
        description='Descrição',
        legend='Legenda',
        order=2,
        only_legend=True,
        color='#ABCDEF',
        background='#123456',
    )

    public = AnswerPublic.from_model(answer)

    assert public.only_legend is True
    assert public.color == '#ABCDEF'
    assert public.background == '#123456'
