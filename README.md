# `README.md`

You should copy the entire content below into the `README.md` file in the root of your `semanticGIS` project.


# 🌳 semanticGIS Project

Welcome to the `semanticGIS` project environment. The goal of this project is to provide a standardized, reproducible, and user-friendly ecosystem for geospatial analysis, suitable for both small student projects and large-scale research.

It combines the power of the Conda package management system (via `micromamba`) with a structured project layout to ensure that all tools, libraries, and scripts work together seamlessly.



## 🏛️ Directory Structure

This project uses a standardized folder structure to keep everything organized.

---


semanticGIS/
│
├── README.md                # This file: essential information for getting started
├── environment.yaml         # Global, non-secret configuration (e.g., common data paths)
├── env/
│   └── semanticGIS_env.yaml   # The definition of the core conda environment
│
├── libs/                    # Core, shared Python modules for the entire semanticGIS system
│
├── projects/                # Contains all individual analysis projects
│   └── exampleProject/      # A template project to be forked for new work
│
└── scripts/                 # Utility scripts for managing the environment
    ├── setup.sh             # Setup script for macOS & Linux
    ├── setup.ps1            # Setup script for Windows
    ├── start-qgis.sh        # Launches QGIS in the environment (macOS/Linux)
    ├── start-qgis.bat       # Launches QGIS in the environment (Windows)
    └── start-environment.bat # (Windows only) Clickable starter for an activated terminal


---

## 🚀 Getting Started: Installation

Follow these steps to set up the complete `semanticGIS` environment on your computer. The process uses a setup script to automate as much as possible.

### **Step 0: Before You Begin - Install Micromamba**

This entire system depends on the `micromamba` package manager. If you do not already have it, this is a **one-time setup** for your computer.

1.  Follow the official instructions at the [Micromamba Installation Guide](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html).
2.  Choose the tab for your operating system (Windows, macOS, or Linux) and run the single command provided.
3.  After the installer finishes, **you must close and re-open your terminal** for the `micromamba` command to be available.

### **Step 1: Download and Prepare Your Project Folder**

1.  **Download the Code:** On the GitHub repository page, click the green **`< > Code`** button and select **`Download ZIP`**.
2.  **Create Your `semanticGIS` Folder:** Create a new, empty folder in a convenient location. Name it **`semanticGIS`**. (e.g., `C:\Users\YourUser\semanticGIS` or `~/semanticGIS`).
3.  **Unzip the Files:** Unzip the downloaded file. It will likely create a folder named `semanticGIS-main`. **Open this folder**, copy all the files and folders from inside, and paste them directly into the **`semanticGIS`** folder you created.

### **Step 2: Run the Setup Script**

This script will check for dependencies and create the `semanticGIS` environment. If the environment already exists, it will inform you and exit safely.

1.  **Open a Terminal:** On **Windows**, open **PowerShell**. On **macOS** or **Linux**, open **Terminal**.
2.  **Navigate to Your Folder:** In the terminal, type `cd` followed by the path to your `semanticGIS` folder.
    * *Example for Windows:* `cd C:\Users\YourUser\semanticGIS`
    * *Example for macOS/Linux:* `cd ~/semanticGIS`
3.  **Execute the Script:** Run the command for your operating system.

    #### **For macOS and Linux:**
    ```bash
    ./scripts/setup.sh
    ```

    #### **For Windows:**
    ⚠️ **Note:** If you get an error about "scripts being disabled", run this command first, then try the setup script again:
    `Set-ExecutionPolicy RemoteSigned -Scope Process`
    ```powershell
    .\scripts\setup.ps1
    ```
The script will now run and guide you through the setup. This may take several minutes.

---

##  workday How to Work in the `semanticGIS` Environment

Once setup is complete, you have several ways to start working.

### **1. Activating the Environment Manually**

This is the standard way to work on all platforms.

**Recommended:** For daily use, we suggest creating a shorter `mamba` alias for `micromamba`.
* **On macOS/Linux:** Add `alias mamba='micromamba'` to your `~/.zshrc` or `~/.bashrc` file.
* **On Windows:** Add `Set-Alias -Name mamba -Value micromamba` to your PowerShell profile (open it with `notepad $PROFILE`).

After restarting your terminal, you can activate the environment with:
```bash
mamba activate semanticGIS
```
You should see `(semanticGIS)` appear at the beginning of your terminal prompt.

### **2. Launching the Environment (Windows Users)**

The setup script created a file named **`start-environment.bat`** in your `semanticGIS` folder. Simply **double-click this file** to open a new PowerShell terminal with the `semanticGIS` environment automatically activated and ready for use.

### **3. Launching the Integrated QGIS Desktop**

Your environment includes a full installation of QGIS that is connected to all the Python libraries in `semanticGIS`. This is the recommended way to do desktop GIS work.

To start QGIS, run the appropriate script from the `scripts/` folder. You can create a desktop shortcut to this script for convenience.

* **On Windows:** Double-click `scripts/start-qgis.bat`
* **On macOS/Linux:** Run `./scripts/start-qgis.sh` from your terminal.

### **4. Working on a Project**

Once your environment is activated, navigate to a specific project within the `projects/` folder and follow the instructions in its own `README.md` file.

```bash
cd projects/exampleProject
```
```
