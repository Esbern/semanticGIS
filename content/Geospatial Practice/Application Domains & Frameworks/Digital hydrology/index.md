---
title: Digital hydrology
draft: false
tags:
aliases:
  - digital hydrology
---
 
- **The Core Problem:** We start with a Digital Elevation Model (DEM). To us, it's a landscape. To a computer, it's just a grid of numbers. A raw DEM is often "hydrologically incorrect"—it contains small errors, or "sinks," (cells lower than all neighbors) that act as mathematical black holes, trapping the flow in an algorithm.
    
- **The Goal:** We must "condition" the DEM to create a "hydrologically correct" surface. This means ensuring every cell has an uninterrupted downhill path to the edge of the dataset. This conditioned DEM is our "digital twin" of the landscape's drainage potential