class PipelineStep:
    """The base class for any step in a semanticGIS pipeline."""
    def __init__(self, pipeline_ref, node_id):
        self.pipeline = pipeline_ref
        self.id = node_id

class VectorStep(PipelineStep):
    """A step that represents a vector dataset."""
    pass

class RasterStep(PipelineStep):
    """A step that represents a raster dataset."""
    pass