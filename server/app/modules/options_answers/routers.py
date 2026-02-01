from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.shared.pagination import paginate_response
from app.shared.schemas import ErrorResponse

from .models import OptionAnswer
from .repository import OptionAnswerRepository
from .schemas import (
    OptionAnswerListPaginated,
    OptionAnswerPartial,
    OptionAnswerPublic,
    OptionAnswerSchema,
)
from .service import OptionAnswerService

router = APIRouter(
    prefix='/api/v1/options_answers',
    tags=['Opções de Respostas'],
)


def get_service(session: Session = Depends(get_session)):
    return OptionAnswerService(OptionAnswerRepository(session))


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    responses={400: {'model': ErrorResponse}},
)
def create_option_answer(
    payload: OptionAnswerSchema,
    service: OptionAnswerService = Depends(get_service),
):
    return OptionAnswerPublic.from_model(service.create(payload))


@router.get(
    '',
    response_model=OptionAnswerListPaginated,
)
def list_option_answers(
    page_number: int = 1,
    page_size: int = 10,
    service: OptionAnswerService = Depends(get_service),
):
    return paginate_response(
        session=service.repository.session,
        query=select(OptionAnswer),
        page_number=page_number,
        page_size=page_size,
        mapper=OptionAnswerPublic.from_model,
    )


@router.get(
    '/{id}',
    response_model=OptionAnswerPublic,
    responses={404: {'model': ErrorResponse}},
)
def get_option_answer(
    id: int,
    service: OptionAnswerService = Depends(get_service),
):
    return OptionAnswerPublic.from_model(service.get(id))


@router.put(
    '/{id}',
    response_model=OptionAnswerPublic,
    responses={
        400: {'model': ErrorResponse},
        404: {'model': ErrorResponse},
    },
)
def update_option_answer(
    id: int,
    payload: OptionAnswerSchema,
    service: OptionAnswerService = Depends(get_service),
):
    return OptionAnswerPublic.from_model(service.update(id, payload))


@router.patch(
    '/{id}',
    response_model=OptionAnswerPublic,
    responses={
        400: {'model': ErrorResponse},
        404: {'model': ErrorResponse},
    },
)
def patch_option_answer(
    id: int,
    payload: OptionAnswerPartial,
    service: OptionAnswerService = Depends(get_service),
):
    return OptionAnswerPublic.from_model(service.patch(id, payload))


@router.delete(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {'model': ErrorResponse}},
)
def delete_option_answer(
    id: int,
    service: OptionAnswerService = Depends(get_service),
):
    service.delete(id)
