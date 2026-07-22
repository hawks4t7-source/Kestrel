"""
Kestrel application.

Central application object responsible for managing the application's
lifecycle and exposing shared services.
"""

from __future__ import annotations

from kestrel.bootstrap.container import ServiceContainer


class KestrelApplication:
    """
    Main application object.
    """

    def __init__(self) -> None:
        self._container = ServiceContainer()
        self._started = False

    @property
    def container(self) -> ServiceContainer:
        """
        Return the application's service container.
        """
        return self._container

    @property
    def started(self) -> bool:
        """
        Return startup state.
        """
        return self._started

    def start(self) -> None:
        """
        Start the application.
        """
        if self._started:
            return

        self._started = True

    def shutdown(self) -> None:
        """
        Shut down the application.
        """
        if not self._started:
            return

        self._container.clear()
        self._started = False

    def restart(self) -> None:
        """
        Restart the application.
        """
        self.shutdown()
        self.start()