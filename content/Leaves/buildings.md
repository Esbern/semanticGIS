---

title: Buildings
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_infrastructure
concept: Cognised physical structures sheltering human activity
question: What buildings exist at a location and what are their characteristics?
threads: []
tags:
  - socio_technical_infrastructure
  - buildings
---

> **Cognised existence:** A building is a roofed, permanent physical structure that shelters human activity. It has use, age, size, and geometric footprint, and these properties may come from different sources.

**Question:** What buildings exist at a location and what are their characteristics?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:building](https://wiki.openstreetmap.org/wiki/Key:building)

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/OpenStreetMap_buildings|OpenStreetMap — `building=*`]]**

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
