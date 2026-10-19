def test_admin_forbidden_without_role(make_client):
    assert make_client(["other"]).get("/test/admin").status_code == 403


def test_admin_allowed_with_role(make_client):
    assert make_client(["admin"]).get("/test/admin").status_code == 200

# TODO : tester le cas « non connecté » une fois le comportement d'auth_client
# hors test confirmé (redirection vers AUTH_PUBLIC_URL ou 401).
