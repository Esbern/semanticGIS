---
title: Elevation
type: leaf
draft: true
sphere: Toposphere
subsphere: toposphere_topography_bathymetry
concept: Cognised vertical position of the Earth's surface
question: What is the elevation at a given location?
realisations: []
threads:
  - elevation-to-hydrosphere-freshwater-surface
tags:
  - hydrosphere_freshwater_surface
primary_collection:
entities: []
key_attributes: []
services: {}
---

> **Cognised existence:** Elevation is the vertical distance of a point on the Earth's surface above a datum. It determines where water flows, where floods reach, how much sun a slope receives, and what is visible from a point.

**Question:** What is the elevation at a given location?

---

## Realisations

### 1. Danmarks Højdemodel (DHM)

[[Datasets by Collection/Grunddatamodellen/DHMOprindelse/index|DHM]] provides Denmark's national elevation data from airborne LiDAR.

#### Spatial Access Path

```
DHM products are raster/point cloud — no entity joins.
Access is by spatial query: give coordinates, get elevation.

DTM (Terrænmodel): bare-earth elevation (0.4m grid)
  └─ Use: hydrology, flood modelling, slope analysis

DSM (Overflademodel): including buildings, vegetation (0.4m grid)
  └─ Use: visibility analysis, urban modelling, solar potential

Point cloud: raw LiDAR returns (~4-5 pts/m²)
  └─ Use: custom processing, building extraction, forestry

Contour lines: derived from DTM (0.5m and 2.5m intervals)
  └─ Use: cartographic display, terrain visualisation

Origin and quality layers: provenance and acquisition context for the DHM products
  └─ Use: quality control, lineage, and interpreting model generation

Historical releases and hillshades: archived DHM vintages and derived terrain visualisations
  └─ Use: temporal comparison, visual interpretation, and archaeological or landscape reading
```

#### Key Attributes

| Attribute | Description |
| --- | --- |
| `elevation_value` | Height in metres above DVR90 datum |
| `horizontal_accuracy` | ~0.15m |
| `vertical_accuracy` | ~0.05m (terrain), ~0.10m (surface) |
| `acquisition_date` | LiDAR campaign date |

### 2. Dataforsyningen Tile Services

Elevation data is also served as web services by SDFI:

- **WCS**: Web Coverage Service for elevation grids
- **Download**: GeoTIFF and LAZ tiles
- **Contour WFS**: Vector contour lines

---

## Cross-Domain Relevance (Threads)

- **Hydrosphere**: Elevation drives water flow direction, flood modelling, catchment delineation. DTM is the foundation for hydrological analysis.

## Classical Theme References

| Standard | Theme | Link |
| --- | --- | --- |
| ISO 19115 | Elevation | [[Classical Classifications/ISO 19115/elevation\\\|Elevation]] |
| INSPIRE | Elevation | [[Classical Classifications/INSPIRE/elevation\\\|Elevation]] |
| UN-GGIM | Elevation and Depth | [[Classical Classifications/UN-GGIM/elevation-and-depth\\\|Elevation and Depth]] |

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/DHMOprindelse/index.md|DHMOprindelse]] (collection)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-historik-2007-hoejdekurver-2.md|Danmarks Højdemodel - Historik (2007 Højdekurver)]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-historik-2007-overflademodel-2.md|Danmarks Højdemodel - Historik (2007 Overflademodel)]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-historik-2007-punktsky.md|Danmarks Højdemodel - Historik (2007 Punktsky)]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-historik-2007-terraenmodel-2.md|Danmarks Højdemodel - Historik (2007 Terrænmodel)]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-historik-2015.md|Danmarks Højdemodel - Historik (2015)]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-hoejdekurver.md|Danmarks Højdemodel - Højdekurver]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-oprindelse-2.md|Danmarks Højdemodel - Oprindelse]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-overdrevet-skyggekort.md|Danmarks Højdemodel - Overdrevet Skyggekort]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-overflade.md|Danmarks Højdemodel - Overflade]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-punktsky.md|Danmarks Højdemodel - Punktsky]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-quick-dhm-2.md|Danmarks Højdemodel - Quick DHM]] (owner)
- [[Datasets by Collection/Grunddatamodellen/GeoDanmark/index.md|GeoDanmark]] (collection)

### Unmatched Realisations

- Dataforsyningen
## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/DHMOprindelse/index.md|DHMOprindelse]] (collection)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-historik-2007-hoejdekurver-2.md|Danmarks Højdemodel - Historik (2007 Højdekurver)]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-historik-2007-overflademodel-2.md|Danmarks Højdemodel - Historik (2007 Overflademodel)]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-historik-2007-punktsky.md|Danmarks Højdemodel - Historik (2007 Punktsky)]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-historik-2007-terraenmodel-2.md|Danmarks Højdemodel - Historik (2007 Terrænmodel)]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-historik-2015.md|Danmarks Højdemodel - Historik (2015)]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-hoejdekurver.md|Danmarks Højdemodel - Højdekurver]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-oprindelse-2.md|Danmarks Højdemodel - Oprindelse]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-overdrevet-skyggekort.md|Danmarks Højdemodel - Overdrevet Skyggekort]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-overflade.md|Danmarks Højdemodel - Overflade]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-punktsky.md|Danmarks Højdemodel - Punktsky]] (owner)
- [[Datasets by Owner/klimadatastyrelsen/danmarks-hoejdemodel-quick-dhm-2.md|Danmarks Højdemodel - Quick DHM]] (owner)
- [[Datasets by Collection/Grunddatamodellen/GeoDanmark/index.md|GeoDanmark]] (collection)

### Unmatched Realisations

- Dataforsyningen
