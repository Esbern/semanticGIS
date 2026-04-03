---
title: A - Explanatory material
draft: false
tags:
---
## The Sanitisation Ritual: Reconstructing Reality

Phase 3 is the bridge between your **World of Discourse** (the ideal model) and the **World of Observation** (the messy reality). The goal is to move data from the "Wild" into your **Data Sanctuary**. This is not a simple import; it is an evaluation process where you decide if a dataset is worthy of your project's logic.

### 1. The Evaluation Matrix: Accept, Transform, Reject

For every entity defined in your Phase 2 Ontology, you must audit the available "Wild Data" using three possible actions:

#### ✅ Accept: The Perfect Match

The data fits your ontology, boundaries, and NOIR requirements perfectly. It can be moved into the Sanctuary with minimal documentation of its provenance.

- _Example:_ Official municipal boundaries or high-quality national terrain models.
    

#### 🔁 Transform: The Sanitisation Ritual

The data contains the "Truth" you need, but it is fragmented or incorrectly structured. You must perform **Sanitisation Rituals** to make it compatible with your World of Discourse.

- **Fragmentation:** Real-world data is often split across systems. For example, the Danish Business Register (**CVR**) holds industry codes (**DB25**), but lacks geometry. You must **Join** it with the Address Register (**DAR**) to ground it in space.
    
- **Schema Mapping:** Converting "Wild" text (e.g., "Open all night") into your defined NOIR **Interval** (e.g., `Closing_Time: 05:00`).
    

#### ❌ Reject: Triggering Procurement or Backflow

The existing data is either missing, biased, or functionally incompatible with your Intent. When you reject a source, you have two choices:

1. **Direct Procurement (Fieldwork):** You go out and observe the phenomena yourself. In SemanticGIS, fieldwork is treated as "Primary Data Collection"—it is just another way to ground an entity.
    
2. **Backflow:** You return to Phase 2 and humble your model, changing your ontology to match what is actually available.
    

### 2. The Technical Reality: "Spade Work" as Grounding

While many traditional GIS courses treat "joining tables" and "geocoding" as analytical steps, in SemanticGIS, these are part of **Grounding**. Until a dataset is joined, filtered, and geocoded, it does not yet inhabit your World of Discourse.

- **The CVR Challenge:** Reconstructing a "Bar" requires joining the Production Unit, the Industry Code (e.g., `56.30.20`), and the DAR address coordinate.
    
- **The Jurisdictional Filter:** You must overlay your geocoded points with boundaries like **Tivoli Gardens**. Even if a bar exists in the "Wild," your model might **Reject** it because it falls under private, rather than municipal, responsibility.
    

_(Note: For complex multi-table joins and geocoding, refer to [Appendix A: Using Agentic AI for Data Grounding].)_

