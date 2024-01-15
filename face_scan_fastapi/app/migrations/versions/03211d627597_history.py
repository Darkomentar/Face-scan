"""history

Revision ID: 03211d627597
Revises: 16de37406a94
Create Date: 2023-11-22 14:26:26.692245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03211d627597'
down_revision = '16de37406a94'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('detect_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_people', sa.Integer(), nullable=True),
    sa.Column('date_time', sa.DateTime(), nullable=False),
    sa.Column('photo', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id_people'], ['people.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('detect_history')
    # ### end Alembic commands ###
