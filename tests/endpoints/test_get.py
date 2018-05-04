from aiohttp.test_utils import unittest_run_loop
from asynctest import CoroutineMock, patch
from http import HTTPStatus

from tests.base import AppBaseTests


class GetTests(AppBaseTests):
    @unittest_run_loop
    async def test_get(self):
        events = ['any', 'ant', 'antique']
        with patch('api.endpoints.get_distinct_events',
                   CoroutineMock(return_value=events)):

            resp = await self.client.request('GET', '/events',
                                             params={'event_startswith': 'an'})

        assert resp.status == HTTPStatus.OK
        text = await resp.json()
        assert {'events': events} == text

    @unittest_run_loop
    async def test_get_any_documents_found(self):
        with patch('api.endpoints.get_distinct_events',
                   CoroutineMock(return_value=[])):
            resp = await self.client.request('GET', '/events',
                                             params={'event_startswith': 'an'})

        assert resp.status == HTTPStatus.NOT_FOUND

    @unittest_run_loop
    async def test_get_without_parameter(self):
        resp = await self.client.request('GET', '/events')

        assert resp.status == HTTPStatus.UNPROCESSABLE_ENTITY
