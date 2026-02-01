from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.shared.pagination import paginate_response
from app.shared.schemas import ErrorResponse

from .models import Form
from .repository import FormRepository
from .schemas import (
    FormListPaginated,
    FormPartial,
    FormPublic,
    FormSchema,
)
from .service import FormService

router = APIRouter(
    prefix='/api/v1/forms',
    tags=['Formulários'],
)


def get_service(session: Session = Depends(get_session)):
    return FormService(FormRepository(session))


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    responses={400: {'model': ErrorResponse}},
)
def create_form(
    payload: FormSchema,
    service: FormService = Depends(get_service),
):
    return FormPublic.from_model(service.create(payload))


@router.get(
    '/',
    response_model=FormListPaginated,
)
def list_forms(
    page_number: int = 1,
    page_size: int = 10,
    service: FormService = Depends(get_service),
):
    return paginate_response(
        session=service.repository.session,
        query=select(Form),
        page_number=page_number,
        page_size=page_size,
        mapper=FormPublic.from_model,
    )


@router.get(
    '/{form_id}',
    response_model=FormPublic,
    responses={404: {'model': ErrorResponse}},
)
def get_form(
    form_id: int,
    service: FormService = Depends(get_service),
):
    return FormPublic.from_model(service.get(form_id))


@router.put(
    '/{form_id}',
    response_model=FormPublic,
    responses={
        400: {'model': ErrorResponse},
        404: {'model': ErrorResponse},
    },
)
def update_form(
    form_id: int,
    payload: FormSchema,
    service: FormService = Depends(get_service),
):
    return FormPublic.from_model(service.update(form_id, payload))


@router.patch(
    '/{form_id}',
    response_model=FormPublic,
    responses={
        400: {'model': ErrorResponse},
        404: {'model': ErrorResponse},
    },
)
def patch_form(
    form_id: int,
    payload: FormPartial,
    service: FormService = Depends(get_service),
):
    return FormPublic.from_model(service.patch(form_id, payload))


@router.delete(
    '/{form_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {'model': ErrorResponse}},
)
def delete_form(
    form_id: int,
    service: FormService = Depends(get_service),
):
    service.delete(form_id)
