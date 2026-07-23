"""
Database model registry.

Ensures all models are imported before table creation.
"""

from kestrel.database.models.project import Project
from kestrel.database.models.target import Target
from kestrel.database.models.asset import Asset
from kestrel.database.models.finding import Finding
from kestrel.database.models.evidence import Evidence


MODELS = [
    Project,
    Target,
    Asset,
    Finding,
    Evidence,
]