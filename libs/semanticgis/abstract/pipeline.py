# semanticgis/abstract/pipeline.py
from __future__ import annotations

import re

from typing import Any, Dict, List, Optional, Sequence, Union

from .steps import PipelineStep, SemanticStep, VisualisationStep
from .functional_complexes import (
    AggregationSummarizationComplex,
    DataIOComplex,
    ExtractionFilteringComplex,
    FuseComplex,
    GeometryGenerationComplex,
    MorphometryComplex,
    ProximityComplex,
    ReferencingNormalizationComplex,
    VisualiseComplex,
)


def _normalise_symbol(name: str) -> Optional[str]:
    """Derive a pipeline-safe symbol from arbitrary user-facing text."""

    cleaned = re.sub(r"[^0-9A-Za-z]+", "_", name).strip("_")
    return cleaned or None

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
        self.nodes: Dict[str, Dict[str, Any]] = {}
        self.edges: List[tuple[str, str]] = []
        self._next_id = 0

        self.io = DataIOComplex(self)
        self.data_io = self.io  # alias for validator lookups
        self.referencing = ReferencingNormalizationComplex(self)
        self.referencing_normalization = self.referencing
        self.extraction = ExtractionFilteringComplex(self)
        self.aggregation = AggregationSummarizationComplex(self)
        self.fuse = FuseComplex(self)
        self.geometry = GeometryGenerationComplex(self)
        self.geometry_generation = self.geometry
        self.morphometry = MorphometryComplex(self)
        self.proximity = ProximityComplex(self)
        self.visualise = VisualiseComplex(self)

    def _get_new_id(self) -> str:
        """Generates a new unique ID for a pipeline node."""
        self._next_id += 1
        return f"node_{self._next_id}"
    
    def _find_node_id_by_name(self, name: str) -> str:
        """Find the node ID backing a symbolic name or human-friendly label."""

        candidate = (name or "").strip()
        if not candidate:
            raise ValueError("Input references must be non-empty strings.")

        sanitized_candidate = _normalise_symbol(candidate)

        for node_id, node_data in self.nodes.items():
            output_name = node_data.get('output_name')
            if output_name == candidate:
                return node_id
            if sanitized_candidate and output_name == sanitized_candidate:
                return node_id

        for node_id, node_data in self.nodes.items():
            if node_data.get('name') == candidate and 'data_input' in node_data.get('operation', ''):
                return node_id

        for node_id, node_data in self.nodes.items():
            if node_data.get('label') == candidate:
                return node_id

        raise ValueError(f"No step in the pipeline is configured to output the data named '{name}'.")
    
    def _resolve_inputs(self, *inputs: Union[str, PipelineStep]) -> List[str]:
        """Normalize a collection of names or step handles into node IDs."""
        resolved: List[str] = []
        for candidate in inputs:
            if candidate is None:
                continue
            if isinstance(candidate, PipelineStep):
                resolved.append(candidate.id)
            elif isinstance(candidate, str):
                resolved.append(self._find_node_id_by_name(candidate))
            elif isinstance(candidate, Sequence):
                resolved.extend(self._resolve_inputs(*candidate))
            else:
                raise TypeError(f"Unsupported input reference type: {type(candidate)}")
        return resolved

    def _inherit_semantics(self, node_id: str, overrides: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Copy the semantic signature of a node and optionally update selected keys."""
        base = dict(self.nodes.get(node_id, {}).get('output_semantics') or {})
        if overrides:
            for key, value in overrides.items():
                if value is not None:
                    base[key] = value
        return base

    def _register_node(
        self,
        *,
        complex_name: str,
        operation: str,
        label: str,
        input_nodes: Optional[List[str]] = None,
        output_semantics: Optional[Dict[str, Any]] = None,
        output_name: Optional[str] = None,
        data_requirements: Optional[List[Dict[str, Any]]] = None,
        provenance: Optional[Dict[str, Any]] = None,
        parameters: Optional[Dict[str, Any]] = None,
        sink: bool = False,
    ) -> PipelineStep:
        node_id = None
        if output_name:
            for existing_id, node_data in self.nodes.items():
                if node_data.get('output_name') == output_name:
                    node_id = existing_id
                    break

        reuse_existing = node_id is not None
        if not reuse_existing:
            node_id = self._get_new_id()

        step_class = VisualisationStep if sink else SemanticStep

        node_payload: Dict[str, Any] = {
            'operation': f"{complex_name}.{operation}",
            'complex': complex_name,
            'label': label,
            'output_name': output_name,
            'output_semantics': output_semantics,
            'data_requirements': data_requirements or [],
            'provenance': provenance or {},
            'parameters': parameters or {},
            'type': step_class,
            'sink': sink,
        }
        self.nodes[node_id] = node_payload

        if reuse_existing:
            self.edges = [edge for edge in self.edges if edge[1] != node_id]

        for input_id in input_nodes or []:
            self.edges.append((input_id, node_id))

        return step_class(self, node_id, output_semantics)
