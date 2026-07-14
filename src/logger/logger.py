"""
Project logger.
"""

import sys

from loguru import logger

from src.config.paths import LOG_DIR
from src.config.settings import settings


LOG_DIR.mkdir(parents=True, exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    level=settings.log_level,
    colorize=True,
)

logger.add(
    LOG_DIR / "warehouse.log",
    level=settings.log_level,
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    enqueue=True,
    backtrace=True,
    diagnose=True,
    encoding="utf-8",
)