# ==============================================================================
# semanticGIS Project Setup Script for PowerShell
# (Located in the 'scripts' folder)
# ==============================================================================

# Stop executing the script if any command fails.
$ErrorActionPreference = "Stop"

# --- Determine Paths and Names ---
$scriptDir = $PSScriptRoot
$projectRoot = (Get-Item $scriptDir).Parent.FullName
$envName = "semanticGIS"
$envFile = Join-Path -Path $projectRoot -ChildPath "env\semanticGIS_env.yaml"

# --- Welcome Message ---
Write-Host "--- semanticGIS Environment Setup ---" -ForegroundColor Yellow
Write-Host "Project Root: $projectRoot"
Write-Host ""

# --- 1. Check if Environment Already Exists ---
Write-Host "Step 1/6: Checking for existing '$envName' environment..."
$envExists = micromamba env list | Select-String -Quiet -Pattern "^$envName\s"
if ($envExists) {
    Write-Host "   - Environment '$envName' already exists. Nothing to do." -ForegroundColor Green
    Write-Host "   - To start working, open a new terminal and run 'mamba activate $envName'."
    Write-Host "   - If you wish to rebuild the environment, please remove it first with 'mamba env remove -n $envName'"
    # Exit the script cleanly without an error.
    exit 0
}
Write-Host "   - Environment does not exist. Proceeding with setup."
Write-Host ""


# --- 2. Check and Set PowerShell Execution Policy ---
Write-Host "Step 2/6: Checking PowerShell Execution Policy..."
# ... (The logic for this section remains unchanged) ...
$currentUserPolicy = Get-ExecutionPolicy -Scope CurrentUser
if ($currentUserPolicy -eq 'Undefined' -or $currentUserPolicy -eq 'Restricted') {
    Write-Host "   - Your current execution policy is '$currentUserPolicy'." -ForegroundColor Yellow
    Write-Host "   - Attempting to set it to 'RemoteSigned' for the current user..."
    try {
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
        Write-Host "   - Execution policy for CurrentUser successfully set to 'RemoteSigned'." -ForegroundColor Green
    } catch {
        Write-Host "   - ERROR: The script failed to set the Execution Policy." -ForegroundColor Red
        Write-Host "   - Please open a NEW PowerShell terminal with 'Run as Administrator' and run this command:"
        Write-Host "   - Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force"
        exit 1
    }
} else {
    Write-Host "   - Execution policy is already sufficient ($currentUserPolicy)." -ForegroundColor Green
}
Write-Host ""

# --- 3. Prerequisite Check: Verify micromamba is installed ---
Write-Host "Step 3/6: Checking for micromamba..."
if (-not (Get-Command micromamba -ErrorAction SilentlyContinue)) {
    Write-Host "   - ERROR: micromamba could not be found." -ForegroundColor Red
    Write-Host "   - Please install it first by following the instructions in the README.md file."
    exit 1
}
Write-Host "   - micromamba is installed." -ForegroundColor Green
Write-Host ""

# --- 4. Create the Conda Environment ---
Write-Host "Step 4/6: Creating the '$envName' environment from '$envFile'..."
Write-Host "   - This may take several minutes."
micromamba create -f $envFile -y
Write-Host "   - '$envName' environment created successfully." -ForegroundColor Green
Write-Host ""

# --- 5. Initialize the Shell ---
Write-Host "Step 5/6: Initializing your shell..."
micromamba shell init -s powershell -p $HOME\micromamba
Write-Host "   - Shell initialization complete." -ForegroundColor Green
Write-Host ""

# --- 6. Create a convenient starter script ---
Write-Host "Step 6/6: Creating a starter script for easy access..."
$starterScriptPath = Join-Path -Path $projectRoot -ChildPath "start-environment.bat"
$batFileContent = @"
@echo off
title semanticGIS Environment
echo Starting PowerShell and activating the semanticGIS environment...
powershell.exe -NoExit -Command "micromamba activate semanticGIS"
"@
Set-Content -Path $starterScriptPath -Value $batFileContent
Write-Host "   - Created 'start-environment.bat' in the main project folder." -ForegroundColor Green
Write-Host ""

# --- Final Instructions ---
Write-Host "--- Setup Complete! ---" -ForegroundColor Green
Write-Host "To start working, double-click the 'start-environment.bat' file, or open a terminal and run 'mamba activate $envName'."
Write-Host ""