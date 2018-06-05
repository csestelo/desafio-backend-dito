import json
from aiohttp.test_utils import unittest_run_loop
from asynctest import CoroutineMock, patch
from http import HTTPStatus

from tests.base import AppBaseTests


class GetTests(AppBaseTests):
    @property
    def cache(self):
        return self.app['redis']

    @unittest_run_loop
    async def test_result_not_cached_result(self):
        events = ['any', 'ant', 'antique']
        with patch('api.endpoints.get_distinct_events',
                   CoroutineMock(return_value=events)):

            resp = await self.client.request('GET', '/events',
                                             params={'event_startswith': 'an'})

        self.assertEqual(HTTPStatus.OK, resp.status)
        text = await resp.json()
        self.assertEqual({'events': events}, text)

    @unittest_run_loop
    async def test_cached_result(self):
        events = ["animal", "anta"]
        await self.cache.set(key='dito_event_startswith_an',
                             value=json.dumps(events))
        with patch('api.endpoints.get_distinct_events', CoroutineMock()) as db:
            resp = await self.client.request('GET', '/events',
                                             params={'event_startswith': 'an'})

        self.assertEqual(HTTPStatus.OK, resp.status)
        text = await resp.json()
        self.assertEqual({'events': events}, text)
        self.assertFalse(db.await_count)

    @unittest_run_loop
    async def test_any_documents_found(self):
        with patch('api.endpoints.get_distinct_events',
                   CoroutineMock(return_value=[])):
            resp = await self.client.request('GET', '/events',
                                             params={'event_startswith': 'an'})

        self.assertEqual(HTTPStatus.NOT_FOUND, resp.status)

    @unittest_run_loop
    async def test_without_parameter(self):
        resp = await self.client.request('GET', '/events')

        self.assertEqual(HTTPStatus.UNPROCESSABLE_ENTITY, resp.status)




