---
title: Habitat Extent
type: leaf
draft: false
sphere: Biosphere
subsphere: biosphere_ecosystems
concept: Delineated spatial extent of habitats and nature-type units
question: Which habitat and nature-type areas are mapped at this location?
realisations:
  - OpenStreetMap
threads: []
tags:
  - biosphere_ecosystems
  - habitat
  - nature
primary_collection: OpenStreetMap
services: {}
---

> **Cognised existence:** Habitat extent describes where ecological units are physically present as mapped spatial entities.

**Question:** Which habitat and nature-type areas are mapped at this location?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Map_features](https://wiki.openstreetmap.org/wiki/Map_features)

---

## Realisations

### OpenStreetMap — natural and habitat proxy tags

OSM does not have a single canonical habitat schema, but many habitat-like extents can be derived from tags such as wetland, heath, scrub, grassland, and woodland.

#### osmnx access

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

habitats = ox.features_from_place(
    "Denmark",
    tags={
        "natural": ["wetland", "heath", "scrub", "grassland", "wood"],
        "landuse": ["forest", "meadow"],
    },
)
```

#### Geofabrik layers

| Layer | Content |
| --- | --- |
| `gis_osm_natural_a_free_1.shp` | Natural polygons |
| `gis_osm_landuse_a_free_1.shp` | Land-use polygons including meadow/forest |

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `habitat_osm_polygons` | OSM via Geofabrik | Polygon | EPSG:4326 | Broad habitat screening, ecological context maps | Legal habitat designation compliance, Annex-level reporting |

---

## Limitations

- Habitat semantics are proxy-based and non-standardized across countries.
- OSM cannot replace official ecological habitat surveys.
- Use as exploratory/open baseline, then validate with authoritative habitat products.

## Realised By Links

- [[Datasets by Collection/OpenStreetMap/index|OpenStreetMap]] (collection)
