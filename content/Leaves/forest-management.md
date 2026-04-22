---
title: Forest Cover and Management
type: leaf
draft: false
sphere: Biosphere
subsphere: Terrestrial_Ecosystems
concept: Forest and woodland areas as land cover and ecological resource
question: Where are forests and woodland areas and what type are they?
realisations:
  - OpenStreetMap
threads: []
tags:
  - biosphere
  - forest
  - land-cover
primary_collection: OpenStreetMap
services: {}
---

> **Cognised existence:** Forests are contiguous areas of tree cover that function as ecological systems, carbon stores, and managed resources. Their spatial extent and type are the primary inputs for biodiversity, climate, and land management analysis.

**Question:** Where are forests and woodland areas and what type are they?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dforest](https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dforest) | [https://wiki.openstreetmap.org/wiki/Tag:natural%3Dwood](https://wiki.openstreetmap.org/wiki/Tag:natural%3Dwood)

---

## Realisations

### OpenStreetMap — `landuse=forest`, `natural=wood`

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

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `forest_osm_polygon` | OSM via Geofabrik | Polygon | EPSG:4326 | Area calculation, fragmentation analysis, map display | Sub-stand classification, age structure, canopy height |

---

## Limitations

- `landuse=forest` vs `natural=wood` distinction is applied inconsistently.
- Species composition and management intensity are not reliably tagged.
- For canopy cover and forest type, consider Global Forest Watch, Copernicus Land Cover, or CORINE Land Cover.

## Realised By Links

- [[Datasets by Collection/OpenStreetMap/index|OpenStreetMap]] (collection)
