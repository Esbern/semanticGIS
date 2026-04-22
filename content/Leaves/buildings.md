---
title: Buildings
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_infrastructure
concept: Cognised physical structures sheltering human activity
question: What buildings exist at a location and what are their characteristics?
realisations:
  - OpenStreetMap
threads: []
tags:
  - socio_technical_infrastructure
  - buildings
primary_collection: OpenStreetMap
services: {}
---

> **Cognised existence:** A building is a roofed, permanent physical structure that shelters human activity. It has use, age, size, and geometric footprint, and these properties may come from different sources.

**Question:** What buildings exist at a location and what are their characteristics?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:building](https://wiki.openstreetmap.org/wiki/Key:building)

---

## Realisations

### OpenStreetMap — `building=*`

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

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `buildings_osm_footprint` | OpenStreetMap | Polygon | EPSG:4326 | Footprint mapping, area calculation, building count, urban morphology | Register-quality attributes (year, use code, heating) are sparse in OSM |
| `buildings_osm_centroid` | OpenStreetMap (derived) | Point | EPSG:4326 | Density mapping, point-in-polygon, proximity counts | Area statistics, shadow and solar analysis |

**Note:** OSM building footprints are the best globally available open polygon source. Attribute quality varies strongly by region and editing community.

---

## Limitations

- Attribute completeness varies widely by country and urban density.
- Year of construction (`start_date`) is sparse globally.
- Building type tags are inconsistent across regions.

## Realised By Links

- [[Datasets by Collection/OpenStreetMap/index|OpenStreetMap]] (collection)
