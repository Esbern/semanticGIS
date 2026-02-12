---
title: Geospatial Operations
draft: false
tags:
aliases:
  - Geospatial Operations
---

In `semanticGIS`, the geospatial operations are defined into nine semantic groups that try to capture the semantics of the GIS project, as well as the five core phases described in [[Geospatial Practice/index|Geospatial Practice]]

## 1. Data Modelling

### The Architect’s Blueprint

This complex is where the project’s **Ontology** is translated into technical reality. It governs the lifecycle of an asset from its external origin to its "registered" status in the project’s sanctuary.

- **Dimensional Slicing:** Explicitly declaring the scale (e.g., NUTS 3, 1:25k) and temporal window (e.g., bi-temporal start/end) of the data.
    
- **Semantic Assumptions:** Stating domain-specific truths (e.g., "assume dangling road segments") that override generic geometric rules.
    
- **Structural Assertions:** Enforcing the "Contract of Readiness" (e.g., `declare_atomic`, `declare_planar`) through automated repairs like fixing self-intersections or exploding multiparts.
    
- **Asset Registration:** The final "handshake" where a dataset is named and assigned its `SpatialNature` and `MeasurementScale`.
    

## 2. Referencing & Normalization

### Establishing a Common Spatial Language

Before disparate assets can interact, they must be brought into mathematical alignment. This complex manages the translation of location.

- **Coordinate Transformations:** Declaratively reprojecting assets into a shared mathematical framework (e.g., ETRS89/UTM32N).
    
- **Semantic Geocoding:** Translating human-readable references (addresses, place-names) into coordinates.
    
- **Indexing Strategies:** Binning continuous space into discrete global grids (H3, S2) to normalize observations across different source geometries.
    

## 3. Extraction & Filtering

### The Sieve: Isolating Scientific Inquiry

This complex focuses the analysis on the specific subset of features relevant to the research question.

- **Attribute Selection:** Filtering by SQL-like queries to isolate specific classes (e.g., "existing roads" vs "planned roads").
    
- **Spatial Slicing:** Clipping or selecting features based on their relationship to a study area boundary.
    
- **Semantic Refinement:** Discarding "noise" to ensure the analysis-ready database contains only the "signal."
    

## 4. Aggregation & Summarization

### Changing the Scale of Observation

Raw data is often too granular for systemic insight. This complex transforms individual features into statistical summaries.

- **Spatial Grouping:** Dissolving boundaries based on shared attributes (e.g., merging field plots into a "Farm" asset).
    
- **Statistical Reduction:** Calculating sums, means, or counts over a group to move from describing instances to describing trends.
    
- **Raster Resampling:** Coarsening pixel resolution to align with macro-scale environmental variables.
    

## 5. Fuse

### Synthesizing Disparate Realities

The power of GIS lies in connecting data that was collected separately. This complex handles the logic of combination.

- **Topological Overlays:** Intersections, Unions, and Erasures that create new geometries from the overlap of two assets.
    
- **Spatial Joins:** Transferring attributes based on location (e.g., "Attach soil type to this well location").
    
- **Attribute Joins:** Linking tables via unique semantic keys (e.g., NUTS codes).
    

## 6. Geometry Generation

### Materializing Theoretical Structures

Sometimes the required data does not exist; it must be algorithmically created to support the research design.

- **Sampling Frameworks:** Generating random points, regular grids, or transects for fieldwork.
    
- **Convex Hulls & Envelopes:** Generating minimum bounding geometries to define study extents.
    
- **Grid Materialization:** Creating the physical polygon boundaries for DGGS cells (H3/S2) declared in Complex 2.
    

## 7. Morphometry

### Quantifying Form and Structure

Everything in the physical world has a shape that drives processes. This complex turns form into a variable.

- **Terrain Analysis:** Calculating slope, aspect, and curvature from continuous surfaces.
    
- **Geometric Metrics:** Measuring area, perimeter, shape compactness, or fractal dimension.
    
- **Surface Interpolation:** Turning discrete points (fieldwork) into a continuous surface (e.g., Kriging or IDW), creating a new "Registered" asset.
    

## 8. Proximity

### Measuring Influence and Distance

Based on Tobler’s First Law, this complex quantifies the "friction" of the space between assets.

- **Distance Matrices:** Calculating the cost or Euclidean distance between points.
    
- **Buffer Generation:** Creating zones of influence or protection around a feature.
    
- **Density Estimation:** Generating heatmaps (Kernel Density) to visualize the clustering of occurrences.
    

## 9. Visualize

### The Ephemeral View

The ultimate goal of analysis is insight. This complex translates abstract machine data into cognitive patterns.

- **Cartographic Mapping:** Applying symbology, scale bars, and layouts for dissemination.
    
- **Statistical Plotting:** Generating histograms, scatter plots, and box plots to visualize attribute distributions.
    
- **Dashboarding:** Creating interactive views that allow the researcher to "interrogate" the registered assets.