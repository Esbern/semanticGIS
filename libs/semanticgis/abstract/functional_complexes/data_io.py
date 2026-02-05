from __future__ import annotations

from typing import Any, Dict, Optional, Union, cast

from ..steps import SemanticStep
from .base import FunctionalComplex
from ..enums import DataModel, SpatialNature

DataModelLike = Union[DataModel, str]
SpatialNatureLike = Union[SpatialNature, str]


def _coerce_data_model(value: DataModelLike) -> str:
    return value.value if isinstance(value, DataModel) else str(value)


def _coerce_spatial_nature(value: SpatialNatureLike) -> str:
    return value.value if isinstance(value, SpatialNature) else str(value)


class DataIOComplex(FunctionalComplex):
    complex_name = "data_io"

    def declare_input(
        self,
        source: str,
        *,
        output_name: str,
        data_model: DataModelLike = DataModel.VECTOR,
        measurement_scale: str = "ratio",
        nature: SpatialNatureLike = SpatialNature.DISCRETE,
        spatial_nature: Optional[SpatialNatureLike] = None,
        description: str = "",
        persistent: bool = False,
        crs: Optional[str] = None,
        label: Optional[str] = None,
        provenance: Optional[Dict[str, Any]] = None,
        attributes: Optional[Dict[str, Dict[str, Any]]] = None,
    ) -> SemanticStep:
        """Register a semantically described data source inside the pipeline graph.

        Every declared input must expose an ``output_name``. This symbol is how
        downstream operations reference the dataset in a fully declarative style.
        Provide a ``label`` when you would like the human-facing graph text to
        differ from the symbolic name; otherwise the label defaults to
        ``output_name``.
        """

        symbol = self._require_symbol(output_name)
        label = label or symbol
        selected_model = _coerce_data_model(data_model)
        semantic_nature = _coerce_spatial_nature(spatial_nature or nature)
        semantics = {
            "data_model": selected_model,
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
        return cast(
            SemanticStep,
            self._register(
                operation="declare_input",
                label=label,
                input_nodes=[],
                output_semantics=semantics,
                output_name=symbol,
                data_requirements=[],
                provenance=provenance_block,
                parameters=parameters,
            ),
        )


    def declare_named_input(
        self,
        name: str,
        *,
        source: str,
        data_model: DataModelLike = DataModel.VECTOR,
        measurement_scale: str = "ratio",
        nature: SpatialNatureLike = SpatialNature.DISCRETE,
        spatial_nature: Optional[SpatialNatureLike] = None,
        description: str = "",
        persistent: bool = False,
        crs: Optional[str] = None,
        label: Optional[str] = None,
        provenance: Optional[Dict[str, Any]] = None,
        attributes: Optional[Dict[str, Dict[str, Any]]] = None,
    ) -> SemanticStep:
        """Backward-compatible helper that enforces a specific symbolic name."""

        return self.declare_input(
            source=source,
            output_name=name,
            data_model=data_model,
            measurement_scale=measurement_scale,
            nature=nature,
            spatial_nature=spatial_nature,
            description=description,
            persistent=persistent,
            crs=crs,
            label=label or name,
            provenance=provenance,
            attributes=attributes,
        )
    
    def ingest_asset(
        self,
        source: str,
        *,
        name: str,
        data_model: DataModelLike = DataModel.VECTOR,
        measurement_scale: str = "ratio",
        nature: SpatialNatureLike = SpatialNature.DISCRETE,
        label: Optional[str] = None,
        description: str = "",
    ) -> SemanticStep:
        """Describe a file- or service-based asset that will be brought into the workflow at execution time."""
        assigned_name = self._require_symbol(name, parameter="name")
        final_label = label or f"Ingest {assigned_name}"
        selected_model = _coerce_data_model(data_model)
        selected_nature = _coerce_spatial_nature(nature)
        semantics = {
            "data_model": selected_model,
            "measurement_scale": measurement_scale,
            "nature": selected_nature,
        }
        parameters = {
            "description": description,
        }
        provenance = {"source": source}
        return cast(
            SemanticStep,
            self._register(
                operation="ingest_asset",
                label=final_label,
                input_nodes=[],
                output_semantics=semantics,
                output_name=assigned_name,
                data_requirements=[],
                provenance=provenance,
                parameters=parameters,
            ),
        )


__all__ = ["DataIOComplex"]
