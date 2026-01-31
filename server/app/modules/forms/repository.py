from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from .models import Form


class FormRepository:
    def __init__(self, session: Session):
        self.session = session

    def list(self):
        return self.session.execute(select(Form)).scalars().all()
    
    def create(self, form: Form) -> Form:
        self.session.add(form)
        self.session.commit()
        self.session.refresh(form)
        return form

    def get_by_id(self, form_id: int) -> Form | None:
        return self.session.get(Form, form_id)

    def delete(self, form: Form):
        self.session.delete(form)
        self.session.commit()
