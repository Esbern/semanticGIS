from typing import TYPE_CHECKING, Optional
from .steps import VectorStep, PipelineStep

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
    
    def declare_input(self, name: str, source: str, description: str = "", persistent: bool = False, crs: str = None):
        """Declares a primary vector data source that is loaded from a file or URL."""
        node_id = self._pipeline._get_new_id()
        self._pipeline.nodes[node_id] = {
            'operation': 'vector.load',
            'output_name': name, # The key is the string 'output_name', the value is the variable 'name'
            'source': source,
            'description': description,
            'persistent': persistent,
            'crs': crs,
            'type': VectorStep,
            'label': f"Load: {name}"
        }
        # This is a declaration, so it returns nothing.

    # This is a new method for declaring derived data
    def declare_derived(self, name: str, description: str = "", persistent: bool = False):
        """Declares a derived vector dataset that will be created by a process."""
        # This method only serves to document intent in the abstract graph for now.
        # It could be used by compilers in the future. We can just have it pass for now.
        pass


    def filter_by_attribute(self, input_vector: VectorStep, attribute: str, operator: str, value, label: str = "") -> VectorStep:
        """Filters features using a simple attribute, operator, and value.

        This provides a simple, guided way to select features, similar to
        the selection tools in desktop GIS. For complex queries involving
        multiple conditions, use `filter_by_sql`.

        Args:
            input_vector (VectorStep): The vector layer to be filtered.
            attribute (str): The name of the attribute column to query.
            operator (str): The comparison operator (e.g., '==', '!=', '>', '<=').
            value: The value to compare against. Strings should be quoted.
            label (str, optional): A custom name for this step.

        Returns:
            VectorStep: A new step representing the filtered layer.
        """
        node_id = self._pipeline._get_new_id()
        self._pipeline.nodes[node_id] = {
            'operation': 'vector.filter_by_attribute',
            'attribute': attribute,
            'operator': operator,
            'value': value,
            'label': label or f"Filter: {attribute} {operator} {value}",
            'type': VectorStep
        }
        self._pipeline.edges.append((input_vector.id, node_id))
        return VectorStep(self._pipeline, node_id)

    def filter_by_sql(self, where_clause: str, input_name: str = None, input_step: PipelineStep = None, output_name: str = None, label: str = "") -> Optional[VectorStep]:
        """Filters features using a SQL 'WHERE' clause.

        This provides a powerful way to perform complex queries using standard
        SQL syntax. The underlying engine is DuckDB.

        Args:
            input_vector (VectorStep): The vector layer to be filtered.
            where_clause (str): The body of a SQL WHERE clause
                (e.g., "SOVEREIGNT = 'Denmark' AND POP_EST > 100000").
            label (str, optional): A custom name for this step.

        Returns:
            VectorStep: A new step representing the filtered layer.
        """
        
        node_id = self._pipeline._get_new_id()
        input_node_id = self._pipeline._get_input_node_id(input_name, input_step) # Using a helper we'll add
        
        self._pipeline.nodes[node_id] = {
            'operation': 'vector.filter_by_sql',
            'input_name': input_name, # <-- THIS LINE WAS MISSING
            'where_clause': where_clause,
            'output_name': output_name,
            'label': label or f"Filter SQL: {where_clause}",
            'type': VectorStep
        }
        self._pipeline.edges.append((input_node_id, node_id))
        
        if not output_name: # If no output_name, it's a scratch step, so return a handle
            return VectorStep(self._pipeline, node_id)
        return None # Otherwise, it's a named milestone, return nothing


    def buffer(self, distance: float, input_name: str = None, input_step: PipelineStep = None, output_name: str = None, label: str = "") -> Optional[VectorStep]:
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
        input_node_id = self._pipeline._get_input_node_id(input_name, input_step) # Using a helper we'll add
        
        self._pipeline.nodes[node_id] = {
            'operation': 'vector.buffer',
            'input_name': input_name, # <-- THIS LINE WAS MISSING
            'distance': distance,
            'output_name': output_name,
            'label': label or f"Buffer ({distance})",
            'type': VectorStep
        }
        self._pipeline.edges.append((input_node_id, node_id))

        if not output_name: # Return a handle for scratch steps
            return VectorStep(self._pipeline, node_id)
        return None