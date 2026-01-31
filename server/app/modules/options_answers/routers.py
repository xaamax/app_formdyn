from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from app.core.database import get_session
from app.core.models import OptionAnswer
from app.shared.pagination import paginate_response

from .schemas import (
    OptionAnswerPaginated,
    OptionAnswerPartial,
    OptionAnswerPublic,
    OptionAnswerSchema,
)

router = APIRouter(
    prefix='/api/v1/options_answers',
    tags=['Opções Respostas'],
)


@router.post(
    '/', response_model=OptionAnswerPublic, status_code=status.HTTP_201_CREATED
)
def create_option_answer(
    payload: OptionAnswerSchema, session: Session = Depends(get_session)
):
    db_option_answer = OptionAnswer(**payload.model_dump())
    session.add(db_option_answer)
    session.commit()
    session.refresh(db_option_answer)
    return OptionAnswerPublic.from_model(db_option_answer)


@router.get(
    path='/',
    response_model=OptionAnswerPaginated,
    status_code=status.HTTP_200_OK,
)
def list_options_answers(
    session: Session = Depends(get_session),
    page_number: int = 1,
    page_size: int = 10,
):
    return paginate_response(
        session=session,
        query=select(OptionAnswer),
        page_number=page_number,
        page_size=page_size,
        mapper=OptionAnswerPublic.from_model,
    )


@router.get(
    path='/{option_answer_id}',
    response_model=OptionAnswerPublic,
    status_code=status.HTTP_200_OK,
)
def get_option_answer(
    option_answer_id: int,
    session: Session = Depends(get_session),
):
    field = session.get(OptionAnswer, option_answer_id)
    if not field:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='OptionAnswer not found',
        )
    return OptionAnswerPublic.from_model(field)


@router.put(
    path='/{option_answer_id}',
    response_model=OptionAnswerPublic,
    status_code=status.HTTP_201_CREATED,
)
def update_option_answer(
    option_answer_id: int,
    field: OptionAnswerSchema,
    session: Session = Depends(get_session),
):
    db_option_answer = session.get(OptionAnswer, option_answer_id)
    if not db_option_answer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='OptionAnswer not found',
        )
    for attr, value in field.model_dump().items():
        setattr(db_option_answer, attr, value)
    session.commit()
    session.refresh(db_option_answer)
    return OptionAnswerPublic.from_model(db_option_answer)


@router.patch(path='/{option_answer_id}', response_model=OptionAnswerPublic)
def patch_option_answer(
    option_answer_id: int,
    field: OptionAnswerPartial,
    session: Session = Depends(get_session),
):
    db_option_answer = session.get(OptionAnswer, option_answer_id)
    if not db_option_answer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='OptionAnswer not found',
        )
    update_data = {
        k: v for k, v in field.model_dump(exclude_unset=True).items()
    }
    for attr, value in update_data.items():
        setattr(db_option_answer, attr, value)
    session.commit()
    session.refresh(db_option_answer)
    return OptionAnswerPublic.from_model(db_option_answer)


@router.delete(
    path='/{option_answer_id}', status_code=status.HTTP_204_NO_CONTENT
)
def delete_option_answer(
    option_answer_id: int,
    session: Session = Depends(get_session),
):
    field = session.get(OptionAnswer, option_answer_id)
    if not field:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='OptionAnswer not found',
        )
    session.delete(field)
    session.commit()
