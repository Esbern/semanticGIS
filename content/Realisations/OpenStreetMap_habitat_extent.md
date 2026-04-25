---
title: "OpenStreetMap — natural and habitat proxy tags Realisation of Habitat Extent"
type: realisation
draft: false
leaf: Habitat Extent
dataset: OpenStreetMap
tags:
  - realisation/openstreetmap
  - leaf/habitat-extent
---

**Leaf:** [[Leaves/habitat-extent|Habitat Extent]]
**Dataset:** OpenStreetMap — natural and habitat proxy tags

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
