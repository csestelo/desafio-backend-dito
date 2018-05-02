from aiohttp.test_utils import AioHTTPTestCase
from asynctest import TestCase
from motor.motor_asyncio import AsyncIOMotorClient

from api.app import EventsApi
from api.config import MONGO_URI, MONGO_TIMEOUT, EVENTS_COLLECTION


class AppBaseTests(AioHTTPTestCase):
    async def get_application(self):
        api = EventsApi()
        return api.app


class MongoBaseTests(TestCase):
    async def setUp(self):
        client = AsyncIOMotorClient(MONGO_URI,
                                    serverSelectionTimeoutMS=MONGO_TIMEOUT)
        db = client['test']
        self.collection = db[EVENTS_COLLECTION]

    async def tearDown(self):
        await self.collection.drop()
