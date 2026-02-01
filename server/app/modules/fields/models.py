from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.shared.entity_base_model import EntityBase


class Field(EntityBase):
    __tablename__ = 'fields'

    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(
        Integer,
        ForeignKey('forms.id', ondelete='CASCADE'),
        nullable=False,
    )
    slug = Column(String, nullable=False)
    name = Column(String, nullable=False)
    order = Column(Integer, nullable=False)
    label = Column(String, nullable=False)
    observation = Column(Text, nullable=True)
    type = Column(Integer, nullable=False)
    optional = Column(Text, nullable=True)
    readonly = Column(Boolean, nullable=False, default=False)
    grid = Column(String, nullable=True)
    size = Column(Integer, nullable=True)
    mask = Column(Text, nullable=True)
    placeholder = Column(Text, nullable=True)

    form = relationship('Form', back_populates='fields')
