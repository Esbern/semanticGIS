from .mermaid import validate_and_generate_mermaid

def validate_pipeline(pipeline_path, concept_registry=None):
    print(f"🔍 Validating pipeline at: {pipeline_path}")
    mermaid_code, errors = validate_and_generate_mermaid(pipeline_path, concept_registry)

    if errors:
        print("❌ Validation Errors:")
        for err in errors:
            print(" -", err)
    else:
        print("✅ Pipeline structure is valid.")
        print("\n📎 Mermaid Diagram:")
        print(mermaid_code)

if __name__ == "__main__":
    test_path = "example.yml"  # Update this path when testing
    validate_pipeline(test_path, concept_registry={"calculate_slope", "calculate_aspect", "buffer_geometry"})
