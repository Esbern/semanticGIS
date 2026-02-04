---
title: The SemanticGIS pipeline Language
draft: false
tags:
aliases:
  - The SemanticGIS pipeline Language
---
 
The Purpose of the semanticGIS pipeline language (sGPL) is to provide a simple way to string GIS operations together.  Primarily for the use in a [[Design rationale]] where sGPL in its own can function as a way of documenting the [[Geospatial Practice/Analytical Modelling/index|Analytical Modelling]] stage of a project. I, however, recommend writing sGPL in a Jupyter notebook like Google Colab because this enables the compilation of the sGPL to flowcharts and visual data models.

The following is an example of a SemanticGIS pipeline 


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


