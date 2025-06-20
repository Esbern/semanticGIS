# semanticgis/abstract/pipeline.py
from .vector_ops import VectorOperations
from .raster_ops import RasterOperations
from .steps import PipelineStep 

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
    
    def _find_node_id_by_name(self, name: str) -> str:
        """Finds the ID of a node that created a named data concept."""
        for node_id, node_data in self.nodes.items():
            if node_data.get('output_name') == name:
                return node_id
        # Also check the original data_input nodes
        for node_id, node_data in self.nodes.items():
            if node_data.get('name') == name and 'data_input' in node_data.get('operation', ''):
                return node_id
        raise ValueError(f"No step in the pipeline is configured to output the data named '{name}'.")
    
    def _get_input_node_id(self, input_name: str = None, input_step: PipelineStep = None) -> str:
        """
        Finds the node ID for an input, whether it's given as a name or a step handle.
        """
        if input_name and input_step:
            raise ValueError("Provide either 'input_name' or 'input_step', not both.")
        
        if input_name:
            # Find the node that has this name as its output
            for node_id, node_data in self.nodes.items():
                if node_data.get('output_name') == input_name:
                    return node_id
            raise ValueError(f"No step in the pipeline is configured to output the data named '{input_name}'.")
        
        if input_step:
            # The handle object already knows its own node ID
            return input_step.id
            
        raise ValueError("No input was provided. You must specify either 'input_name' or 'input_step'.")
