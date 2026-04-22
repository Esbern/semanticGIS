---
title: Geospatial Reference Framework
draft: true
tags:
  - toposphere_geospatial_reference_framework
---


**Sphere:** [Toposphere]

### Description

The **Geospatial Reference Framework** serves as the mathematical and legal substrate of the SPHERE Protocol. It provides the "Geometric DNA" for all entities by defining the specific Coordinate Reference Systems (CRS) and spatial protocols required for a **Realization** to be placed accurately in 3D/4D space.

---

### Key Logic

- **Mathematical Substrate:** This twig does not contain physical shapes (delineations); instead, it contains the mathematical rules that allow those shapes to exist and be interpreted by an AI.
    
- **CRS as Cognitive Entities:** Each coordinate system (e.g., EPSG:25832) is treated as a **Leaf**, acting as a "Logical Interpreter" for datasets.
    
- **Authority Alignment:** Every leaf in this twig is threaded to the **Governance** twig to ensure that the chosen "math" aligns with legal mandates (such as SDFI standards in Denmark or GISCO standards in the EU).
    

---

### Representative Leaves (Mathematical Anchors)

|**Leaf ID**|**Title**|**Intent & Scope**|
|---|---|---|
|`crs_epsg_25832`|**ETRS89 / UTM zone 32N**|The official 2D horizontal grid for Danish administrative and high-precision cadastral data.|
|`crs_epsg_25832_dvr90`|**ETRS89 + DVR90**|The 3D vertical realization using the **Danish Vertical Reference 1990**.|
|`crs_epsg_3035`|**ETRS89-LAEA (Europe)**|The Lambert Azimuthal Equal Area projection used for continental-scale statistical comparisons and EU environmental reporting.|
|`crs_epsg_3857`|**Web Mercator**|The global standard for interactive web maps and visual navigation (Google Maps/OpenStreetMap perspective).|

---

### Standard Operational Attributes

To guide the AI in selecting the correct coordinate frame for a given task, each leaf contains the following:

- **Operational Scale:** [Local, National, or Continental].
    
- **Spatial Coverage:** The specific extent where the CRS is valid (e.g., "Denmark" or "Europe").
    
- **Primary Intent:** The target output type, such as **Print**, **High-Precision Export**, or **Statistical Comparison**.
    

---

### Relational Threads

- **Mandated By:** Threads to `socio_technical_governance` to identify the **Responsible Authority** (e.g., SDFI, Eurostat, or EPSG) behind the coordinate definition.
    
- **Frames:** Threads to **Realizations** to provide the necessary spatial reference for any incoming "Spade" (dataset).