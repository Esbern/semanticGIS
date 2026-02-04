from __future__ import annotations

from typing import Any, Dict, Optional, cast

from ..steps import VisualisationStep
from .base import FunctionalComplex, SemanticInput


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
        """Declare a visualisation intent for one or more datasets without binding to a rendering engine."""
        input_nodes = self._resolve_inputs(dataset)
        if not input_nodes:
            raise ValueError("visualise.map requires at least one dataset to plot.")
        label = label or "Visualise map"
        parameters = {"style": style or {}, "emphasis": emphasis}
        return cast(
            VisualisationStep,
            self._register(
                operation="map",
                label=label,
                input_nodes=input_nodes,
                output_semantics=None,
                output_name=None,
                data_requirements=[{} for _ in input_nodes],
                parameters=parameters,
                sink=True,
            ),
        )


__all__ = ["VisualiseComplex"]
