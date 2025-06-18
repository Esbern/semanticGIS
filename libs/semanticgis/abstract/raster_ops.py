from typing import TYPE_CHECKING
from .steps import RasterStep

# This avoids a circular import error while still allowing type hints
if TYPE_CHECKING:
    from .pipeline import Pipeline

class RasterOperations:
    """A container for all raster-based pipeline operations."""
    def __init__(self, pipeline: "Pipeline"):
        self._pipeline = pipeline

    def load(self, path: str, label: str = "") -> RasterStep:
        """Adds a step to load a raster file from a path."""
        node_id = self._pipeline._get_new_id()
        self._pipeline.nodes[node_id] = {
            'operation': 'raster.load',
            'path': path,
            'label': label or f"Load: {path.split('/')[-1]}",
            'type': RasterStep  # This is crucial for our validator
        }
        return RasterStep(self._pipeline, node_id)