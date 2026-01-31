from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.shared.entity_base_model import EntityBase


class OptionAnswer(EntityBase):
    __tablename__ = 'options_answers'

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
    order = Column(Integer, nullable=False)

    form = relationship('Form', back_populates='options_answers')
    answer = relationship('Answer', back_populates='options_answers')
