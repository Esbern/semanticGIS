# semanticgis/abstract/pipeline.py
from .vector_ops import VectorOperations
from .raster_ops import RasterOperations

class Pipeline:
    """Represents an abstract workflow of geospatial operations.

    The Pipeline object does not perform any GIS processing itself. Instead, it
    acts as a blueprint, building a directed acyclic graph (DAG) of all the
    data sources and operations defined by the user. This abstract graph can
    then be passed to a 'compiler' to be executed, validated, or visualized.

    Attributes:
        name (str): The user-defined name of the workflow.
        nodes (dict): A dictionary storing the data for each step (node) in the graph.
        edges (list): A list of tuples representing the connections (edges) between nodes.
        vector (VectorOperations): Accessor for all vector-based operations.
        raster (RasterOperations): Accessor for all raster-based operations.
    """
    def __init__(self, name: str = "SemanticGIS Workflow"):
        """Initializes a new, empty pipeline.

        Args:
            name (str, optional): A descriptive name for the workflow.
                Defaults to "SemanticGIS Workflow".
        """
        self.name = name
        self.nodes = {}
        self.edges = []
        self._next_id = 0

        # The accessor objects that provide the hierarchical API
        self.vector = VectorOperations(self)
        self.raster = RasterOperations(self)

    def _get_new_id(self) -> str:
        """Generates a new unique ID for a pipeline node."""
        self._next_id += 1
        return f"node_{self._next_id}"