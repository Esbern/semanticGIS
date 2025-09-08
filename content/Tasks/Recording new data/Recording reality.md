---
title: Recording reality
draft: false
tags:
---


### ### The Four Fundamental Methods of Registration

Whether you are conducting an exploratory pilot study or the final, structured survey, you will use one of four fundamental methods to capture data about the world. These methods are universal. What changes between the pilot and the final registration is your **goal**, your **tools**, and your **level of precision**.

- In the **pilot study**, your goal is **exploration**. You use unstructured tools (notebooks, paper maps 📝) to test your ontology and find its weaknesses.
    
- In the **final registration**, your goal is **production**. You use structured tools (survey apps, pre-printed forms 📱) to apply your finalized ontology consistently and create clean data.
    

---

### 1. Delineating: Defining Area Boundaries

This is the act of drawing a line that separates one type of area from another based on your classification rules.

- **During the Pilot:** You'll use a pencil to **sketch** a boundary on a paper map. The goal isn't a perfect line; it's to find where your rules get fuzzy. If you can't decide where the boundary between "park" and "wild area" goes, make a note! That ambiguity is a valuable discovery.
    
- **During Final Registration:** You'll use a GPS-enabled app to create a precise **polygon**. You are no longer questioning the rules but applying them consistently to produce a clean, final feature.
    

---

### 2. Inventorying: Locating and Describing Discrete Objects

This is the act of creating a record for individual, distinct items, noting their location and properties. I've renamed "Mapping" to "Inventorying" to be more precise about the action.

- **During the Pilot:** You'll use a notebook and map to **list** the objects you find, like park benches. You might write, "Found a strange concrete bench, not in my schema. What is it?" This is a successful test of your ontology.
    
- **During Final Registration:** You will use a survey app with a pre-defined form. For each bench, you'll create a new **point feature** and fill in its attributes (`material`, `condition`) from a dropdown list. There are no surprises; the work is systematic.
    

---

### 3. Tracing: Recording a Linear Path

This is the act of capturing the route or trajectory of a moving entity or linear feature.

- **During the Pilot:** You'll **sketch** a path on your map, noting where it's clear and where it disappears. The sketch is a rough record used to understand the nature of the path itself.
    
- **During Final Registration:** You will walk the path and use a GPS tracker in an app to create a smooth, accurate **LineString feature**. The goal is a precise geometric representation.
    

---

### 4. Counting: Tallying Occurrences

This is the act of counting the number of items within a given location or area, resulting in a single numerical attribute.

- **During the Pilot:** You'll make simple **tally marks** in your notebook (e.g., `|||| ||`). You might add a note: "Hard to distinguish between saplings and bushes—re-check definition." You are testing the clarity of what you're supposed to be counting.
    
- **During Final Registration:** You will enter a final number into a specific field in your survey app (e.g., `tree_count: 142`). The action is a final, definitive **data entry**.
## Representing observations: The Spatial Table

Once we have performed our observations—whether by counting, tracing, delineating, or mapping—we need a systematic way to store this information. The universal structure for organizing data is the table. In GIS, we use a special kind of table that has a "spatial awareness."

At its core, all vector-based geospatial data is stored in tables where each row represents a single observed feature (like a specific tree, a single road, or one park) and each column represents an attribute (a characteristic of that feature).

---

### The Anatomy of a Spatial Table

A spatial table has three key components:

1. Rows (or Records): Each row in the table corresponds to a single, discrete feature that was observed in the real world. If you have a dataset of trees, each row represents one individual tree.
    
2. Attribute Columns (or Fields): These are the standard columns you would find in any table. Each column describes a specific property of the features. For our trees, we might have columns for species, height_meters, and condition.
    
3. The Geometry Column: This is the special column that makes a table spatial. It stores the "where" information for each feature. For each row, the geometry column contains the coordinate data that defines the feature's shape—whether it's a point (for a tree), a line (for a road), or a polygon (for a park).
    

Let's look at a simple example of a tree inventory:

|   |   |   |   |   |
|---|---|---|---|---|
|feature_id|species|height_meters|condition|geometry|
|1|Oak|15.2|Good|POINT (55.7 12.5)|
|2|Birch|11.8|Fair|POINT (55.8 12.4)|
|3|Oak|18.5|Good|POINT (55.7 12.6)|

In GIS software, this fundamental structure—a table containing a geometry column—is often referred to as a layer or a feature class. But it's crucial to remember that underneath these labels is the simple, powerful concept of a spatial table.

### The Power of the Table: The Relational Model

The true power of organizing our observations into a spatial table lies in its simple, predictable structure. This clean format isn't just for storage; it's a foundation for action. It allows us to perform powerful operations directly on our data, such as filtering the table to show only the trees in 'Good' condition or combining it with other tables to discover new insights.

These fundamental operations—selecting, transforming, and combining data—are not just ad-hoc tricks. They are formalised in a branch of mathematics known as relational algebra. The relational data model, which you'll find at the heart of nearly all modern database systems and GIS software, is the practical implementation of these mathematical principles. 🧠

Therefore, by structuring our observations into a simple table, we unlock the ability to perform complex, repeatable, and logically sound analysis. It's this robust, formalised approach that elevates GIS from a simple map-making tool to a true analytical science. 
