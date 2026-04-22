---
title: "[CRS Name (e.g., EPSG:25832)]"
type: leaf
draft: true
id: crs_epsg_code
sphere: Toposphere
subsphere: toposphere_geospatial_reference_framework
question: "Which coordinate reference system frames this dataset?"
realisations: []
threads:
  - "[crs_id]-mandated-by-governance"
tags:
  - toposphere_geospatial_reference_framework
flow_mode: static
temporal_mmu: static
---

> **Mathematical intent:** [e.g., ETRS89 / UTM zone 32N — the official 2D horizontal grid for Danish administrative data.]

**Operational Scale:** [Local / National / Continental]  
**Spatial Coverage:** [e.g., Denmark, Europe, Global]  
**Primary Intent:** [e.g., Print, High-Precision Export, Web Map, Statistical Comparison]  
**Responsible Authority:** [e.g., SDFI, EPSG, GISCO]

---

## Governance Thread

| Thread id | Source | Predicate | Target | Relation type |
|---|---|---|---|---|
| `[crs_id]-mandated-by-governance` | `[crs_id]` | `mandated_by` | `socio_technical_governance` | `mandated_by` |