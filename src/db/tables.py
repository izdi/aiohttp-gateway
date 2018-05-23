import sqlalchemy as sa

__all__ = (
    'restaurants',
)


_metadata = sa.MetaData()

restaurants = sa.Table(
    'restaurants', _metadata,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.Text, nullable=False),
    sa.Column('opens_at', sa.DateTime, nullable=False),
    sa.Column('closes_at', sa.DateTime, nullable=False)
)
