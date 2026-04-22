---
title: Geodetic Control Points
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_governance
concept: Cognised fixed reference positions for spatial measurement
question: >-
  Where are the geodetic control points, and what coordinates and accuracy do
  they define?
realisations: []
threads: []
tags: []
primary_collection:
primary_collection_path: /Datasets-by-Collection/Grunddatamodellen/Fikspunkter/
entities: []
key_attributes: []
services: {}
---

> **Cognised existence:** A geodetic control point is a monumented position whose coordinates are determined to high accuracy so that all subsequent surveys and mapping can be tied to a common spatial reference. Without control points, independent datasets cannot be spatially registered to one another.

**Question:** Where are the geodetic control points, and what coordinates and accuracy do they define?

---

## Realisations

### 1. Fikspunkter — National Geodetic Network

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

---

## When to Use This Leaf

- **Datum alignment**: verifying or transforming coordinates between ETRS89, System 34, DVR90, and DNN.
- **Survey control**: anchoring new field measurements to the national reference network.
- **Quality assessment**: checking whether a dataset's spatial accuracy is consistent with the control network it was tied to.

For ordinary address, parcel, or topographic work, control points are usually background infrastructure. Start from [[Leaves/addresses|Addresses]], [[Leaves/cadastral-parcels|Cadastral Parcels]], or [[Leaves/transport-networks|Transport Networks]] instead.

---

## Temporal Model

Bitemporal. Control point coordinates are revised when re-measured; old coordinate vintages remain accessible through `virkningFra`/`virkningTil`.

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/Fikspunkter/index.md|Fikspunkter]] (collection)
## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/Fikspunkter/index.md|Fikspunkter]] (collection)
