#!/bin/zsh

# ==============================================================================
# Starts QGIS from within the semanticGIS environment. (macOS GUI Version)
# ==============================================================================

# Source the user's Zsh configuration file to find the 'micromamba' command.
# This is ESSENTIAL for portability.
if [[ -f ~/.zshrc ]]; then
  source ~/.zshrc
fi

# Check if micromamba is available after sourcing the config.
if ! command -v micromamba &> /dev/null; then
    echo "Error: 'micromamba' command not found." >&2
    echo "Please ensure micromamba is installed and configured in your ~/.zshrc file." >&2
    read -p "Press Enter to close..."
    exit 1
fi

echo "› Starting QGIS from within the semanticGIS environment..."

# Launch the command.
# - The final '&' backgrounds the process so the script can finish immediately.
# - macOS Launch Services will manage the GUI app, preventing it from closing.
# - 'nohup' is NOT used as it strips the necessary GUI context on macOS.
# - '&> /dev/null' is used to prevent stray command-line output.
micromamba run -n semanticGIS qgis &> /dev/null &

exit 0