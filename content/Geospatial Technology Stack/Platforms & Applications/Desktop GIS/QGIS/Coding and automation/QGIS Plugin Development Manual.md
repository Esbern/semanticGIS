---
title: GIS Plugin Development Manual
draft: false
tags:
---
Creating a qgis plugin is also relatival simple just install the plugin builder plugin and run it it will create a nice templet to work with.

Personally after running using the plugin builder i change the structure a bit to something that fits my likings better.



## **Project Structure & Clean Naming**

This guide outlines a **modular** and **scalable** approach to developing a QGIS plugin, ensuring: ✅ **No unnecessary prefixes** (cleaner names).  
✅ **A single `dialog_loader.py` to manage multiple dialogs dynamically**.  
✅ **A `dev` mode (loads `.ui` files) and a `dist` mode (loads compiled `.py` UI files)**.  
✅ **Simple switching between development and distribution states**.

---

## **📂 File Structure**

```
geo_ilum/
│── __init__.py          # Tells QGIS to load plugin.py
│── plugin.py            # Main plugin logic
│── dialog_loader.py     # Dynamically loads UI files
│── dialog_1.ui          # Main UI file (Qt Designer)
│── dialog_2.ui          # Secondary UI file (Qt Designer)
│── dialog_1_ui.py       # Compiled UI file (generated for dist mode)
│── dialog_2_ui.py       # Compiled UI file (generated for dist mode)
│── database.py          # Handles database interactions (optional)
```

---

## **1️⃣ Set Plugin Mode in `plugin.py`**

This file **controls the plugin's state** (`dev` or `dist`) and registers dialogs.

```python
from PyQt5.QtWidgets import QAction
from .dialog_loader import DialogLoader

# Switch between development ("dev") and distribution ("dist") mode
PLUGIN_MODE = "dev"  # Change to "dist" when distributing

class GeoILUM:
    def __init__(self, iface):
        self.iface = iface
        self.dlg_main = None
        self.dlg_secondary = None

        # Add menu actions
        self.menu = "&GeoILUM Plugin"
        self.action_main = QAction("Open Main Dialog", self.iface.mainWindow())
        self.action_secondary = QAction("Open Secondary Dialog", self.iface.mainWindow())

        self.action_main.triggered.connect(self.run_main_dialog)
        self.action_secondary.triggered.connect(self.run_secondary_dialog)

    def initGui(self):
        """Create menu entries in QGIS."""
        self.iface.addPluginToMenu(self.menu, self.action_main)
        self.iface.addPluginToMenu(self.menu, self.action_secondary)

    def unload(self):
        """Remove menu entries on unload."""
        self.iface.removePluginMenu(self.menu, self.action_main)
        self.iface.removePluginMenu(self.menu, self.action_secondary)

    def run_main_dialog(self):
        """Open Main Dialog."""
        if not self.dlg_main:
            self.dlg_main = DialogLoader("dialog_1", PLUGIN_MODE)  # Pass mode
        self.dlg_main.show()
        self.dlg_main.exec_()

    def run_secondary_dialog(self):
        """Open Secondary Dialog."""
        if not self.dlg_secondary:
            self.dlg_secondary = DialogLoader("dialog_2", PLUGIN_MODE)  # Pass mode
        self.dlg_secondary.show()
        self.dlg_secondary.exec_()
```

---

## **2️⃣ Load UI Dynamically in `dialog_loader.py`**

This script handles **both `dev` and `dist` modes**.

```python
import os
from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDialog

class DialogLoader(QDialog):
    def __init__(self, ui_name, mode="dev", parent=None):
        """Loads UI dynamically based on plugin mode."""
        super().__init__(parent)

        if mode == "dev":
            # Development Mode: Load .ui file dynamically
            FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), f"{ui_name}.ui"))
            self.ui = FORM_CLASS()
            self.ui.setupUi(self)

        elif mode == "dist":
            # Distribution Mode: Load pre-compiled .py UI file
            compiled_ui_module = f".{ui_name}_ui"
            try:
                compiled_ui = __import__(compiled_ui_module, globals(), locals(), ["Ui_MainWindow"], 0)
                self.ui = compiled_ui.Ui_MainWindow()
                self.ui.setupUi(self)
            except ImportError:
                print(f"Error: Compiled UI file {ui_name}_ui.py not found. Falling back to .ui file.")
                FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), f"{ui_name}.ui"))
                self.ui = FORM_CLASS()
                self.ui.setupUi(self)
```

### **How This Works**

✅ **In `dev` mode**, `.ui` files are loaded dynamically.  
✅ **In `dist` mode**, `.py` UI files are used (faster loading).  
✅ **If the compiled UI is missing, it falls back to the `.ui` file** (prevents crashes).

---

## **3️⃣ Generate `.py` UI Files for Distribution**

Before packaging the plugin, compile the UI files:

```sh
pyuic5 -o dialog_1_ui.py dialog_1.ui
pyuic5 -o dialog_2_ui.py dialog_2.ui
```

Then, **switch to `dist` mode** in `plugin.py`:

```python
PLUGIN_MODE = "dist"
```

Now the plugin will **load the compiled UI** instead of parsing `.ui` files at runtime.

---

## **4️⃣ `__init__.py` (Plugin Entry Point)**

This file tells QGIS **where to find `plugin.py`**.

```python
from .plugin import GeoILUM

def classFactory(iface):
    return GeoILUM(iface)
```

✅ **Keeps QGIS looking only inside `geo_ilum/` (no external conflicts).**

---

## **🛠 Development vs. Distribution**

|Mode|`.ui` or `.py`?|When to Use?|
|---|---|---|
|`dev`|Loads `.ui` files|While actively developing (no need to recompile).|
|`dist`|Loads `.py` UI files|For packaging & release (faster loading).|

---

## **🚀 Summary**

### ✅ **No unnecessary prefixes**

- Uses **`plugin.py`**, **`dialog_loader.py`**, and **`database.py`** instead of `geo_ilum_plugin.py`.

### ✅ **Single `dialog_loader.py` handles all dialogs**

- Loads **any UI dynamically** based on a **single function call**.

### ✅ **Supports both `dev` and `dist` modes**

- **`dev`** → Uses `.ui` (easier for development).
- **`dist`** → Uses `.py` (faster for release).

### ✅ **Easily switch between modes**

- Just **change `PLUGIN_MODE = "dev"` to `"dist"`**.

---

## **🚀 Next Steps**

### **1️⃣ Development Phase**

- Keep **`PLUGIN_MODE = "dev"`** in `plugin.py`.
- Modify UI in **Qt Designer** (`.ui` files).
- No need to recompile `.ui` files.

### **2️⃣ Before Release**

- Compile `.ui` files:
    
    ```sh
    pyuic5 -o dialog_1_ui.py dialog_1.ui
    pyuic5 -o dialog_2_ui.py dialog_2.ui
    ```
    
- Change `PLUGIN_MODE = "dist"` in `plugin.py`.
- Package & distribute!

---

## **🛠 Extra Enhancements**

- Add **error handling** to check if `dialog_1.ui` or `dialog_1_ui.py` is missing.
- Store **database settings** in `QSettings` so they persist between sessions.
- Support **PostGIS connections** in `database.py`.

---

🚀 **Now your QGIS plugin is modular, scalable, and easy to maintain!** 🚀