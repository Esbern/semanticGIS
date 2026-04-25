---
title: "OpenStreetMap — `building=*` Realisation of Buildings"
type: realisation
draft: false
leaf: Buildings
dataset: OpenStreetMap
tags:
  - realisation/openstreetmap
  - leaf/buildings
---

**Leaf:** [[Leaves/buildings|Buildings]]
**Dataset:** OpenStreetMap — `building=*`

OSM contains building footprints globally. Coverage is excellent in urban areas and variable in rural and developing regions.

**Primary tag:** `building=yes` (generic), or typed values such as `building=residential`, `building=commercial`, `building=school`, `building=hospital`.

#### osmnx access

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

buildings = ox.features_from_place(
    "Copenhagen, Denmark",
    tags={"building": True}
)
# Returns GeoDataFrame, geometry = Polygon/MultiPolygon, CRS = EPSG:4326
```

#### Geofabrik layer

`gis_osm_buildings_a_free_1.shp` — polygon layer, fields: `osm_id`, `code`, `fclass`, `name`.

#### Overpass (fallback)

```ql
[out:json][timeout:90];
area["name"="Copenhagen"]["admin_level"="7"]->.a;
(way["building"](area.a); relation["building"](area.a););
out body; >; out skel qt;
```

#### Key OSM attributes

| Tag | Meaning |
| --- | --- |
| `building=*` | Building type (residential, commercial, industrial, school) |
| `building:levels=*` | Number of above-ground floors |
| `start_date=*` | Construction year (sparse) |
| `name=*` | Building name (public buildings) |
| `addr:housenumber`, `addr:street` | Address tags (variable coverage) |
