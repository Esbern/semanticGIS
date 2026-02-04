from __future__ import annotations

from semanticgis.abstract.pipeline import Pipeline


def compile(pipeline: Pipeline, fetch_results: list | None = None) -> dict:
    """Placeholder compiler that defers execution until the new semantic runtime ships."""

    raise NotImplementedError(
        "The Python executor is temporarily disabled while the functional complexes "
        "are validated through the Mermaid and QGIS compilers."
    )