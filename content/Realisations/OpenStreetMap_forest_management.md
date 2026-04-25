---
title: "OpenStreetMap — `landuse=forest`, `natural=wood` Realisation of Forest Cover and Management"
type: realisation
draft: false
leaf: Forest Cover and Management
dataset: OpenStreetMap
tags:
  - realisation/openstreetmap
  - leaf/forest-management
---

**Leaf:** [[Leaves/forest-management|Forest Cover and Management]]
**Dataset:** OpenStreetMap — `landuse=forest`, `natural=wood`

OSM distinguishes between managed forest (`landuse=forest`) and natural woodland (`natural=wood`). In practice both are used for forested areas and coverage is globally extensive.

#### osmnx access

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

# Managed forest
forest = ox.features_from_place(
    "Denmark",
    tags={"landuse": "forest"}
)

# Natural woodland
woodland = ox.features_from_place(
    "Denmark",
    tags={"natural": "wood"}
)
```

#### Geofabrik layers

| Layer | Relevant `fclass` values |
| --- | --- |
| `gis_osm_landuse_a_free_1.shp` | `forest` |
| `gis_osm_natural_a_free_1.shp` | `wood` |

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `landuse=forest` | Managed / commercial forest |
| `natural=wood` | Natural or semi-natural woodland |
| `leaf_type=broadleaved` | Broadleaf / deciduous |
| `leaf_type=needleleaved` | Coniferous |
| `leaf_type=mixed` | Mixed |
| `managed=yes/no` | Whether actively managed |
| `name=*` | Forest name |
