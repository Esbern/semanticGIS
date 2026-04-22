---
title: SPHERE Thread Conventions
draft: false
tags:

  - protocol
  - sphere
  - graph

---

This note defines how SPHERE models cross-domain concepts that do not fit a strict tree.

## Core Rules

1. SPHERE is graph-native. Branches and twigs are navigation views.
2. A leaf may belong to one or many twigs.
3. Twig membership is descriptive, not exclusive ownership.
4. Cross-domain relations are explicit threads, not only tags.
5. Tags are for filtering and search, not semantic relation logic.

## Leaf Membership Model

Each leaf can declare:

- `twig_membership`: one or many twig aliases
- `primary_lens`: optional preferred entry lens for navigation
- `threads`: explicit relation ids connecting this leaf to one twig per thread
- `flow_mode`: `gauge` for place-fixed state series, or `ant` for moving-entity traces
- `temporal_mmu`: minimum meaningful update cadence (`static`, `episodic`, `stream`)

When a concept is intrinsically cross-domain, `primary_lens` can be omitted.

The ant metaphor is encoded as `flow_mode: ant` and should be used for trajectories, routes, and moving actors.

## Thread Contract

Each thread must define:

- `id`: stable edge id
- `source`: id of the originating entity (leaf, realization, or anchor)
- `predicate`: the directional verb — chosen from the standard predicate vocabulary below
- `target`: id of the receiving entity (leaf, twig, realization, or anchor)
- `leaf`: source leaf id (for cross-twig threads; same as `source` when source is a leaf)
- `twig`: target twig alias (for cross-twig threads; same as `target` when target is a twig)
- `relation_type`: coarse semantic category of the connection (for agent filtering)
- `question`: what this edge helps answer
- `rationale`: short explanation

### Standard Predicate Vocabulary

| Predicate | Meaning | Typical source → target |
|---|---|---|
| `determines` | Source is a causal or constraining factor for target | Leaf → Leaf |
| `is_property_of` | Source describes an attribute of target | Leaf → Leaf |
| `influences_classification_of` | Source contributes evidence to a classification decision in target | Leaf → Leaf |
| `realizes_intent_of` | Source dataset is the concrete evidence for the question posed by target | Realization → Leaf |
| `anchored_by` | Source is spatially or legally pinned to target unit | Realization → Anchor |
| `framed_by` | Source uses target as its coordinate reference system | Realization → CRS Leaf |
| `conflicts_with` | Source and target disagree on the same question (World of Discourse flag) | Realization → Realization |
| `mandated_by` | Target authority defines or legally requires source | CRS Leaf → Governance Anchor |
| `is_primary_evidence_for` | Source is the canonical input type for target twig | Leaf → Twig |
| `cross_twig_relevance` | Source is relevant to target twig without belonging there primarily | Leaf → Twig |

Thread granularity rule:

- One thread connects one entity to one entity.
- If a leaf is relevant to five twigs, create five threads.
- Do not use multi-target thread arrays.

## Thread-Only Model

Threads are the canonical cross-domain relation model.
Do not add alias fields for older terminology in new files.

## Initial Reference Example

See [[Leaves/bathing-water-quality|Bathing Water Quality]] for a concrete multi-twig leaf using one-thread-per-twig links.
