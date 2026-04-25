---
title: "Ejerfortegnelsen — Ownership Realisation of Cadastral Parcels"
type: realisation
draft: false
leaf: Cadastral Parcels
dataset: Ejerfortegnelsen
tags:
  - realisation/ejerfortegnelsen
  - leaf/cadastral-parcels
---

**Leaf:** [[Leaves/cadastral-parcels|Cadastral Parcels]]
**Dataset:** Ejerfortegnelsen — Ownership

[[Datasets by Collection/Grunddatamodellen/Ejerfortegnelsen/index|Ejerfortegnelsen]] links parcels to their owners (persons and organisations).

#### Spatial Access Path

```
ejerforhold (ownership record)
  │  FK: → jordstykke (via BFE-nummer or matrikelnummer + ejerlavskode)
  ▼
jordstykke.geometri (from Matrikel)
```

Ownership itself has no geometry — it inherits from the parcel. **2 levels of joins** to get from ownership to space.

## Temporal Model

Bitemporal. Parcel boundaries change through subdivision, merger, and resurvey — all tracked with `virkningFra`/`virkningTil`.
