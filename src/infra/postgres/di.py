from collections.abc import AsyncIterable

import psycopg
from dishka import Provider, Scope, provide, provide_all
from psycopg.rows import TupleRow

from src.config import Config
from src.infra.postgres.repo.user.repository import UserRepository


class PostgresProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def provide_psycopg_connection(
        self, config: Config
    ) -> AsyncIterable[psycopg.AsyncConnection[TupleRow]]:
        connect = await psycopg.AsyncConnection.connect(
            config.postgres.dsn,
        )
        async with connect as conn:
            yield conn

    @provide(scope=Scope.REQUEST)
    async def provide_psycopg_transaction(
        self, conn: psycopg.AsyncConnection[TupleRow]
    ) -> AsyncIterable[psycopg.AsyncTransaction]:
        async with conn.transaction() as tx:
            yield tx

    repositories = provide_all(UserRepository, scope=Scope.REQUEST)
