from datetime import datetime
from unittest.mock import patch

from aiohttp.test_utils import unittest_run_loop
from http import HTTPStatus

from asynctest import CoroutineMock

from api.config import DATETIME_FORMAT
from tests.base import AppBaseTests


class PostTests(AppBaseTests):
    @unittest_run_loop
    async def test_post_with_correct_arguments_returns_200(self):
        params = {'event': 'buy',
                  'timestamp': datetime.now().strftime(DATETIME_FORMAT)}

        with patch('api.endpoints.insert_event', CoroutineMock()):
            resp = await self.client.request('POST', '/events',
                                             json=params)

        assert HTTPStatus.CREATED == resp.status

    @unittest_run_loop
    async def test_post_without_required_argument_returns_422(self):
        resp = await self.client.request('POST', '/events',
                                         json={'event': 'buy'})

        assert resp.status == HTTPStatus.UNPROCESSABLE_ENTITY

    @unittest_run_loop
    async def test_post_with_invalid_argument_returns_422(self):
        resp = await self.client.request('POST', '/events',
                                         json={'event': 'buy',
                                               'timestamp': 'invalid datetime'})

        assert resp.status == HTTPStatus.UNPROCESSABLE_ENTITY
