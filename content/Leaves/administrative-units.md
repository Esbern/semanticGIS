---
title: Administrative Units
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_governance
concept: Cognised territorial divisions for governance and statistical aggregation
question: Which administrative area does a location belong to?
realisations:
  - OpenStreetMap
threads: []
tags:
  - socio_technical_governance
  - administrative
primary_collection: OpenStreetMap
services: {}
---

> **Cognised existence:** Administrative units are territorial divisions defined by governance acts. They exist because a political authority declared them. Their boundaries determine jurisdiction, statistical aggregation, electoral geography, and service responsibility.

**Question:** Which administrative area does a location belong to?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative)

---

## Realisations

### OpenStreetMap — `boundary=administrative`

OSM carries administrative boundary relations globally, tagged with `admin_level=*`. The numeric level indicates hierarchical tier but the meaning varies by country.

**Global `admin_level` conventions (varies by country):**

| admin_level | Common use |
| --- | --- |
| 2 | National boundary |
| 4 | State / region / province |
| 6 | County / department |
| 7–8 | Municipality / district |
| 9–10 | Sub-municipal (ward, parish) |

Per-country mappings: [https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative)

#### osmnx access (recommended)

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

# Geocode a named area to its boundary polygon
gdf = ox.geocode_to_gdf("Copenhagen Municipality, Denmark")

# Get all municipalities in a country
municipalities = ox.features_from_place(
    "Denmark",
    tags={"boundary": "administrative", "admin_level": "7"}
)
```

#### Overpass (fallback)

```ql
[out:json][timeout:120];
(
  relation["boundary"="administrative"]["admin_level"="7"]["ISO3166-1"="DK"];
);
out body; >; out skel qt;
```

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `boundary=administrative` | Administrative boundary relation |
| `admin_level=*` | Hierarchy level (country-specific meaning) |
| `name=*` | Official name |
| `name:en=*` | English name |
| `ISO3166-1=*` | ISO country code (level 2) |
| `ISO3166-2=*` | ISO sub-national code |
| `ref=*` | Official code reference |

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `admin_osm_polygon` | OSM via osmnx / Overpass | Polygon (relation) | EPSG:4326 | Area queries, point-in-polygon, map display, aggregation | Legal boundary disputes — OSM may lag official updates |

---

## Limitations

- OSM administrative boundaries may lag official updates (elections, boundary changes).
- `admin_level` values are country-specific — always check the OSM wiki for the country in question.
- Boundary quality is highest in Europe and North America; variable elsewhere.

## Realised By Links

- [[Datasets by Collection/OpenStreetMap/index|OpenStreetMap]] (collection)
