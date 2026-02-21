@run:
    uv run uvicorn src.main:app --reload
@lint:
    uv run ruff check --fix
    uv run ruff format