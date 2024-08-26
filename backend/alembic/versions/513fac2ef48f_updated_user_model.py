"""Updated User model

Revision ID: 513fac2ef48f
Revises: edaf59e6b197
Create Date: 2024-08-13 19:18:14.966613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '513fac2ef48f'
down_revision = 'edaf59e6b197'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_id', table_name='users')
    op.drop_index('ix_users_nickname', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nickname', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_admin', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.create_index('ix_users_nickname', 'users', ['nickname'], unique=False)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    # ### end Alembic commands ###
