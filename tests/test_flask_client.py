import pytest

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_root(client):
    rv = client.get('/')

    assert b'control.r' in rv.data


def test_today(client):
    rv = client.get('/today')

    assert b'align="center' in rv.data


def test_graph(client):
    rv = client.get('/statis')

    assert b'google.visualization.ColumnChart' in rv.data

