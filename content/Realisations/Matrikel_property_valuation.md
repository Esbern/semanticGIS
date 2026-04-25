---
title: "Matrikel — Spatial Anchor Realisation of Property Valuation"
type: realisation
draft: false
leaf: Property Valuation
dataset: Matrikel
tags:
  - realisation/matrikel
  - leaf/property-valuation
---

**Leaf:** [[Leaves/property-valuation|Property Valuation]]
**Dataset:** Matrikel — Spatial Anchor

[[Datasets by Collection/Grunddatamodellen/Matrikel/index|Matrikel]] provides the parcel geometry that gives valuations their spatial extent. Join via BFE number.

## Temporal Model

Valuation year (`aar`) defines the temporal slice. Only completed ("locked") valuations are published. Historical valuations remain accessible. The underlying bitemporal model (`registreringFra`/`virkningFra`) tracks when each record was registered versus when the valuation became effective.
