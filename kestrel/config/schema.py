"""
Configuration schema for Kestrel.
"""

from pydantic import BaseModel


class ApplicationConfig(BaseModel):
    name: str
    version: str


class DatabaseConfig(BaseModel):
    engine: str
    file: str


class LoggingConfig(BaseModel):
    level: str
    file: str
    rotation: str
    retention: str


class WorkspaceConfig(BaseModel):
    directory: str


class ReportsConfig(BaseModel):
    default_format: str


class AIConfig(BaseModel):
    enabled: bool


class Config(BaseModel):
    application: ApplicationConfig
    database: DatabaseConfig
    logging: LoggingConfig
    workspace: WorkspaceConfig
    reports: ReportsConfig
    ai: AIConfig