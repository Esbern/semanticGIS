---

title: Habitat Extent
type: leaf
draft: false
sphere: Biosphere
subsphere: biosphere_ecosystems
concept: Delineated spatial extent of habitats and nature-type units
question: Which habitat and nature-type areas are mapped at this location?
threads: []
tags:
  - biosphere_ecosystems
  - habitat
  - nature
---

> **Cognised existence:** Habitat extent describes where ecological units are physically present as mapped spatial entities.

**Question:** Which habitat and nature-type areas are mapped at this location?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Map_features](https://wiki.openstreetmap.org/wiki/Map_features)

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/OpenStreetMap_habitat_extent|OpenStreetMap — natural and habitat proxy tags]]**

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
