@echo off
title Starting QGIS
echo.
echo =================================================================
echo  Starting QGIS from within the semanticGIS environment...
echo  Please be patient, QGIS may take a moment to launch.
echo  You can close this black terminal window after QGIS starts.
echo =================================================================
echo.


echo Starting PowerShell and activating the semanticGIS environment...
powershell.exe  -Command "micromamba run -n semanticGIS qgis"