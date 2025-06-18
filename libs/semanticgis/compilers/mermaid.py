# In semanticgis/compilers/mermaid.py

from semanticgis.abstract.pipeline import Pipeline

def compile(pipeline: Pipeline) -> str:
    """
    Compiles the pipeline object into a complete, renderable Mermaid
    Markdown block.
    """
    lines = []
    
    lines.append("graph TD;")
    lines.append("")

    for node_id, node_data in pipeline.nodes.items():
        label = node_data.get('label', node_id).replace('"', "'")
        lines.append(f'    {node_id}["{label}"]')

    lines.append("")
    lines.append("    %% -- Connections --")
    for from_node, to_node in pipeline.edges:
        lines.append(f"    {from_node} --> {to_node}")
    
    # Join the lines and wrap the result in a Mermaid code block
    mermaid_body = "\n".join(lines)
    return f"```mermaid\n{mermaid_body}\n```"