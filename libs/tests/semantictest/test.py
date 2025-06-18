# Cell 1: Import core components
from semanticgis.abstract import Pipeline, RasterStep, VectorStep
from semanticgis.compilers import mermaid, validate, qgis_recipy

from IPython.display import display, Markdown

print("✅ semanticGIS libraries imported successfully!")

p = Pipeline(name="Scaffold Test Workflow")
print(f"Pipeline '{p.name}' created.")

# Step 1: Load a vector layer (Correct)
buildings = p.vector.load(
    path="path/to/some/buildings.geojson", #<-- CHANGE THIS PATH
    label="Building Footprints"
)
print(f"Defined step: {buildings.id} ({p.nodes[buildings.id]['label']})")

# Step 2: Load a raster layer (Correct)
elevation = p.raster.load(
    path="path/to/some/elevation.tif", #<-- CHANGE THIS PATH
    label="Elevation Model"
)
print(f"Defined step: {elevation.id} ({p.nodes[elevation.id]['label']})")

# Step 3: Intentionally try to buffer the raster layer (INCORRECT!)
# The 'buffer' method in our VectorOperations class expects a VectorStep.
# This will test our type-checking validator.
invalid_buffer_step = p.vector.buffer(
    input_vector=elevation, 
    distance=50.0,
    label="Invalid Buffer on Raster"
)
print(f"Defined step: {invalid_buffer_step.id} ({p.nodes[invalid_buffer_step.id]['label']})")
validate.compile(p)