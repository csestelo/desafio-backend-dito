import asyncio
import random
import time
from datetime import datetime
from itertools import repeat

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from typing import List, Dict

from api.config import INSERT_DOCS_QTY, DATETIME_FORMAT, MONGO_URI, \
    EVENTS_COLLECTION, MONGO_DB_NAME, BULK_INSERTION_QTY

POSSIBLE_EVENTS = ['buy', 'sell', 'watch', 'exchange', 'steal', 'dance',
                   'got rich', 'be jealous', 'swim', 'got naked']


def create_random_datetime_string() -> str:
    random_timestamp = round(random.uniform(0, time.time()), 2)
    datetime_string = datetime.fromtimestamp(random_timestamp)
    return datetime.strftime(datetime_string, DATETIME_FORMAT)


def create_messages(qty: int) -> List[Dict]:
    return [{"event": random.choice(POSSIBLE_EVENTS),
             "timestamp": create_random_datetime_string()}
            for i in range(qty)]


def msgs_per_insertion(total: int = INSERT_DOCS_QTY,
                       per_insertion: int = BULK_INSERTION_QTY) -> List[int]:
    n_insertions, rest = divmod(total, per_insertion)
    qtd = list(repeat(per_insertion, n_insertions))
    if rest:
        qtd.append(rest)
    return qtd


async def insert_docs(messages: List[Dict], collection: AsyncIOMotorCollection):
    inserted = await collection.insert_many(messages)
    print({"info": f'Inserted {len(inserted.inserted_ids)} docs.'})


def run(mongo_db=MONGO_DB_NAME):
    conn = AsyncIOMotorClient(MONGO_URI)
    collection = conn[mongo_db][EVENTS_COLLECTION]

    msgs_qty = msgs_per_insertion()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        *(insert_docs(create_messages(qty), collection) for qty in msgs_qty))
    )

    conn.close()
    loop.close()


if __name__ == '__main__':
    run()
