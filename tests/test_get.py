from api.app import app


async def test_get(aiohttp_client, loop):
    client = await aiohttp_client(app)
    resp = await client.get('/events')
    assert resp.status == 200
    text = await resp.json()
    assert {"haha": "oi"} == text
