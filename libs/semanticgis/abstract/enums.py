from __future__ import annotations

from enum import Enum


class SpatialNature(str, Enum):
    """Spatial measurement domains for semantic datasets."""

    DISCRETE = "discrete"
    CONTINUOUS = "continuous"


class DataModel(str, Enum):
    """Supported data model categories for semantic datasets."""

    VECTOR = "vector"
    RASTER = "raster"
    TBD = "tbd"


__all__ = ["SpatialNature", "DataModel"]
