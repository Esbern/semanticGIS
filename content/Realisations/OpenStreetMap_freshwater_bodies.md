---
title: "OpenStreetMap — `waterway=*`, `natural=water` Realisation of Surface Freshwater Bodies"
type: realisation
draft: false
leaf: Surface Freshwater Bodies
dataset: OpenStreetMap
tags:
  - realisation/openstreetmap
  - leaf/freshwater-bodies
---

**Leaf:** [[Leaves/freshwater-bodies|Surface Freshwater Bodies]]
**Dataset:** OpenStreetMap — `waterway=*`, `natural=water`

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
