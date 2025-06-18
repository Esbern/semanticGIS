from typing import TYPE_CHECKING
from .steps import VectorStep

# Avoids circular import issue with Pipeline
if TYPE_CHECKING:
    from .pipeline import Pipeline

class VectorOperations:
    def __init__(self, pipeline: "Pipeline"):
        self._pipeline = pipeline

    def load(self, path: str, label: str = "") -> VectorStep:
        """Adds a step to load a vector file."""
        node_id = self._pipeline._get_new_id()
        self._pipeline.nodes[node_id] = {
            'operation': 'vector.load',
            'path': path,
            'label': label or f"Load: {path.split('/')[-1]}",
            'type': VectorStep
        }
        return VectorStep(self._pipeline, node_id)

    def buffer(self, input_vector: VectorStep, distance: float, label: str = "") -> VectorStep:
        """Creates a zone of a specified distance around a set of features.

        This tool is used to answer questions of proximity. For example, you could
        use it to find all areas within 500 meters of a river to identify
        a riparian protection zone, or to determine which properties fall
        within 1km of a proposed new road.

        GIS Concept:
            A buffer operation creates a new polygon layer. The distance is
            applied in the units of the input layer's Coordinate Reference
            System (CRS), such as meters or decimal degrees. It's crucial
            to ensure your data is in a suitable projected CRS before
            running a buffer if you are using distance units like meters.

        Args:
            input_vector (VectorStep): The layer you want to create buffers
                for, typically from a `p.vector.load()` step.
            distance (float): The distance for the buffer. This value should
                be in the same units as the layer's CRS (e.g., meters).
            label (str, optional): A custom, human-readable name for this step
                in the workflow diagram. If not provided, a default will be
                generated.

        Returns:
            VectorStep: A new step in the pipeline representing the buffered
            polygons.

        Example:
            >>> p = Pipeline(name="River Protection Zone Analysis")
            >>> # Load a layer representing rivers
            >>> rivers = p.vector.load(
            ...     "data/rivers.shp", label="Major Rivers"
            ... )
            >>> # Create a 500-meter protection zone around the rivers
            >>> protection_zone = p.vector.buffer(
            ...     rivers, distance=500.0, label="500m Riparian Zone"
            ... )

        See Also:
            `Detailed Web Documentation <https://semanticgis.org/docs/vector/buffer>`_
        """
        node_id = self._pipeline._get_new_id()
        self._pipeline.nodes[node_id] = {
            'operation': 'vector.buffer',
            'distance': distance,
            'label': label or f"Buffer ({distance}m)",
            'type': VectorStep
        }
        self._pipeline.edges.append((input_vector.id, node_id))
        return VectorStep(self._pipeline, node_id)