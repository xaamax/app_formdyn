from typing import Generic, Type, TypeVar

from sqlalchemy.orm import Session
from sqlalchemy.sql import select

T = TypeVar('T')


class RepositoryBase(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def list(self) -> list[T]:
        return self.session.execute(select(self.model)).scalars().all()

    def get_by_id(self, entity_id: int) -> T | None:
        return self.session.get(self.model, entity_id)

    def create(self, entity: T) -> T:
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def delete(self, entity: T) -> None:
        self.session.delete(entity)
        self.session.commit()
