---
title: Population
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_socioeconomic
concept: Cognised spatial distribution of human inhabitants and settlement hierarchy
question: How is population distributed and what are settlement characteristics?
realisations:
  - OpenStreetMap
threads: []
tags:
  - socio_technical_socioeconomic
  - population
  - settlements
primary_collection: OpenStreetMap
services: {}
---

> **Cognised existence:** Population is the spatial distribution of people and settlement structure across territory.

**Question:** How is population distributed and what are settlement characteristics?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:place](https://wiki.openstreetmap.org/wiki/Key:place)

---

## Realisations

### OpenStreetMap — settlement proxy via `place=*`

OSM does not model full demographic registers, but it captures settlement hierarchy (city, town, village, hamlet) and some population-tagged places.

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

`gis_osm_places_free_1.shp` — place points with optional `population` field.

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `place=city` | Major settlement |
| `place=town` | Town |
| `place=village` | Village |
| `place=hamlet` | Hamlet |
| `place=suburb` | Suburb/neighborhood |
| `population=*` | Population estimate (optional, sparse) |

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `population_osm_place_points` | OSM via Geofabrik | Point | EPSG:4326 | Settlement hierarchy mapping, nearest-settlement analysis | Official population totals, demographic structure, per-capita reporting |

---

## Limitations

- OSM is not an official census dataset.
- Population figures are sparse and inconsistent.
- Use OSM for settlement structure, then enrich with official census products.

## Realised By Links

- [[Datasets by Collection/OpenStreetMap/index|OpenStreetMap]] (collection)
