---
title: "Ejendomsvurdering — Assessed Values Realisation of Property Valuation"
type: realisation
draft: false
leaf: Property Valuation
dataset: Ejendomsvurdering
tags:
  - realisation/ejendomsvurdering
  - leaf/property-valuation
---

**Leaf:** [[Leaves/property-valuation|Property Valuation]]
**Dataset:** Ejendomsvurdering — Assessed Values

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

## Temporal Model

Valuation year (`aar`) defines the temporal slice. Only completed ("locked") valuations are published. Historical valuations remain accessible. The underlying bitemporal model (`registreringFra`/`virkningFra`) tracks when each record was registered versus when the valuation became effective.
