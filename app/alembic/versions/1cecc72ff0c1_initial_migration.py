"""initial migration

Revision ID: 1cecc72ff0c1
Revises: 
Create Date: 2024-01-25 18:19:49.694671

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '1cecc72ff0c1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('date_start', sa.DateTime(), nullable=False),
    sa.Column('date_predicted_conclusion', sa.DateTime(), nullable=False),
    sa.Column('date_conclusion', sa.DateTime(), nullable=True),
    sa.Column('developers_quantity', sa.Integer(), nullable=True),
    sa.Column('develop_hours', sa.Integer(), nullable=True),
    sa.Column('stack', sa.String(length=100), nullable=False),
    sa.Column('xp_level', sa.String(length=100), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('company_field', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_projects_id'), 'projects', ['id'], unique=False)
    op.drop_index('email', table_name='users')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_index('nickname', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('experience', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('date_register', mysql.DATETIME(), nullable=True),
    sa.Column('user_type', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('week_hours', mysql.FLOAT(), nullable=True),
    sa.Column('current_job', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('nickname', mysql.VARCHAR(length=40), nullable=False),
    sa.Column('expert', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('company_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('nickname', 'users', ['nickname'], unique=True)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_index('email', 'users', ['email'], unique=True)
    op.drop_index(op.f('ix_projects_id'), table_name='projects')
    op.drop_table('projects')
    # ### end Alembic commands ###
