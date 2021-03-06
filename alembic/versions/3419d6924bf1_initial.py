"""Initial

Revision ID: 3419d6924bf1
Revises: c71327948762
Create Date: 2021-03-23 16:17:20.466198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3419d6924bf1'
down_revision = 'c71327948762'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chanels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('icon', sa.String(length=256), nullable=True),
    sa.Column('disabled', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shows',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('start_t', sa.DateTime(), nullable=True),
    sa.Column('end_t', sa.DateTime(), nullable=True),
    sa.Column('chanel_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shows')
    op.drop_table('chanels')
    # ### end Alembic commands ###
