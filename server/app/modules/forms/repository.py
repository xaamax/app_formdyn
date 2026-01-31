from sqlalchemy.orm import Session

from app.shared.repository_base import RepositoryBase
from .models import Form


class FormRepository(RepositoryBase[Form]):
    def __init__(self, session: Session):
        super().__init__(session, Form)
