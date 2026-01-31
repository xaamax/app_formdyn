from sqlalchemy.orm import Session

from app.shared.repository_base import RepositoryBase

from .models import Field


class FieldRepository(RepositoryBase[Field]):
    def __init__(self, session: Session):
        super().__init__(session, Field)
