---
title: Explanatorial meterial
draft: false
tags:
---
## Writing the Ontological Will of the Project

Data modelling in **SemanticGIS** is not a technical exercise in database schema design; it is a philosophical act of creation. In this phase, you are defining the **World of Discourse**—the logic that dictates what is "real" and what is "calculable" within your project.

### 1. The Stewardship Dividend: Backflow and Negotiation

Data modelling does not happen in a vacuum. In our Copenhagen Case Study, the client responded to your Phase 1 **Design Rationale** by allocating resources for **Field Work**. They want to move beyond the business register to understand the "Informal Party Zone."

This is a classic example of **Backflow**. Because you identified the "Unseen" harbour-front in your scope, the client now tasks you with capturing the **Phenomena** of the street: the interplay between Bluetooth "sound boxes," wooden decking, and groups of dancing people. We must now update our model to accommodate these complex, social entities.

### 2. From Phenomena to the World of Discourse

To model effectively, we must understand the layers of reality we are navigating:

- **Phenomena:** These are the raw, sensory inputs—the sights, sounds, and physical experiences of the city. Following Kant, we acknowledge the **Noumenon** (the thing-in-itself) is inaccessible; we only work with the **Phenomenon** (the world as it appears to our sensors or field notes).
    
- **The World of Observation:** This is the realm populated by these raw, unstructured phenomena. It is "Wild" data.
    
- **The World of Discourse:** This is the structured, project-specific reality created when you apply an **Ontology** to your observations. Your ontology determines what "exists." If your ontology defines "Nightlife" but ignores "Bakeries," then bakeries do not exist in your World of Discourse.
    
### 3. Representing Reality: Objects vs. Property Fields

In your World of Discourse, you must choose how to represent phenomena geometrically and logically:

- **Object-Based (Discrete):** You view the world as a collection of distinct **Objects**—Points, Lines, or Polygons. These objects have properties that describe them as a **homogeneous whole** (e.g., a "Building" has one "Construction Date").
    
- **Field-Based (Continuous):** You view the world as a **Property Field**—a spatially continuous surface where values vary at every coordinate. Examples include sound levels, temperature, or "Atmospheric Vibrancy." There is no "whole object"; there is only the value at a specific point in space.
    

### 4. Tangible vs. Defined Entities: The Boundary Problem

As a practitioner, you must navigate the difference between physical certainty and conceptual definition:

- **Tangible Objects:** Physical things with clear edges, like **Benches**, **Wooden Decking**, or **Plazas**
    
- **Defined (Abstract) Objects:** Entities created by human intent or social activity, like a **"Party Zone."**
    

Defining boundaries is a **Wicked Problem**. Consider the "Bar": Is its boundary the physical walls? The legal terrace? Or the "social cloud" of people drinking on the pavement? Your choice depends on your **Intent**. For cleaning crews, the "Social Extent" (where the litter lands) is the only boundary that matters.

### 5. Incorporating Temporality: The Dimension of Change

Temporality is the often-neglected dimension of GIS. It allows the model to capture history, current states, and cycles.

- **Opening Hours:** These define the **Interval** of a venue’s existence. A bar that is closed is, for the purpose of a nighttime analysis, non-existent.
    
- **Seasonality:** Like "Wetlands" in environmental management, our "Harbour Baths" are seasonal entities. They only enter the World of Discourse as "Party Zones" during summer months.

- Temporality allows the model to capture cycles. A "Bench" is a static physical object, but its **Semantic Role** changes. At 10:00 AM, it is "Seating for Elderly"; at 10:00 PM, it is the "Core of a Party Zone." We must use **Temporal Toggles** to reflect when these social entities "exist."

### 6. NOIR: The Rules of Inference

To ensure your **Autonomous Orphan** is scientifically sound, you must assign every attribute a **NOIR Level**. This defines what **mathematical inferences** are logically valid for the "Adoptive Parent" (human or AI):

- **Nominal (Labels):** Categories (e.g., 'Club' vs 'Pub'). _Inference: Mode/Frequency._
    
- **Ordinal (Ranks):** Subjective orders (e.g., 'Quiet' to 'Riotous'). _Inference: Median._ (Calculating a mean is a semantic hallucination).
    
- **Interval (Scales):** Numbers with no true zero (e.g., _Time of Day_, _temperature in degrees Celsius_). _Inference: Differences._
    
- **Ratio (Absolutes):** Numbers with a true zero (e.g., _Decibel levels_). _Inference: All mathematical operations._