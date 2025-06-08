#!/bin/bash

# ==============================================================================
# Starts QGIS from within the semanticGIS environment.
# ==============================================================================

echo "› Starting QGIS from within the semanticGIS environment..."
echo "› Please be patient, QGIS may take a moment to launch."

# The 'run' command executes a program from within an environment.
# The '&' at the end runs the process in the background, freeing up
# your terminal immediately.
micromamba run -n semanticGIS qgis &