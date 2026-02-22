from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import Config
from src.main.di import get_async_container
from src.presentation.setup import setup_app


def setup_fastapi(config: Config) -> FastAPI:
    app = FastAPI()

    container = get_async_container(config)
    setup_dishka(container=container, app=app)

    cors = config.cors

    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors.allow_origins,
        allow_credentials=cors.allow_credentials,
        allow_methods=cors.allow_methods,
        allow_headers=cors.allow_headers,
    )

    setup_app(app)

    return app
