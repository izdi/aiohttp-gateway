import os

from aiohttp import web

from db import DatabaseClient
from views import (
    RestaurantView,
    RestaurantsView,
)

__all__ = (
    'get_application',
)


async def init_db(app):
    client = DatabaseClient(
        host=os.environ['POSTGRES__HOST'],
        port=os.environ['POSTGRES__PORT'],
        database=os.environ['POSTGRES__DATABASE'],
        user=os.environ['POSTGRES__USER'],
        password=os.environ['POSTGRES__PASSWORD']
    )
    app['db_client'] = await client.connect()
    app.on_cleanup.append(client.close)


async def get_application():
    app = web.Application(debug=False)

    await init_db(app)

    app.add_routes([
        web.view('/restaurants', RestaurantsView),
        web.view('/restaurant/{restaurant_id:\d+}', RestaurantView),
    ])

    return app

if __name__ == '__main__':
    web.run_app(get_application())
