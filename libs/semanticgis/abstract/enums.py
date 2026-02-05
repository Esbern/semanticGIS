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


class MeasurementScale(str, Enum):
    """Enumerates supported measurement scales for attribute metadata."""

    NOMINAL = "nominal"
    ORDINAL = "ordinal"
    INTERVAL = "interval"
    RATIO = "ratio"


class DataFormat(str, Enum):
    """Canonical identifiers for common geospatial storage formats."""

    GEOPACKAGE = "gpkg"
    GEOJSON = "geojson"
    SHAPEFILE = "shp"
    CSV = "csv"
    POSTGIS = "postgis"
    COG = "cog"
    WFS = "wfs"
    TBD = "tbd"


__all__ = ["SpatialNature", "DataModel", "MeasurementScale", "DataFormat"]
