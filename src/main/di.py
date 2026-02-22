from dishka import AsyncContainer, Provider, make_async_container

from src.application.auth.di import AuthServiceProvider
from src.config import Config


class GlobalProvider(Provider):
    pass


def get_async_container(config: Config) -> AsyncContainer:

    return make_async_container(
        GlobalProvider(), AuthServiceProvider(), context={Config: config}
    )
