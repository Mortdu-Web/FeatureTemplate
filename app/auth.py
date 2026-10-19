"""Point d'entrée unique vers l'authentification.

Les routes importent `require_auth` d'ici (jamais directement de auth_client) :
un seul endroit à modifier si le client SSO change, et possibilité de simuler
un utilisateur en test (config TEST_USER) sans serveur d'auth.
"""
from functools import wraps

from auth_client import require_auth as _require_auth
from flask import abort, current_app, g


def require_auth(*roles):
    def decorator(view):
        protected = _require_auth(*roles)(view)

        @wraps(view)
        def wrapper(*args, **kwargs):
            test_user = current_app.config.get("TEST_USER")
            if current_app.testing and test_user is not None:
                if roles and not set(roles) & set(test_user.get("roles", [])):
                    abort(403)
                g.user = test_user
                return view(*args, **kwargs)
            return protected(*args, **kwargs)

        return wrapper

    return decorator
