def test_health_is_public(client):
    r = client.get("/test/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_home_shows_user(client):
    r = client.get("/test/")
    assert r.status_code == 200
    assert b"alice" in r.data


def test_whoami(make_client):
    r = make_client(["editor"]).get("/test/whoami")
    assert r.get_json()["roles"] == ["editor"]


def test_404_uses_error_template(client):
    r = client.get("/test/nope")
    assert r.status_code == 404
    assert "Page introuvable".encode() in r.data


def test_static_follows_prefix(client):
    assert client.get("/test/static/css/base.css").status_code == 200
