from aiohttp import web
from motor.motor_asyncio import AsyncIOMotorClient

from api.config import MONGO_URI, APP_PORT, MONGO_TIMEOUT
from api.endpoints import get, post


class EventsApi(object):
    def __init__(self):
        self.app = web.Application()
        self.add_routes()
        self.app['mongodb'] = AsyncIOMotorClient(
            MONGO_URI, serverSelectionTimeoutMS=MONGO_TIMEOUT
        )

    def start(self):
        web.run_app(self.app, port=APP_PORT)

    def add_routes(self):
        self.app.add_routes([web.get('/events', get),
                             web.post('/events', post)])


if __name__ == '__main__':
    EventsApi().start()
