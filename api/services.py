async def insert_event(collection, event_args):
    await collection.insert_one({
        "event": event_args["event"],
        "timestamp": event_args["timestamp"]
    })
