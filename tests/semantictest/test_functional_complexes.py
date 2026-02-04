"""Unit tests for the semanticGIS functional complexes abstraction layer."""
from __future__ import annotations

import pytest

from semanticgis.abstract import Pipeline
from semanticgis.compilers import mermaid, qgis_recipy, validate


def _build_vector_buffer_pipeline() -> Pipeline:
    pipeline = Pipeline(name="Vector Buffer Happy Path")
    parks = pipeline.io.declare_input(
        name="urban_parks",
        source="memory://parks",
        data_model="vector",
        measurement_scale="ratio",
        nature="discrete",
        description="Synthetic green infrastructure polygons",
    )
    pipeline.proximity.buffer(
        dataset=parks,
        distance=150,
        units="meters",
        output_name="cooling_zone",
        label="Cooling influence zone",
    )
    return pipeline


def test_proximity_buffer_accepts_vector_inputs() -> None:
    """Ensure that a vector dataset flows through the Proximity complex without validation errors."""
    pipeline = _build_vector_buffer_pipeline()
    errors = validate.compile(pipeline, output="list")
    assert errors == []


def test_proximity_buffer_rejects_raster_inputs() -> None:
    """Raster semantics should trigger a validation error when buffered."""
    pipeline = Pipeline(name="Raster Buffer Negative Case")
    raster = pipeline.io.ingest_asset(
        source="memory://thermal",
        name="thermal_field",
        data_model="raster",
        measurement_scale="interval",
        nature="continuous",
    )
    pipeline.proximity.buffer(
        dataset=raster,
        distance=25,
        units="meters",
        label="Invalid raster buffer",
    )
    errors = validate.compile(pipeline, output="list")
    assert any("requires 'vector'" in error for error in errors)


def test_compilers_emit_artifacts() -> None:
    """Mermaid and QGIS compilers should run end-to-end on a semantic pipeline."""
    pipeline = _build_vector_buffer_pipeline()
    mermaid_output = mermaid.compile(pipeline)
    qgis_output = qgis_recipy.compile(pipeline)

    assert mermaid_output.startswith("```mermaid")
    assert f"# QGIS Recipe: {pipeline.name}" in qgis_output


def test_declare_input_captures_attribute_metadata() -> None:
    """Attribute schemas should be stored in the node parameters for provenance."""
    pipeline = Pipeline(name="Metadata Capture")
    attributes = {
        "SOVEREIGNT": {"scale": "nominal", "description": "State name"},
        "POP_EST": {"scale": "ratio", "description": "Population"},
    }
    step = pipeline.io.declare_input(
        name="Europa_countries",
        source="memory://eu",
        spatial_nature="discrete",
        data_model="vector",
        attributes=attributes,
    )

    node = pipeline.nodes[step.id]
    assert node["output_semantics"]["nature"] == "discrete"
    assert node["parameters"]["attributes"] == attributes
