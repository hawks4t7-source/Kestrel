"""
Configuration manager.
"""

from pathlib import Path
import shutil
import yaml

from kestrel.core.paths import CONFIG_DIR
from kestrel.config.schema import Config

DEFAULT_CONFIG = (
    Path(__file__).parent
    / "defaults"
    / "default_config.yaml"
)

USER_CONFIG = CONFIG_DIR / "config.yaml"


def initialize_config() -> None:
    """
    Create the user's config file if it doesn't exist.
    """
    if not USER_CONFIG.exists():
        shutil.copy(DEFAULT_CONFIG, USER_CONFIG)


def load_config() -> Config:
    """
    Load and validate the configuration.
    """
    initialize_config()

    with open(USER_CONFIG, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return Config.model_validate(data)