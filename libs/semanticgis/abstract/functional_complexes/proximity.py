from __future__ import annotations

from typing import Dict, Optional, cast

from ..steps import SemanticStep
from .base import FunctionalComplex, SemanticInput


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
        """Define an influence zone around input geometries with a specified radial distance."""
        input_nodes = self._resolve_inputs(dataset)
        if not input_nodes:
            raise ValueError("buffer requires at least one dataset reference.")
        inherited_semantics = self._inherit_semantics(
            input_nodes[0],
            {"measurement_scale": measurement_scale} if measurement_scale else None,
        )
        inherited_semantics["measurement_scale"] = measurement_scale or inherited_semantics.get(
            "measurement_scale",
            "ratio",
        )
        label = label or f"Buffer {distance} {units}"
        parameters = {"distance": distance, "units": units}
        requirements = [{"data_model": "vector"}]
        return cast(
            SemanticStep,
            self._register(
                operation="buffer",
                label=label,
                input_nodes=input_nodes,
                output_semantics=inherited_semantics,
                output_name=output_name,
                data_requirements=requirements,
                parameters=parameters,
            ),
        )


__all__ = ["ProximityComplex"]
