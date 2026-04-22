---
title: Property Valuation
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_socioeconomic
concept: Cognised assessed value of real property for taxation
question: What is the official assessed value of a property?
realisations: []
threads:
  - valuation-to-cadastral-parcels
tags: []
primary_collection:
primary_collection_path: /Datasets-by-Collection/Grunddatamodellen/Ejendomsvurdering/
entities: []
key_attributes: []
services: {}
---

> **Cognised existence:** A property valuation is the state's periodic assessment of a property's monetary value for taxation purposes. It is tied to a legal property unit (BFE) but is not itself a geometric object — its spatial meaning comes from the parcel or building it values.

**Question:** What is the official assessed value of a property?

---

## Realisations

### 1. Ejendomsvurdering — Assessed Values

[[Datasets by Collection/Grunddatamodellen/Ejendomsvurdering/index|Ejendomsvurdering]] is the authoritative register of property valuations.

#### Spatial Access Path

```
VUR_Ejendomsvurdering (assessed value record)
  │  FK: → VUR_Vurderingsejendom (valuation property unit)
  │          │  FK: → VUR_BFEKrydsreference → BFEnummer
  ▼
jordstykke.geometri (from Matrikel, via BFE)
```

Valuations carry **no geometry** of their own. Spatial access requires joining through the **BFE number** to `jordstykke` in [[Datasets by Collection/Grunddatamodellen/Matrikel/index|Matrikel]] for parcel geometry, or to BBR for building geometry.

#### Key Entities

| Entity | Role |
| --- | --- |
| **VUR_Ejendomsvurdering** | The valuation: assessed property value, land value, use code, year |
| **VUR_Vurderingsejendom** | The valuation property unit (may span multiple cadastral parcels) |
| **VUR_BFEKrydsreference** | Cross-reference linking BFE identifiers to valuation records |
| **VUR_Fordeling** | Owner-occupied portion allocation (for mixed-use properties) |
| **VUR_Grundvaerdispecifikation** | Breakdown of land value calculation |
| **VUR_Fritagelse** | Tax exemption records |

#### Key Attributes

| Attribute | Description |
| --- | --- |
| `ejendomvaerdiBeloeb` | Total assessed property value (DKK) |
| `grundvaerdiBeloeb` | Assessed land value (DKK) |
| `aar` | Valuation year (residential: odd years; other: even years) |
| `benyttelseKode` | Property use code |
| `BFEnummer` | Property identifier linking to cadastral register |
| `ESRejendomsnummer` | Legacy property number |

### 2. Matrikel — Spatial Anchor

[[Datasets by Collection/Grunddatamodellen/Matrikel/index|Matrikel]] provides the parcel geometry that gives valuations their spatial extent. Join via BFE number.

---

## Cross-Domain Relevance (Threads)

- **Cadastral Parcels**: Valuations are always tied to legal property units. Start from [[Leaves/cadastral-parcels|Cadastral Parcels]] when the question is about parcel identity, then attach valuation as an attribute.

## When to Use This Leaf

- **Tax analysis**: municipal revenue projections, property tax burden mapping.
- **Value-based spatial analysis**: mapping assessed value per area, identifying valuation outliers.
- **Urban economics**: correlating property values with accessibility, services, or environmental factors.

For questions about who owns a property rather than what it is worth, use [[Leaves/cadastral-parcels|Cadastral Parcels]] instead.

---

## Temporal Model

Valuation year (`aar`) defines the temporal slice. Only completed ("locked") valuations are published. Historical valuations remain accessible. The underlying bitemporal model (`registreringFra`/`virkningFra`) tracks when each record was registered versus when the valuation became effective.

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/Ejendomsvurdering/index.md|Ejendomsvurdering]] (collection)
- [[Datasets by Collection/Grunddatamodellen/Matrikel/index.md|Matrikel]] (collection)
## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/Ejendomsvurdering/index.md|Ejendomsvurdering]] (collection)
- [[Datasets by Collection/Grunddatamodellen/Matrikel/index.md|Matrikel]] (collection)
