---
title: "SPHERE: Semantic Protocol for Human and Earth Relational Environments"
draft: false
tags:

  - protocol
  - sphere

---

**Semantic Protocol for Human and Earth Relational Environments**

SPHERE is the organising protocol behind this site. It structures how heterogeneous datasets—registries that serve many domains at once—are decomposed into discoverable, purpose-specific units that both humans and AI agents can navigate.

## The Problem

A registry like [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index|CVR]] contains 27 object classes and 361 attributes. It serves questions about industry classification, spatial footprint, ownership structure, financial health, and more. No single description captures all of these purposes. An agent asking "where are Copenhagen's restaurants?" needs different metadata than one asking "who owns this company?"—yet both draw from the same registry.

Flat dataset catalogs force a choice: either one monolithic description per registry (too broad) or one page per entity (too low-level). Neither matches how questions are actually asked.

## The Tree-Crown Metaphor

SPHERE models data as a tree crown:

| Element | Role | Example |
| --- | --- | --- |
| **Branch (Sphere)** | Thematic domain—a cluster of related phenomena | Socio-Technical, Hydrosphere, Biosphere |
| **Twig (Subsphere)** | Narrower domain within a sphere | Governance, Infrastructure, Socioeconomic |
| **Leaf** | A semantic aspect of a dataset—answers one kind of question | "Business Industry Classification" |
| **Thread** | Cross-domain connection where a leaf is relevant to multiple spheres | Industry codes link Socio-Technical to Biosphere (environmental impact) |

The current protocol uses **7 branches**: Atmosphere, Biosphere, Hydrosphere, Lithosphere, Pedosphere, Socio-Technical, and Toposphere.

### How it works

1. **Spheres** group phenomena by theme (→ [[SPHERE]])
2. **Leaves** decompose registries into purpose-specific semantic aspects (→ [[Leaves/index|Leaves]])
3. Each leaf points down to **Dataset** documentation (→ [[Datasets by Collection]]) and **Services** (GraphQL, WFS, file download)
4. **Threads** tag leaves that cross sphere boundaries, enabling lateral discovery

## The Architecture Chain

```
Leaf (semantic aspect, answers a question type)
  → Realisation (implementation mapping, join logic, dataset choice)
    → Dataset (registry info, license, temporal model)
      → Service (GraphQL endpoint, WFS, file download, API key)
```

An agent navigating SPHERE:

1. Identifies the **sphere** matching its question domain
2. Browses **leaves** within that sphere to understand the concept conceptually
3. Identifies the **realisation** that best fits its technical or authoritative requirements
4. Follows the realisation's mapping and join logic to the **dataset** documentation
5. Uses **service** references to access the actual data

## Leaf Schema

Every leaf page uses this frontmatter structure:

```yaml
---
title: <human-readable leaf name>
type: leaf
draft: false
sphere: <primary sphere>
subsphere: <subsphere within the primary sphere>
concept: <semantic concept from the collection's semantic organisation>
question: <what kind of question does this leaf help answer?>
threads:
  - <cross-domain thread ids this leaf connects through>
tags:
  - collection/<collection-slug>
---
```

## Threads: Cross-Domain Connections

Many phenomena sit at the boundary between spheres. Industry codes in CVR classify economic activity (Socio-Technical) but also signal environmental impact (Biosphere) and thematic human partitioning of space (Socio-Technical Perception & Thematics). Rather than duplicating leaves, SPHERE uses **threads**—explicit cross-domain relations that connect leaves to other twigs.

An agent exploring the Biosphere can discover CVR industry classification through thread traversal, without CVR needing to "belong" to Biosphere.

For the current graph-first conventions with multi-twig leaves and explicit threads, see [[SPHERE Thread Conventions]].

## Backward Compatibility

The existing 338+ pages in [[Datasets by Collection]] and [[SPHERE]] remain unchanged. They form the **Dataset** tier of the architecture chain. Leaves add a new semantic layer on top, linking down to those pages. Nothing is removed or reorganised.

## Classical Metadata Standards

Three widely-used geospatial classification systems — ISO 19115, INSPIRE, and UN-GGIM — define flat lists of topic categories. SPHERE maps all 67 classical themes into the tree hierarchy, providing a **Rosetta Stone** between legacy catalog keywords and the sphere/subsphere/thread structure. This enables systematic harvesting from existing metadata servers.

See [[Classical Classifications/index|Classical Classifications → SPHERE Mapping]] for the full concordance.

## Navigation

| Starting point | Path |
| --- | --- |
| I have a question about a domain | **[[SPHERE]]** → find sphere → browse leaves |
| I know the registry | **[[Datasets by Collection]]** → registry page → follow leaf backlinks |
| I want to browse all semantic aspects | **[[Leaves/index\\\|All Leaves]]** |
| I have a classical metadata keyword (ISO/INSPIRE/UN-GGIM) | **[[Classical Classifications/index\\\|Classical Classifications]]** → find theme → follow to sphere |
| I want the protocol definition | You are here |

## Status

SPHERE is in pilot phase. The first leaves cover [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index|CVR]] as a proof of concept, decomposing it into four semantic aspects: industry classification, spatial footprint, ownership structure, and financial profile.

## Machine-Readable Discovery

For programmatic agent access, the full sphere/leaf/thread graph is available as a JSON index:

- **Sphere index**: [/assets/sphere-index.v1.json](/assets/sphere-index.v1.json)

This file contains all spheres, leaves with their entities and key attributes, service pointers, and thread cross-references. Agents can fetch this single file to discover everything available.
