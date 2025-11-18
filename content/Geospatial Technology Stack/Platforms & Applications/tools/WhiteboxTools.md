---
title: WhiteboxTools Open Core (WbT)
draft: true
tags:
---

WhiteboxTools is an advanced geospatial software package and a data analysis platform developed at the University of Guelph’s **[Geomorphometry and Hydrogeomatics Research Group](https://jblindsay.github.io/ghrg/index.html)** (GHRG). The project began in January 2017 and quickly evolved in terms of its analytical capabilities. Some of WhiteboxTools features include:. The **Open Core** is a free open source component consisting of more than 450 tools that can either can be run from either the command line, called from Python or R and finally is also available as plugin got QGIS and ArcGIS

# Installation
Go to  https://www.whiteboxgeo.com/geospatial-software/ and chose Download and then scroll down to wher it sayes # Download WhiteboxTools Open Core vX.X.X (X.X.X)is the current version as of writing this 2.4.0.
You will be presenter with a page based on what the browser thinks your  OS is here you can change to other OS versions if required or just download whitboxTools for the selected OS. This will download a zip file containing all required elements.  The zip files containes a WBT folder 
Copy the WBT folder and its entire contents to any location on your system.  in my case on windows i use the folder C:\OSGeo4W
# Using in QGIS
In order to use WhiteboxTools in QGIS you need a plugin named WhiteboxTools for QGIS see: [[Managing QGIS plugins]]. for a guide on how to install plugins
After installing the plugin you need to tell QGIS wherr you placed the the executabul file from the plugin (it is the WBT folder in the ZIP  file you downloaded and moved earlier.)  You do this by clicking settings -> Options and then choosing the Processing section
![[Pasted image 20251113103603.png]]
click the three dots after WthiteboxTool executabul and locate the whitboxTool executabul. in my case it is C:/OSGeo4W/WBT/whitebox_tools.exe
![[Pasted image 20251113103723.png]]Whitebox tools are now reedy to be used in QGIS. You find the tools in the Processing ->Processing Toolbox and then down in the WhiteboxTools section
![[Pasted image 20251113104900.png]] 
You can read about the differant tools at https://www.whiteboxgeo.com/manual/wbt_book/intro.html
