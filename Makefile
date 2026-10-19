.PHONY: dev test lint build up down logs
dev:
	flask --app wsgi run --debug --port 5000
test:
	pytest
lint:
	ruff check .
build:
	docker compose build
up:
	docker compose up -d --build
down:
	docker compose down
logs:
	docker compose logs -f
