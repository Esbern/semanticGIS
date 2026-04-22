---
title: Energy Infrastructure
type: leaf
draft: false
sphere: Socio_Technical
subsphere: Socio_technical_infrastructure
concept: Energy generation, transmission, and distribution infrastructure corridors and assets
question: Which energy infrastructures are present here, and what operational constraints apply?
realisations:
  - OpenStreetMap
threads: []
tags:
  - socio_technical_infrastructure
  - energy
  - utilities
primary_collection: OpenStreetMap
services: {}
---

> **Cognised existence:** Energy infrastructure is the spatial network of generation assets, substations, and transmission/distribution lines.

**Question:** Which energy infrastructures are present here, and what operational constraints apply?

**OSM wiki:** [https://wiki.openstreetmap.org/wiki/Key:power](https://wiki.openstreetmap.org/wiki/Key:power)

---

## Realisations

### OpenStreetMap — `power=*`

OSM contains global energy-network features: plants, substations, transmission towers, and power lines.

#### osmnx access

```python
import osmnx as ox
ox.settings.cache_folder = ".cache/"

power_features = ox.features_from_place(
    "Denmark",
    tags={"power": True},
)
```

#### Key OSM tags

| Tag | Meaning |
| --- | --- |
| `power=line` | Transmission/distribution overhead line |
| `power=cable` | Underground/submarine cable |
| `power=substation` | Substation polygon or point |
| `power=plant` | Power plant area |
| `power=generator` | Single generator (wind turbine, solar, etc.) |
| `generator:source=*` | Source type (wind, solar, gas, hydro, etc.) |

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

## Realised By Links

- [[Datasets by Collection/OpenStreetMap/index|OpenStreetMap]] (collection)
