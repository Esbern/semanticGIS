---

title: Property Valuation
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_socioeconomic
concept: Cognised assessed value of real property for taxation
question: What is the official assessed value of a property?
threads:
  - valuation-to-cadastral-parcels
tags: []
---

> **Cognised existence:** A property valuation is the state's periodic assessment of a property's monetary value for taxation purposes. It is tied to a legal property unit (BFE) but is not itself a geometric object — its spatial meaning comes from the parcel or building it values.

**Question:** What is the official assessed value of a property?

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/Ejendomsvurdering_property_valuation|Ejendomsvurdering — Assessed Values]]**
- **[[Realisations/Matrikel_property_valuation|Matrikel — Spatial Anchor]]**

---

## Cross-Domain Relevance (Threads)

- **Cadastral Parcels**: Valuations are always tied to legal property units. Start from [[Leaves/cadastral-parcels|Cadastral Parcels]] when the question is about parcel identity, then attach valuation as an attribute.

## When to Use This Leaf

- **Tax analysis**: municipal revenue projections, property tax burden mapping.
- **Value-based spatial analysis**: mapping assessed value per area, identifying valuation outliers.
- **Urban economics**: correlating property values with accessibility, services, or environmental factors.

For questions about who owns a property rather than what it is worth, use [[Leaves/cadastral-parcels|Cadastral Parcels]] instead.

---
