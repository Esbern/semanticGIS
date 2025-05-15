import argparse
import subprocess
import sys
import os
import yaml
from pathlib import Path
from dotenv import load_dotenv
import streamlit.components.v1 as components
from gsce.validate import validate_pipeline

load_dotenv()
ENV_NAME = "geospatial"

def run_command(cmd_list):
    subprocess.run(cmd_list, check=True)

def gui():
    run_command([sys.executable, "-m", "streamlit", "run", "gui/app.py"])

def qgis():
    env = os.environ.copy()
    conda_env_bin = Path(sys.executable).parent
    env["PATH"] = f"{conda_env_bin}:{env['PATH']}"
    subprocess.Popen(["qgis"], env=env)

def jupyter():
    run_command(["jupyter-lab"])



def list_projects():
    projects_path = Path("projects")
    for project in projects_path.iterdir():
        config_path = project / "config.yml"
        if config_path.exists():
            with open(config_path, "r") as f:
                cfg = yaml.safe_load(f)
            print(f"- {cfg.get('title', project.name)}: {cfg.get('description', '')}")
        else:
            print(f"- {project.name} (no config.yml)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GeoSpatial Computing Environment")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("gui", help="Launch the Streamlit GUI")
    subparsers.add_parser("qgis", help="Launch QGIS")
    subparsers.add_parser("jupyter", help="Launch JupyterLab")
    subparsers.add_parser("projects", help="List available projects")

    validate_parser = subparsers.add_parser("validate", help="Validate a pipeline YAML file and render Mermaid diagram")
    validate_parser.add_argument("file", help="Path to pipeline YAML file")

    args = parser.parse_args()

    if args.command == "gui":
        gui()
    elif args.command == "qgis":
        qgis()
    elif args.command == "jupyter":
        jupyter()
    elif args.command == "projects":
        list_projects()
    elif args.command == "validate":
        validate_pipeline(args.file)
    else:
        parser.print_help()
