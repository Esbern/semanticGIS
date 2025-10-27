---
title: Digital hydrology
draft: false
tags:
aliases:
  - digital hydrology
---
Digital hydrology is concerned with modelling water flow on and below the surface.  There are two main areas of problems that are addressed through digital hydrology:
1. Waterborne transport of unwanted substances either to aquatic receptors such as the sea, lakes, streams, etc. or underground water resources used for drinking water. 
2. Flooding and local water infiltration, here we primarily look at how much water will flow through a given point and how it is distributed in time.

Although the the applications of digital hydrology focus differentiation problem sets in different physical environments
```
└── 📁 Application Domains
    └── 📁 Digital Hydrology
        ├── 📄 0. Introduction to Digital Hydrology
        │    ├── (What are the key concepts? Why is flow special?)
        │    ├── (The central role of DTMs vs. DSMs)
        │
        ├── 📄 1. Deep Dive: Hydrological Conditioning of DFMs
        │    ├── (The detailed discussion of sinks, fill vs. breach, and parameters)
        │
        ├── 📁 Project: Landscape Nutrient Runoff
        │   ├── 📄 0. Context: (The scientific question - "Where are the Critical Source Areas?")
        │   ├── 📄 1. Problem Definition: (Ontology: DTM, Land Use, TWI, Risk)
        │   ├── 📄 2. Data Acquisition: (Finding LULC, DTM, Soils)
        │   ├── 📄 3. Analytical Design: (The abstract pipeline: TWI, Flow Accumulation)
        │   ├── 📄 4. Implementation: (The concrete QGIS/Whitebox recipe)
        │   ├── 📄 5. Results & Communication: (The final CSA risk map)
        │
        ├── 📁 Project: Urban Surface Flooding
        │   ├── 📄 0. Context: (The problem - "Where can we site LAR solutions?")
        │   ├── 📄 1. Problem Definition: (Ontology: DSM, Ponding Depth, Flow Paths)
        │   ├── 📄 2. Data Acquisition: (Finding high-res DSM, buildings)
        │   ├── 📄 3. Analytical Design: (The abstract pipeline: Fill Depressions, Flow Paths)
        │   ├── 📄 4. Implementation: (The concrete recipe)
        │   ├── 📄 5. Results & Communication: (The ponding map for siting rain gardens)
        │
        └── ... (Future project folders)
```



## Surface Water Flow

**The Core Problem:** We start with a raster data set representing elevation (a DTM or DSM). To a computer, this is just a grid of numbers. An algorithm simulating water flow will stop, or "get trapped," in any cell that is lower than all its neighbors. We call these cells **"sinks."**

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