async def insert_event(collection, event_args):
    await collection.insert_one({
        "event": event_args["event"],
        "timestamp": event_args["timestamp"]
    })


async def get_distinct_events(collection, filters):
    return await collection.distinct(key="event", filter={
        "event": {
            "$regex": f"^{filters['event_startswith']}"
        }
    })
