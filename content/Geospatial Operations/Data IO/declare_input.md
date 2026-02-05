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
- 

|Parameter|Type|Required|Description|
|---|---|---|---|
|**`source`**|`str`|**Yes**|Path to the file (Local or URL). _Example: "data/roads.gpkg"_|
|**`output_name`**|`str`|**Yes**|The unique ID for this data state. Used as the `source` for future steps.|
|**`data_model`**|`Enum`|No|Defines if the data is `VECTOR` or `RASTER`. Defaults to `VECTOR`.|
|**`spatial_nature`**|`Enum`|No|Defines if boundaries are `DISCRETE` (Objects) or `CONTINUOUS` (Fields).|
|**`attributes`**|`dict`|No|A dictionary mapping column names to their **Measurement Scale** and Description.|
|**`pre_filter`**|`str`|No|An SQL `WHERE` clause to filter rows during ingestion. _Example: "speed > 50"_|
|**`spatial_filter`**|`str`|No|The `output_name` of a polygon dataset used to clip this input geographically.|
|**`crs`**|`str`|No|The Coordinate Reference System (e.g., "EPSG:25832").|
|**`label`**|`str`|No|The text that appears in the Mermaid flowchart. Defaults to `output_name`.|
## Template
``` Python
# --- SEMANTIC DATA DECLARATION TEMPLATE ---
p.io.declare_input(
    source      = "PATH_OR_URL_HERE",
    output_name = "UNIQUE_SYMBOL_NAME",
    label       = "Friendly Human Name",  # Appears in the Flowchart
    
    # Semantic Metadata
    data_model     = sg.DataModel.VECTOR, 
    spatial_nature = sg.SpatialNature.DISCRETE,
    
    # The Attribute Contract (Defining the science)
    attributes = {
        "COLUMN_NAME": {
            "scale": sg.MeasurementScale.RATIO, 
            "description": "Short explanation of this variable"
        }
    },
    
    # Geographical and Logical Gates (Optional)
    pre_filter     = None,  # e.g., "attribute > 10"
    spatial_filter = None,  # e.g., "study_area_polygon"
    
    # Technical Metadata
    crs         = None,     # e.g., "EPSG:25832"
    data_format = sg.DataFormat.GEOPACKAGE
)
```