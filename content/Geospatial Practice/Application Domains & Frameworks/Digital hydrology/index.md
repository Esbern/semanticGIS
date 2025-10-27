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

Although the the applications of digital hydrology focus differentiation problem sets in different physical environments they share two common moddeling aspects namely:
1. [[Horisontal flow over a surface]].
2. Vertical flow as infiltration or evaluation.

It is recommended to read these general articles befor reading the specific case articles on
1. Landscape Nutrient Runoff
2. Urban Surface Flooding


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




There is a skima between global moddels and simulation models
It seams it might be intresting to consider the differance betrwwn a static GIS based model like g.wathershead with mor dynamic modells where  percipitation can be varied is time and space.
It looks like [synxflow](https://synxflow.readthedocs.io) could be an intresting starting point.
Also [landlab](https://landlab.github.io/#/) has potential. Although landbab is more focused on landscape forming processes ther is a  tutorial including a video on using landlab for flooding modelling available at https://hatarilabs.com/ih-en/flood-simulation-from-direct-rainfall-with-python-and-landlab-tutorial
	Finaly 