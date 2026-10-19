# Conventions

## Principe
Un dépôt = un conteneur = une feature. Tous les services rejoignent le réseau Docker
externe `web` et sont exposés par le reverse proxy sous `/<slug>/`.

## Structure
| Chemin | Rôle |
|---|---|
| `app/__init__.py` | factory `create_app()`, handlers d'erreurs, variables de template |
| `app/config.py` | config lue depuis l'environnement |
| `app/auth.py` | seul point d'import de `auth_client` (+ simulation en test) |
| `app/routes/` | un fichier par domaine fonctionnel, enregistré dans `__init__.py` |
| `app/templates/`, `app/static/` | UI du service |
| `tests/` | pytest, auth simulée via `TEST_USER` |
| `scripts/` | `init.sh`, `healthcheck.py` |

## Ajouter une fonctionnalité
1. Créer `app/routes/ma_feature.py` avec un `Blueprint`.
2. L'enregistrer dans `app/routes/__init__.py` avec `url_prefix=prefix`.
3. Protéger avec `@require_auth()` ou `@require_auth("role")` (import depuis `..auth`).
4. Ajouter template(s) et tests.

## Conventions
- Toutes les routes sont sous `URL_PREFIX` ; le statique aussi.
- `/health` public (healthcheck Docker), tout le reste protégé par défaut.
- Un port hôte unique par service (ex. 25000 auth, 25001 hub-app, 25002...).
- Configuration uniquement par `.env`, jamais de secret dans le dépôt.
- `auth-client` épinglé sur un tag Git ; le mettre à jour = changer le tag.
