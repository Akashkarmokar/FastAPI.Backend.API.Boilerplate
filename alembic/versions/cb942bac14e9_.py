"""empty message

Revision ID: cb942bac14e9
Revises: 874ab9351c09
Create Date: 2024-06-19 16:28:40.549726

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb942bac14e9'
down_revision: Union[str, None] = '874ab9351c09'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bios', 'note')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bios', sa.Column('note', sa.TEXT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
