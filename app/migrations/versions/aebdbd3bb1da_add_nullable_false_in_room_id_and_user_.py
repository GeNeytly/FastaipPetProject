"""add nullable=False in room_id and user_id

Revision ID: aebdbd3bb1da
Revises: 1d5355a3f3a6
Create Date: 2023-09-13 15:34:49.413890

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aebdbd3bb1da'
down_revision: Union[str, None] = '1d5355a3f3a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bookings', 'room_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('bookings', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bookings', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('bookings', 'room_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
