import streamlit as st
import yaml
from pathlib import Path

st.set_page_config(page_title="GSCE", layout="wide")
st.title("🌍 GeoSpatial Computing Environment (GSCE)")

projects_path = Path("projects")
project_dirs = [d for d in projects_path.iterdir() if d.is_dir()]

for project in project_dirs:
    config_path = project / "config.yml"
    if config_path.exists():
        with open(config_path) as f:
            cfg = yaml.safe_load(f)
        st.subheader(cfg.get("title", project.name))
        st.write(cfg.get("description", ""))
        if "link" in cfg:
            st.markdown(f"[Launch Project App]({cfg['link']})")
    else:
        st.subheader(project.name)
        st.write("_No config.yml found_")
