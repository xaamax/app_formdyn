from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.shared.entity_base_model import EntityBase


class FormAnswer(EntityBase):
    __tablename__ = 'forms_answers'

    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(
        Integer,
        ForeignKey('forms.id', ondelete='CASCADE'),
        nullable=False,
    )
    answer_id = Column(
        Integer,
        ForeignKey('answers.id', ondelete='CASCADE'),
        nullable=False,
    )
    value = Column(Text, nullable=True)

    form = relationship('Form', back_populates='forms_answers')
    answer = relationship('Answer', back_populates='forms_answers')
