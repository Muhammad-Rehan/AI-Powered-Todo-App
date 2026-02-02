"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
from sqlalchemy.dialects import postgresql

# revision identifiers
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade() -> None:
    op.add_column('task', sa.Column('dueDate', sa.DateTime(), nullable=True))
    op.add_column('task', sa.Column('priority', sa.String(length=20), nullable=True,
    server_default='Medium'))
    op.add_column('task', sa.Column('tags', sa.JSON(), nullable=True, server_default='[]')) # Usi      JSON for list of strings
   
def downgrade() -> None:
    op.drop_column('task', 'tags')
    op.drop_column('task', 'priority')
    op.drop_column('task', 'dueDate')