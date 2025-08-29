---
title: Python geospatial libraries
draft: false
tags:
---

[Murat Kendir](https://github.com/muratkendir) maintains a list of geospatial libraries for Python (The following is a copy from October  2024 the updated version of his lists can be accesed at https://github.com/tum-gis/geoPythonInfoTree/blob/main/docs/index.md
## Geospatial Libraries



 **Library Name** | **Data Type** | **Accessible Data Sources** | **Tags** 
---|---|---|---
 [altair][1] | Vector |  | visualization 
 [ArcPy][2] | Vector & Raster | ArcGIS | ArcGIS 
 [basemap][3] | Vector & Raster |  | projection 
 [canopy][4] | Vector |  |  
 [cartopy][5] | Vector & Raster |  | analysis visualization 
 [Cgal-bindings][6] | Vector |  |  
 [DataCube][7] | Raster | Satellite Imagery | satellite imagery 
 [descartes][8] | Raster |  | image 
 [earthpy][9] | Vector & Raster |  | plot 
 [EoxServer][10] | Raster & Vector | Earth Observation | ESA 
 [Fiona][11] | Vector |  | read write 
 [FME Python][12] | Vector & Raster |  | FME 
 [Folium][13] | Vector & Raster |  | web map leaflet 
 [GDAL][14] | Vector & Raster |  | manipulation 
 [geemap][15] | Raster & Vector | Google | earth engine 
 [GeoAlchemy2][16] | Vector |  | SpatialLite PostGIS 
 [geographiclib][17] | Vector |  | geodesic calculations 
 [geojsonio][18] | Vector |  | geojson 
 [Geomet][19] | Vector |  | geojson WKT WKB 
 [Geopandas][20] | Vector |  | pandas 
 [geoplot][21] | Vector |  | visualization 
 [Geopy][22] | Vector | Nominatim Google | geocoder 
 [Geos][23] | Vector |  | JTS 
 [geotiff][24] | raster |  | tif 
 [gippy][25] | Raster |  | image processing 
 [Grass][26] | Vector & Raster |  |  
 [h3][27] | Vector |  | uber 
 [ipyleaflet][28] | Raster |  | web map leaflet 
 [istSOS][29] | Vector |  | Sensor 
 [laszip][30] | PointCloud |  | LAS LAZ 
 [liblas][31] | PointCloud |  | LAS LAZ 
 [libosmium][32] | Vector | OSM | OSM 
 [LİDAR][33] | Vector & Raster |  | DEM 
 [mapboxgl-jupyter][34] | Vector & Raster | mapbox | mapbox 
 [mapclassify][35] | Raster |  | choropleth classification 
 [Mapnik][36] | raster |  | Mapnik Boost 
 [MatPlotLib][37] | Vector & Raster |  | visualization 
 [mdal][38] | Vector |  | mesh 
 [networkx][39] | Vector |  | network analysis 
 [Numpy][40] | Vector |  | Array 
 [Opencv-python][41] | Raster |  | Vision 
 [openrouteservice][42] | Vector | openrouteservice | route 
 [OSMnx][43] | Vector | osm | network analysis 
 [pandana][44] | Vector |  | pandas network 
 [pdal][45] | PointCloud |  | pointcloud 
 [peartree][46] | Vector |  | network 
 [psycopgr][47] | Vector |  | pgrouting 
 [pyCWS][48] |  |  | CSW 
 [pygeoapi][49] | Vector |  | OGC Feature API 
 [PyGMT][50] | Vector & Raster | Blue Marble | generic mapping tools 
 [pylas][51] | PointCloud |  | LAS LAZ 
 [pymap3d][52] | Vector |  | ecef coordinate 
 [pyproj][53] | Raster & Vector |  | CS 
 [pyQGIS][54] | Vector & Raster |  | QGIS 
 [pyroutelib3][55] | Vector | osm | routing 
 [pysal][56] | Vector |  | analysis 
 [pyshp][57] | Vector |  | shape 
 [pyWPS][58] |  |  | WPS 
 [Rasterio][59] | Raster |  |  
 [Re][60] | Vector |  | regular expressions 
 [routingpy][61] | Vector | google ors here | routing 
 [RSGISLib][62] | Raster |  | remote sensing 
 [RTree][63] | Vector |  | Spatial indexing 
 [scikit][64] | Raster |  | image 
 [sentinelhub][65] | Raster | sentinel landsat modis |  
 [Shapely][66] | Vector |  |  
 [urbansim][67] | Vector |  | statistical models 
 [verde][68] | Raster |  | gridding 
 [whitebox][69] | Vector & Raster |  | analysis 
 [GemGIS][70] | Vector & Raster |  | height elevation 
 [MovingPandas][71] | Vector |  | moving 
 [GeoSnap][72] | Vector |  | Neighbourhood 
 [GeoCube][73] | Vector |  | geopandas xarray 
 [SQLAlchemy][74] | Database |  | SQL 
 [GeoViews][75] | Vector & Raster |  | geographic 
 [TensorFlow][76] | Vector & Raster |  | machine learning 
 [Keras][77] | Vector |  | deep learning 
 [Hugging Face][78] | Semantics |  | NLP 
 [GeoParquet][79] | Vector & Raster |  | io 
 [GeoPySpark][80] | Raster |  | raster processing 
 [GeoDjango][81] | Vector & Raster |  | web framework 
 [PyGIMLi][82] | Vector & Raster |  | geophysics 
 [PyNIO][83] | Vector & Raster |  | climate weather 
 [OWSLib][84] | Vector & Raster |  | wms wfs wmts 
 [PyOGC][85] | Vector & Raster |  | wms wfs feature 
 [Plotly][86] | Raster |  | wms wmts xyz 
 [pyDeck][87] | Vector & Raster |  | map geojson 3D 
 [Osrm-py][88] | Vector |  | routing 
 [pylode][89] | Vector |  | ontology 
 [pytdml][90] | Vector & Raster |  | AI, training, learning 
 [esridump][91] | Vector |  | shp, geojson, esri 

[1]: https://altair-viz.github.io/index.html
[2]: https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/alphabetical-list-of-arcpy-functions.htm
[3]: https://matplotlib.org/basemap/users/index.html
[4]: https://github.com/CanopySimulations/canopy-python
[5]: https://scitools.org.uk/cartopy/docs/latest/reference/index.html
[6]: https://github.com/sciencectn/cgal-bindings
[7]: https://datacube-core.readthedocs.io/en/latest/api/core-classes/datacube.html
[8]: https://pypi.org/project/descartes/
[9]: https://earthpy.readthedocs.io/en/latest/
[10]: https://docs.eoxserver.org/en/stable/apidoc/modules.html
[11]: https://fiona.readthedocs.io/en/stable/
[12]: https://docs.safe.com/fme/html/fmepython/index.html
[13]: https://python-visualization.github.io/folium/
[14]: https://gdal.org/api/python.html
[15]: https://geemap.org/
[16]: https://geoalchemy-2.readthedocs.io/en/latest/index.html
[17]: https://geographiclib.sourceforge.io/1.52/python/index.html
[18]: https://github.com/jwass/geojsonio.py
[19]: https://github.com/geomet/geomet
[20]: https://geopandas.org/en/stable/docs.html
[21]: https://residentmario.github.io/geoplot/api_reference.html
[22]: https://github.com/geopy/geopy
[23]: https://libgeos.org/
[24]: https://github.com/KipCrossing/geotiff
[25]: https://gippy.readthedocs.io/en/latest/
[26]: https://grasswiki.osgeo.org/wiki/GRASS_Python_Scripting_Library
[27]: https://h3geo.org/docs/
[28]: https://github.com/jupyter-widgets/ipyleaflet
[29]: http://istsos.org/en/latest/doc/
[30]: https://github.com/tmontaigu/laszip-python
[31]: https://liblas.org/tutorial/python.html
[32]: https://github.com/osmcode/pyosmium
[33]: https://lidar.gishub.org/
[34]: https://mapbox-mapboxgl-jupyter.readthedocs-hosted.com/en/latest/
[35]: https://github.com/pysal/mapclassify
[36]: https://mapnik.org/docs/v2.2.0/api/python/index.html
[37]: https://matplotlib.org/stable/api/index.html
[38]: https://www.mdal.xyz/api/python_api.html#python-api
[39]: https://networkx.org/documentation/stable/reference/index.html
[40]: https://numpy.org/doc/stable/reference/index.html#reference
[41]: https://pypi.org/project/opencv-python/
[42]: https://openrouteservice.org/dev/#/api-docs
[43]: https://osmnx.readthedocs.io/en/stable/index.html
[44]: http://udst.github.io/pandana/
[45]: https://pdal.io/python.html
[46]: https://github.com/kuanb/peartree
[47]: https://github.com/herrkaefer/psycopgr
[48]: https://pycsw.org/
[49]: https://docs.pygeoapi.io/en/stable/index.html
[50]: https://www.pygmt.org/latest/
[51]: https://pylas.readthedocs.io/en/latest/index.html
[52]: https://geospace-code.github.io/pymap3d/
[53]: https://pyproj4.github.io/pyproj/latest/
[54]: https://qgis.org/pyqgis/master/
[55]: https://github.com/MKuranowski/pyroutelib3
[56]: https://pysal.org/libpysal/api.html
[57]: https://github.com/GeospatialPython/pyshp
[58]: https://pywps.org/
[59]: https://rasterio.readthedocs.io/en/latest/
[60]: https://docs.python.org/3/library/re.html
[61]: https://routingpy.readthedocs.io/en/latest/?badge=latest
[62]: http://rsgislib.org/rsgislib.html
[63]: https://toblerity.org/rtree/
[64]: https://scikit-image.org/docs/stable/api/api.html
[65]: https://sentinelhub-py.readthedocs.io/en/latest/
[66]: https://shapely.readthedocs.io/en/stable/
[67]: https://udst.github.io/urbansim/index.html
[68]: https://www.fatiando.org/verde/latest/
[69]: https://github.com/giswqs/whitebox-python
[70]: https://gemgis.readthedocs.io
[71]: https://movingpandas.github.io/movingpandas/
[72]: https://spatialucr.github.io/geosnap-guide
[73]: https://corteva.github.io/geocube
[74]: https://docs.sqlalchemy.org/en/20/
[75]: https://geoviews.org/
[76]: https://www.tensorflow.org/api_docs/python/tf
[77]: https://keras.io/api/
[78]: https://huggingface.co/
[79]: https://github.com/darcy-r/geoparquet-python
[80]: https://geopyspark.readthedocs.io/en/latest/
[81]: https://docs.djangoproject.com/en/3.2/ref/contrib/gis/
[82]: https://www.pygimli.org/documentation.html
[83]: https://www.pyngl.ucar.edu/Nio.shtml
[84]: https://owslib.readthedocs.io/en/latest/
[85]: https://github.com/RyanWalker277/PyOGC
[86]: https://plotly.com/python/
[87]: https://deckgl.readthedocs.io/en/latest/index.html
[88]: https://github.com/gojuno/osrm-py
[89]: https://pypi.org/project/pylode/
[90]: https://github.com/TrainingDML/pytdml
[91]: https://github.com/openaddresses/pyesridump