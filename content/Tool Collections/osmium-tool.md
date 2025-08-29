---
title: osmium-tool
draft: false
tags:
---
 osmium-tool is a tool for :
 - Get information about an [[OpenStreetMap]].osm file
- Show the differences between OSM files
- Convert OSM files from one format into another (supports all XML and [[OSM.PBF]] formats and several more)
- Merge and apply change files to an OSM file (with or without history)
- Create OSM change files from OSM data files
- Extract data from OSM history files for a given point in time or a time range
- Sort OSM files
- Create geographical extracts from OSM files
- Filter OSM files by tags
- Filter changesets by many different criteria
- And much more...

Manual available at https://osmcode.org/osmium-tool/manual.html

The tool is, among another thing useful for preparing [[OpenStreetMap]] data for the use in [[OpenTripPlanner]]
I have a [[Docker]] setup that combines osmium-too and [[JupyterLab]] availabul at https://github.com/Esbern/transportation-analysis the notebook for using osmium-tool is https://github.com/Esbern/transportation-analysis/blob/main/osm-pbf_clip.ipynb

