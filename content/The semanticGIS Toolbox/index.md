---
title: The semanticGIS Toolbox
draft: false
tags:
aliases:
  - The semanticGIS Toolbox
---
 In this folder you a software agnostic description of the key methods used in a [[GIS-garden/Concepts/SemanticGIS/GIS project|GIS project]]. The methods link to there implementations in [[QGIS]], [[ArcGIS pro]] and .

  At the same time this section also holds the the documentation and structure of the SemanticGIS pipline language

a example of which is given below:


``` 
import semanticGIS as sg
# Initialize the pipeline
pl = sg.pipeline()

# --- Proximity Operations ---
# The .buffer() method will inspect the input_layer and automatically
# call the correct vector or raster implementation.
buffered_layer = pl.proximity.buffer(input_layer, distance=100, dissolve=True)

# --- Overlay Operations ---
intersected_layer = pl.overlay.intersect(vector_layer_a, vector_layer_b)

# --- General Analysis ---
# The .cluster() method works on the attributes of vector or raster data
clustered_layer = pl.analysis.cluster(
    input_layer, 
    method='kmeans', 
    num_clusters=5, 
    fields=['soil_carbon', 'elevation']
)
```