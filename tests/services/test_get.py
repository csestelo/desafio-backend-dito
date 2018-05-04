from api import services
from tests.base import MongoBaseTests


class ServicesTest(MongoBaseTests):
    async def test_get_distinct_events(self):
        events = [{'event': 'buy', 'timestamp': '5678'},
                  {'event': 'steal', 'timestamp': '234'},
                  {'event': 'steady', 'timestamp': '976'}]

        await self.collection.insert_many(events)
        assert 3 == await self.collection.count()

        distinct_events = await services.get_distinct_events(self.collection, 'st')

        assert ['steal', 'steady'] == distinct_events
