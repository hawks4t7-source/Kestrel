"""
Service container for Kestrel.

The container owns all singleton services used by the application.
Services are registered once during bootstrap and shared across
the application.
"""

from __future__ import annotations

from typing import Any


class ServiceContainer:
    """
    Simple dependency injection container.

    Stores singleton services used throughout the application.
    """

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        """
        Register a singleton service.
        """
        if name in self._services:
            raise ValueError(f"Service '{name}' is already registered.")

        self._services[name] = service

    def get(self, name: str) -> Any:
        """
        Retrieve a registered service.
        """
        try:
            return self._services[name]
        except KeyError as exc:
            raise KeyError(f"Service '{name}' is not registered.") from exc

    def exists(self, name: str) -> bool:
        """
        Check whether a service exists.
        """
        return name in self._services

    def remove(self, name: str) -> None:
        """
        Remove a registered service.
        """
        self._services.pop(name, None)

    def clear(self) -> None:
        """
        Remove all services.
        """
        self._services.clear()

    def list_services(self) -> list[str]:
        """
        Return all registered service names.
        """
        return sorted(self._services.keys())

    def __contains__(self, name: str) -> bool:
        return name in self._services

    def __len__(self) -> int:
        return len(self._services)