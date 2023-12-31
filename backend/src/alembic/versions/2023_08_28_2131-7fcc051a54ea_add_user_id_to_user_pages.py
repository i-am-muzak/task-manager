"""Add: user_id to user_pages

Revision ID: 7fcc051a54ea
Revises: 7b8dc83839ca
Create Date: 2023-08-28 21:31:41.492178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fcc051a54ea'
down_revision = '7b8dc83839ca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_pages', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_user_pages_user_id', 'user_pages', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_user_pages_user_id', 'user_pages', type_='foreignkey')
    op.drop_column('user_pages', 'user_id')
    # ### end Alembic commands ###
