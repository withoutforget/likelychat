from os import getenv

from structlog import get_logger

from src.config import Config, get_config_from
from src.infra.logger.logging import setup_logger
from src.main.web import setup_fastapi

config_path = getenv("CONFIG_PATH", "./config/config.toml")

config: Config = get_config_from(config_path)
setup_logger(config.logger)

logger = get_logger(__name__)
logger.info("Logger set up")

app = setup_fastapi(config)
