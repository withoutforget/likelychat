from dishka import (
    AsyncContainer,
    Provider,
    Scope,
    from_context,
    make_async_container,
)
from fastapi import Request

from src.application.auth.di import AuthServiceProvider
from src.config import Config


class GlobalProvider(Provider):
    request = from_context(provides=Request, scope=Scope.REQUEST)


def get_async_container(config: Config) -> AsyncContainer:

    return make_async_container(
        GlobalProvider(), AuthServiceProvider(), context={Config: config}
    )
