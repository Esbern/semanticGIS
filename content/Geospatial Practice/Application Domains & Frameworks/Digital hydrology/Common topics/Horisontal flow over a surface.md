---
title: Horisontal flow over a surface
draft: false
tags:
---
## Surface Water Flow

**The Core Problem:** All algorithms simulating water flow over a surface are guided be the simpel principal that water flows downwards as a response to gravity. While this seams as a reasonable start assumption it has som severe limitations on how digital hydrology works. The surface water flows over is typical a raster data set representing elevation (a DTM or DSM). To a computer, this is just a grid of numbers and the basic rule of water flowing downwards implies in the digital world water will only flow form a cell with a given value say 20 meters above sea-level to a neighbour cell with a lower value. 
Figur XXX
This opens up two key questions:
1. What to do if there are more than one neighbouring cell with values lower than the current cell ?
2. What to do if there are no neighbouring cells with lower values ?

. An algorithm simulating water flow will stop, or "get trapped," in any cell that is lower than all its neighbors. We call these cells **"sinks."**

**A Critical Distinction: Sinks are Features, Not Just Errors** The term "hydrologically incorrect" is misleading. It's not that the _data_ is wrong; it's that the _raw data_ doesn't represent the _process_ we want to model. Sinks are often real:

- **Landscape Sinks:** In the Danish post-glacial landscape, features like **"dødishuller"** (kettle holes left by melting ice blocks) are true sinks. They are natural retention basins.
    
- **Urban Sinks:** In a city (using a DSM), real sinks are everywhere: courtyards, parks with raised curbs, underpasses, or any area designed to hold water.
    

**The Goal: Conditioning the Surface to Model a Process** To model _connected overland flow_ (i.e., how water moves _across_ the entire landscape), we must first simulate what happens _within_ these sinks. We do this by "filling" them.

The **fill operation** simulates a rain event. It fills these sinks with "digital water" up to their **"pour point"**—the lowest cell on their rim. Once filled, the water "spills" out of this pour point and continues its flow across the landscape.

**"Filling" is a Modeling Choice, Not a "Fix"** This is the most important step. You are not "fixing errors"; you are **setting the parameters of your simulation**. This is why many fill tools (like in Whitebox) have a **maximum fill depth** parameter:

- **No `max_fill` (infinite):** This is for a _theoretical, macro-scale analysis_. You are asking, "What is the total theoretical drainage network if _all_ basins fill and spill?" This is common for regional catchment delineation.
    
- **High `max_fill`:** This models a _major storm event_ (e.g., a 100-year storm). You assume large depressions will fill and connect.
    
- **Low `max_fill` (e.g., 0.15m):** This models a _small, specific rain incident_. You are simulating curb-level flooding. Water will pond in shallow depressions but might not be deep enough to spill out of larger ones (like a park). This is essential for urban modeling and LAR solutions.
    

Therefore, "hydrological conditioning" is your **first and most critical modeling decision**. The parameters you choose define the scientific question you are asking.
    
- **The Goal:** We must "condition" the DEM to create a "hydrologically correct" surface. This means ensuring every cell has an uninterrupted downhill path to the edge of the dataset. This conditioned DEM is our "digital twin" of the landscape's drainage potential


 
One of the main sources of errors in horological modelling is bridges. The problem is that terrain models often are generated from Lidar scanning of the surface, resulting in the bridge being represented as the surface. In practice, this means that the bridge functions as a dam in the hydrological model. To ensure correct hydrological modelling, it is common to create  where bridges are removed.