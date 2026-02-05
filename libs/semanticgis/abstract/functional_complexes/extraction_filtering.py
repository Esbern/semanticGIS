from __future__ import annotations

from typing import Any, Dict, Optional, cast

from ..steps import SemanticStep
from .base import FunctionalComplex, SemanticInput


class ExtractionFilteringComplex(FunctionalComplex):
    complex_name = "extraction"

    def filter_by_attribute(
        self,
        dataset: SemanticInput,
        *,
        output_name: str,
        attribute: str,
        operator: str,
        value: Any,
        label: Optional[str] = None,
    ) -> SemanticStep:
        """Reduce a dataset to the subset of features that satisfy a single attribute comparison."""
        symbol = self._require_symbol(output_name)
        label = label or symbol
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
        return cast(
            SemanticStep,
            self._register(
                operation="filter_by_attribute",
                label=label,
                input_nodes=input_nodes,
                output_semantics=inherited_semantics,
                output_name=symbol,
                data_requirements=requirements,
                parameters=parameters,
            ),
        )

    def filter_by_sql(
        self,
        dataset: SemanticInput,
        *,
        output_name: str,
        where_clause: str,
        label: Optional[str] = None,
    ) -> SemanticStep:
        """Express a complex predicate as a SQL WHERE clause and bind it to the dataset symbolically."""
        input_nodes = self._resolve_inputs(dataset)
        if not input_nodes:
            raise ValueError("filter_by_sql requires a dataset reference.")
        inherited_semantics = self._inherit_semantics(input_nodes[0])
        symbol = self._require_symbol(output_name)
        label = label or symbol
        parameters = {"where_clause": where_clause}
        requirements = [{"data_model": inherited_semantics.get("data_model", "any")}]
        return cast(
            SemanticStep,
            self._register(
                operation="filter_by_sql",
                label=label,
                input_nodes=input_nodes,
                output_semantics=inherited_semantics,
                output_name=symbol,
                data_requirements=requirements,
                parameters=parameters,
            ),
        )


__all__ = ["ExtractionFilteringComplex"]
