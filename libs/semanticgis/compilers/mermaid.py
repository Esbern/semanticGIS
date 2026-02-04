from __future__ import annotations

import base64
from typing import Dict, List, Optional, Tuple, Union
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from semanticgis.abstract.pipeline import Pipeline


def compile(
    pipeline: Pipeline,
    *,
    type: str = "md",
    dpi: int = 150,
    figsize: Optional[Tuple[float, float]] = None,
    return_bytes: bool = False,
) -> Union[str, bytes]:
    """Render the pipeline either as Markdown code block or inline PNG.

    Args:
        pipeline: Pipeline to render.
        type: "md"/"markdown" for a fenced Mermaid block (default) or "graph"/"image" to
            embed a PNG using the mermaid.ink render service.
        dpi: Virtual DPI used to estimate pixel width when `type` renders an image.
        figsize: Optional (width, height) tuple in inches to influence the rendered image width.
    """

    body = _build_mermaid_body(pipeline)
    kind = type.lower()
    if kind in {"md", "markdown", "code"}:
        return f"```mermaid\n{body}\n```"

    if kind in {"graph", "image", "img"}:
        try:
            image_bytes = _fetch_mermaid_png(body)
        except RuntimeError as exc:
            if return_bytes:
                raise
            fallback = f"```mermaid\n{body}\n```"
            return f"{fallback}\n\n<!-- Mermaid render failed: {exc} -->"

        if return_bytes:
            return image_bytes

        width_attr = ""
        if figsize:
            width_px = max(int(figsize[0] * dpi), 1)
            width_attr = f' width="{width_px}"'
        encoded = base64.b64encode(image_bytes).decode("ascii")
        return f'<img src="data:image/png;base64,{encoded}" alt="Mermaid graph"{width_attr}/>'

    raise ValueError("type must be 'md' or 'graph'")


def _build_mermaid_body(pipeline: Pipeline) -> str:
    lines: List[str] = []
    dataset_nodes: List[Tuple[str, str]] = []
    process_nodes: List[Tuple[str, str]] = []
    dataset_lookup: Dict[str, str] = {}
    process_lookup: Dict[str, str] = {}

    lines.append("flowchart TD")
    lines.append("")

    for node_id, node_data in pipeline.nodes.items():
        name = node_data.get('output_name') or node_data.get('name')
        op_label = node_data.get('label', node_id)
        complex_name = node_data.get('complex', 'workflow')
        semantic_signature = node_data.get('output_semantics') or {}
        semantics_bits = [
            semantic_signature.get('data_model'),
            semantic_signature.get('measurement_scale'),
            semantic_signature.get('nature'),
        ]
        semantics_bits = [bit for bit in semantics_bits if bit]

        metadata_chunks = []
        if semantics_bits:
            metadata_chunks.append(" / ".join(semantics_bits))

        dataset_label = op_label
        if name:
            dataset_label = f"<b>{name}</b><br/>{op_label}"
        if metadata_chunks:
            dataset_label += "<br/><small>" + " | ".join(metadata_chunks) + "</small>"
        dataset_label = dataset_label.replace('"', "'")

        operation_fqn = node_data.get('operation', complex_name)
        process_label = f"{op_label}<br/><small>{operation_fqn}</small>".replace('"', "'")

        has_semantic_output = bool(node_data.get('output_semantics') or node_data.get('output_name'))
        needs_process_node = (complex_name != 'data_io') or not has_semantic_output

        if has_semantic_output:
            dataset_id = f"{node_id}_data"
            dataset_lookup[node_id] = dataset_id
            dataset_nodes.append((dataset_id, dataset_label))

        if needs_process_node:
            process_id = f"{node_id}_proc"
            process_lookup[node_id] = process_id
            process_nodes.append((process_id, process_label))

    lines.append("    %% -- Nodes --")
    for dataset_id, label in dataset_nodes:
        lines.append(f"    {dataset_id}(({label}))")
    for process_id, label in process_nodes:
        lines.append(f"    {process_id}[{label}]")
    lines.append("")
    lines.append("    %% -- Connections --")

    for from_node, to_node in pipeline.edges:
        from_dataset = dataset_lookup.get(from_node)
        to_process = process_lookup.get(to_node)
        to_dataset = dataset_lookup.get(to_node)
        if from_dataset and to_process:
            lines.append(f"    {from_dataset} --> {to_process}")
        elif from_dataset and to_dataset:
            lines.append(f"    {from_dataset} --> {to_dataset}")

    for node_id in pipeline.nodes:
        proc_id = process_lookup.get(node_id)
        data_id = dataset_lookup.get(node_id)
        if proc_id and data_id:
            lines.append(f"    {proc_id} --> {data_id}")

    return "\n".join(lines)


def _fetch_mermaid_png(mermaid_source: str) -> bytes:
    encoded = base64.urlsafe_b64encode(mermaid_source.encode("utf-8")).decode("ascii")
    url = f"https://mermaid.ink/img/{encoded}"
    try:
        request = Request(url, headers={"User-Agent": "semanticgis-mermaid/1.0"})
        with urlopen(request) as response:  # type: ignore[arg-type]
            if response.status != 200:
                raise RuntimeError(f"HTTP {response.status}")
            return response.read()
    except (HTTPError, URLError) as exc:  # pragma: no cover - network edge cases
        raise RuntimeError(str(exc)) from exc