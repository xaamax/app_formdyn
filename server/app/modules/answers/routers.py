from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.shared.pagination import paginate_response
from app.shared.schemas import ErrorResponse

from .models import Answer
from .repository import AnswerRepository
from .schemas import (
    AnswerListPaginated,
    AnswerPartial,
    AnswerPublic,
    AnswerSchema,
)
from .service import AnswerService

router = APIRouter(
    prefix='/api/v1/answers',
    tags=['Respostas'],
)


def get_service(session: Session = Depends(get_session)):
    return AnswerService(AnswerRepository(session))


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    responses={400: {'model': ErrorResponse}},
)
def create_field(
    payload: AnswerSchema,
    service: AnswerService = Depends(get_service),
):
    return AnswerPublic.from_model(service.create(payload))


@router.get(
    '/',
    response_model=AnswerListPaginated,
)
def list_fields(
    page_number: int = 1,
    page_size: int = 10,
    service: AnswerService = Depends(get_service),
):
    return paginate_response(
        session=service.repository.session,
        query=select(Answer),
        page_number=page_number,
        page_size=page_size,
        mapper=AnswerPublic.from_model,
    )


@router.get(
    '/{id}/',
    response_model=AnswerPublic,
    responses={404: {'model': ErrorResponse}},
)
def get_field(
    id: int,
    service: AnswerService = Depends(get_service),
):
    return AnswerPublic.from_model(service.get(id))


@router.put(
    '/{id}/',
    response_model=AnswerPublic,
    responses={
        400: {'model': ErrorResponse},
        404: {'model': ErrorResponse},
    },
)
def update_field(
    id: int,
    payload: AnswerSchema,
    service: AnswerService = Depends(get_service),
):
    return AnswerPublic.from_model(service.update(id, payload))


@router.patch(
    '/{id}/',
    response_model=AnswerPublic,
    responses={
        400: {'model': ErrorResponse},
        404: {'model': ErrorResponse},
    },
)
def patch_field(
    id: int,
    payload: AnswerPartial,
    service: AnswerService = Depends(get_service),
):
    return AnswerPublic.from_model(service.patch(id, payload))


@router.delete(
    '/{id}/',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {'model': ErrorResponse}},
)
def delete_field(
    id: int,
    service: AnswerService = Depends(get_service),
):
    service.delete(id)
