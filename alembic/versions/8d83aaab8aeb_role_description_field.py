"""Role description field.

Revision ID: 8d83aaab8aeb
Revises: 3c1af34ce07e
Create Date: 2022-10-16 01:02:57.913419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d83aaab8aeb'
down_revision = '3c1af34ce07e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('description', sa.String(length=1024), nullable=True))
    op.alter_column('roles', 'name',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('roles', 'code',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.create_unique_constraint(None, 'roles', ['code'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'roles', type_='unique')
    op.alter_column('roles', 'code',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('roles', 'name',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.drop_column('roles', 'description')
    # ### end Alembic commands ###