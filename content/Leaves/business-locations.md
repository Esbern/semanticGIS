---

title: Business Locations
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_infrastructure
concept: Cognised physical operating locations where enterprises conduct activity
question: Where does a business physically operate?
threads: []
tags:
  - socio_technical_infrastructure
  - business
  - poi
---

> **Cognised existence:** A business location is the physical place where economic activity happens. It is an operational presence in space, not only a legal registration.

**Question:** Where does a business physically operate?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:shop](https://wiki.openstreetmap.org/wiki/Key:shop) | [https://wiki.openstreetmap.org/wiki/Key:amenity](https://wiki.openstreetmap.org/wiki/Key:amenity) | [https://wiki.openstreetmap.org/wiki/Key:office](https://wiki.openstreetmap.org/wiki/Key:office)

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/OpenStreetMap_business_locations|OpenStreetMap — `shop=*`, `amenity=*`, `office=*`]]**

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
