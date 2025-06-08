#!/bin/bash

# ==============================================================================
# semanticGIS Project Setup Script
# (Located in the 'scripts' folder)
# ==============================================================================

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Determine Project Root Directory ---
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
PROJECT_ROOT=$(dirname "$SCRIPT_DIR")
ENV_FILE="$PROJECT_ROOT/env/semanticGIS_env.yaml"
ENV_NAME="semanticGIS"

# --- Welcome Message ---
echo "--- semanticGIS Environment Setup for macOS & Linux ---"
echo "Project Root: $PROJECT_ROOT"
echo ""

# --- 1. Check if Environment Already Exists ---
echo "Step 1/4: Checking for existing '$ENV_NAME' environment..."
# 'micromamba env list' lists all environments. We grep for the exact name.
# The command returns a non-zero exit code if the grep finds nothing.
if micromamba env list | grep -q "^$ENV_NAME\s"; then
    echo "   - Environment '$ENV_NAME' already exists. Nothing to do."
    echo "   - To start working, open a new terminal and run 'mamba activate $ENV_NAME'."
    echo "   - If you wish to rebuild the environment, please remove it first with 'mamba env remove -n $ENV_NAME'"
    exit 0
fi
echo "   - Environment does not exist. Proceeding with setup."
echo ""

# --- 2. Prerequisite Check: Verify micromamba is installed ---
echo "Step 2/4: Checking for micromamba..."
if ! command -v micromamba &> /dev/null; then
    echo "   - ERROR: micromamba could not be found."
    echo "   - Please install it first by following the instructions in the README.md file."
    exit 1
fi
echo "   - micromamba is installed."
echo ""

# --- 3. Create the Conda Environment ---
echo "Step 3/4: Creating the '$ENV_NAME' environment from '$ENV_FILE'..."
echo "   - This may take several minutes."
micromamba create -f "$ENV_FILE" -y
echo "   - '$ENV_NAME' environment created successfully."
echo ""

# --- 4. Initialize the Shell ---
echo "Step 4/4: Initializing your shell..."
USER_SHELL=$(basename "$SHELL")
micromamba shell init -s "$USER_SHELL" -p ~/micromamba
echo "   - Shell initialization complete."
echo ""

# --- Final Instructions ---
echo "--- Setup Complete! ---"
echo "To finish, please close and re-open your terminal, then activate with 'mamba activate $ENV_NAME'."
echo ""