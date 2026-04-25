---
title: "OpenStreetMap — `boundary=protected_area`, `leisure=nature_reserve` Realisation of Nature Protection Areas"
type: realisation
draft: false
leaf: Nature Protection Areas
dataset: OpenStreetMap
tags:
  - realisation/openstreetmap
  - leaf/nature-protection-areas
---

**Leaf:** [[Leaves/nature-protection-areas|Nature Protection Areas]]
**Dataset:** OpenStreetMap — `boundary=protected_area`, `leisure=nature_reserve`

OSM maps protected areas globally. Coverage is linked to WDPA (World Database of Protected Areas) imports in many countries.

#### osmnx access

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

# Protected areas
protected = ox.features_from_place(
    "Denmark",
    tags={"boundary": "protected_area"}
)

# Nature reserves
reserves = ox.features_from_place(
    "Denmark",
    tags={"leisure": "nature_reserve"}
)
```

#### Overpass (fallback)

```ql
[out:json][timeout:120];
area["name"="Denmark"]["admin_level"="2"]->.dk;
(
  relation["boundary"="protected_area"](area.dk);
  way["boundary"="protected_area"](area.dk);
  relation["leisure"="nature_reserve"](area.dk);
);
out body; >; out skel qt;
```

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `boundary=protected_area` | Designated protected area of any type |
| `protect_class=*` | IUCN protection category (1a, 1b, 2, 3, 4, 5, 6) |
| `protection_title=*` | Official designation name (e.g. "National Park", "Nature Reserve") |
| `leisure=nature_reserve` | Nature reserve |
| `name=*` | Official name |
| `ref:WDPA=*` | WDPA (World Database of Protected Areas) identifier |
