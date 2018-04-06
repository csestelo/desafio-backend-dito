from aiohttp import web
from webargs.aiohttpparser import use_args

from api.schemas import PostSchema, GetSchema


@use_args(GetSchema)
async def get(request):
    return web.json_response({'haha': 'oi'})


@use_args(PostSchema)
async def post(request):
    return web.json_response({'haha': 'tchau'})


app = web.Application()
app.add_routes([web.get('/events', get),
                web.post('/events', post)])

if __name__ == '__main__':
    web.run_app(app)
