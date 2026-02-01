"""update form type required

Revision ID: 3089e4aff330
Revises: 02dfd18a8ac9
Create Date: 2026-01-31 19:05:24.002647

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3089e4aff330'
down_revision: Union[str, Sequence[str], None] = '02dfd18a8ac9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
