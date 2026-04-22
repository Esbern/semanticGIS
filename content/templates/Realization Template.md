---
title: "[Realization Name]"
type: realization
draft: true
id: real_id_string
source: "[e.g., CVR Register, LiDAR Point Cloud]"
temporal_mmu: "[e.g., 5 changes/hour, episodic, stream]"
flow_mode: "[ant / gauge]"
threads:
  - "[real_id]-realizes-[leaf_id]"
  - "[real_id]-anchored-by-[anchor_id]"
  - "[real_id]-framed-by-[crs_id]"
tags: []
---

> **Spade:** [One sentence describing what this dataset actually contains and who produces it.]

---

## Mandatory Threads

| Thread id | Source | Predicate | Target | Relation type |
|---|---|---|---|---|
| `[real_id]-realizes-[leaf_id]` | `[real_id]` | `realizes_intent_of` | `[leaf_id]` | `realizes_intent_of` |
| `[real_id]-anchored-by-[anchor_id]` | `[real_id]` | `anchored_by` | `[anchor_id]` | `anchored_by` |
| `[real_id]-framed-by-[crs_id]` | `[real_id]` | `framed_by` | `[crs_id]` | `framed_by` |

## Validation Thread (World of Discourse)

| Thread id | Source | Predicate | Target | Relation type |
|---|---|---|---|---|
| `[real_id]-conflicts-with-[other_real_id]` | `[real_id]` | `conflicts_with` | `[other_real_id]` | `conflicts_with` |