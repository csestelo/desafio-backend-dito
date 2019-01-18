import json
from aiohttp import web
from http import HTTPStatus
from webargs.aiohttpparser import use_args

from api.config import EVENTS_COLLECTION, MONGO_DB_NAME, REDIS_TTL
from api.schemas import PostSchema, GetSchema
from api.services import insert_event, get_distinct_events

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET",
    "Access-Control-Allow-Headers": "Content-Type"
}


@use_args(GetSchema())
async def get(request, args):
    cache = request.app['redis']
    key = f'dito_event_startswith_{args["event_startswith"]}'

    cached_result = await cache.get(key=key, encoding='utf8')

    if cached_result:
        return web.json_response(status=HTTPStatus.OK,
                                 data={"events": json.loads(cached_result)},
                                 headers=CORS_HEADERS)

    collection = request.app['mongodb'][MONGO_DB_NAME][EVENTS_COLLECTION]
    events = await get_distinct_events(collection=collection,
                                       startswith=args['event_startswith'])

    if not events:
        return web.json_response(status=HTTPStatus.NOT_FOUND,
                                 headers=CORS_HEADERS)

    await cache.set(key, json.dumps(events), expire=REDIS_TTL)
    return web.json_response(status=HTTPStatus.OK, data={"events": events},
                             headers=CORS_HEADERS)


@use_args(PostSchema())
async def post(request, args):
    collection = request.app['mongodb'][MONGO_DB_NAME][EVENTS_COLLECTION]
    await insert_event(collection=collection, event_args=args)

    return web.json_response(status=HTTPStatus.CREATED)
