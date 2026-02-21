from src.config import Config, get_config_from
import asyncio

from src.infra.logger.logging import setup_logger
from structlog import get_logger

from src.main.web import setup_fastapi

async def main() -> None:
    config: Config = get_config_from('./config/config.toml') 
    setup_logger(config.logger)

    logger = get_logger(__name__)
    logger.info("Logger set up")

    app = setup_fastapi(config)

if __name__ == '__main__':
    asyncio.run(main())