from aiohttp.test_utils import unittest_run_loop
from asynctest import patch, CoroutineMock

from tests.base import MongoBaseTests, AppBaseTests


class CacheTest(AppBaseTests, MongoBaseTests):
    @unittest_run_loop
    async def test_dont_access_db_in_second_request(self):
        with patch.object(self.collection, 'distinct',
                          CoroutineMock(return_value='certinho')) as db:

            await self.client.request('GET', '/events',
                                      params={'event_startswith': 'an'})

            await self.client.request('GET', '/events',
                                      params={'event_startswith': 'an'})

            assert 2 == db.await_count
