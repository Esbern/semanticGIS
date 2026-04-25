---
title: "OpenStreetMap — `place=*`, `name=*` Realisation of Geographical Names"
type: realisation
draft: false
leaf: Geographical Names
dataset: OpenStreetMap
tags:
  - realisation/openstreetmap
  - leaf/geographical-names
---

**Leaf:** [[Leaves/geographical-names|Geographical Names]]
**Dataset:** OpenStreetMap — `place=*`, `name=*`

OSM contains named place points globally, from cities to hamlets, plus named topographic features. It is the primary open dataset for geocoding and place labelling.

#### osmnx access

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

# All named places in an area
places = ox.features_from_place(
    "Denmark",
    tags={"place": ["city", "town", "village", "hamlet", "suburb"]}
)

# Geocode a place name to coordinates + boundary polygon
gdf = ox.geocode_to_gdf("Aarhus, Denmark")
```

#### Geofabrik layer

`gis_osm_places_free_1.shp` — point layer, fields: `osm_id`, `code`, `fclass` (city/town/village/hamlet/suburb/island…), `name`, `population`.

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `place=city` | City (typically > 100k pop.) |
| `place=town` | Town |
| `place=village` | Village |
| `place=hamlet` | Hamlet |
| `place=suburb` | Suburb or named neighbourhood |
| `place=island` | Island |
| `place=locality` | Named uninhabited location |
| `name=*` | Primary name (local language) |
| `name:en=*` | English name |
| `population=*` | Population estimate (sparse) |
