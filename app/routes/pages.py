"""Pages HTML."""
from flask import Blueprint, render_template

from ..auth import require_auth

bp = Blueprint("pages", __name__)


@bp.get("/")
@require_auth()
def home():
    return render_template("index.html", title="Accueil")


# Exemple de page protégée par rôle : à supprimer ou adapter.
@bp.get("/admin")
@require_auth("admin")
def admin():
    return render_template("index.html", title="Zone admin")
