from pathlib import Path
import yaml
from typing import Dict, Any

def load_config_with_override(
    base_config_path: Path, 
    override_filename_suffix: str = ".local"
) -> Dict[str, Any]:
    """
    Loads a base YAML config file and overrides its values with a local version.

    The override file is assumed to be in the same directory as the base file,
    with a suffix appended to its name (e.g., 'config.yaml' -> 'config.local.yaml').

    Args:
        base_config_path (Path): The full path to the main configuration file.
        override_filename_suffix (str, optional): The suffix to identify the
                                                   override file. Defaults to ".local".

    Returns:
        Dict[str, Any]: The final, combined configuration dictionary.
    """
    # Construct the path for the local override file
    local_config_path = base_config_path.with_suffix(f'{override_filename_suffix}{base_config_path.suffix}')

    config = {}
    if base_config_path.exists():
        with open(base_config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f) or {} # Ensure it's a dict even if file is empty
    else:
        # It might be better to raise an error if the base config is essential
        print(f"Warning: Base config file not found at {base_config_path}")

    # If a local override file exists, load it and update the main config
    if local_config_path.exists():
        print(f"Info: Applying local override from {local_config_path}")
        with open(local_config_path, 'r', encoding='utf-8') as f:
            override_config = yaml.safe_load(f)
            if isinstance(override_config, dict):
                config.update(override_config)
    
    return config