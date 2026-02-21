import tomllib
from dataclasses import dataclass
from pathlib import Path

from adaptix import Retort


@dataclass(slots=True)
class LoggerConfig:
    debug: bool
    level: str


@dataclass(slots=True)
class Config:
    logger: LoggerConfig


def get_config_from(path: str) -> Config:
    with Path.open(path, "rb") as file:
        raw_config = tomllib.load(file)
        return Retort().load(raw_config, Config)
