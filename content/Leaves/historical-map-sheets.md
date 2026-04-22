---
title: Historical Map Sheets
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_governance
concept: Cognised geographic divisions of historical cartographic production
question: >-
  Which historical map sheet covers this location, and what cartographic source
  does it represent?
realisations: []
threads: []
tags: []
primary_collection:
primary_collection_path: /Datasets-by-Collection/Grunddatamodellen/HistoriskeKortbladsinddelinger/
entities: []
key_attributes: []
services: {}
---

> **Cognised existence:** A historical map sheet is a defined geographic area for which a printed or drawn cartographic product was produced. The sheet division records which map series, scale, and time period a given area was covered by — serving as an index into Denmark's cartographic heritage.

**Question:** Which historical map sheet covers this location, and what cartographic source does it represent?

---

## Realisations

### 1. HistoriskeKortbladsinddelinger — Map Sheet Index

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

---

## When to Use This Leaf

- **Archival georeferencing**: finding which historical map covers an area of interest and linking to the scanned source via `HKPNlink`.
- **Cartographic history**: understanding how Denmark's mapping evolved across map series and scales.
- **Heritage analysis**: relating modern features to their historical cartographic representation.
- **Temporal context**: the `maalt_aar` and `udgivet_aar` attributes document when an area was surveyed and published, useful for understanding the provenance of historical spatial information.

For modern topographic or cadastral data, use [[Leaves/transport-networks|Transport Networks]], [[Leaves/cadastral-parcels|Cadastral Parcels]], or [[Leaves/elevation|Elevation]] instead.

---

## Temporal Model

Bitemporal. Sheet divisions are versioned through `virkningFra`/`virkningTil`, but in practice most records represent a stable historical footprint. The `maalt_aar` and `udgivet_aar` attributes capture the cartographic temporal provenance directly.

## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/HistoriskeKortbladsinddelinger/index.md|HistoriskeKortbladsinddelinger]] (collection)
## Realised By Links

- [[Datasets by Collection/Grunddatamodellen/HistoriskeKortbladsinddelinger/index.md|HistoriskeKortbladsinddelinger]] (collection)
