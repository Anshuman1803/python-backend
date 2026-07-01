# app/config/__init__.py

import sys
from pydantic import ValidationError

from .settings import get_settings
from .logging import logger 

try:
    settings = get_settings()

    logger.info("Checking required environment variables")
    required_envs = {
        "MONGO_USER": settings.MONGO_USER,
        "MONGO_PASS": settings.MONGO_PASS,
        "MONGO_DBNAME": settings.MONGO_DBNAME
    }
    missing_envs = [
        key for key, value in required_envs.items()
        if value is None or value == ""
    ]

    if missing_envs:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing_envs)}"
        )
    logger.info("Required environment variables check passed successfully.")

except ValidationError as error:
    logger.error("Environment validation failed")
    logger.error(error)
    sys.exit(1)

except ValueError as error:
    logger.error("Environment configuration error")
    logger.error(error)
    sys.exit(1)

__all__ = ["settings", "logger"]