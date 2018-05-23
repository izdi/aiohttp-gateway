import sqlalchemy as sa

from db.client import Client
from db.tables import restaurants

__all__ = (
    'DatabaseClient',
)


class DatabaseClient(Client):
    async def get_restaurants(self):
        query = sa.select([restaurants])
        result = await self.fetchall(query)
        return result

    async def get_restaurant_by_id(self, id):
        query = sa.select([restaurants]).where(
            restaurants.c.id == id
        )
        result = await self.fetchone(query)
        return result

    async def create_restaurant(self, name, opens_at, closes_at):
        query = restaurants.insert().values(
            name=name, opens_at=opens_at, closes_at=closes_at
        )
        result = await self.fetchone(query)
        return result[0]

    async def update_restaurant_by_id(self, id, **values):
        query = restaurants.update().returning(
            restaurants.c.id
        ).where(
            restaurants.c.id == id
        ).values(values)

        result = await self.fetchone(query)
        return result

    async def delete_restaurant_by_id(self, id):
        query = restaurants.delete().returning(
            restaurants.c.id
        ).where(
            restaurants.c.id == id
        )

        result = await self.fetchone(query)
        return result
