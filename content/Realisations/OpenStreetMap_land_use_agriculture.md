---
title: "OpenStreetMap — `landuse=*` Realisation of Agricultural Land Management"
type: realisation
draft: false
leaf: Agricultural Land Management
dataset: OpenStreetMap
tags:
  - realisation/openstreetmap
  - leaf/land-use-agriculture
---

**Leaf:** [[Leaves/land-use-agriculture|Agricultural Land Management]]
**Dataset:** OpenStreetMap — `landuse=*`

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
