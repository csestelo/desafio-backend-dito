from aiohttp import web
from http import HTTPStatus
from webargs.aiohttpparser import use_args

from api.config import EVENTS_COLLECTION, MONGO_DB_NAME
from api.schemas import PostSchema
from api.services import insert_event


async def get(request):
    return web.json_response({'haha': 'oi'})


@use_args(PostSchema())
async def post(request, args):
    collection = request.app['mongodb'][MONGO_DB_NAME][EVENTS_COLLECTION]
    await insert_event(collection=collection, event_args=args)

    return web.json_response(status=HTTPStatus.CREATED)
