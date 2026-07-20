"""
kestrel.workspace.exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Custom exceptions used by the Kestrel Workspace subsystem.

These exceptions provide meaningful error types that can be
caught by higher-level modules (CLI, bootstrap, plugins, etc.)
instead of relying on generic Python exceptions.

Author:
    Kestrel Development Team

License:
    MIT
"""

from __future__ import annotations


class WorkspaceError(Exception):
    """
    Base exception for all workspace-related errors.

    Every workspace exception should inherit from this class so
    callers can catch a single exception type when appropriate.

    Example
    -------
    try:
        ...
    except WorkspaceError:
        ...
    """

    default_message = "Workspace operation failed."

    def __init__(self, message: str | None = None):
        super().__init__(message or self.default_message)


class WorkspaceInitializationError(WorkspaceError):
    """
    Raised when the workspace cannot be created or initialized.
    """

    default_message = "Failed to initialize workspace."


class WorkspaceValidationError(WorkspaceError):
    """
    Raised when the workspace structure is invalid.
    """

    default_message = "Workspace validation failed."


class WorkspacePermissionError(WorkspaceError):
    """
    Raised when Kestrel lacks permission to access
    the workspace.
    """

    default_message = "Insufficient permissions for workspace."


class WorkspaceNotFoundError(WorkspaceError):
    """
    Raised when an expected workspace does not exist.
    """

    default_message = "Workspace not found."


class WorkspaceAlreadyExistsError(WorkspaceError):
    """
    Raised when attempting to create a workspace
    that already exists.
    """

    default_message = "Workspace already exists."


class InvalidWorkspacePathError(WorkspaceError):
    """
    Raised when the configured workspace path
    is invalid.
    """

    default_message = "Invalid workspace path."


class DirectoryCreationError(WorkspaceError):
    """
    Raised when a required directory cannot be created.
    """

    default_message = "Unable to create required directory."


class DirectoryDeletionError(WorkspaceError):
    """
    Raised when a directory cannot be removed.
    """

    default_message = "Unable to delete directory."


class WorkspaceConfigurationError(WorkspaceError):
    """
    Raised when workspace configuration is invalid.
    """

    default_message = "Workspace configuration error."


class WorkspaceIntegrityError(WorkspaceError):
    """
    Raised when corruption or missing critical
    files/directories are detected.
    """

    default_message = "Workspace integrity check failed."


class ProjectDirectoryError(WorkspaceError):
    """
    Raised for project directory related failures.
    """

    default_message = "Project directory operation failed."


class ReportDirectoryError(WorkspaceError):
    """
    Raised when report directory operations fail.
    """

    default_message = "Report directory operation failed."


class EvidenceDirectoryError(WorkspaceError):
    """
    Raised when evidence storage cannot be accessed.
    """

    default_message = "Evidence directory operation failed."


class LogDirectoryError(WorkspaceError):
    """
    Raised when log directory cannot be created
    or accessed.
    """

    default_message = "Log directory operation failed."


class DatabaseDirectoryError(WorkspaceError):
    """
    Raised when database directory cannot
    be initialized.
    """

    default_message = "Database directory operation failed."


class TemporaryDirectoryError(WorkspaceError):
    """
    Raised when the temporary directory
    cannot be managed.
    """

    default_message = "Temporary directory operation failed."