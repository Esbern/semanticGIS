---
title:
draft: false
tags:
---
 
The Purpose of the semantic GIS pipeline language is to provide a simple way of stringing the GIS operations together. The following is an example of a SemanticGIS pipline 


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