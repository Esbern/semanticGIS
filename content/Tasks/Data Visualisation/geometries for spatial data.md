---
title: Geometries for Spatial Data
draft: false
tags:
---
 When explicitly referencing a location relative to the Earth using coordinates, these coordinates represent simple geometry, such as points, lines, and polygons in 2 (x,y) or 3 (x,y,z) dimensions. While it is also possible to work with time as a dimension, this is typically nor part of the geometry but rather that entities can be represented by different geometries at different times (x,y,z, time). 
 Before diving deeper into this, it is important to remember that coordinates alone are not enough to explicitly refer to a Location Relative to the Earth; we also need to specify the [[Coordinate Reference System (CRS)]].
For a Python-based demonstration of how points, lines, and polygons can be used to represent spatial data, see https://github.com/Esbern/GIS_demo/blob/main/simplegeodata_plot.ipynb
While the Python demonstration illustrates the essence of geometries for spatial data, Desktop GIS and their underlying data structures add an additional layer of complexity to the set of geometries. The [[GeoPackage]] format operates with not less than 10 different geometry types. [[Geometry types in geopackage database ]]

While the (X,Y,Z) coordinate is the basis for 3D visualisation, the application domains of 3D visualisation and analysis use somewhat different terms from traditional GIS.