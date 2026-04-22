---
title: Agricultural Land Management
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_resource_utilisation
concept: Agricultural production and land management regimes describing cultivated use classes
question: Which agricultural land-use classes apply in this area?
realisations:
  - OpenStreetMap
threads: []
tags:
  - socio_technical_resource_utilisation
  - agriculture
  - land-use
primary_collection: OpenStreetMap
services: {}
---

> **Cognised existence:** Agricultural land management is the way cultivated surfaces are classified and used over time.

**Question:** Which agricultural land-use classes apply in this area?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:landuse](https://wiki.openstreetmap.org/wiki/Key:landuse)

---

## Realisations

### OpenStreetMap — `landuse=*`

OSM provides global land-use polygons, including agricultural classes such as farmland, meadow, orchard, and vineyard.

#### osmnx access

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

agri = ox.features_from_place(
    "Denmark",
    tags={"landuse": ["farmland", "meadow", "orchard", "vineyard", "greenhouse_horticulture"]},
)
```

#### Geofabrik layer

`gis_osm_landuse_a_free_1.shp` — polygon layer with `fclass` values for land-use classes.

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `landuse=farmland` | Cultivated agricultural land |
| `landuse=meadow` | Meadow / pasture |
| `landuse=orchard` | Orchard |
| `landuse=vineyard` | Vineyard |
| `landuse=greenhouse_horticulture` | Greenhouse production |

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `agri_osm_polygons` | OSM via Geofabrik | Polygon | EPSG:4326 | Area totals, land-use share, overlap with protection zones | Crop-yield modelling and subsidy compliance |

---

## Limitations

- Agricultural classes are broad and not crop-specific.
- Mapping quality depends on local contributors.
- For policy-grade agriculture statistics, use national LPIS or equivalent.

## Realised By Links

- [[Datasets by Collection/OpenStreetMap/index|OpenStreetMap]] (collection)
