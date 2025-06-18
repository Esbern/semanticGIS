import inspect
from semanticgis.abstract.pipeline import Pipeline
from semanticgis.abstract.steps import PipelineStep

def compile(pipeline: Pipeline, output: str = 'print'):
    """
    Validates the pipeline and presents the results.

    Args:
        pipeline (Pipeline): The semanticGIS pipeline object to validate.
        output (str): The desired output format.
                      'print' (default): Prints a formatted, user-friendly report to the console.
                      'list': Returns a list of error strings.
    """
    # 1. Get the raw list of errors from our internal logic function
    errors = _get_validation_errors(pipeline)

    # 2. Handle the output based on the user's choice
    if output == 'list':
        return errors
    
    elif output == 'print':
        if not errors:
            print("✅ SUCCESS: All workflow checks passed!")
        else:
            print(f"❌ FAILED: Found {len(errors)} error(s) in the workflow.")
            print("-" * 30)
            for error in errors:
                print(f"  - {error}")
            print("-" * 30)
        # When printing, we don't return anything from the function
        return None
    else:
        raise ValueError(f"Invalid output type '{output}'. Choose from 'print' or 'list'.")


def _get_validation_errors(pipeline: Pipeline) -> list[str]:
    """
    Internal logic to find all validation errors in a pipeline.
    This function contains the logic we developed previously.
    
    Returns:
        A list of error strings.
    """
    errors = []
    # ... (All the validation logic we wrote and debugged goes here) ...
    def get_method_from_name(op_name: str):
        try:
            parts = op_name.split('.')
            category_obj = getattr(pipeline, parts[0])
            method = getattr(category_obj, parts[1])
            return method
        except (AttributeError, IndexError):
            return None

    for node_id, node_data in pipeline.nodes.items():
        op_name = node_data.get('operation')
        if not op_name or 'load' in op_name:
            continue
        method = get_method_from_name(op_name)
        if not method:
            errors.append(f"Node '{node_id}' ({node_data['label']}): Operation '{op_name}' not found.")
            continue
        parent_edges = [edge for edge in pipeline.edges if edge[1] == node_id]
        parent_nodes_with_ids = [(pipeline.nodes[from_id], from_id) for from_id, to_id in parent_edges]
        sig = inspect.signature(method)
        params_to_check = list(sig.parameters.values())
        step_params = [p for p in params_to_check if inspect.isclass(p.annotation) and issubclass(p.annotation, PipelineStep)]
        if len(parent_nodes_with_ids) != len(step_params):
            errors.append(f"Node '{node_id}' ({node_data['label']}): Mismatched number of inputs. Expected {len(step_params)}, got {len(parent_nodes_with_ids)}.")
            continue
        for i, param in enumerate(step_params):
            parent_node, parent_node_id = parent_nodes_with_ids[i]
            expected_type = param.annotation
            actual_type = parent_node.get('type', PipelineStep)
            if not issubclass(actual_type, expected_type):
                errors.append(f"Node '{node_id}' ({node_data['label']}): Argument '{param.name}' expected type <{expected_type.__name__}> but received <{actual_type.__name__}> from parent '{parent_node_id}' ({parent_node['label']}).")
    
    return errors