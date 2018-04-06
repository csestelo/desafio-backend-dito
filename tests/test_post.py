from api.app import app


async def test_post(aiohttp_client, loop):
    client = await aiohttp_client(app)
    resp = await client.post('/events')
    assert resp.status == 200
    text = await resp.json()
    assert {"haha": "tchau"} == text
