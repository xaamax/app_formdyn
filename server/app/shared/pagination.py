from typing import Callable, Generic, List, TypeVar

from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.orm import Session

T = TypeVar('T')


class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]
    page_number: int
    page_size: int
    total_items: int


def paginate_response(
    *,
    session: Session,
    query,
    page_number: int,
    page_size: int,
    mapper: Callable,
):
    page_number = max(page_number, 1)
    page_size = max(page_size, 1)

    offset = (page_number - 1) * page_size

    total_items = session.scalar(
        select(func.count()).select_from(query.subquery())
    )

    records = session.scalars(query.offset(offset).limit(page_size)).all()

    return {
        'items': [mapper(record) for record in records],
        'page_number': page_number,
        'page_size': page_size,
        'total_items': total_items,
    }
