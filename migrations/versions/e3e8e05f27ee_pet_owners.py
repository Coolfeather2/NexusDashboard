"""pet owners

Revision ID: e3e8e05f27ee
Revises: 3132aaef7413
Create Date: 2022-02-11 23:18:20.978203

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e3e8e05f27ee'
down_revision = '3132aaef7413'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pet_names', sa.Column('owner_id', mysql.BIGINT(), nullable=True))
    op.create_foreign_key(None, 'pet_names', 'charinfo', ['owner_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pet_names', type_='foreignkey')
    op.drop_column('pet_names', 'owner_id')
    # ### end Alembic commands ###