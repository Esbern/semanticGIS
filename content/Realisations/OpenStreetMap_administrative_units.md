---
title: "OpenStreetMap — `boundary=administrative` Realisation of Administrative Units"
type: realisation
draft: false
leaf: Administrative Units
dataset: OpenStreetMap
tags:
  - realisation/openstreetmap
  - leaf/administrative-units
---

**Leaf:** [[Leaves/administrative-units|Administrative Units]]
**Dataset:** OpenStreetMap — `boundary=administrative`

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
