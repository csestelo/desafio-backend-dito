import aioredis
from aiohttp import web
from motor.motor_asyncio import AsyncIOMotorClient

from api.config import APP_PORT, MONGO_PARAMS, REDIS_PARAMS
from api.endpoints import get, post


class EventsApi(object):
    def __init__(self):
        self.app = web.Application()
        self.app.on_startup.append(self.start_dbs)
        self.app.on_cleanup.append(self.close_dbs)
        self.add_routes()

    def start(self):
        web.run_app(self.app, port=APP_PORT)

    def add_routes(self):
        self.app.add_routes([web.get('/events', get),
                             web.post('/events', post)])

    async def start_dbs(self, app):
        app['mongodb'] = AsyncIOMotorClient(**MONGO_PARAMS)
        app['redis'] = await aioredis.create_redis_pool(**REDIS_PARAMS)

    async def close_dbs(self, app):
        app['redis'].close()
        await app['redis'].wait_closed()

        app['mongodb'].close()
