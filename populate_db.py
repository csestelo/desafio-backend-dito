import asyncio
import random
import time
from datetime import datetime
from itertools import repeat

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from typing import List, Dict, Generator

from pymongo.errors import ConnectionFailure

from api.config import INSERT_DOCS_QTY, DATETIME_FORMAT, EVENTS_COLLECTION, \
    MONGO_DB_NAME, BULK_INSERTION_QTY, logger, MONGO_PARAMS

POSSIBLE_EVENTS = ['buy', 'sell', 'watch', 'exchange', 'steal', 'steady',
                   'got rich', 'be jealous', 'extend', 'got naked', 'be famous']


def create_random_datetime_string() -> str:
    random_timestamp = round(random.uniform(0, time.time()), 2)
    datetime_string = datetime.fromtimestamp(random_timestamp)
    return datetime.strftime(datetime_string, DATETIME_FORMAT)


def create_messages(qty: int) -> List[Dict]:
    for i in range(qty):
        yield {"event": random.choice(POSSIBLE_EVENTS),
               "timestamp": create_random_datetime_string()}


def msgs_per_insertion(total: int = INSERT_DOCS_QTY,
                       per_insertion: int = BULK_INSERTION_QTY) -> Generator:
    n_insertions, rest = divmod(total, per_insertion)
    for item in repeat(per_insertion, n_insertions):
        yield item

    if rest:
        yield rest


async def insert_docs(messages: List[Dict], collection: AsyncIOMotorCollection):
    inserted = await collection.insert_many(messages)
    logger.info({"info": f'Inserted {len(inserted.inserted_ids)} docs.'})


def get_collection(conn, mongo_db=MONGO_DB_NAME):
    return conn[mongo_db][EVENTS_COLLECTION]


async def connect():
    connected = False
    while not connected:
        conn = AsyncIOMotorClient(**MONGO_PARAMS)
        collection = get_collection(conn)

        try:
            await collection.create_index('event')
            connected = True
        except ConnectionFailure:
            logger.warn({'info': 'Could not connect, trying again in 1 sec.'})
            await asyncio.sleep(1)
            continue

    return conn, collection


async def run():
    conn, collection = await connect()
    msgs_qty = msgs_per_insertion()

    await asyncio.gather(
        *(insert_docs(create_messages(qty), collection) for qty in msgs_qty))

    conn.close()

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(run())
