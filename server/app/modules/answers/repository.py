from sqlalchemy.orm import Session

from app.shared.repository_base import RepositoryBase

from .models import Answer


class AnswerRepository(RepositoryBase[Answer]):
    def __init__(self, session: Session):
        super().__init__(session, Answer)
