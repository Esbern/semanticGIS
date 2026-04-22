---
title: "[Leaf Title]"
type: leaf
draft: true
id: leaf_id_string
sphere: "[e.g., Socio-Technical]"
subsphere: "[e.g., socio_technical_governance]"
question: "What is the [specific aspect] at this location?"
cognitive_category: "[Anchor / Property / Flux]"
realisations: []
threads: []
tags:
  - "[subsphere_tag]"
flow_mode: "[gauge / ant]"
temporal_mmu: "[static / episodic / stream]"
---

> **Cognitive existence:** [One sentence stating what this leaf represents as a human question about the world.]

**Question:** [Same as frontmatter question]

**Responsible Authority:** [e.g., SDFI, GISCO]

---

## Standard Semantic Threads

| Thread id | Source | Predicate | Target | Relation type |
|---|---|---|---|---|
| `[leaf_id]-is-property-of-[parent]` | `[leaf_id]` | `is_property_of` | `[parent_leaf_id]` | `is_property_of` |
| `[leaf_id]-influences-[related]` | `[leaf_id]` | `influences_classification_of` | `[related_leaf_id]` | `influences_classification_of` |

## Typical Realisations

_List concrete datasets that realize the intent of this leaf._

## Geometry Representations

_Document all geometric encodings available for this leaf concept on this hub. A project must select one explicitly — representations are not interchangeable._

| Rep ID | Source Dataset | Geometry Type | Native CRS | Field Path | Suitable For | Not Suitable For |
|---|---|---|---|---|---|---|
| `[leaf_id]_point` | [Dataset] | Point | EPSG:XXXX | [field.path] | [e.g. density mapping, proximity] | [e.g. area calculation, overlap] |
| `[leaf_id]_polygon` | [Dataset] | Polygon | EPSG:XXXX | [field.path] | [e.g. area statistics, boundary analysis] | [e.g. network routing] |

## Cross-Domain Relevance (Threads)

_Add one entry per twig this leaf connects to outside its primary sphere._