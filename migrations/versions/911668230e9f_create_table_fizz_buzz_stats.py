"""CREATE TABLE fizz_buzz_stats

Revision ID: 911668230e9f
Revises: 
Create Date: 2024-01-16 21:11:49.076042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '911668230e9f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('fizz_buzz_stats',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('int1', sa.Integer(), nullable=False),
                    sa.Column('int2', sa.Integer(), nullable=False),
                    sa.Column('limit', sa.Integer(), nullable=False),
                    sa.Column('str1', sa.String(50), nullable=False),
                    sa.Column('str2', sa.String(50), nullable=False),
                    sa.Column('hits', sa.Integer(), default=1),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('fizz_buzz_stats')
