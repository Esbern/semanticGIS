from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence, Union

from ..steps import PipelineStep

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

    def _require_symbol(self, value: Optional[str], *, parameter: str = "output_name") -> str:
        """Ensure a human-specified symbol exists for string-based referencing."""

        if value is None:
            raise ValueError(f"{self.complex_name}.{parameter} must be provided.")
        if not isinstance(value, str):
            raise TypeError(f"{self.complex_name}.{parameter} must be a string, not {type(value)!r}.")
        candidate = value.strip()
        if not candidate:
            raise ValueError(f"{self.complex_name}.{parameter} cannot be empty or whitespace.")
        return candidate

    def _register(
        self,
        *,
        operation: str,
        label: str,
        input_nodes: List[str],
        output_semantics: Optional[Dict[str, Any]] = None,
        output_name: Optional[str] = None,
        data_requirements: Optional[List[Dict[str, Any]]] = None,
        provenance: Optional[Dict[str, Any]] = None,
        parameters: Optional[Dict[str, Any]] = None,
        sink: bool = False,
    ) -> PipelineStep:
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


__all__ = ["FunctionalComplex", "SemanticInput"]
