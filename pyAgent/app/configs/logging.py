from loguru import logger;
import sys;

logger.remove();

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
)

logger.add(
    "logs/app.log",
    level="INFO",
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
)


logger.add(
    "logs/error.log",
    level="ERROR",
    rotation="20 MB",
    retention="60 days",
    format="<red>{time:YYYY-MM-DD HH:mm:ss}</red> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
)