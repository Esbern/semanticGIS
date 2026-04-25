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
threads: []
tags: []
---

> **Cognised existence:** A historical map sheet is a defined geographic area for which a printed or drawn cartographic product was produced. The sheet division records which map series, scale, and time period a given area was covered by — serving as an index into Denmark's cartographic heritage.

**Question:** Which historical map sheet covers this location, and what cartographic source does it represent?

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/HistoriskeKortbladsinddelinger_historical_map_sheets|HistoriskeKortbladsinddelinger — Map Sheet Index]]**

---

## When to Use This Leaf

- **Archival georeferencing**: finding which historical map covers an area of interest and linking to the scanned source via `HKPNlink`.
- **Cartographic history**: understanding how Denmark's mapping evolved across map series and scales.
- **Heritage analysis**: relating modern features to their historical cartographic representation.
- **Temporal context**: the `maalt_aar` and `udgivet_aar` attributes document when an area was surveyed and published, useful for understanding the provenance of historical spatial information.

For modern topographic or cadastral data, use [[Leaves/transport-networks|Transport Networks]], [[Leaves/cadastral-parcels|Cadastral Parcels]], or [[Leaves/elevation|Elevation]] instead.

---
