"""Unit tests for the semanticGIS functional complexes abstraction layer."""
from __future__ import annotations

import pathlib
import sys

import pytest

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
LIB_PATH = REPO_ROOT / "libs"
if str(LIB_PATH) not in sys.path:
    sys.path.insert(0, str(LIB_PATH))

from semanticgis.abstract import (
    Pipeline,
    DataModel,
    SpatialNature,
    MeasurementScale,
    DataFormat,
)
from semanticgis.compilers import mermaid, qgis_recipy, validate


def _build_vector_buffer_pipeline() -> Pipeline:
    pipeline = Pipeline(name="Vector Buffer Happy Path")
    parks = pipeline.io.declare_input(
        source="memory://parks",
        output_name="urban_parks",
        data_model=DataModel.VECTOR,
        spatial_nature=SpatialNature.DISCRETE,
        description="Synthetic green infrastructure polygons",
        label="Urban Parks",
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
    raster = pipeline.io.declare_input(
        source="memory://thermal",
        output_name="thermal_field",
        data_model=DataModel.RASTER,
        spatial_nature=SpatialNature.CONTINUOUS,
    )
    pipeline.proximity.buffer(
        dataset=raster,
        distance=25,
        units="meters",
        output_name="invalid_buffer",
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
        "SOVEREIGNT": {"scale": MeasurementScale.NOMINAL, "description": "State name"},
        "POP_EST": {"scale": MeasurementScale.RATIO, "description": "Population"},
    }
    step = pipeline.io.declare_input(
        source="memory://eu",
        output_name="eu_dataset",
        spatial_nature=SpatialNature.DISCRETE,
        data_model=DataModel.VECTOR,
        attributes=attributes,
        data_format=DataFormat.GEOJSON,
    )

    node = pipeline.nodes[step.id]
    assert node["output_semantics"]["nature"] == "discrete"
    assert node["parameters"]["attributes"] == attributes
    assert node["parameters"]["format"] == DataFormat.GEOJSON.value


def test_declare_input_pre_and_spatial_filters() -> None:
    pipeline = Pipeline(name="Input Filters")
    mask = pipeline.io.declare_input(
        source="memory://mask",
        output_name="nordic_mask",
        data_model=DataModel.VECTOR,
        label="Nordic AOI",
        spatial_nature=SpatialNature.DISCRETE,
    )

    step = pipeline.io.declare_input(
        source="memory://eu",
        output_name="eu_dataset",
        data_model=DataModel.VECTOR,
        spatial_nature=SpatialNature.DISCRETE,
        pre_filter="POP_EST > 0",
        spatial_filter=mask,
        attributes={
            "POP_EST": {"scale": MeasurementScale.RATIO, "description": "Population"}
        },
    )

    node = pipeline.nodes[step.id]
    assert node["parameters"]["pre_filter"] == "POP_EST > 0"
    assert node["parameters"]["spatial_filter"] == mask.id
    assert (mask.id, step.id) in pipeline.edges


def test_declare_input_rejects_attributes_missing_scale() -> None:
    pipeline = Pipeline(name="Invalid Attributes")
    with pytest.raises(ValueError):
        pipeline.io.declare_input(
            source="memory://eu",
            output_name="invalid",
            attributes={"POP_EST": {"description": "Population"}},
        )


def test_declare_input_defaults_label_from_output() -> None:
    pipeline = Pipeline(name="Auto Label")
    step = pipeline.io.declare_input(
        source="memory://auto",
        output_name="Europa_countries",
        data_model=DataModel.VECTOR,
        spatial_nature=SpatialNature.DISCRETE,
    )

    node = pipeline.nodes[step.id]
    assert node["label"] == "Europa_countries"
    assert node["output_name"] == "Europa_countries"
def test_redeclaring_output_overwrites_existing_node() -> None:

    pipeline = Pipeline(name="Redeclare input")
    first = pipeline.io.declare_input(
        source="memory://parks_a",
        output_name="shared_dataset",
        data_model=DataModel.VECTOR,
        label="Original Parks",
        description="First version",
        spatial_nature=SpatialNature.DISCRETE,
    )
    second = pipeline.io.declare_input(
        source="memory://parks_b",
        output_name="shared_dataset",
        data_model=DataModel.VECTOR,
        label="Updated Parks",
        description="Second version",
        spatial_nature=SpatialNature.DISCRETE,
    )

    assert first.id == second.id
    node = pipeline.nodes[first.id]
    assert node["label"] == "Updated Parks"
    assert node["parameters"]["description"] == "Second version"


def test_validator_requires_upstream_source_for_operations() -> None:
    pipeline = Pipeline(name="Dangling step")
    pipeline.io.declare_input(
        source="memory://parks",
        output_name="parks",
        data_model=DataModel.VECTOR,
        spatial_nature=SpatialNature.DISCRETE,
    )

    pipeline._register_node(
        complex_name="extraction",
        operation="filter_by_sql",
        label="Dangling filter",
        input_nodes=[],
        output_semantics={"data_model": "vector"},
        output_name="lonely_dataset",
        data_requirements=[{"data_model": "vector"}],
        parameters={"where_clause": "1=1"},
    )

    errors = validate.compile(pipeline, output="list")
    assert any("Must reference at least one upstream dataset" in error for error in errors)


def test_pipeline_resolves_dataset_by_label_reference() -> None:
    pipeline = Pipeline(name="Label Reference Convenience")
    pipeline.io.declare_input(
        source="memory://auto",
        output_name="europa_countries",
        label="Europa countries dataset",
        data_model=DataModel.VECTOR,
        spatial_nature=SpatialNature.DISCRETE,
    )

    filtered = pipeline.extraction.filter_by_sql(
        dataset="Europa countries dataset",
        where_clause="SOVEREIGNT = 'Denmark'",
        output_name="denmark_subset",
        label="Kingdom of Denmark",
    )

    input_node_id = next(
        node_id
        for node_id, node_data in pipeline.nodes.items()
        if node_data["label"] == "Europa countries dataset"
    )
    assert (input_node_id, filtered.id) in pipeline.edges
