from fastapi import APIRouter, FastAPI

from src.presentation.healthcheck.get import ROUTER as HEALTHCHECK_ROUTER


def setup_app(app: FastAPI) -> None:
    api = APIRouter(prefix="/api/v1")

    api.include_router(HEALTHCHECK_ROUTER)

    app.include_router(api)
