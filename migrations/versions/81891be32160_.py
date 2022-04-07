"""empty message

Revision ID: 81891be32160
Revises: f48a5e819f7f
Create Date: 2022-04-07 21:59:39.932275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81891be32160'
down_revision = 'f48a5e819f7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ad_model', sa.Column('date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ad_model', 'date')
    # ### end Alembic commands ###