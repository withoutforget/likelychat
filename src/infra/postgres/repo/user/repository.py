from dataclasses import dataclass
from uuid import UUID

import psycopg
from psycopg.rows import TupleRow, dict_row

from src.infra.postgres.repo.user.model import UserModel


@dataclass(slots=True)
class UserRepository:
    _conn: psycopg.AsyncConnection[TupleRow]

    def _map(self, row: dict) -> UserModel:
        return UserModel(
            id=row["id"],
            username=row["username"],
            password=row["password"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
        )

    async def create(self, username: str, hashed_password: str) -> UserModel:
        async with self._conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(
                """
                INSERT INTO users (username, password)
                VALUES (%s, %s)
                RETURNING *
                """,
                (username, hashed_password),
            )
            row = await cur.fetchone()
            return self._map(row)

    async def get_by_id(self, user_id: UUID) -> UserModel | None:
        async with self._conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(
                "SELECT * FROM users WHERE id = %s",
                (user_id,),
            )
            row = await cur.fetchone()
            return self._map(row) if row else None

    async def get_by_username(self, username: str) -> UserModel | None:
        async with self._conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(
                "SELECT * FROM users WHERE username = %s",
                (username,),
            )
            row = await cur.fetchone()
            return self._map(row) if row else None

    async def update_password(
        self, user_id: UUID, hashed_password: str
    ) -> UserModel | None:
        async with self._conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(
                """
                UPDATE users
                SET password = %s, updated_at = NOW()
                WHERE id = %s
                RETURNING *
                """,
                (hashed_password, user_id),
            )
            row = await cur.fetchone()
            return self._map(row) if row else None

    async def delete(self, user_id: UUID) -> bool:
        async with self._conn.cursor() as cur:
            await cur.execute(
                "DELETE FROM users WHERE id = %s",
                (user_id,),
            )
            return cur.rowcount > 0

    async def exists(self, username: str) -> bool:
        async with self._conn.cursor() as cur:
            await cur.execute(
                "SELECT 1 FROM users WHERE username = %s",
                (username,),
            )
            return await cur.fetchone() is not None
