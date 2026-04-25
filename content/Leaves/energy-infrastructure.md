---

title: Energy Infrastructure
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_infrastructure
concept: Energy generation, transmission, and distribution infrastructure corridors and assets
question: Which energy infrastructures are present here, and what operational constraints apply?
threads: []
tags:
  - socio_technical_infrastructure
  - energy
  - utilities
---

> **Cognised existence:** Energy infrastructure is the spatial network of generation assets, substations, and transmission/distribution lines.

**Question:** Which energy infrastructures are present here, and what operational constraints apply?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:power](https://wiki.openstreetmap.org/wiki/Key:power)

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/OpenStreetMap_energy_infrastructure|OpenStreetMap — `power=*`]]**

---

## Geometry Representations

| Rep ID | Source Dataset | Geometry Type | Native CRS | Suitable For | Not Suitable For |
| --- | --- | --- | --- | --- | --- |
| `energy_osm_lines` | OSM | LineString | EPSG:4326 | Corridor mapping, crossing analysis, length summaries | Grid flow simulation |
| `energy_osm_points_polygons` | OSM | Point/Polygon | EPSG:4326 | Asset inventory maps, proximity to settlements | Capacity and operational dispatch modelling |

---

## Limitations

- Voltage and capacity attributes are incomplete.
- Power network topology may be partially mapped.
- For regulatory planning, validate against national grid operator datasets.
