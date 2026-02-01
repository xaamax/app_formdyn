from sqlalchemy.orm import Session

from app.shared.repository_base import RepositoryBase

from .models import FormAnswer


class FormAnswerRepository(RepositoryBase[FormAnswer]):
    def __init__(self, session: Session):
        super().__init__(session, FormAnswer)
