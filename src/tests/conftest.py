import pytest

from smart_shield.app import create_app


@pytest.fixture
def app():
    _app = create_app(test=True)
    _app.config["TESTING"] = True

    yield _app


@pytest.fixture()
def client(app):
    client = app.test_client()
    yield client
