from asynctest import TestCase
from motor.motor_asyncio import AsyncIOMotorClient

from api import services
from api.config import MONGO_URI, EVENTS_COLLECTION, MONGO_TIMEOUT


class ServicesTest(TestCase):
    async def setUp(self):
        client = AsyncIOMotorClient(MONGO_URI,
                                    serverSelectionTimeoutMS=MONGO_TIMEOUT)
        db = client['test']
        self.collection = db[EVENTS_COLLECTION]

    async def tearDown(self):
        await self.collection.drop()

    async def test_insert_event(self):
        event_args = {'event': 'buy', 'timestamp': '5678'}
        await services.insert_event(self.collection, event_args)

        inserted_doc = await self.collection.find({}, {"_id": 0}).to_list(None)

        assert inserted_doc == [event_args]
