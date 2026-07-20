"""
Executable entry point.
"""

from kestrel.core.bootstrap import initialize
from kestrel.cli.app import app

initialize()

if __name__ == "__main__":
    app()