"""user modal migration first time in RESTAPI.

Revision ID: 66bb4237b46b
Revises: 
Create Date: 2023-08-19 12:51:02.339657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66bb4237b46b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppy',
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puppy')
    # ### end Alembic commands ###
