import pytest

from main import get_application


@pytest.fixture
def client(loop, aiohttp_client):
    app = loop.run_until_complete(get_application())
    return loop.run_until_complete(aiohttp_client(app))


async def test_create__ok(client):
    resp = await client.post('/restaurants', json={
        'name': 'Sadhu',
        'opens_at': '2018-05-23T09:49:30Z',
        'closes_at': '2018-05-23T09:49:30Z'
    })
    assert resp.status == 200

    data = await resp.json()
    assert data['name'] == 'Sadhu'


async def test_create__failed(client):
    resp = await client.post('/restaurants', json={
        'opens_at': '2018-05-23T09:49:30Z',
        'closes_at': '2018-05-23T09:49:30Z'
    })
    assert resp.status == 400

    errors = await resp.json()
    assert errors['name']['error_msg'] == 'field required'


async def test_get_restaurants__ok(client):
    resp = await client.get('/restaurants')
    assert resp.status == 200

    data = await resp.json()
    assert data['restaurants'][0]['name'] == 'Sadhu'


async def test_get__ok(client):
    resp = await client.get('/restaurant/1')
    assert resp.status == 200

    data = await resp.json()
    assert data['name'] == 'Sadhu'


async def test_update__ok(client):
    resp = await client.put('/restaurant/1', params={
        'name': 'Sadhu Nightly',
        'opens_at': '2018-05-23T09:49:30Z',
    })

    assert resp.status == 204


async def test_update__null(client):
    resp = await client.put('/restaurant/99', params={
        'name': 'Sadhu Nightly',
        'opens_at': '2018-05-23T09:49:30Z',
        'closes_at': '2018-05-23T09:49:30Z'
    })

    assert resp.status == 404


async def test_delete__ok(client):
    resp = await client.delete('/restaurant/1')

    assert resp.status == 204


async def test_delete__not_found(client):
    resp = await client.delete('/restaurant/1')

    assert resp.status == 404
