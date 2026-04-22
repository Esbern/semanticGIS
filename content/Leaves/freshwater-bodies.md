---
title: Surface Freshwater Bodies
type: leaf
draft: false
sphere: Hydrosphere
subsphere: Freshwater_Surface
concept: Lakes, rivers, streams, and other surface freshwater features
question: What surface freshwater bodies exist at a location and how do they flow?
realisations:
  - OpenStreetMap
threads: []
tags:
  - hydrosphere
  - freshwater
  - water
primary_collection: OpenStreetMap
services: {}
---

> **Cognised existence:** Surface freshwater bodies are the visible hydrological features of the landscape — rivers, streams, lakes, ponds, reservoirs, and canals. They are both ecological habitats and infrastructure.

**Question:** What surface freshwater bodies exist at a location and how do they flow?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:waterway](https://wiki.openstreetmap.org/wiki/Key:waterway) | [https://wiki.openstreetmap.org/wiki/Tag:natural%3Dwater](https://wiki.openstreetmap.org/wiki/Tag:natural%3Dwater)

---

## Realisations

### OpenStreetMap — `waterway=*`, `natural=water`

OSM covers rivers, streams, lakes, and canals globally. Linear waterways are tagged on ways; standing water bodies on closed ways or relations.

#### osmnx access

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

# Rivers and streams (linear)
waterways = ox.features_from_place(
    "Copenhagen, Denmark",
    tags={"waterway": ["river", "stream", "canal", "drain"]}
)

# Lakes and ponds (polygon)
water_bodies = ox.features_from_place(
    "Copenhagen, Denmark",
    tags={"natural": "water"}
)
```

#### Geofabrik layers

| Layer | Content |
| --- | --- |
| `gis_osm_waterways_free_1.shp` | Rivers, streams, canals — LineString |
| `gis_osm_water_a_free_1.shp` | Lakes, ponds, reservoirs — Polygon |

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `waterway=river` | River |
| `waterway=stream` | Stream |
| `waterway=canal` | Canal |
| `waterway=drain` | Drainage channel |
| `natural=water` | Water body (lake, pond, reservoir) |
| `water=lake` | Lake (sub-tag of `natural=water`) |
| `water=reservoir` | Reservoir |
| `water=pond` | Pond |
| `name=*` | Name of the water body |

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `freshwater_osm_lines` | OSM via Geofabrik | LineString | EPSG:4326 | Network tracing, flow direction, river mapping | Catchment area calculation |
| `freshwater_osm_polygons` | OSM via Geofabrik | Polygon | EPSG:4326 | Surface area, shoreline mapping | Flow routing, upstream/downstream analysis |

**Important:** For catchment / drainage basin analysis, a DEM-derived hydrological network (e.g. Copernicus DEM + SAGA/WhiteboxTools) is more reliable than OSM waterways.

---

## Limitations

- Small streams are under-mapped in many regions.
- Flow direction is implied by way direction but not always correct.
- For hydrological modelling, supplement with DEM-derived data.

## Realised By Links

- [[Datasets by Collection/OpenStreetMap/index|OpenStreetMap]] (collection)
