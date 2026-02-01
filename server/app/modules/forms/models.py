from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from app.shared.entity_base_model import EntityBase


class Form(EntityBase):
    __tablename__ = 'forms'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    type = Column(Integer, nullable=True)

    fields = relationship(
        'Field',
        back_populates='form',
        cascade='all, delete-orphan',
        passive_deletes=True,
    )

    options_answers = relationship(
        'OptionAnswer',
        back_populates='form',
        cascade='all, delete-orphan',
        passive_deletes=True,
    )
