"""Configuration : tout vient des variables d'environnement (.env)."""
import os


def _url(name: str, default: str) -> str:
    return os.environ.get(name, default).rstrip("/")


class Config:
    SERVICE_SLUG = "__SLUG__"
    SERVICE_TITLE = "__TITLE__"

    # Préfixe sous lequel le reverse proxy expose ce service
    URL_PREFIX = _url("URL_PREFIX", "/__SLUG__")
    # Service d'authentification : vu par le navigateur (redirections, logout)
    AUTH_PUBLIC_URL = _url("AUTH_PUBLIC_URL", "http://localhost:25000/auth")
    # URL publique de ce service (retour après déconnexion)
    PUBLIC_URL = _url("PUBLIC_URL", "http://localhost:__PORT__/__SLUG__")
