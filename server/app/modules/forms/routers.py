from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from app.core.database import get_session
from app.core.models import Form
from .schemas import FormList, FormPublic, FormPartial, FormSchema

router = APIRouter(
    prefix='/api/v1/forms',
    tags=['Formulários'],
)


@router.post(
    path='/', response_model=FormPublic, status_code=status.HTTP_201_CREATED
)
def create_form(form: FormSchema, session: Session = Depends(get_session)):
    form = Form(**form.model_dump())
    session.add(form)
    session.commit()
    session.refresh(form)
    return form


@router.get(path='/', response_model=FormList, status_code=status.HTTP_200_OK)
def list_forms(
    session: Session = Depends(get_session),
    page_number: int = 0,
    page_size: int = 10,
):
    query = session.scalars(select(Form).offset(page_number).limit(page_size))
    forms = query.all()
    return {'forms': [FormPublic.from_model(form) for form in forms]}


@router.get(path='/{form_id}', response_model=FormPublic, status_code=status.HTTP_200_OK)
def get_form(
    form_id: int,
    session: Session = Depends(get_session),
):
    form = session.get(Form, form_id)
    if not form:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Form not found'
        )
    return form


@router.put(
    path='/{form_id}',
    response_model=FormPublic,
    status_code=status.HTTP_201_CREATED,
)
def update_form(
    form_id: int,
    form: FormSchema,
    session: Session = Depends(get_session),
):
    db_form = session.get(Form, form_id)
    if not db_form:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Form not found'
        )
    for field, value in form.model_dump().items():
        setattr(db_form, field, value)
    session.commit()
    session.refresh(db_form)
    return db_form


@router.patch(path='/{form_id}', response_model=FormPublic)
def patch_form(form_id: int, form: FormPartial, session: Session = Depends(get_session)):
    db_form = session.get(Form, form_id)
    if not db_form:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Form not found'
        )
    update_data = {k: v for k, v in form.model_dump(exclude_unset=True).items()}
    for field, value in update_data.items():
        setattr(db_form, field, value)
    session.commit()
    session.refresh(db_form)
    return db_form


@router.delete(path='/{form_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_form(
    form_id: int,
    session: Session = Depends(get_session),
):
    form = session.get(Form, form_id)
    if not form:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Form not found'
        )
    session.delete(form)
    session.commit()
