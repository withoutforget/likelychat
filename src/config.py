import tomllib
from dataclasses import dataclass
from pathlib import Path

from adaptix import Retort


@dataclass(slots=True)
class LoggerConfig:
    debug: bool
    level: str


@dataclass(slots=True)
class CORSConfig:
    allow_origins: list[str]
    allow_credentials: bool
    allow_methods: list[str]
    allow_headers: list[str]


@dataclass(slots=True)
class AuthServiceConfig:
    secret_key: str
    algorithm: str
    token_timeout: int


@dataclass(slots=True)
class PostgresConfig:
    host: str
    port: int
    database: str
    user: str
    password: str

    @property
    def dsn(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass(slots=True)
class Config:
    logger: LoggerConfig
    cors: CORSConfig
    auth: AuthServiceConfig
    postgres: PostgresConfig


def get_config_from(path: str) -> Config:
    with Path.open(path, "rb") as file:
        raw_config = tomllib.load(file)
        return Retort().load(raw_config, Config)
