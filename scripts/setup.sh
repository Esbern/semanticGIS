#!/bin/bash

# ==============================================================================
# semanticGIS Project Setup Script
# (Located in the 'scripts' folder)
# ==============================================================================

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Determine Project Root Directory ---
# This makes the script runnable from anywhere by finding its own location
# and then navigating up one level to the project root.
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
PROJECT_ROOT=$(dirname "$SCRIPT_DIR")
ENV_FILE="$PROJECT_ROOT/env/semanticGIS_env.yaml"

# --- Welcome Message ---
echo "--- semanticGIS Environment Setup for macOS & Linux ---"
echo "Project Root: $PROJECT_ROOT"
echo ""

# --- 1. Prerequisite Check: Verify micromamba is installed ---
echo "Step 1/3: Checking for micromamba..."
if ! command -v micromamba &> /dev/null; then
    echo "   - ERROR: micromamba could not be found."
    echo "   - Please install it first by following the instructions in the README.md file."
    exit 1
fi
echo "   - micromamba is installed."
echo ""

# --- 2. Create the Conda Environment ---
echo "Step 2/3: Creating the 'semanticGIS' environment from '$ENV_FILE'..."
echo "   - This may take several minutes depending on your internet connection."
micromamba create -f "$ENV_FILE" -y
echo "   - 'semanticGIS' environment created successfully."
echo ""

# --- 3. Initialize the Shell ---
echo "Step 3/3: Initializing your shell to use 'mamba activate'..."
USER_SHELL=$(basename "$SHELL")
micromamba shell init -s "$USER_SHELL" -p ~/micromamba
echo "   - Shell initialization complete."
echo ""

# --- Final Instructions ---
echo "--- Setup Complete! ---"
echo "To finish, please do the following:"
echo "   1. Close this terminal window completely."
echo "   2. Open a new terminal window."
echo "   3. Follow the instructions in the README to create the 'mamba' alias (recommended)."
echo "   4. You can then activate the environment by running:"
echo "      mamba activate semanticGIS"
echo ""