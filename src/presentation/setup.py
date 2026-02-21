from fastapi import FastAPI, APIRouter

from src.presentation.healthcheck.get import ROUTER as healthcheck_router

def setup_app(app: FastAPI) -> None:
    api = APIRouter(prefix = '/api/v1')
    
    api.include_router(healthcheck_router)

    app.include_router(api)