---

title: Nature Protection Areas
type: leaf
draft: false
sphere: Biosphere
subsphere: Conservation
concept: Designated areas where nature conservation is the primary land management objective
question: What areas are designated for nature protection at a location?
threads: []
tags:
  - biosphere
  - conservation
  - protected-areas
---

> **Cognised existence:** Nature protection areas are politically designated zones where biodiversity and natural heritage take precedence over other land uses. Their boundaries carry legal weight and are the primary input for conservation planning.

**Question:** What areas are designated for nature protection at a location?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dprotected_area](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dprotected_area) | [https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dnature_reserve](https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dnature_reserve)

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/OpenStreetMap_nature_protection_areas|OpenStreetMap — `boundary=protected_area`, `leisure=nature_reserve`]]**

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `protection_osm_polygon` | OSM via Overpass | Polygon (relation/way) | EPSG:4326 | Area calculation, overlap analysis, map display | Legal boundary disputes — always verify against official national source |

---

## Limitations

- OSM protected area boundaries may lag official updates.
- `protect_class` is not consistently tagged.
- For authoritative data consider: EEA CDDA (Europe), WDPA (global), or national environment agency sources.
