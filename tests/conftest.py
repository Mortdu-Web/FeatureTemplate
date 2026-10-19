import pytest

from app import create_app


@pytest.fixture
def make_client():
    """Fabrique un client de test connecté avec les rôles donnés."""

    def _make(roles=()):
        app = create_app({
            "TESTING": True,
            "URL_PREFIX": "/test",
            "TEST_USER": {"username": "alice", "email": "alice@example.org", "roles": list(roles)},
        })
        return app.test_client()

    return _make


@pytest.fixture
def client(make_client):
    return make_client()
