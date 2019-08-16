"""init

Revision ID: 0941889000dd
Revises: 
Create Date: 2019-08-16 12:20:20.161978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0941889000dd'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedbacks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.Text(), nullable=False),
    sa.Column('full_name', sa.Text(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_feedbacks'))
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feedbacks')
    # ### end Alembic commands ###