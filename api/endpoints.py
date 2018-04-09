from aiohttp import web
from webargs.aiohttpparser import use_args

from api.schemas import PostSchema


async def get(request):
    return web.json_response({'haha': 'oi'})


@use_args(PostSchema())
async def post(request, args):
    return web.json_response({'haha': 'tchau'})
