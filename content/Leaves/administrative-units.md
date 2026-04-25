---

title: Administrative Units
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_governance
concept: Cognised territorial divisions for governance and statistical aggregation
question: Which administrative area does a location belong to?
threads: []
tags:
  - socio_technical_governance
  - administrative
---

> **Cognised existence:** Administrative units are territorial divisions defined by governance acts. They exist because a political authority declared them. Their boundaries determine jurisdiction, statistical aggregation, electoral geography, and service responsibility.

**Question:** Which administrative area does a location belong to?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative)

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/OpenStreetMap_administrative_units|OpenStreetMap — `boundary=administrative`]]**
- **[[Realisations/Natural_Earth_administrative_units|Natural Earth — `ne_10m_admin_0_countries`, `ne_10m_admin_1_states_provinces`]]**

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `admin_osm_polygon` | OSM via osmnx / Overpass | Polygon (relation) | EPSG:4326 | Area queries, point-in-polygon, map display, aggregation | Legal boundary disputes — OSM may lag official updates |
| `admin_ne_10m_countries` | Natural Earth 10m — de facto countries | Polygon | EPSG:4326 | Operational global maps, statistics attribution, population linkage | Legal sovereignty disputes |
| `admin_ne_10m_sovereignty` | Natural Earth 10m — de jure sovereignty | Polygon | EPSG:4326 | Diplomatic/legal contexts, treaty and international law framing | Operational routing or services in disputed territories |
| `admin_ne_10m_disputed` | Natural Earth 10m — disputed areas | Polygon | EPSG:4326 | Visualising contested zones, geopolitical analysis | Any authoritative administrative attribution |
| `admin_ne_50m_polygon` | Natural Earth 50m | Polygon | EPSG:4326 | World-view context mapping | Regional or local detail |

---

## Limitations

- OSM administrative boundaries may lag official updates (elections, boundary changes).
- `admin_level` values are country-specific — always check the OSM wiki for the country in question.
- Boundary quality is highest in Europe and North America; variable elsewhere.
- Natural Earth `admin_0_countries` represents de facto administration, not de jure sovereignty — they diverge for ~20–30 territories globally (occupied areas, breakaway states, dependencies). Always confirm which layer is appropriate for the analytical context before use.
