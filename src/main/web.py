from fastapi import FastAPI
from src.config import Config
from src.presentation.setup import setup_app

def setup_fastapi(config: Config) -> FastAPI:
    app = FastAPI()

    setup_app(app)

    return app