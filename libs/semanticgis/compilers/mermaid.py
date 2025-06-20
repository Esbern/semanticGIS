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

    # 1. Add all the node definitions with their labels
    for node_id, node_data in pipeline.nodes.items():
        # --- New, smarter label logic ---
        # A declared name is the most important part of the label
        name = node_data.get('output_name') or node_data.get('name')
        op_label = node_data.get('label', node_id)
        
        # Format the final label using HTML-like syntax for Mermaid
        if name:
            # If it's a named milestone, make the name bold
            final_label = f"<b>{name}</b><br/>{op_label}"
        else:
            final_label = op_label
        
        # Sanitize quotes and create the node definition
        final_label = final_label.replace('"', "'")
        lines.append(f'    {node_id}["{final_label}"]')

    lines.append("")
    lines.append("    %% -- Connections --")
    for from_node, to_node in pipeline.edges:
        lines.append(f"    {from_node} --> {to_node}")
    
    # Join the lines and wrap the result in a Mermaid code block
    mermaid_body = "\n".join(lines)
    return f"```mermaid\n{mermaid_body}\n```"