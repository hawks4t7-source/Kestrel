"""
Filesystem paths used by Kestrel.
"""

from pathlib import Path

from platformdirs import PlatformDirs

from kestrel.core.constants import APP_NAME

_dirs = PlatformDirs(APP_NAME, APP_NAME)

CONFIG_DIR = Path(_dirs.user_config_dir)
DATA_DIR = Path(_dirs.user_data_dir)
CACHE_DIR = Path(_dirs.user_cache_dir)
LOG_DIR = DATA_DIR / "logs"

for directory in (CONFIG_DIR, DATA_DIR, CACHE_DIR, LOG_DIR):
    directory.mkdir(parents=True, exist_ok=True)