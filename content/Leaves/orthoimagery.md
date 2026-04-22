---
title: Orthoimagery
type: leaf
draft: true
sphere: Toposphere
subsphere: toposphere_remote_sensed_observations
concept: Cognised visual representation of the Earth's surface from above
question: What does the Earth's surface look like at a location?
realisations: []
threads:
  - orthoimagery-to-remote-sensed-observations
  - orthoimagery-to-perception-thematics
tags:
  - toposphere_remote_sensed_observations
  - socio_technical_perception_thematics
flow_mode: gauge
temporal_mmu: episodic
primary_collection:
entities: []
key_attributes: []
services: {}
---

> **Cognised existence:** Orthoimagery is a geometrically corrected aerial or satellite photograph — the surface as seen from above, with positional accuracy. It is the most intuitive spatial data: it shows what the world *looks like*.

**Question:** What does the Earth's surface look like at a location?

---

## Realisations

### 1. GeoDanmark Orthophotos

National aerial photography cooperatively produced by SDFI and municipalities.

#### Spatial Access Path

```
Raster tiles — no entity joins. Access by spatial extent.

Forårsfoto: leaf-off (spring), 12.5 cm resolution, annual
Sommerfoto: leaf-on (summer), 12.5 cm resolution, annual
```

### 2. Dataforsyningen Services

SDFI distributes orthophotos and historical imagery as web services:

- **WMTS/WMS**: Tiled map services for web applications
- **Download**: GeoTIFF tiles
- **Historical archive**: Aerial photos from 1944–present (variable resolution)

### 3. Copernicus (Sentinel-2)

Free European satellite imagery:

- 10m resolution, 13 spectral bands
- 5-day revisit time
- Global coverage

**Spatial access**: All realisations are raster — accessed by spatial extent query, no entity joins.

---

## Cross-Domain Relevance (Threads)

- **Toposphere Imagery & Evidence**: Imagery is direct visual evidence of surface state at acquisition time.
- **Socio-Technical Perception & Thematics**: Thematic classifications derived from imagery belong to human interpretive partitioning layers.

## Classical Theme References

| Standard | Theme | Link |
| --- | --- | --- |
| ISO 19115 | Imagery/BaseMaps/EarthCover | [[Classical Classifications/ISO 19115/imageryBaseMapsEarthCover\\\|Imagery/BaseMaps/EarthCover]] |
| INSPIRE | Orthoimagery | [[Classical Classifications/INSPIRE/orthoimagery\\\|Orthoimagery]] |
| UN-GGIM | Orthoimagery | [[Classical Classifications/UN-GGIM/orthoimagery\\\|Orthoimagery]] |

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/GeoDanmark/index.md|GeoDanmark]] (collection)

### Unmatched Realisations

- Dataforsyningen
- Copernicus
