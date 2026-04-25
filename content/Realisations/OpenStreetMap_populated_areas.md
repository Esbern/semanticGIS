---
title: "OpenStreetMap — settlement entities via `place=*` Realisation of Populated Areas and Settlements"
type: realisation
draft: false
leaf: Populated Areas and Settlements
dataset: OpenStreetMap
tags:
  - realisation/openstreetmap
  - leaf/populated-areas
---

**Leaf:** [[Leaves/populated-areas|Populated Areas and Settlements]]
**Dataset:** OpenStreetMap — settlement entities via `place=*`

OSM models settlements directly using `place` tags. This is suitable for settlement hierarchy mapping and nearest-settlement analysis.

#### osmnx access

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

settlements = ox.features_from_place(
    "Denmark",
    tags={"place": ["city", "town", "village", "hamlet", "suburb"]},
)
```

#### Geofabrik layer

`gis_osm_places_free_1.shp` — place points with optional attributes such as `population`.

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `place=city` | Major settlement |
| `place=town` | Town |
| `place=village` | Village |
| `place=hamlet` | Hamlet |
| `place=suburb` | Suburb/neighborhood |
| `population=*` | Optional settlement population estimate |
