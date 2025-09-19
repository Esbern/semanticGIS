---
title: Municipality based analysis of public transport coverage (A use case)
draft: false
tags:
  - UseCase
---
 
This use case is set up to demonstrate how to use [[OpenTripPlanner]] to analyse how well the addresses within a municipality are connected to different services.
The steps covered are:
- Downloading all [[Addresses]] for a Danish municipality
- Downloading [[OpenStreetMap]] data for Denmark
- Clipping the [[OpenStreetMap]] data using [[osmium-tool]] to the [[Bounding Box]] of the municipality.
- Downloading the [[GTFS]] data for Denmark
- Downloading the [[NeTEx]] data for Denmark
- Starting [[OpenTripPlanner]]
- Loading the [[GTFS]] and clipped [[OpenStreetMap]] data into [[OpenTripPlanner]]
- Loading the [[NeTEx]] and clipped [[OpenStreetMap]] data into [[OpenTripPlanner]]
- Query a single journey
- Programmatic Query all addressed  in a pandas data frame against a data frame fo destinations

Tools used
- [[Docker]]
- [[JupyterLab]]
- [[Python]]
- [[Pandas]]
- [[osmium-tool]]

Data used
- [[Addresses]]
- [[GTFS]]
- [[NeTEx]]
- [[OpenStreetMap]]

**Code and configuration** for the project can be accessed as a GitHub representative https://github.com/Esbern/transportation-analysis
