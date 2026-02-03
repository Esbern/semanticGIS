---
title: Geospatial Operations
draft: false
tags:
aliases:
  - Geospatial Operations
---

In `semanticGIS`, we distinguish strictly between **Structure** (the nouns: vectors, rasters, lists) and **Operations** (the verbs: transforming, filtering, measuring). Every analytical step you take will fall into one of the following nine foundational complexes.

### 1. Data I/O

The Bridge Between Storage and Memory

Analysis cannot occur on a hard drive; it happens in active memory. This complex manages the critical transition of data between its persistent "resting" state (files like GeoPackages, CSVs, GeoTIFFs, or remote API streams) and the "active" AbstractFeatureSet objects used in our pipelines. Operations here are not about changing data, but about accessing and persisting it. It forces the user to be explicit about the provenance of their inputs and the format of their outputs, ensuring that the entry and exit points of the analytical chain are clearly defined.

### 2. Referencing & Normalization

Establishing a Common Spatial Language

Before two datasets can be compared, they must "speak" the same spatial language. This complex houses operations that transform the method used to describe location.

This includes:
- **Semantic Translation (Geocoding):** Converting human-readable references (addresses, place names) into spatial coordinates.
- **Coordinate Transformations:** Reprojecting data from one mathematical framework (e.g., Lat/Lon) to another (e.g., UTM) to ensure alignment.
- **Indexing Strategies:** Calculating discrete global grid indices (like H3 or S2) to bin continuous space into standard units.
Unlike geometric tools that reshape objects, these operations fundamentally alter the **reference keys** used to define where an object exists, ensuring interoperability across the entire project.

### 3. Extraction & Filtering

The Sieve: Refining the Dataset

Scientific inquiry is often about reduction—isolating the signal from the noise. This complex contains the tools used to reduce a dataset to a specific subset of interest based on defined criteria. Whether you are selecting features based on their attributes (e.g., "Select cities with population > 1 million") or their location (e.g., "Select wells inside this watershed"), the goal is identical: to discard irrelevant data. This is the "WHERE" clause of GIS, focusing the analysis solely on the features that matter to the specific scientific question.

### 4. Aggregation & Summarization
Changing the Scale of Observation

Raw data is often too granular to reveal broad patterns. This complex transforms detailed data into meaningful summaries by grouping elements together. It includes Vector operations like "Group By" and "Dissolve" (merging counties into states) and Raster operations like Resampling (coarsening pixel resolution). By calculating statistics (sums, means, counts) over these groups, we move from describing individual instances to describing systemic trends. This is the primary engine for statistical reporting and multi-scale analysis.

### 5. Fuse

Synthesising Disparate Sources

The power of GIS lies in connecting data that was collected separately. The fuse complex handles the logic of combination, bridging the gap between distinct layers. This includes Attribute Joins (linking tables via ID codes), Spatial Joins (transferring attributes based on location), and Overlays (Intersections and Unions that geometrically combine features). These operations answer questions of relationship: "How does Layer A relate to Layer B?" and are essential for multi-criteria decision making.

### 6. Geometry Generation

Creating New Spatial Features

Sometimes the data you need does not exist; it must be created. This complex covers operations that generate new geometries from scratch or based on algorithmic patterns, rather than modifying existing ones. This includes creating sampling frameworks (random points), defining study extents (bounding boxes), and—crucially—materialising DGGS grids (generating the actual polygon boundaries of H3/S2 cells). These tools allow you to impose a theoretical structure or sampling design onto the physical world.

### 7. Morphometry

Quantifying Form and Structure

Everything in the physical world has a shape, and that shape drives environmental processes. This complex focuses on measuring the geometric properties of objects and surfaces. For Rasters (terrain), this means calculating slope, aspect, and roughness. For Vectors, it involves measuring perimeter, area, shape compactness, or fractal dimension. These operations turn the visual geometry of a feature into quantifiable metrics that can be used as variables in statistical models.

### 8. Proximity

Measuring Influence and Distance

Based on Tobler's First Law of Geography ("Near things are more related than distant things"), this complex quantifies the "friction" of distance. It includes calculating distance matrices between points, generating Buffers to define zones of protection or hazard, and estimating Density (like heatmaps) to visualize clustering. These tools allow us to move beyond simple location ("Where is it?") to context ("What is it near, and how does that neighborhood influence it?").

### 9. Visualise

The Ephemeral View

The ultimate goal of analysis is insight, and insight often requires visual representation. This complex handles the generation of human-readable outputs—maps, charts, histograms, and scatter plots. Unlike other operations that produce data for the next step in the pipeline, visualize operations are "sinks"—they produce ephemeral views for interpretation. They translate the abstract numbers and geometries of the machine into the cognitive patterns of the human analyst.
