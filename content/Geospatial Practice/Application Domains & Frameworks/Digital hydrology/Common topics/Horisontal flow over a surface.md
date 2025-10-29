---
title: Horisontal flow over a surface
draft: false
tags:
---
## Surface Water Flow

**The Core Problem:** Determine the paths of water, sediment,and contaminant movement through a landscape is key in nanny applications. All algorithms simulating water flow over a surface are guided be the simpel principal that water flows downwards as a response to gravity. While this seams as a reasonable start assumption it has som severe limitations on how digital hydrology works. The surface water flows over is typical a raster data set representing elevation (a DTM or DSM). To a computer, this is just a grid of numbers and the basic rule of water flowing downwards implies in the digital world water will only flow form a cell with a given value say 20 meters above sea-level to a neighbour cell with a lower value. 
Figur XXX
This opens up two key questions:
1. What to do if there are more than one neighbouring cell with values lower than the current cell ?
2. What to do if there are no neighbouring cells with lower values ?

### Answering Question 1: How Do We Distribute the Flow?

This is the problem of **flow partitioning**. When water is on a slope (like a ridge or a simple hillside), it doesn't just flow to _one_ point; it _spreads_. Different algorithms, or **Flow Direction Models**, handle this in different ways.

#### 1. The D8 Model (Single Flow Direction)

This is the classic and simplest solution.

- **How it works:** The algorithm looks at all 8 neighboring cells and finds the one with the **steepest gradient** (steepest drop). It then assigns **100% of the flow** from the center cell to that _single_ neighbor.
    
- **The Implication (Our Modeling Choice):** This model is "deterministic" and computationally fast. However, it's a poor representation of real-world physics. On a ridge or flat plain, it forces flow into artificial, parallel lines and cannot model **divergent flow** (water fanning out). It's best suited for steep, V-shaped valleys where flow is highly _convergent_.
    

#### 2. The Multiple Flow Direction (MFD) Model

This model was designed to solve the D8 problem.

- **How it works:** Instead of finding the _single_ steepest cell, this algorithm looks at _all_ neighboring cells that are lower than the center cell. It then **partitions the flow** among them. The amount of flow each neighbor receives is proportional to its gradient—the steeper the drop, the more flow it gets.
    
- **The Implication:** This is much better at modeling **divergent flow** and how water _spreads_ across a landscape. It's an excellent choice for modeling how runoff might spread out from a farm field or across a gentle slope. Its weakness is that it can sometimes be _too_ dispersive, "smearing" the flow too much.
    

#### 3. The D-Infinity (D$\infty$) Model

This is a more sophisticated and physically realistic model.

- **How it works:** The D-Infinity model doesn't limit itself to the 8 discrete directions. Instead, it calculates the **true steepest downhill slope** as a continuous 360-degree **angle** (or vector).
    
- This flow vector will almost always point _between_ two of the 8 neighboring cells. The algorithm then **splits 100% of the flow between only those two cells**. The proportion each cell gets is based on how close the vector angle is to that cell's center.
    
- **The Implication:** This is often the best compromise. It allows for flow to spread (diverge) on ridges and concentrate (converge) in valleys in a way that is less "smeared" than MFD and less "artificial" than D8.
    

The model you choose is a critical analytical decision. The **Flow Accumulation** grid—and thus any subsequent analysis like **Topographic Wetness Index (TWI)**—will look _dramatically_ different depending on whether you chose D8, MFD, or D$\infty$.


An algorithm simulating water flow will stop, or "get trapped," in any cell that is lower than all its neighbors. We call these cells **"sinks."**

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