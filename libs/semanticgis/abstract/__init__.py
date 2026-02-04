# semanticgis/abstract/__init__.py

"""
The abstract module defines the core, tool-agnostic components for building
a semanticGIS workflow. This is the primary user-facing API.
"""

# Promote the key user-facing classes to the top-level of the 'abstract' namespace.
# This allows users to write 'from semanticgis.abstract import Pipeline'.
from .pipeline import Pipeline
from .steps import SemanticStep, VisualisationStep

# Note: The user interacts with operations through the functional complexes
# (e.g., my_pipeline.proximity.buffer(...)) instead of importing operations directly.

# Define the public API for 'from semanticgis.abstract import *'
# This controls what users get with a wildcard import and helps linters.
__all__ = [
    'Pipeline',
    'SemanticStep',
    'VisualisationStep',
]