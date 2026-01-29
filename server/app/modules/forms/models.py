from sqlalchemy import Column, Integer, Text

from app.shared.entity_base_model import EntityBase


class Form(EntityBase):
    __tablename__ = 'forms'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    type = Column(Integer)
