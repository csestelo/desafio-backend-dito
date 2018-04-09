from aiohttp.test_utils import AioHTTPTestCase

from api.app import EventsApi


class BaseTests(AioHTTPTestCase):
    async def get_application(self):
        api = EventsApi()
        return api.app
