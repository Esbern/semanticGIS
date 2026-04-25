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
threads: []
tags: []
---

> **Cognised existence:** A geodetic control point is a monumented position whose coordinates are determined to high accuracy so that all subsequent surveys and mapping can be tied to a common spatial reference. Without control points, independent datasets cannot be spatially registered to one another.

**Question:** Where are the geodetic control points, and what coordinates and accuracy do they define?

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/Fikspunkter_geodetic_control_points|Fikspunkter — National Geodetic Network]]**

---

## When to Use This Leaf

- **Datum alignment**: verifying or transforming coordinates between ETRS89, System 34, DVR90, and DNN.
- **Survey control**: anchoring new field measurements to the national reference network.
- **Quality assessment**: checking whether a dataset's spatial accuracy is consistent with the control network it was tied to.

For ordinary address, parcel, or topographic work, control points are usually background infrastructure. Start from [[Leaves/addresses|Addresses]], [[Leaves/cadastral-parcels|Cadastral Parcels]], or [[Leaves/transport-networks|Transport Networks]] instead.

---
