from dataclasses import dataclass
import tomllib

from adaptix import Retort


@dataclass(slots=True)
class LoggerConfig:
    debug: bool
    level: str


@dataclass(slots=True)
class Config:
    logger: LoggerConfig


def get_config_from(path: str) -> Config:
    with open(path, "rb") as file:
        raw_config = tomllib.load(file)
        return Retort().load(raw_config, Config)