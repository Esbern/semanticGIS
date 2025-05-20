## 🧭 Overview

This process is used when working **outside the structured GSCE dataset ontology** — that is, when you have access to a known **source** (such as a folder or database), but the **data itself is not yet described or classified** within the GSCE framework.

> 💡 It inverts the usual case: instead of loading a known type of data from an unknown location, you are loading **unknown data from a known source**.

This process is useful for:

- Ad hoc or exploratory analysis
    
- Preprocessing bulk data before organizing it in GSCE's ontology
    
- Teaching students how to discover, inspect, and document new datasets
    

⚠️ **It is imperative that users manually document the data after loading**, either by assigning metadata, linking it to concepts, or preparing it for validation.

This general-purpose loader supports folders, databases, GeoPackages, and online services. It uses a filter to select relevant datasets and supports both bulk and single-object modes.

---

## 📦 Inputs

```
inputs:
  source:
    type: string
    description: Path to folder, database connection string, or service URL

  source_type:
    type: enum
    values: [folder, geopackage, postgis, duckdb, api, wfs, wcs, s3]
    description: Type of backend to access

  filter:
    type: string or list
    optional: true
    description: Regex or list of dataset/layer names to include

  single:
    type: boolean
    default: false
    description: If true, return only one dataset (first match)
```

---

## 📤 Outputs

```
outputs:
  dataset_list:
    type: list or object
    description: List of datasets (or a single dataset if `single: true`)
```

Each dataset is typically returned as a structured object:

```
- name: geotopes
  path: public.geotopes
  source_type: postgis
  crs: EPSG:25832
  geometry_type: Polygon
```

---

## 🔍 Examples

### 🏞 Load all shapefiles from a folder

```
inputs:
  source: data/land_cover/
  source_type: folder
  filter: ".*\\.shp$"
  single: false
```

### 🧪 Load specific tables from a PostGIS connection

```
inputs:
  source: "postgres://gis@localhost/geo"
  source_type: postgis
  filter: ["geotopes", "geotope_properties"]
  single: false
```

### 📦 Load a single raster layer from a GeoPackage

```
inputs:
  source: data/elevation.gpkg
  source_type: geopackage
  filter: "dtm_10m"
  single: true
```

---

## 💡 Notes

- The `filter` parameter can be a regex (e.g., `.*\.tif$`) or a list of names.
    
- This process does not interpret dataset semantics — only identifies files or layers matching structural rules.
    
- Users must **document and classify** the outputs if used in an ontology-aware workflow.
    
- Can be used in `foreach` blocks to iterate over returned datasets.
    
- Future backends like `s3`, `http`, or `zipfile` may be supported with minimal extensions.
    

---

## 📘 Usage in Pipeline

```
steps:
  - name: load_all_layers
    process: load_data_from_source
    inputs:
      source: "data/dtm_tiles"
      source_type: folder
      filter: "*.tif"
    outputs:
      - elevation_tiles

  - foreach: elevation_tiles
    as: tile
    do:
      - name: slope_{{ tile.name }}
        process: calculate_slope
        inputs:
          raster: "{{ tile.path }}"
```

---

This process bridges the gap between structured GSCE analysis and exploratory or external data workflows.