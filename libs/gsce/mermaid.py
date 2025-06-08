import yaml

def validate_and_generate_mermaid(yaml_path, concept_registry=None):
    with open(yaml_path) as f:
        pipeline_data = yaml.safe_load(f)

    pipeline = pipeline_data.get("pipeline", {})
    steps = pipeline.get("steps", [])
    acquisition = pipeline.get("acquisition", [])

    lines = ["graph TD"]
    errors = []
    defined_outputs = set()
    all_inputs = set()

    for item in acquisition:
        name = item.get("name")
        if not name:
            errors.append("❌ Acquisition item missing 'name'")
            continue
        desc = item.get("description", "")
        lines.append(f'  {name}["📥 {name}\\n{desc}"]')
        defined_outputs.add(name)

    for step in steps:
        step_name = step.get("name")
        if not step_name:
            errors.append("❌ Step missing 'name'")
            continue

        concept = step.get("concept", "undefined")
        lines.append(f'  {step_name}["🔧 {step_name}\\n({concept})"]')

        inputs = step.get("input", [])
        for input_var in inputs:
            all_inputs.add(input_var)
            if input_var not in defined_outputs:
                errors.append(f"❌ Step '{step_name}' uses undefined input: '{input_var}'")
            lines.append(f'  {input_var} --> {step_name}')

        outputs = step.get("output", {})
        if isinstance(outputs, list):
            for out in outputs:
                for k, v in out.items():
                    desc = v.get("description", "")
                    lines.append(f'  {step_name} --> {k}["📤 {k}\\n{desc}"]')
                    defined_outputs.add(k)
        elif isinstance(outputs, dict):
            for k, v in outputs.items():
                desc = v.get("description", "")
                lines.append(f'  {step_name} --> {k}["📤 {k}\\n{desc}"]')
                defined_outputs.add(k)
        else:
            errors.append(f"❌ Step '{step_name}' has invalid or missing 'output' field")

        if concept_registry and concept != "undefined":
            if concept not in concept_registry:
                errors.append(f"❌ Unknown concept '{concept}' in step '{step_name}'")

    return "\n".join(lines), errors
