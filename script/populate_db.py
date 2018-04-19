import asyncio
import random
import time
from datetime import datetime

from aiohttp import ClientSession
from http import HTTPStatus

from api.config import INSERT_DOCS_QTY, DATETIME_FORMAT, POST_URL

POSSIBLE_EVENTS = ['buy', 'sell', 'watch', 'exchange', 'steal', 'dance',
                   'got rich', 'be jealous', 'swim', 'got naked']


def create_random_datetime():
    random_timestamp = round(random.uniform(0, time.time()), 2)
    datetime_string = datetime.fromtimestamp(random_timestamp)
    return datetime.strftime(datetime_string, DATETIME_FORMAT)


def create_messages():
    return [{"event": random.choice(POSSIBLE_EVENTS),
             "timestamp": create_random_datetime()}
            for i in range(INSERT_DOCS_QTY)]


async def insert_doc(message):
    with ClientSession() as session:
        resp = await session.post(POST_URL, json=message)

        if resp.status == HTTPStatus.CREATED:
            print({"info": f'Inserted doc: {message}'})
            return

        print({"info": f'Was not possible insert doc: {message}',
               "status_code": resp.status})
        return


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    *(insert_doc(msg) for msg in create_messages())
))
loop.close()
