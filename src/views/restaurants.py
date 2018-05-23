import json
from aiohttp import web

from pydantic import ValidationError

from helpers.json import json_dumps
from schemas.restaurants import (
    CreateRestaurant,
    UpdateRestaurant,
)

__all__ = (
    'RestaurantsView',
    'RestaurantView',
)


class RestaurantsView(web.View):
    async def get(self):
        db = self.request.app['db_client']
        restaurants = await db.get_restaurants()

        return web.json_response({'restaurants': [
            dict(restaurant) for restaurant in restaurants
        ]}, dumps=json_dumps)

    async def post(self):
        data = await self.request.json()

        try:
            data = CreateRestaurant(**data)
        except ValidationError as e:
            return web.json_response(json.loads(e.json()),
                                     status=web.HTTPBadRequest.status_code)

        name = data.name
        opens_at = data.opens_at
        closes_at = data.closes_at

        db = self.request.app['db_client']
        restaurant_id = await db.create_restaurant(name, opens_at, closes_at)

        return web.json_response({
            'id': restaurant_id,
            'name': data.name,
            'opens_at': opens_at.isoformat(),
            'closes_at': closes_at.isoformat(),
        })


class RestaurantView(web.View):
    async def get(self):
        restaurant_id = self.request.match_info['restaurant_id']

        db = self.request.app['db_client']
        restaurant = await db.get_restaurant_by_id(restaurant_id)

        if restaurant is None:
            return web.json_response(status=web.HTTPNotFound.status_code)

        return web.json_response({
            'id': restaurant.id,
            'name': restaurant.name,
            'opens_at': restaurant.opens_at.isoformat(),
            'closes_at': restaurant.closes_at.isoformat(),
        })

    async def put(self):
        restaurant_id = self.request.match_info['restaurant_id']
        data = self.request.query

        try:
            data = UpdateRestaurant(**data)
        except ValidationError as e:
            return web.json_response(json.loads(e.json()),
                                     status=web.HTTPBadRequest.status_code)

        data = {
            kv_pair[0]: kv_pair[1]
            for kv_pair in data
            if kv_pair[1] is not None
        }

        db = self.request.app['db_client']
        update_result = await db.update_restaurant_by_id(restaurant_id, **data)

        if not update_result:
            return web.json_response(status=web.HTTPNotFound.status_code)

        return web.json_response(status=web.HTTPNoContent.status_code)

    async def delete(self):
        restaurant_id = self.request.match_info['restaurant_id']

        db = self.request.app['db_client']
        delete_result = await db.delete_restaurant_by_id(restaurant_id)

        if not delete_result:
            return web.json_response(status=web.HTTPNotFound.status_code)

        return web.json_response(status=web.HTTPNoContent.status_code)
