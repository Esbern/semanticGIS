---
title: "Danmarks Højdemodel (DHM) Realisation of Elevation"
type: realisation
draft: false
leaf: Elevation
dataset: Danmarks Højdemodel
tags:
  - realisation/danmarks_h_jdemodel_dhm
  - leaf/elevation
---

**Leaf:** [[Leaves/elevation|Elevation]]
**Dataset:** Danmarks Højdemodel (DHM)

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
