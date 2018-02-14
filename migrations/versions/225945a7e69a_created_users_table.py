"""Created users table

Revision ID: 225945a7e69a
Revises: 
Create Date: 2018-02-14 11:23:20.688421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '225945a7e69a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=25), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('bank_name', sa.String(length=255), nullable=False),
    sa.Column('acc_no', sa.String(length=255), nullable=False),
    sa.Column('acc_name', sa.String(length=255), nullable=False),
    sa.Column('terms', sa.Boolean(), nullable=True),
    sa.Column('waye', sa.String(length=25), nullable=True),
    sa.Column('credit', sa.String(length=25), nullable=True),
    sa.Column('status', sa.String(length=25), nullable=True),
    sa.Column('seller_id', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('acc_name')
    )
    op.create_index(op.f('ix_users_acc_no'), 'users', ['acc_no'], unique=True)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_phone'), 'users', ['phone'], unique=True)
    op.create_index(op.f('ix_users_seller_id'), 'users', ['seller_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_seller_id'), table_name='users')
    op.drop_index(op.f('ix_users_phone'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_acc_no'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###