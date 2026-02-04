from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional, Sequence, Union

from .steps import PipelineStep, SemanticStep, VisualisationStep

SemanticInput = Union[str, PipelineStep, Sequence[Union[str, PipelineStep]]]


def _ensure_sequence(candidate: SemanticInput | None) -> List[Union[str, PipelineStep]]:
    if candidate is None:
        return []
    if isinstance(candidate, (list, tuple, set)):
        return list(candidate)
    return [candidate]


class FunctionalComplex:
    """Shared utilities for every functional complex accessor."""

    complex_name: str = "undefined"

    def __init__(self, pipeline):
        self._pipeline = pipeline

    def _resolve_inputs(self, *inputs: SemanticInput) -> List[str]:
        resolved: List[str] = []
        for input_group in inputs:
            resolved.extend(self._pipeline._resolve_inputs(*_ensure_sequence(input_group)))
        return resolved

    def _inherit_semantics(self, node_id: str, overrides: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self._pipeline._inherit_semantics(node_id, overrides or {})

    def _register(self, *, operation: str, label: str, input_nodes: List[str], output_semantics: Optional[Dict[str, Any]] = None, output_name: Optional[str] = None, data_requirements: Optional[List[Dict[str, Any]]] = None, provenance: Optional[Dict[str, Any]] = None, parameters: Optional[Dict[str, Any]] = None, sink: bool = False) -> PipelineStep:
        return self._pipeline._register_node(
            complex_name=self.complex_name,
            operation=operation,
            label=label,
            input_nodes=input_nodes,
            output_semantics=output_semantics,
            output_name=output_name,
            data_requirements=data_requirements,
            provenance=provenance,
            parameters=parameters,
            sink=sink,
        )


class DataIOComplex(FunctionalComplex):
    complex_name = "data_io"

    def declare_input(
        self,
        name: str,
        source: str,
        *,
        data_model: str = "vector",
        measurement_scale: str = "ratio",
        nature: str = "discrete",
        spatial_nature: Optional[str] = None,
        description: str = "",
        persistent: bool = False,
        crs: Optional[str] = None,
        label: Optional[str] = None,
        provenance: Optional[Dict[str, Any]] = None,
        attributes: Optional[Dict[str, Dict[str, Any]]] = None,
    ) -> SemanticStep:
        """Summary:
            Register a named, semantically described data source inside the pipeline graph without touching the actual bytes.
        Use Case:
            Declare authoritative river centrelines from a data portal so subsequent steps can reference them by the concept name `riparian_network`.
        GIS Concept:
            Separating provenance (who/what/when) from processing intentions enforces reproducibility and allows the DAG to be serialized into recipes and compilers before any data access happens.
        Args:
            name: Registry key for downstream references.
            source: Human-readable or URL pointer describing where the data originates.
            data_model: Conceptual storage expectation (`vector`, `raster`, `table`, `mesh`, or `any`).
            measurement_scale: Semantic measurement scale (nominal, ordinal, interval, ratio).
            nature: Whether the phenomenon is `discrete` (objects) or `continuous` (fields).
            spatial_nature: Optional alias for `nature` to align with pedagogy (e.g., discrete/continuous, object/field).
            description: Free-form narrative describing the asset.
            persistent: Flag that the asset already exists in durable storage.
            crs: Optional reference system identifier to capture alignment constraints.
            label: Optional override for the node label in diagrams.
            provenance: Additional structured metadata (e.g., citation, license).
            attributes: Optional dictionary describing attribute schema metadata (scale, description, units, etc.).
        Returns:
            SemanticStep: Handle to the declared concept so it can be referenced programmatically.
        Example:
            >>> import semanticgis as sg
            >>> pl = sg.Pipeline(name="Riparian Safety Study")
            >>> rivers = pl.io.declare_input(
            ...     name="riparian_network",
            ...     source="https://data.example/org/rivers.gpkg",
            ...     data_model="vector",
            ...     nature="discrete",
            ...     measurement_scale="ratio",
            ... )
        See Also:
            https://semanticgis.org/Geospatial-Operations/Data%20IO/Declare%20Input
        """
        label = label or f"Declare {name}"
        semantic_nature = spatial_nature or nature
        semantics = {
            "data_model": data_model,
            "measurement_scale": measurement_scale,
            "nature": semantic_nature,
        }
        parameters = {
            "persistent": persistent,
            "crs": crs,
            "description": description,
            "attributes": attributes or {},
        }
        provenance_block = provenance or {}
        provenance_block.setdefault("source", source)
        return self._register(
            operation="declare_input",
            label=label,
            input_nodes=[],
            output_semantics=semantics,
            output_name=name,
            data_requirements=[],
            provenance=provenance_block,
            parameters=parameters,
        )

    def ingest_asset(
        self,
        source: str,
        *,
        name: Optional[str] = None,
        data_model: str = "vector",
        measurement_scale: str = "ratio",
        nature: str = "discrete",
        label: Optional[str] = None,
        description: str = "",
    ) -> SemanticStep:
        """Summary:
            Describe a file- or service-based asset that will be brought into the workflow at execution time using just-in-time semantics.
        Use Case:
            Pull a cloud-hosted raster tile service for vegetation indices without downloading it upfront, yet still reference it inside the DAG.
        GIS Concept:
            Separating the symbolic reference (`source`) from the execution engine allows different compilers (Mermaid, QGIS) to reuse the same intent while late-binding to the appropriate loader.
        Args:
            source: Path, URL, or logical locator for the asset.
            name: Optional symbolic name other nodes can reference; autogenerated if omitted.
            data_model: Expected representation (vector, raster, table, mesh, any).
            measurement_scale: Semantic measurement scale for operations that care about units.
            nature: Discrete features or continuous fields.
            label: Optional caption in documentation outputs.
            description: Additional context for provenance blocks.
        Returns:
            SemanticStep: Handle to the ingested asset concept.
        Example:
            >>> pl = sg.Pipeline()
            >>> dem = pl.io.ingest_asset(
            ...     source="s3://elevation/eudem.vrt",
            ...     data_model="raster",
            ...     measurement_scale="interval",
            ...     nature="continuous"
            ... )
        See Also:
            https://semanticgis.org/Geospatial-Operations/Data%20IO/Ingest
        """
        assigned_name = name or f"asset_{self._pipeline._next_id + 1}"
        final_label = label or f"Ingest {assigned_name}"
        semantics = {
            "data_model": data_model,
            "measurement_scale": measurement_scale,
            "nature": nature,
        }
        parameters = {
            "description": description,
        }
        provenance = {"source": source}
        return self._register(
            operation="ingest_asset",
            label=final_label,
            input_nodes=[],
            output_semantics=semantics,
            output_name=assigned_name,
            data_requirements=[],
            provenance=provenance,
            parameters=parameters,
        )


class ReferencingNormalizationComplex(FunctionalComplex):
    complex_name = "referencing"


class ExtractionFilteringComplex(FunctionalComplex):
    complex_name = "extraction"

    def filter_by_attribute(
        self,
        dataset: SemanticInput,
        *,
        attribute: str,
        operator: str,
        value: Any,
        label: Optional[str] = None,
        output_name: Optional[str] = None,
    ) -> SemanticStep:
        """Summary:
            Reduce a dataset to the subset of features that satisfy a single attribute comparison.
        Use Case:
            Isolate schools where `ENROLLMENT > 500` before running accessibility modelling.
        GIS Concept:
            Attribute predicates change the statistical population; storing the intent in the DAG clarifies why downstream aggregations see fewer features and enforces awareness of measurement scales for the compared column.
        Args:
            dataset: Named concept or SemanticStep referencing the source features.
            attribute: Attribute/field name to evaluate.
            operator: Comparison operator string (`==`, `!=`, `>`, `>=`, `<`, `<=`).
            value: Literal value used for comparison; compilers will serialize the literal appropriately.
            label: Optional override used in human-facing outputs.
            output_name: Optional named milestone if the result should be referenced symbolically later.
        Returns:
            SemanticStep: Handle describing the filtered dataset.
        Example:
            >>> wetlands = pl.io.declare_input(name="wetlands", source="/data/wetlands.gpkg")
            >>> protected = pl.extraction.filter_by_attribute(
            ...     wetlands,
            ...     attribute="STATUS",
            ...     operator="==",
            ...     value="protected"
            ... )
        See Also:
            https://semanticgis.org/Geospatial-Operations/Extraction%20%26%20Filtering/Filter%20By%20Attribute
        """
        label = label or f"Attribute filter: {attribute} {operator} {value}"
        input_nodes = self._resolve_inputs(dataset)
        if not input_nodes:
            raise ValueError("At least one dataset must be supplied to filter_by_attribute.")
        inherited_semantics = self._inherit_semantics(input_nodes[0])
        requirements = [{"data_model": inherited_semantics.get("data_model", "vector")}]
        parameters = {
            "attribute": attribute,
            "operator": operator,
            "value": value,
        }
        return self._register(
            operation="filter_by_attribute",
            label=label,
            input_nodes=input_nodes,
            output_semantics=inherited_semantics,
            output_name=output_name,
            data_requirements=requirements,
            parameters=parameters,
        )

    def filter_by_sql(
        self,
        dataset: SemanticInput,
        *,
        where_clause: str,
        label: Optional[str] = None,
        output_name: Optional[str] = None,
    ) -> SemanticStep:
        """Summary:
            Express a complex predicate as a SQL WHERE clause and bind it to the dataset symbolically.
        Use Case:
            Select parcels where zoning is residential, slope < 8%, and parcel area exceeds 600 square meters before suitability analysis.
        GIS Concept:
            Late-binding SQL lets the executor choose DuckDB, PostGIS, or another engine while the abstract graph still captures the logical predicate for provenance.
        Args:
            dataset: Step handle or registered name for the dataset to filter.
            where_clause: SQL expression without the `WHERE` keyword.
            label: Optional override caption.
            output_name: Optional symbolic name for downstream references.
        Returns:
            SemanticStep: New step referencing the filtered subset.
        Example:
            >>> cities = pl.io.ingest_asset("/data/cities.parquet", name="cities")
            >>> nordic = pl.extraction.filter_by_sql(
            ...     dataset="cities",
            ...     where_clause="Region = 'Nordic' AND Pop > 500000"
            ... )
        See Also:
            https://semanticgis.org/Geospatial-Operations/Extraction%20%26%20Filtering/Filter%20By%20SQL
        """
        input_nodes = self._resolve_inputs(dataset)
        if not input_nodes:
            raise ValueError("filter_by_sql requires a dataset reference.")
        inherited_semantics = self._inherit_semantics(input_nodes[0])
        label = label or f"SQL filter: {where_clause}"
        parameters = {"where_clause": where_clause}
        requirements = [{"data_model": inherited_semantics.get("data_model", "any")}]
        return self._register(
            operation="filter_by_sql",
            label=label,
            input_nodes=input_nodes,
            output_semantics=inherited_semantics,
            output_name=output_name,
            data_requirements=requirements,
            parameters=parameters,
        )


class AggregationSummarizationComplex(FunctionalComplex):
    complex_name = "aggregation"


class FuseComplex(FunctionalComplex):
    complex_name = "fuse"


class GeometryGenerationComplex(FunctionalComplex):
    complex_name = "geometry_generation"


class MorphometryComplex(FunctionalComplex):
    complex_name = "morphometry"


class ProximityComplex(FunctionalComplex):
    complex_name = "proximity"

    def buffer(
        self,
        dataset: SemanticInput,
        *,
        distance: float,
        units: str = "meters",
        label: Optional[str] = None,
        output_name: Optional[str] = None,
        measurement_scale: Optional[str] = None,
    ) -> SemanticStep:
        """Summary:
            Define an influence zone around input geometries with a specified radial distance.
        Use Case:
            Delineate 300-meter safety envelopes around high-voltage transmission lines before evaluating compatible land uses.
        GIS Concept:
            Buffering demands a projected CRS with meaningful linear units and assumes vector geometries; this method flags that requirement so compilers can halt or warn when fed rasters.
        Args:
            dataset: Feature dataset reference (handle or name).
            distance: Numeric distance expressed in the `units` argument.
            units: Descriptive units string stored for compilers (meters, kilometers, feet, degrees).
            label: Optional caption for diagram outputs.
            output_name: Optional symbolic name for the buffered result.
            measurement_scale: Override for output measurement scale if, for example, buffering a categorical footprint but needing ratio distances.
        Returns:
            SemanticStep: Handle referencing the buffered features.
        Example:
            >>> lines = pl.io.declare_input(name="transmission", source="/data/lines.gpkg")
            >>> safety = pl.proximity.buffer(lines, distance=300, units="meters", output_name="safety_zone")
        See Also:
            https://semanticgis.org/Geospatial-Operations/Proximity/Buffer
        """
        input_nodes = self._resolve_inputs(dataset)
        if not input_nodes:
            raise ValueError("buffer requires at least one dataset reference.")
        inherited_semantics = self._inherit_semantics(input_nodes[0], {"measurement_scale": measurement_scale} if measurement_scale else None)
        inherited_semantics["measurement_scale"] = measurement_scale or inherited_semantics.get("measurement_scale", "ratio")
        label = label or f"Buffer {distance} {units}"
        parameters = {"distance": distance, "units": units}
        requirements = [{"data_model": "vector"}]
        return self._register(
            operation="buffer",
            label=label,
            input_nodes=input_nodes,
            output_semantics=inherited_semantics,
            output_name=output_name,
            data_requirements=requirements,
            parameters=parameters,
        )


class VisualiseComplex(FunctionalComplex):
    complex_name = "visualise"

    def map(
        self,
        dataset: SemanticInput,
        *,
        style: Optional[Dict[str, Any]] = None,
        label: Optional[str] = None,
        emphasis: Optional[str] = None,
    ) -> VisualisationStep:
        """Summary:
            Declare a visualisation intent for one or more datasets without binding to a rendering engine.
        Use Case:
            Produce a flowchart node that signals the pipeline culminates in a choropleth map for stakeholders.
        GIS Concept:
            Visualisation sinks consume data and emit insight; recording styling hints in the DAG allows compilers to export QGIS layout recipes or Mermaid storyboards.
        Args:
            dataset: Dataset handle or registered name to visualise.
            style: Optional dictionary with symbolic styling hints.
            label: Optional override caption.
            emphasis: Optional textual cue for the story being told (e.g., "Equity gap").
        Returns:
            VisualisationStep: Sink node handle for completeness checks.
        Example:
            >>> suitability = pl.proximity.buffer("schools", distance=500)
            >>> pl.visualise.map(suitability, emphasis="Safe schools buffer")
        See Also:
            https://semanticgis.org/Geospatial-Operations/Visualise/Map
        """
        input_nodes = self._resolve_inputs(dataset)
        if not input_nodes:
            raise ValueError("visualise.map requires at least one dataset to plot.")
        label = label or "Visualise map"
        parameters = {"style": style or {}, "emphasis": emphasis}
        return self._register(
            operation="map",
            label=label,
            input_nodes=input_nodes,
            output_semantics=None,
            output_name=None,
            data_requirements=[{} for _ in input_nodes],
            parameters=parameters,
            sink=True,
        )