# semanticgis/abstract/__init__.py

"""
The abstract module defines the core, tool-agnostic components for building
a semanticGIS workflow. This is the primary user-facing API.
"""

# Promote the key user-facing classes to the top-level of the 'abstract' namespace.
# This allows users to write 'from semanticgis.abstract import Pipeline'.
from .pipeline import Pipeline
from .steps import VectorStep, RasterStep

# Note: We likely DON'T need to expose vector_ops here, because the user
# will access those methods via an instance of the Pipeline class
# (e.g., my_pipeline.vector.buffer(...)), not by importing it directly.

# Define the public API for 'from semanticgis.abstract import *'
# This controls what users get with a wildcard import and helps linters.
__all__ = [
    'Pipeline',
    'VectorStep',
    'RasterStep',
]