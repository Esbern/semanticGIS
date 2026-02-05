---
title: Declare Input
draft: false
tags:
aliases:
  - Declare Input
---
### 1. Philosophical Intent

The `declare_input` operation is the bridge between a physical file and a scientific concept. In **semanticGIS**, we do not simply "open files"; we declare the nature of the evidence we are bringing into our analytical environment. By being explicit about the **Data Model**, **Spatial Nature**, and **Measurement Scales**, you enable the system to protect you from illogical operations (e.g., trying to calculate the "average" of a categorical soil map).

### 2. Semantic Gating (The Sieve)

Rarely do we need an entire database for a specific study. `declare_input` allows you to define the **Scope of Interest** immediately:

- **Attribute Filter (`pre_filter`)**: Applies an SQL-style constraint at the moment of entry.
    
    - _Example:_ `status = 'Active'` ensures that retired or planned features never enter the pipeline logic.
        
- **Spatial Filter (`spatial_filter`)**: Constrains the input to the geometry of a previously declared discrete dataset.
    
    - _Constraint:_ The spatial filter must be a **Discrete** dataset (e.g., a Study Area polygon).
        

### 3. The Attribute Contract

Within the `attributes` dictionary, you define the "meaning" of your columns.

- **Scale**: This refers to **Stevens' Scales of Measurement**.
    
    - **Nominal/Ordinal**: Categorical data that should not be used in traditional arithmetic.
        
    - **Interval/Ratio**: Quantitative data suitable for statistical modeling.
        
- **Inference**: If all attributes share a scale, the dataset inherits that scale. If they differ, the dataset is marked as `mixed`.
    

### 4. Technical Specifications

- **Declarative Style**: This operation does not return the data itself, but a **symbolic reference**. You reference the data in downstream steps using the `output_name` string.
    
- **Data Format**: While the system attempts to detect formats, explicitly setting `data_format` (e.g., `DataFormat.GEOPACKAGE`) ensures the correct connector is used in cross-platform environments (QGIS vs. Python).