---
title: Business Locations
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_infrastructure
concept: Cognised physical operating locations where enterprises conduct activity
question: Where does a business physically operate?
realisations:
  - OpenStreetMap
threads: []
tags:
  - socio_technical_infrastructure
  - business
  - poi
primary_collection: OpenStreetMap
services: {}
---

> **Cognised existence:** A business location is the physical place where economic activity happens. It is an operational presence in space, not only a legal registration.

**Question:** Where does a business physically operate?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:shop](https://wiki.openstreetmap.org/wiki/Key:shop) | [https://wiki.openstreetmap.org/wiki/Key:amenity](https://wiki.openstreetmap.org/wiki/Key:amenity) | [https://wiki.openstreetmap.org/wiki/Key:office](https://wiki.openstreetmap.org/wiki/Key:office)

---

## Realisations

### OpenStreetMap — `shop=*`, `amenity=*`, `office=*`

OSM provides global point and polygon features for businesses and services. Coverage is strongest in dense urban areas.

#### osmnx access

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

businesses = ox.features_from_place(
    "Copenhagen, Denmark",
    tags={
        "shop": True,
        "amenity": ["restaurant", "cafe", "bank", "pharmacy", "hospital", "school"],
        "office": True,
    },
)
```

#### Geofabrik layers

| Layer | Content |
| --- | --- |
| `gis_osm_pois_free_1.shp` | Point POIs including shops and amenities |
| `gis_osm_pois_a_free_1.shp` | Polygon POIs |

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `shop=*` | Retail business class |
| `amenity=*` | Public/commercial service class |
| `office=*` | Office function |
| `name=*` | Business name |
| `brand=*` | Brand chain |
| `opening_hours=*` | Opening schedule |

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `business_osm_points` | OSM via Geofabrik | Point | EPSG:4326 | Distribution mapping, nearest-service search, density analysis | Parcel-level frontage and floor area analysis |
| `business_osm_polygons` | OSM via Geofabrik | Polygon | EPSG:4326 | Site footprint context, land-use overlap | Routing without network graph |

---

## Limitations

- OSM does not provide legal company identifiers by default.
- Categories are community-defined and inconsistent across regions.
- Business closure/opening dynamics are unevenly updated.

## Realised By Links

- [[Datasets by Collection/OpenStreetMap/index|OpenStreetMap]] (collection)
