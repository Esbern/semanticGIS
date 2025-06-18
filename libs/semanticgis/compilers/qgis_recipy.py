# In semanticgis/compilers/qgis.py

from semanticgis.abstract.pipeline import Pipeline

def compile(pipeline: Pipeline) -> str:
    """
    Compiles the pipeline into a human-readable, step-by-step recipe
    in Markdown format.
    """
    recipe_steps = []
    
    recipe_steps.append(f"# QGIS Recipe: {pipeline.name}")
    
    step_number = 1
    for node_id, node_data in pipeline.nodes.items():
        op_name = node_data.get('operation', '')
        label = node_data.get('label', node_id)
        
        step_md = f"### Step {step_number}: {label}\n\n"
        
        if 'vector.load' in op_name:
            path = node_data.get('path', 'N/A')
            step_md += f"**Action**: Load a vector layer.\n\n"
            step_md += f"* **Details**: From the main menu, go to `Layer > Add Layer > Add Vector Layer...` and browse to the file at `{path}`."
        
        elif 'raster.load' in op_name:
            path = node_data.get('path', 'N/A')
            step_md += f"**Action**: Load a raster layer.\n\n"
            step_md += f"* **Details**: From the main menu, go to `Layer > Add Layer > Add Raster Layer...` and browse to the file at `{path}`."

        elif 'vector.buffer' in op_name:
            distance = node_data.get('distance', 'N/A')
            input_node_id = next((from_node for from_node, to_node in pipeline.edges if to_node == node_id), None)
            input_label = pipeline.nodes[input_node_id]['label'] if input_node_id else "the previous step's output"
            
            step_md += f"**Action**: Create a buffer.\n\n"
            step_md += f"* **Details**: Go to the `Processing Toolbox` and search for the **Buffer** tool.\n"
            step_md += f"* **Settings**:\n"
            step_md += f"    * *Input layer*: `{input_label}`\n"
            step_md += f"    * *Distance*: `{distance}`"
        
        else:
            step_md += f"**Operation**: `{op_name}`"

        recipe_steps.append(step_md)
        step_number += 1
        
    return "\n\n---\n\n".join(recipe_steps)