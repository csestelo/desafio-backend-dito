from aiohttp import web

from api.endpoints import get, post


class EventsApi(object):
    def __init__(self):
        self.app = web.Application()
        self.add_routes()

    def start(self):
        web.run_app(self.app)

    def add_routes(self):
        self.app.add_routes([web.get('/events', get),
                             web.post('/events', post)])


if __name__ == '__main__':
    EventsApi().start()
