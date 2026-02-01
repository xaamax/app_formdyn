from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.shared.pagination import paginate_response
from app.shared.schemas import ErrorResponse

from .models import Field
from .repository import FieldRepository
from .schemas import (
    FieldListPaginated,
    FieldPartial,
    FieldPublic,
    FieldSchema,
)
from .service import FieldService

router = APIRouter(
    prefix='/api/v1/fields',
    tags=['Campos'],
)


def get_service(session: Session = Depends(get_session)):
    return FieldService(FieldRepository(session))


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    responses={400: {'model': ErrorResponse}},
)
def create_field(
    payload: FieldSchema,
    service: FieldService = Depends(get_service),
):
    return FieldPublic.from_model(service.create(payload))


@router.get(
    '/',
    response_model=FieldListPaginated,
)
def list_fields(
    page_number: int = 1,
    page_size: int = 10,
    service: FieldService = Depends(get_service),
):
    return paginate_response(
        session=service.repository.session,
        query=select(Field),
        page_number=page_number,
        page_size=page_size,
        mapper=FieldPublic.from_model,
    )


@router.get(
    '/{id}/',
    response_model=FieldPublic,
    responses={404: {'model': ErrorResponse}},
)
def get_field(
    id: int,
    service: FieldService = Depends(get_service),
):
    return FieldPublic.from_model(service.get(id))


@router.put(
    '/{id}/',
    response_model=FieldPublic,
    responses={
        400: {'model': ErrorResponse},
        404: {'model': ErrorResponse},
    },
)
def update_field(
    id: int,
    payload: FieldSchema,
    service: FieldService = Depends(get_service),
):
    return FieldPublic.from_model(service.update(id, payload))


@router.patch(
    '/{id}/',
    response_model=FieldPublic,
    responses={
        400: {'model': ErrorResponse},
        404: {'model': ErrorResponse},
    },
)
def patch_field(
    id: int,
    payload: FieldPartial,
    service: FieldService = Depends(get_service),
):
    return FieldPublic.from_model(service.patch(id, payload))


@router.delete(
    '/{id}/',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {'model': ErrorResponse}},
)
def delete_field(
    id: int,
    service: FieldService = Depends(get_service),
):
    service.delete(id)
