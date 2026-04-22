---
title: Nature Protection Areas
type: leaf
draft: false
sphere: Biosphere
subsphere: Conservation
concept: Designated areas where nature conservation is the primary land management objective
question: What areas are designated for nature protection at a location?
realisations:
  - OpenStreetMap
threads: []
tags:
  - biosphere
  - conservation
  - protected-areas
primary_collection: OpenStreetMap
services: {}
---

> **Cognised existence:** Nature protection areas are politically designated zones where biodiversity and natural heritage take precedence over other land uses. Their boundaries carry legal weight and are the primary input for conservation planning.

**Question:** What areas are designated for nature protection at a location?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dprotected_area](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dprotected_area) | [https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dnature_reserve](https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dnature_reserve)

---

## Realisations

### OpenStreetMap — `boundary=protected_area`, `leisure=nature_reserve`

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

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `protection_osm_polygon` | OSM via Overpass | Polygon (relation/way) | EPSG:4326 | Area calculation, overlap analysis, map display | Legal boundary disputes — always verify against official national source |

---

## Limitations

- OSM protected area boundaries may lag official updates.
- `protect_class` is not consistently tagged.
- For authoritative data consider: EEA CDDA (Europe), WDPA (global), or national environment agency sources.

## Realised By Links

- [[Datasets by Collection/OpenStreetMap/index|OpenStreetMap]] (collection)
