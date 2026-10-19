"""Enregistrement des blueprints. Un fichier = un domaine fonctionnel."""
from flask import Flask

from . import api, pages


def register_routes(app: Flask) -> None:
    prefix = app.config["URL_PREFIX"]
    app.register_blueprint(pages.bp, url_prefix=prefix)
    app.register_blueprint(api.bp, url_prefix=prefix)
