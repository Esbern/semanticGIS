---
title: QGIS
draft: false
tags:
  - QGIS
---
QGIS is an Open-Source (free to use) desktop GIS that can handle the needs of most Geospatial projects. In addition to the built-in functionality of QGIS, there are hundreds of so-called plugins that can extend the functionality of QGIS. 

## Installing QGIS.
Installing QGIS is relatively easy just go to https://www.qgis.org/download/. The website normally determines the OS you are using and gives you the option to download a Long-term version or the latest for your OS. **However I do not recommend using the official installers for different reasons**.  For teaching purposes at RUC i recomend using the the [[SemanticGIS]] instillation approach that install a micromamba python environment and runs QGIS in this environment ensures a similar experience on windows and Mac. If you are using a windows computer use the **OSGeo4W** installer her you can costumire your instillation and have e easier update path to new versions. For mac users I recomend installing QGIS in a isolated python environment since many key functions of QGIS do not work in the default python environment of the mac. The easiest is here to follow the instillation description found in the [[SemanticGIS]] project . I recommend using the latest. For **Mac users** please read the tips for the first launch For **Windows users** who know they want to use QGIS for more than just some months I recommend using the OSGeo4W installer since it is easier to update QGIS later.

## Costimising QGIS

QGIS has a lot of options to customise how it looks and feels. It can, therefore, sometimes be difficult to follow [documentation](https://www.qgis.org/resources/hub/) /[[Tutorials]]/[[QGIS demos|Demos]]. There are two primary customisations you will need to master in order to make your QGIS look like the one someone else is using or in time look how you want it to look, and that is [[Changing the UI language]] and [[showing hiding and moving the UI panels]]

## Extending QGIS
Plugins are a powerful feature in QGIS that allow you to extend the functionality of the software. Most plugins are available from the official QGIS Plugin Repository—the “app store” for QGIS. Read about installing and managing plugins in the note [[Managing QGIS plugins]]

## Accessing data in QGIS

Once QGIS is installed and configured, the next task is typically to access some geospatial data. There are many different ways of doing this depending on the data type and method of access. To read more, read the article “[Accessing data in QGIS](https://www.geoinformatics.online/geospatial-technology/general-purpose-gisapps/qgis/accessing-data-in-qgis/)“

## [Up and running with QGIS](https://www.geoinformatics.online/geospatial-technology/general-purpose-gisapps/qgis/up-and-running-with-qgis/)

This article takes you through the first basic steps of using QGIS from loading data to producing a map.