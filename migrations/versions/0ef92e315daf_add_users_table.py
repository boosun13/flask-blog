"""add users table

Revision ID: 0ef92e315daf
Revises: e27e4853f23e
Create Date: 2023-09-24 06:21:51.444874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ef92e315daf'
down_revision = 'e27e4853f23e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.String(length=26), nullable=False),
    sa.Column('account_id', sa.String(length=26), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False, comment='登録メールアドレス'),
    sa.Column('registered_at', sa.DateTime(), nullable=False, comment='登録日時'),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], ),
    sa.PrimaryKeyConstraint('id'),
    comment='アカウントのユーザー情報'
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users_account_id'), ['account_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_account_id'))

    op.drop_table('users')
    # ### end Alembic commands ###
