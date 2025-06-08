# ==============================================================================
# semanticGIS Project Setup Script for PowerShell
#
# This script performs the initial setup for the semanticGIS environment AND
# creates a simple starter script for daily use.
# ==============================================================================

# Stop executing the script if any command fails.
$ErrorActionPreference = "Stop"

# --- Welcome Message ---
Write-Host "--- semanticGIS Environment Setup ---" -ForegroundColor Yellow
Write-Host "This script will prepare the base 'semanticGIS' conda environment."
Write-Host ""

# --- 1. Check and Set PowerShell Execution Policy ---
Write-Host "Step 1/5: Checking PowerShell Execution Policy..."

$currentUserPolicy = Get-ExecutionPolicy -Scope CurrentUser

if ($currentUserPolicy -eq 'Undefined' -or $currentUserPolicy -eq 'Restricted') {
    Write-Host "   - Your current execution policy is '$currentUserPolicy'." -ForegroundColor Yellow
    Write-Host "   - Attempting to set it to 'RemoteSigned' for the current user..."

    try {
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
        Write-Host "   - Execution policy for CurrentUser successfully set to 'RemoteSigned'." -ForegroundColor Green
    }
    catch {
        Write-Host "   - ERROR: The script failed to set the Execution Policy." -ForegroundColor Red
        Write-Host "   - Please open a NEW PowerShell terminal with 'Run as Administrator' and run this command:"
        Write-Host "   - Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force"
        Write-Host "   - After running that command, please re-run this setup script."
        exit 1
    }
} else {
    Write-Host "   - Execution policy is already sufficient ($currentUserPolicy)." -ForegroundColor Green
}
Write-Host ""


# --- 2. Prerequisite Check: Verify micromamba is installed ---
Write-Host "Step 2/5: Checking for micromamba..."
if (-not (Get-Command micromamba -ErrorAction SilentlyContinue)) {
    Write-Host "   - ERROR: micromamba could not be found." -ForegroundColor Red
    Write-Host "   - Please install it first by following the instructions in the README.md file."
    exit 1
}
Write-Host "   - micromamba is installed." -ForegroundColor Green
Write-Host ""


# --- 3. Create the Conda Environment ---
Write-Host "Step 3/5: Creating the 'semanticGIS' environment..."
Write-Host "   - This may take several minutes."
micromamba create -f env\semanticGIS_env.yaml -y
Write-Host "   - 'semanticGIS' environment created successfully." -ForegroundColor Green
Write-Host ""


# --- 4. Initialize the Shell ---
Write-Host "Step 4/5: Initializing your shell for 'mamba activate'..."
micromamba shell init -s powershell -p $HOME\micromamba
Write-Host "   - Shell initialization complete." -ForegroundColor Green
Write-Host ""


# --- 5. Create a convenient starter script ---
Write-Host "Step 5/5: Creating a starter script for easy access..."

# This .bat file explicitly calls powershell.exe and tells it to run the
# 'micromamba activate' command, then stay open. This is robust and
# does not depend on the user creating a 'mamba' alias.
$batFileContent = @"
@echo off
title semanticGIS Environment
echo Starting PowerShell and activating the semanticGIS environment...
powershell.exe -NoExit -Command "micromamba activate semanticGIS"
"@

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$starterScriptPath = Join-Path -Path $projectRoot -ChildPath "start-environment.bat"

Set-Content -Path $starterScriptPath -Value $batFileContent

Write-Host "   - Created 'start-environment.bat' in the main project folder." -ForegroundColor Green
Write-Host ""


# --- Final Instructions ---
Write-Host "--- Setup Complete! ---" -ForegroundColor Green
Write-Host "To start working, you can now simply double-click the 'start-environment.bat' file."
Write-Host "It will open a new PowerShell terminal with the 'semanticGIS' environment automatically activated."
Write-Host ""
Write-Host "We also recommend following the instructions in the README to create a convenient 'mamba' alias."
Write-Host ""