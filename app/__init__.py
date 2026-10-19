"""Application factory du service."""
from flask import Flask, g, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

from .config import Config
from .routes import register_routes

ERRORS = {
    403: "Accès refusé",
    404: "Page introuvable",
    500: "Erreur interne",
}


def create_app(overrides: dict | None = None) -> Flask:
    cfg = {k: getattr(Config, k) for k in dir(Config) if k.isupper()}
    cfg.update(overrides or {})

    # Le reverse proxy route /<prefix>/* vers ce conteneur : le statique doit suivre.
    app = Flask(__name__, static_url_path=f"{cfg['URL_PREFIX']}/static")
    app.config.update(cfg)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

    register_routes(app)
    _register_error_handlers(app)

    @app.context_processor
    def inject_globals():
        return {
            "service_title": app.config["SERVICE_TITLE"],
            "user": g.get("user"),
            "logout_url": f"{app.config['AUTH_PUBLIC_URL']}/logout?next={app.config['PUBLIC_URL']}/",
        }

    return app


def _register_error_handlers(app: Flask) -> None:
    for code, message in ERRORS.items():
        app.register_error_handler(
            code,
            lambda e, code=code, message=message: (
                render_template("errors/error.html", code=code, message=message),
                code,
            ),
        )
