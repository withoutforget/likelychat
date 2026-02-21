from structlog import get_logger

from src.config import Config, get_config_from
from src.infra.logger.logging import setup_logger
from src.main.web import setup_fastapi


config: Config = get_config_from('./config/config.toml') 
setup_logger(config.logger)

logger = get_logger(__name__)
logger.info("Logger set up")

app = setup_fastapi(config)

