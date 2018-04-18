from unittest.mock import patch

from aiohttp.test_utils import unittest_run_loop
from http import HTTPStatus

from asynctest import CoroutineMock

from tests.base import BaseTests


class PostTests(BaseTests):
    @unittest_run_loop
    async def test_post_with_correct_arguments_returns_200(self):
        with patch('api.endpoints.insert_event', CoroutineMock()):
            resp = await self.client.request('POST', '/events',
                                             json={'event': 'buy',
                                                   'timestamp': ''})

        assert resp.status == HTTPStatus.CREATED

    @unittest_run_loop
    async def test_post_without_required_argument_returns_422(self):
        resp = await self.client.request('POST', '/events',
                                         json={'event': 'buy'})
        assert resp.status == HTTPStatus.UNPROCESSABLE_ENTITY
