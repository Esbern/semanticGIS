from semanticgis.abstract.pipeline import Pipeline

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
    """Inspect the DAG for missing operations and semantic contract violations."""

    errors: list[str] = []

    def get_method_from_name(op_name: str):
        try:
            complex_key, op_key = op_name.split('.')
        except ValueError:
            return None
        complex_obj = getattr(pipeline, complex_key, None)
        if complex_obj is None:
            return None
        return getattr(complex_obj, op_key, None)

    for node_id, node_data in pipeline.nodes.items():
        op_name = node_data.get('operation')
        label = node_data.get('label', node_id)
        if not op_name:
            errors.append(f"Node '{node_id}' ({label}): Missing operation identifier.")
            continue

        method = get_method_from_name(op_name)
        if not method:
            errors.append(f"Node '{node_id}' ({label}): Operation '{op_name}' not found on pipeline complexes.")

        parent_edges = [edge for edge in pipeline.edges if edge[1] == node_id]
        parent_nodes_with_ids = [(pipeline.nodes[from_id], from_id) for from_id, _ in parent_edges]
        data_requirements = node_data.get('data_requirements') or []

        if data_requirements and len(parent_nodes_with_ids) != len(data_requirements):
            errors.append(
                f"Node '{node_id}' ({label}): Expected {len(data_requirements)} inputs based on semantic rules "
                f"but received {len(parent_nodes_with_ids)}."
            )
            continue

        for idx, (parent_node, parent_node_id) in enumerate(parent_nodes_with_ids):
            expectation = data_requirements[idx] if idx < len(data_requirements) else {}
            semantics = parent_node.get('output_semantics') or {}
            for key, expected_value in expectation.items():
                if not expected_value or expected_value == 'any':
                    continue
                actual_value = semantics.get(key)
                if actual_value is None:
                    errors.append(
                        f"Node '{node_id}' ({label}): Parent '{parent_node_id}' lacks semantic key '{key}' required by the operation."
                    )
                    continue
                if isinstance(expected_value, (list, tuple, set)):
                    if actual_value not in expected_value:
                        errors.append(
                            f"Node '{node_id}' ({label}): Parent '{parent_node_id}' provides {key}='{actual_value}' "
                            f"but operation requires one of {sorted(expected_value)}."
                        )
                elif expected_value != actual_value:
                    errors.append(
                        f"Node '{node_id}' ({label}): Parent '{parent_node_id}' provides {key}='{actual_value}' "
                        f"but operation requires '{expected_value}'."
                    )

    return errors