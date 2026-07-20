"""
Logging configuration for Kestrel.
"""

from loguru import logger
from kestrel.core.paths import LOG_DIR


def configure_logging() -> None:
    """
    Configure console and file logging.
    """

    # Remove default logger
    logger.remove()

    # Console logging
    logger.add(
        sink=lambda msg: print(msg, end=""),
        level="INFO",
        colorize=True,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
               "<level>{level: <8}</level> | "
               "<cyan>{name}</cyan>:<cyan>{function}</cyan> - "
               "<level>{message}</level>",
    )

    # File logging
    logger.add(
        LOG_DIR / "kestrel.log",
        rotation="10 MB",
        retention="30 days",
        level="DEBUG",
        encoding="utf-8",
    )