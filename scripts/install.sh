#!/bin/bash

echo "---------------------------------------"
echo "Setting up QGIS environment with Conda"
echo "---------------------------------------"

conda create -n qgis_env --file env/qgis_env.yml -y
conda activate qgis_env

echo "Done! To start QGIS, run:"
echo "bash scripts/start_qgis.sh"
