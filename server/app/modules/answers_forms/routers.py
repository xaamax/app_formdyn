from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from app.core.database import get_session
from app.core.models import AnswerForm
from app.shared.pagination import paginate_response

from .schemas import AnswerFormPaginated, AnswerFormPartial, AnswerFormPublic, AnswerFormSchema

router = APIRouter(
    prefix='/api/v1/answers_forms',
    tags=['Formulários Respostas'],
)


@router.post(
    '/', response_model=AnswerFormPublic, status_code=status.HTTP_201_CREATED
)
def create_field(
    payload: AnswerFormSchema, session: Session = Depends(get_session)
):
    db_field = AnswerForm(**payload.model_dump())
    session.add(db_field)
    session.commit()
    session.refresh(db_field)
    return AnswerFormPublic.from_model(db_field)


@router.get(
    path='/', response_model=AnswerFormPaginated, status_code=status.HTTP_200_OK
)
def list_answers_form(
    session: Session = Depends(get_session),
    page_number: int = 1,
    page_size: int = 10,
):
    return paginate_response(
        session=session,
        query=select(AnswerForm),
        page_number=page_number,
        page_size=page_size,
        mapper=AnswerFormPublic.from_model,
    )


@router.get(
    path='/{field_id}',
    response_model=AnswerFormPublic,
    status_code=status.HTTP_200_OK,
)
def get_field(
    field_id: int,
    session: Session = Depends(get_session),
):
    field = session.get(AnswerForm, field_id)
    if not field:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='AnswerForm not found'
        )
    return AnswerFormPublic.from_model(field)


@router.put(
    path='/{field_id}',
    response_model=AnswerFormPublic,
    status_code=status.HTTP_201_CREATED,
)
def update_field(
    field_id: int,
    field: AnswerFormSchema,
    session: Session = Depends(get_session),
):
    db_field = session.get(AnswerForm, field_id)
    if not db_field:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='AnswerForm not found'
        )
    for attr, value in field.model_dump().items():
        setattr(db_field, attr, value)
    session.commit()
    session.refresh(db_field)
    return AnswerFormPublic.from_model(db_field)


@router.patch(path='/{field_id}', response_model=AnswerFormPublic)
def patch_field(
    field_id: int, field: AnswerFormPartial, session: Session = Depends(get_session)
):
    db_field = session.get(AnswerForm, field_id)
    if not db_field:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='AnswerForm not found'
        )
    update_data = {
        k: v for k, v in field.model_dump(exclude_unset=True).items()
    }
    for attr, value in update_data.items():
        setattr(db_field, attr, value)
    session.commit()
    session.refresh(db_field)
    return AnswerFormPublic.from_model(db_field)


@router.delete(path='/{field_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_field(
    field_id: int,
    session: Session = Depends(get_session),
):
    field = session.get(AnswerForm, field_id)
    if not field:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='AnswerForm not found'
        )
    session.delete(field)
    session.commit()
