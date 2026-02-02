"""Add dueDate, priority, and tags to Task

Revision ID: 4736b61b508a
Revises: 
Create Date: 2026-02-01 22:15:21.923212

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
from sqlalchemy.dialects import postgresql

# revision identifiers
revision = '4736b61b508a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('task', sa.Column('dueDate', sa.DateTime(), nullable=True))
    op.add_column('task', sa.Column('priority', sa.String(length=20), nullable=True,
    server_default='Medium'))
    op.add_column('task', sa.Column('tags', sa.JSON(), nullable=True, server_default='[]')) # Usi      JSON for list of strings
   
def downgrade() -> None:
    op.drop_column('task', 'tags')
    op.drop_column('task', 'priority')
    op.drop_column('task', 'dueDate')