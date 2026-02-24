@run:
    uv run uvicorn src.main.main:app --reload
@lint:
    uv run ruff check --fix
    uv run ruff format
@migrate:
    flyway migrate