# In semanticgis/compilers/mermaid.py

from semanticgis.abstract.pipeline import Pipeline


def compile(pipeline: Pipeline) -> str:
    """Render the pipeline as a flowchart with ArcGIS-style data/process glyphs."""

    lines: list[str] = []
    dataset_nodes: list[tuple[str, str]] = []
    process_nodes: list[tuple[str, str]] = []
    dataset_lookup: dict[str, str] = {}
    process_lookup: dict[str, str] = {}

    lines.append("flowchart TD")
    lines.append("")

    for node_id, node_data in pipeline.nodes.items():
        name = node_data.get('output_name') or node_data.get('name')
        op_label = node_data.get('label', node_id)
        complex_name = node_data.get('complex', 'workflow')
        semantic_signature = node_data.get('output_semantics') or {}
        complex_caption = complex_name.replace('_', ' ').title()
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
        is_data_io = complex_name == 'data_io'
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

    mermaid_body = "\n".join(lines)
    return f"```mermaid\n{mermaid_body}\n```"