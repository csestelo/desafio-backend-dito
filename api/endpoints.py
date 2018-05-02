from aiohttp import web
from http import HTTPStatus
from webargs.aiohttpparser import use_args

from api.config import EVENTS_COLLECTION, MONGO_DB_NAME
from api.schemas import PostSchema, GetSchema
from api.services import insert_event, get_distinct_events


@use_args(GetSchema())
async def get(request, args):
    collection = request.app['mongodb'][MONGO_DB_NAME][EVENTS_COLLECTION]
    events = await get_distinct_events(collection=collection, filters=args)

    if not events:
        return web.json_response(status=HTTPStatus.NOT_FOUND)

    return web.json_response(status=HTTPStatus.OK, data={"events": events})


@use_args(PostSchema())
async def post(request, args):
    collection = request.app['mongodb'][MONGO_DB_NAME][EVENTS_COLLECTION]
    await insert_event(collection=collection, event_args=args)

    return web.json_response(status=HTTPStatus.CREATED)
