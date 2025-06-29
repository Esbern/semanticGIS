# Geospatial Environment Setup

Welcome to the official setup instructions for the **Geospatial Environment**, developed by Roskilde University. This environment is designed to support a variety of users including:

- University students in planning, environmental science, and geography
- Smallholder farmers and agricultural advisors
- Municipal staff working with spatial data
- Citizen science projects and community mapping groups

The environment is fully self-contained and installs only the tools and data **relevant to your user type**, based on your profile. It uses the **Conda environment management system** to keep things clean, consistent, and isolated from the rest of your system.

---

## ✅ What This Setup Will Do

Once installed and launched, this geospatial environment will:

- Install QGIS in a controlled Conda environment (independent from any existing QGIS installs)
- Install essential Python packages for working with spatial data, including Parquet and DuckDB
- Let you choose your user type (e.g., student, farmer, municipality) on first run
- Download data and tools appropriate for your user type from a central configuration file on GitHub
- Maintain your personal settings (e.g., user type, login credentials) in a private `.env` file

> All operations are local to your computer. No system files are touched.
> You can delete the entire environment at any time with no side effects.

---

## 📦 Prerequisite: Conda or Miniforge

This setup depends on the **Conda environment system**. We recommend using **Miniforge**, a lightweight open-source alternative to Anaconda.

### 🔹 If you *don’t* have Conda installed:
Visit the official site and download Miniforge for your operating system:
https://github.com/conda-forge/miniforge

Choose the version that matches your system (macOS Intel/ARM or Windows).

After downloading, you need to run the installer script:
- On macOS/Linux: run the `.sh` script in a terminal
- On Windows: run the `.exe` installer (or right-click and open as administrator)

### 🔹 If you already have Anaconda or Miniconda installed:
You can use your existing Conda installation. Just make sure the `conda` command works in your terminal. We recommend creating a new environment named `qgis_env` to avoid conflicts.

> Note: We assume a basic level of comfort with using the terminal for installation. However, **after this initial setup**, most interactions (QGIS and data downloads) will be fully graphical or require only one-click launch scripts.

---

## 🔧 Step-by-Step Setup

### 1. Download the GitHub Release

Go to the [Releases section of the project GitHub repo](https://github.com/YOUR_GITHUB_USERNAME/RUCgeospatial/releases) and download the latest `.zip` file.

Unzip it somewhere convenient (e.g., your Documents folder).

### 2. Run the Setup Script

Open your terminal or command prompt:

#### On macOS/Linux:
```bash
cd path/to/unzipped/folder
bash scripts/install.sh
```

#### On Windows:
Double-click `scripts\install.bat` or run:
```cmd
cd path\to\unzipped\folder
scripts\install.bat
```

This will:
- Create a Conda environment called `qgis_env`
- Install QGIS, GDAL, DuckDB, and other packages
- Set up the local tool for downloading datasets based on your selected user type

### 3. Set Up Your `.env` File

On first use, the tool will prompt you to select your user type. It will then store your preferences in a file named `.env` in the project folder. This file may include:

```dotenv
USER_TYPE=student
USERNAME=your_username_here
PASSWORD=your_password_here
```

This file remains private and is never committed to GitHub.

---

## 🚀 Using the Tools

### Start QGIS
After setup, you can start QGIS using the provided launcher:

- On macOS/Linux:
```bash
bash scripts/start_qgis.sh
```

- On Windows:
```cmd
scripts\start_qgis.bat
```

### Run the Download Tool
You can also run the interactive dataset downloader:
```bash
conda activate qgis_env
streamlit run downloader/streamlit_app.py
```

This tool will:
- Detect your user type
- Fetch available datasets from GitHub
- Allow you to download and store them locally in a `data/` folder

---

## 🧼 Uninstalling
If you ever want to remove the environment, you can run:
```bash
conda remove --name qgis_env --all
```
And delete the project folder.

---

## 🔁 Environment Philosophy

We aim to keep everything in **a single Conda environment** (`qgis_env`) to avoid confusion. This makes it easier to update or add new tools.

Only if there are package conflicts or highly specialized needs will additional environments be introduced — and this will be clearly communicated.

---

## ❓ Need Help?
If you run into issues, please contact your instructor or support contact, or create an issue on the GitHub repo.

---

Let’s build something geospatial 🌍 together!

