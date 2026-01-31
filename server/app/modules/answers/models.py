from sqlalchemy import Boolean, Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.shared.entity_base_model import EntityBase


class Answer(EntityBase):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=False)
    legend = Column(String, nullable=True)
    order = Column(Integer, nullable=False)
    only_legend = Column(Boolean, default=False)
    color = Column(String, nullable=True)
    background = Column(String, nullable=True)

    options_answers = relationship(
        'OptionAnswer',
        back_populates='answer',
        cascade='all, delete-orphan',
        passive_deletes=True,
    )
