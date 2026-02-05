"""Smoke-test the semanticGIS functional complexes within an interactive notebook."""

from semanticgis.abstract import Pipeline, DataModel, SpatialNature
from semanticgis.compilers import mermaid, validate, qgis_recipy

from IPython.display import display, Markdown

print("✅ semanticGIS libraries imported successfully!")

p = Pipeline(name="Scaffold Test Workflow")
print(f"Pipeline '{p.name}' created.")

# Step 1: Register inputs via the Data I/O complex
buildings = p.io.ingest_asset(
    source="path/to/some/buildings.geojson",  # <-- CHANGE THIS PATH
    name="building_footprints",
    data_model=DataModel.VECTOR,
    label="Building Footprints"
)
print(f"Defined step: {buildings.id} ({p.nodes[buildings.id]['label']})")

elevation = p.io.ingest_asset(
    source="path/to/some/elevation.tif",  # <-- CHANGE THIS PATH
    name="elevation_model",
    data_model=DataModel.RASTER,
    measurement_scale="interval",
    nature=SpatialNature.CONTINUOUS,
    label="Elevation Model"
)
print(f"Defined step: {elevation.id} ({p.nodes[elevation.id]['label']})")

# Step 2: Intentionally attempt an invalid proximity operation on a raster semantic
invalid_buffer_step = p.proximity.buffer(
    dataset=elevation,
    distance=50.0,
    output_name="invalid_buffer",
    label="Invalid Buffer on Raster"
)
print(f"Defined step: {invalid_buffer_step.id} ({p.nodes[invalid_buffer_step.id]['label']})")

# Trigger the validator to surface the semantic contract violation
issues = validate.compile(p, output='list')
display(Markdown("\n".join(f"- {issue}" for issue in issues)))

# Render the documentation artifacts for visual inspection
display(Markdown(mermaid.compile(p)))
display(Markdown(qgis_recipy.compile(p)))