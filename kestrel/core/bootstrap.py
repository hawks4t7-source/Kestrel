"""
Kestrel Application Bootstrap.

Delegates application startup to the Bootstrap Engine.
"""

from __future__ import annotations

from kestrel.bootstrap.application import KestrelApplication
from kestrel.bootstrap.lifecycle import ApplicationLifecycle


def initialize() -> KestrelApplication:
    """
    Initialize the Kestrel application.

    Returns
    -------
    KestrelApplication
        Running application instance.
    """

    app = KestrelApplication()

    lifecycle = ApplicationLifecycle(app)

    lifecycle.startup()

    return app