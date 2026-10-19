"""Endpoints techniques / JSON."""
from flask import Blueprint, g, jsonify

from ..auth import require_auth

bp = Blueprint("api", __name__)


@bp.get("/health")
def health():
    return {"status": "ok"}


@bp.get("/whoami")
@require_auth()
def whoami():
    return jsonify(g.user)  # username, email, roles
