from datetime import datetime, timezone

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr

from app.core.database import Base


class EntityBase(Base):
    __abstract__ = True

    @declared_attr
    def created_at(cls):
        return Column(
            DateTime,
            default=lambda: datetime.now(timezone.utc),
            nullable=False,
        )

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime,
            nullable=True,
            onupdate=lambda: datetime.now(timezone.utc),
        )

    @declared_attr
    def deleted_at(cls):
        return Column(DateTime(timezone=True), nullable=True)
