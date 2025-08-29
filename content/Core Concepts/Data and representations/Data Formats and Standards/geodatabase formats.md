---
title: geodatabase formats
draft: false
tags:
  - Data-format
---
 
Geodatabase is an umbrella term used by ESRI for their proprietary data formats.
The three main variants of the geodatabase used are:
- **File based geotadatas** (FGDB). The file-based GeoDataBase is simply a folder with the .gdb extension. The advantage of the format is its speed, but it lacks native SQL support.
- **Mobile geodatabase** (Mobile GDB), The Mobile GeoDataBase is like the [[GeoPackage]], a SQLite database container, but with ESRI's proprietary spatial data format. Note that ArcGIS Pro can also use [[GeoPackage]] format. 
- **Enterprise Geodatabase**. The enterprise GeoDataBase is like the Mobile GeoDataBase, a database container, in this case typically  [[PostgreSQL]] or Oracle, with ESRI's proprietary spatial data format. Again, ArcGIS Pro can use [[PostgreSQL]] with the public domain [[Open Geospatial Consortium (OGC)]] geodata formats as implemented by [[PostGIS]]



