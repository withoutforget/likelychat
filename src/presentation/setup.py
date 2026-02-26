from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, FastAPI

from src.presentation.auth.login import ROUTER as LOGIN_ROUTER
from src.presentation.auth.register import ROUTER as REGISTER_ROUTER
from src.presentation.healthcheck.get import ROUTER as HEALTHCHECK_ROUTER


def setup_app(app: FastAPI) -> None:
    api = APIRouter(prefix="/api/v1", route_class=DishkaRoute)

    api.include_router(HEALTHCHECK_ROUTER)
    api.include_router(LOGIN_ROUTER, prefix="/auth")
    api.include_router(REGISTER_ROUTER, prefix="/auth")


    app.include_router(api)
