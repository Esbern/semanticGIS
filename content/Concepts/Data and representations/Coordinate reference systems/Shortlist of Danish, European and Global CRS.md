---
title: Shortlist of Danish, European and Global CRS
draft: false
tags:
  - example-tag
---
 
### Danish CRS
Almost all public geospatial data is delivered in the CRS named ERTS89 / UTM zone 32. The ESPG code for this CRS is 25832. This is a 2D coordinate system but is also used in most Danish 3D, assuming a [[vertical datum]] such as DVR90. For 3D data it is therefor more correct to also specify the vertical datum using a compound CRS such as ESPG 7416, which is ERTS89 / UTM zone 32 + DVR90.

European CRS

| Coordinate reference system/<br>projection | Name and definition                                                                                                                  | Types of coordinates         | When to be used – purpose                                                                                                                                          |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ETRS89                                     | European Terrestrial Reference System 1989                                                                                           | Datum in decimal degrees     | Any scale vector data representation.<br><br>- All reference vector data should be stored as ETRS89 datum.<br><br>- Not suitable for map display purposes.         |
| ETRS-LAEA                                  | Lambert Azimuthal Equal Area 5210<br><br>Latitude of origin: 52 N<br><br>                                                            | Map projection in metres<br> | Small scale mapping 1:500 000 or smaller<br><br>applications including<br><br>- spatial analysis<br><br>- storing raster data<br><br>- map display covering Europe |
| ETRS-LAEA                                  | Lambert Azimuthal Equal Area 5265<br><br>Latitude of origin: 52 N<br><br>Longitude of origin (central meridian): 65 E                | Map projection in metres     | Small scale mapping 1:500 000 or smaller<br><br>applications including<br><br>- map display covering Euasia                                                        |
| ETRS-LCC                                   | Lambert Conformal Conical<br><br>Latitude of origin (Parallels) at 35 N and 65 N<br><br>Longitude of origin (central meridian): 10 E | Map projection in metres     | Small scale mapping<br><br>Only to be used for applications requiring an object to be rendered in its true shape                                                   |
| ETRS-TMzn  (UTM)                           | Universal Transversal Mercator<br><br>Different zones (zn) can be used                                                               | Map projection in metres     | Large-scale mapping<br><br> 1:10 000–1:499 999                                                                                                                     |

For examples of differant projections, see
https://github.com/Esbern/GIS_demo/blob/main/Projections.ipynb