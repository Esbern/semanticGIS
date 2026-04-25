---
title: "HistoriskeKortbladsinddelinger — Map Sheet Index Realisation of Historical Map Sheets"
type: realisation
draft: false
leaf: Historical Map Sheets
dataset: HistoriskeKortbladsinddelinger
tags:
  - realisation/historiskekortbladsinddelinger
  - leaf/historical-map-sheets
---

**Leaf:** [[Leaves/historical-map-sheets|Historical Map Sheets]]
**Dataset:** HistoriskeKortbladsinddelinger — Map Sheet Index

[[Datasets by Collection/Grunddatamodellen/HistoriskeKortbladsinddelinger/index|HistoriskeKortbladsinddelinger]] provides polygon footprints of historical map-sheet divisions.

#### Spatial Access Path

```
HISTKORT_Kortbladsinddeling → GM_Surface polygon (direct geometry, no joins)
```

Each sheet division carries its own **polygon geometry** representing the geographic extent of a single map sheet.

#### Key Attributes

| Attribute | Description |
| --- | --- |
| `kortbladnummer` | Sheet number/name identifying a geographic area |
| `kortvaerk` | Name of the historical map series |
| `maalestok` | Map scale |
| `navn` | Proper name of the sheet area |
| `daekningomraade` | Coverage area description |
| `maalt_aar` | Year of original survey |
| `udgivet_aar` | Year of publication |
| `sidstRettet_aar` | Year of last correction |
| `HKPNlink` | Hyperlink to scanned map at hkpn.dk |
| `orginalkortprojektion` | Original map projection |
| `originalehjoernekoordinater` | Corner coordinates in original projection |

## Temporal Model

Bitemporal. Sheet divisions are versioned through `virkningFra`/`virkningTil`, but in practice most records represent a stable historical footprint. The `maalt_aar` and `udgivet_aar` attributes capture the cartographic temporal provenance directly.
