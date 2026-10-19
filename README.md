# __TITLE__

Squelette de service Flask + Docker, avec SSO via `auth-client`.

## Créer un nouveau service depuis ce template
1. Sur GitHub : *Use this template* (ou copier le dossier).
2. `./scripts/init.sh mon-service 25002 "Mon Service"`
3. Éditer `.env`, puis `make up`.
4. Déclarer la route `/mon-service/` dans le reverse proxy.

## Développement
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
make test
make dev        # http://localhost:5000/__SLUG__/ (nécessite l'auth joignable)
```

## Docker
```bash
docker network create web   # une seule fois
make up
```

Voir [docs/architecture.md](docs/architecture.md) pour les conventions.
