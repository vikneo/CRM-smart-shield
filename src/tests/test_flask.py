import pytest
from flask import Flask


def test_create_app(app):
    """Testing a created application is Flask"""

    assert isinstance(app, Flask)
    assert app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite://"


@pytest.mark.parametrize(
    "route",
    [
        "/",
    ],
)
def test_route_status_method_get(client, route):
    """Checking paths for get requests"""

    route_status = client.get(route)
    assert route_status.status_code == 200
