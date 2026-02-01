from sqlalchemy.orm import Session

from app.shared.repository_base import RepositoryBase

from .models import OptionAnswer


class OptionAnswerRepository(RepositoryBase[OptionAnswer]):
    def __init__(self, session: Session):
        super().__init__(session, OptionAnswer)
