from api import services
from tests.base import MongoBaseTests


class ServicesTest(MongoBaseTests):
    async def test_insert_event(self):
        event_args = {'event': 'buy', 'timestamp': '5678'}
        await services.insert_event(self.collection, event_args)

        inserted_doc = await self.collection.find({}, {"_id": 0}).to_list(None)

        assert inserted_doc == [event_args]
