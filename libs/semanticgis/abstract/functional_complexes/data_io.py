from __future__ import annotations

from typing import Any, Dict, Optional, cast

from ..steps import SemanticStep
from .base import FunctionalComplex


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
        """Register a named, semantically described data source inside the pipeline graph."""
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
        return cast(
            SemanticStep,
            self._register(
                operation="declare_input",
                label=label,
                input_nodes=[],
                output_semantics=semantics,
                output_name=name,
                data_requirements=[],
                provenance=provenance_block,
                parameters=parameters,
            ),
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
        """Describe a file- or service-based asset that will be brought into the workflow at execution time."""
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
