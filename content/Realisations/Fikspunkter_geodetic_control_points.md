---
title: "Fikspunkter — National Geodetic Network Realisation of Geodetic Control Points"
type: realisation
draft: false
leaf: Geodetic Control Points
dataset: Fikspunkter
tags:
  - realisation/fikspunkter
  - leaf/geodetic-control-points
---

**Leaf:** [[Leaves/geodetic-control-points|Geodetic Control Points]]
**Dataset:** Fikspunkter — National Geodetic Network

[[Datasets by Collection/Grunddatamodellen/Fikspunkter/index|Fikspunkter]] is Denmark's authoritative register of geodetic control points covering horizontal (plan) and vertical (height) networks for Denmark, Greenland, and the Faroe Islands.

#### Spatial Access Path

```
All fikspunkt entities carry direct GM_Point geometry.

PlanfikspunktDanmark  → point (northing, easting in ETRS89/UTM32N)
HøjdefikspunktDanmark → point + kote (height above DVR90)
FikspunktSys34        → point (legacy System 34 planar coordinates)
HøjdefikspunktDNN     → point + kote (legacy Dansk Normal Nul reference)
```

**No joins needed** — each control point carries its own coordinates.

#### Entity Types

| Entity | Role | Scope |
| --- | --- | --- |
| **PlanfikspunktDanmark** | Horizontal control point | Denmark (ETRS89) |
| **HøjdefikspunktDanmark** | Vertical control point | Denmark (DVR90) |
| **FikspunktSys34** | Legacy horizontal control | Denmark (System 34) |
| **HøjdefikspunktDNN** | Legacy vertical control | Denmark (DNN) |
| **PlanfikspunktGrønland** | Horizontal control point | Greenland |
| **PlanfikspunktFærøerne** | Horizontal control point | Faroe Islands |
| **HøjdefikspunktGrønland** | Vertical control point | Greenland |
| **HøjdefikspunktFærøerne** | Vertical control point | Faroe Islands |

#### Key Attributes

| Attribute | Description |
| --- | --- |
| `fikspunktsnummer` | Unique point identifier |
| `northing` / `easting` | Plane coordinates |
| `kote` | Height value |
| `klasse` | Accuracy class (plan points) |
| `koteklasse` | Accuracy class (height points) |
| `maalemetode` | Survey method |
| `middelfejl` | Mean error estimate |
| `maaleaar` | Year of measurement |

## Temporal Model

Bitemporal. Control point coordinates are revised when re-measured; old coordinate vintages remain accessible through `virkningFra`/`virkningTil`.
