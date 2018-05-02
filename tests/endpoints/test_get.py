from aiohttp.test_utils import unittest_run_loop

from tests.base import AppBaseTests


class GetTests(AppBaseTests):
    @unittest_run_loop
    async def test_get(self):
        resp = await self.client.request('GET', '/events')
        assert resp.status == 200
        text = await resp.json()
        assert {"haha": "oi"} == text
