from __future__ import annotations

from typing import Any, Dict, Optional


class PipelineStep:
    """Base handle that references a node inside the semanticGIS pipeline graph."""

    def __init__(self, pipeline_ref, node_id: str, semantic_signature: Optional[Dict[str, Any]] = None):
        self.pipeline = pipeline_ref
        self.id = node_id
        self.semantic_signature = semantic_signature or {}

    def describe(self) -> Dict[str, Any]:
        """Return the raw node metadata stored in the pipeline graph."""
        return self.pipeline.nodes.get(self.id, {})


class SemanticStep(PipelineStep):
    """Represents a semantically described dataset (independent of storage model)."""


class VisualisationStep(PipelineStep):
    """Represents a sink step that emits insight instead of a new dataset."""