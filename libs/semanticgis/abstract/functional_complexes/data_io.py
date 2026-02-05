from __future__ import annotations

from typing import Any, Dict, Optional, List, Union, cast

from ..steps import SemanticStep
from .base import FunctionalComplex, SemanticInput
from ..enums import DataModel, SpatialNature, MeasurementScale, DataFormat

DataModelLike = Union[DataModel, str]
SpatialNatureLike = Union[SpatialNature, str]
MeasurementScaleLike = Union[MeasurementScale, str]
DataFormatLike = Union[DataFormat, str]


def _coerce_data_model(value: DataModelLike) -> str:
    return value.value if isinstance(value, DataModel) else str(value)


def _coerce_spatial_nature(value: SpatialNatureLike) -> str:
    return value.value if isinstance(value, SpatialNature) else str(value)


def _coerce_measurement_scale(value: MeasurementScaleLike) -> str:
    return value.value if isinstance(value, MeasurementScale) else str(value)


def _coerce_data_format(value: DataFormatLike) -> str:
    return value.value if isinstance(value, DataFormat) else str(value)


def _normalise_attributes(attributes: Optional[Dict[str, Dict[str, Any]]]) -> Dict[str, Dict[str, Any]]:
    if not attributes:
        return {}
    normalised: Dict[str, Dict[str, Any]] = {}
    for attr_name, metadata in attributes.items():
        if not isinstance(metadata, dict):
            raise TypeError(f"Attribute metadata for '{attr_name}' must be a mapping, not {type(metadata)!r}.")
        if "scale" not in metadata:
            raise ValueError(f"Attribute '{attr_name}' must declare a 'scale'.")
        scale_value = _coerce_measurement_scale(metadata["scale"])
        description = metadata.get("description", "")
        normalised[attr_name] = {"scale": scale_value, "description": description}
    return normalised


def _infer_dataset_scale(attributes: Dict[str, Dict[str, Any]]) -> Optional[str]:
    if not attributes:
        return None
    unique_scales = {meta["scale"] for meta in attributes.values() if meta.get("scale")}
    if not unique_scales:
        return None
    if len(unique_scales) == 1:
        return unique_scales.pop()
    return "mixed"


class DataIOComplex(FunctionalComplex):
    complex_name = "data_io"

    def declare_input(
        self,
        source: str,
        *,
        output_name: str,
        data_model: DataModelLike = DataModel.VECTOR,
        spatial_nature: SpatialNatureLike = SpatialNature.DISCRETE,
        description: str = "",
        crs: Optional[str] = None,
        label: Optional[str] = None,
        attributes: Optional[Dict[str, Dict[str, Any]]] = None,
        pre_filter: Optional[str] = None,
        spatial_filter: Optional[SemanticInput] = None,
        data_format: DataFormatLike = DataFormat.TBD,
    ) -> SemanticStep:
        """This operation establishes the "Scientific Contract" for a dataset before any analysis begins.
        Key Concepts:
            output_name: The unique symbolic name (registry key) used to reference this data in all downstream steps.
            Semantic Gating: Use pre_filter (attribute logic) and spatial_filter (geographic bounds) to define the specific subset of the world you are analyzing.
            Attribute Metadata: Defining the scale (Nominal, Ratio, etc.) of your columns enables the pipeline to validate the scientific logic of your calculations.
        Optionally specify ``pre_filter`` (a SQL WHERE clause applied before the
        dataset is registered) and/or ``spatial_filter`` (a polygon dataset that
        constrains the declared input).
        
        Full Specification: https://semanticgis.org/Geospatial-Operations/Data-IO/declare_input
       
        """

        symbol = self._require_symbol(output_name)
        label = label or symbol
        filter_nodes: List[str] = self._resolve_inputs(spatial_filter) if spatial_filter is not None else []
        selected_model = _coerce_data_model(data_model)
        semantic_nature = _coerce_spatial_nature(spatial_nature)
        attribute_metadata = _normalise_attributes(attributes)
        inferred_scale = _infer_dataset_scale(attribute_metadata)
        selected_format = _coerce_data_format(data_format)
        semantics = {
            "data_model": selected_model,
            "nature": semantic_nature,
        }
        if inferred_scale:
            semantics["measurement_scale"] = inferred_scale
        parameters = {
            "crs": crs,
            "description": description,
            "attributes": attribute_metadata,
            "format": selected_format,
            "source": source,
        }
        if pre_filter:
            parameters["pre_filter"] = pre_filter
        if spatial_filter is not None:
            if isinstance(spatial_filter, SemanticStep):
                parameters["spatial_filter"] = spatial_filter.id
            else:
                parameters["spatial_filter"] = str(spatial_filter)
        provenance_block = {"source": source}
        return cast(
            SemanticStep,
            self._register(
                operation="declare_input",
                label=label,
                input_nodes=filter_nodes,
                output_semantics=semantics,
                output_name=symbol,
                data_requirements=[],
                provenance=provenance_block,
                parameters=parameters,
            ),
        )


__all__ = ["DataIOComplex"]
