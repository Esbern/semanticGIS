---
title: 
draft: false
tags: 
---
 
### 1. Backflow Report

**Outcome:** Client (City Council) accepted Phase 1's bias warning and funded field work to investigate the "Micro-Geography" of the harbour-front. **New Intent:** To understand the relationship between urban design (Decking/Benches) and social friction (Sound boxes/Shouting).

### 2. The Project Ontology (World of Discourse)

- **Entity: The Venue (Object):** Discrete polygons. Boundary = **Legal Extent** (Walls + Licensed Terrace).
    
- **Entity: Atmospheric Vibrancy (Property Field):** A continuous surface of social intensity derived from noise data and field notes.

- **Entity: Urban Feature (Object):** Tangible polygons (Wooden Decking, Benches, Open Plazas, Natural Vegetation).
    
- **Entity: Social Group (Object):** A discrete point representing a cluster of people.
    
- **Entity: Noise Emission (Field):** A continuous surface representing the reach of specific phenomena (Singing, Shouting, Soundboxes).

- **Entity: The Party Zone (Defined Object):** A "Fuzzy" polygon created where the Vibrancy Field exceeds a specific intensity threshold.
    

### 3. Attribute Ontology & NOIR Grounding

| Entity       | Attribute      | NOIR Level   | Semantic Intent / Inference Rule                             |
| ------------ | -------------- | ------------ | ------------------------------------------------------------ |
| `Venue`      | `Category`     | **Nominal**  | Categorization (Bar, Club, etc.)                             |
| `Venue`      | `Closing_Time` | **Interval** | **Temporality:** Limits the venue's "existence" in time.     |
| `Field_Obs`  | `Vibe_Rank`    | **Ordinal**  | **Subjective** intensity (1-5). _Rule: Median only._         |
| `Noise`      | `dB_Peak`      | **Ratio**    | Continuous Field measurement. All math permitted.            |
| `Urban_Feat` | `Type`         | **Nominal**  | (e.g., Decking, Bench, Plaza). The "Stage" of activity.      |
| `Social_Grp` | `Activity`     | **Nominal**  | (e.g., Sitting, Walking, Dancing).                           |
| `Social_Grp` | `Group_Size`   | **Ratio**    | Actual count. All mathematical inferences permitted.         |
| `Noise_Emis` | `Source`       | **Nominal**  | (e.g., Soundbox, Singing, Shouting).                         |
| `Noise_Emis` | `Intensity`    | **Ordinal**  | (e.g., Audible, Intrusive, Disruptive). _Rule: Median only._ |

### 4. Ontological Decisions

**Delimiting "The Bar":** We model the **Bar** as its legal footprint (Walls + Terrace). However, to capture "Social Friction," we will overlay this with the **Noise Emission Field**. This allows the **Autonomous Orphan** to see how noise from a "Soundbox" spills over from the **Tangible Decking** into "Quiet" **Natural Vegetation** areas.

**Delimiting the "Party":** We have decided that a "Party" exists where a `Social_Grp` with an `Activity` of 'Dancing' or 'Singing' is spatially joined to an `Urban_Feat` of 'Wooden Decking'. This creates a clear, logical rule for identifying the "Informal Zone" that the CVR register cannot see.