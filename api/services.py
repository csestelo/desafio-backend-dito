from aiocache import cached, RedisCache

from api.config import REDIS_TTL, REDIS_PARAMS


async def insert_event(collection, event_args):
    await collection.insert_one({
        "event": event_args["event"],
        "timestamp": event_args["timestamp"]
    })


@cached(ttl=REDIS_TTL, cache=RedisCache, **REDIS_PARAMS)
async def get_distinct_events(collection, startswith):
    return await collection.distinct(key="event", filter={
        "event": {
            "$regex": f"^{startswith}"
        }
    })
