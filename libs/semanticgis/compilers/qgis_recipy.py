# In semanticgis/compilers/qgis.py

from semanticgis.abstract.pipeline import Pipeline


def compile(pipeline: Pipeline) -> str:
    """Compile the abstract DAG into a sequential QGIS-friendly recipe."""

    recipe_steps = [f"# QGIS Recipe: {pipeline.name}"]

    step_number = 1
    for node_id, node_data in pipeline.nodes.items():
        op_name = node_data.get('operation', '')
        label = node_data.get('label', node_id)
        complex_name = node_data.get('complex', '')
        parameters = node_data.get('parameters', {})

        step_lines = [f"### Step {step_number}: {label}", ""]

        if op_name == 'data_io.declare_input':
            source = parameters.get('source') or node_data.get('provenance', {}).get('source', 'N/A')
            data_model = (node_data.get('output_semantics') or {}).get('data_model', 'vector')
            data_format = parameters.get('format')
            if data_model == 'raster':
                action = "Load a raster layer"
                menu = "Layer > Add Layer > Add Raster Layer..."
            else:
                action = "Load a vector layer"
                menu = "Layer > Add Layer > Add Vector Layer..."
            step_lines.append(f"**Action**: {action} and register it as `{node_data.get('output_name')}`.")
            step_lines.append("")
            detail_line = f"* **Details**: Use `{menu}` and browse to `{source}`."
            if data_format:
                detail_line += f" Format hint: `{data_format}`."
            crs = parameters.get('crs')
            if crs:
                detail_line += f" Record CRS `{crs}`."
            step_lines.append(detail_line)

        elif op_name == 'extraction.filter_by_attribute':
            attribute = parameters.get('attribute')
            operator = parameters.get('operator')
            value = parameters.get('value')
            input_node_id = next((frm for frm, to in pipeline.edges if to == node_id), None)
            input_label = pipeline.nodes[input_node_id]['label'] if input_node_id else 'previous result'
            step_lines.append("**Action**: Use the Field Calculator or Expression Selection to filter features.")
            step_lines.append("")
            step_lines.append("* **Details**:")
            step_lines.append(f"    * *Layer*: `{input_label}`")
            step_lines.append(f"    * *Expression*: `{attribute} {operator} {value}`")

        elif op_name == 'extraction.filter_by_sql':
            where_clause = parameters.get('where_clause')
            input_node_id = next((frm for frm, to in pipeline.edges if to == node_id), None)
            input_label = pipeline.nodes[input_node_id]['label'] if input_node_id else 'previous result'
            step_lines.append("**Action**: Run a SQL query using the DB Manager or Virtual Layer feature.")
            step_lines.append("")
            step_lines.append("* **Details**:")
            step_lines.append(f"    * *Source layer*: `{input_label}`")
            step_lines.append(f"    * *WHERE clause*: `{where_clause}`")

        elif op_name == 'proximity.buffer':
            distance = parameters.get('distance', 'N/A')
            units = parameters.get('units', 'meters')
            input_node_id = next((frm for frm, to in pipeline.edges if to == node_id), None)
            input_label = pipeline.nodes[input_node_id]['label'] if input_node_id else 'previous result'
            step_lines.append("**Action**: Run the Processing Toolbox → Buffer tool.")
            step_lines.append("")
            step_lines.append("* **Settings**:")
            step_lines.append(f"    * *Input*: `{input_label}`")
            step_lines.append(f"    * *Distance*: `{distance} {units}`")
            step_lines.append("    * Ensure the layer is in an appropriate projected CRS before buffering.")

        elif op_name == 'visualise.map':
            emphasis = parameters.get('emphasis')
            step_lines.append("**Action**: Configure a map layout or styling preset for presentation.")
            step_lines.append("")
            if emphasis:
                step_lines.append(f"* **Story Focus**: {emphasis}")
            style = parameters.get('style') or {}
            if style:
                step_lines.append("* **Style Hints**:")
                for key, value in style.items():
                    step_lines.append(f"    * {key}: {value}")

        else:
            step_lines.append(f"**Operation**: `{op_name}` (complex: {complex_name}).")
            if parameters:
                step_lines.append("* **Parameters**:")
                for key, value in parameters.items():
                    step_lines.append(f"    * {key}: {value}")

        recipe_steps.append("\n".join(step_lines))
        step_number += 1

    return "\n\n---\n\n".join(recipe_steps)