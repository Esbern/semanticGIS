---
title: Open Trip Planner  (OTP)
draft: false
tags: 
aliases:
  - OTP
---
**OpenTripPlanner (OTP)** is an advanced, open-source route planning software designed to provide individualised journey suggestions based on multiple criteria, making it a powerful tool for both users and transportation planners. Unlike simpler route planners that focus solely on departure times, OTP takes into account a range of factors such as arrival time, the number of transfers, and accessibility options, offering highly tailored travel solutions.

### **Key Features of OpenTripPlanner**

1. **Multi-Criteria Journey Planning**:
   OTP allows users to plan journeys based on various criteria:
   - **Departure and Arrival Times**: Users can specify either their desired departure or arrival time, and OTP will generate routes that meet these requirements.
   - **Number of Transfers**: OTP considers the number of transfers in a journey, offering routes that minimise changes between different modes of transport.
   - **Accessibility**: OTP supports accessibility options, providing routes that are suitable for individuals with mobility challenges, such as wheelchair users.

2. **Multi-Modal Transport Support**:
   OTP supports a wide range of transportation modes, including:
   - **Walking and Cycling**: For the first and last mile segments of the journey.
   - **Public Transit**: Buses, trains, trams, and other forms of mass transit.
   - **Demand-Responsive Transport (DRT)**: OTP includes support for DRT services, which offer flexible routing and scheduling based on passenger demand, rather than fixed routes and schedules.

### **Data Sources Supported by OpenTripPlanner**

1. **Transit Data**:
   OTP can use both **[[GTFS]] (General Transit Feed Specification)** and **[[NeTEx]] (Network Timetable Exchange)** data for the transit section of the journey. [[GTFS]] is widely used for basic public transit data, while [[NeTEx]] provides a more detailed and feature-rich alternative, allowing OTP to model and optimise complex transit systems accurately.

2. **[[OpenStreetMap]] (OSM) Data**:
   OTP consumes OpenStreetMap data in the `.osm.pbf` format, which is a compact binary format used to store and distribute OSM data. This data provides the detailed street and path networks necessary for modeling the first and last mile of journeys, as well as walking, cycling, and driving routes within urban environments.

### **Algorithms Used in OpenTripPlanner**

OTP uses a combination of sophisticated algorithms to optimise each segment of the journey:

1. **A* Algorithm for the First Mile**:
   The **A* (A-star)** algorithm is used for the first mile segment of the journey, which typically involves walking or cycling from the starting location to the nearest transit stop. The A* algorithm is a pathfinding and graph traversal algorithm that finds the shortest path between two points, considering factors like distance, terrain, and road conditions.

2. **RAPTOR Algorithm for Public Transit**:
   For the transit portion of the journey, OTP employs the **RAPTOR (Round-bAsed Public Transit Optimized Route)** algorithm. RAPTOR is a highly efficient algorithm specifically designed for public transit route planning. It works by quickly evaluating multiple routes to find the optimal path through a public transit network, taking into account schedules, transfers, and travel time. RAPTOR is particularly effective at handling the complex constraints and multiple transfer possibilities inherent in public transit systems.

3. **A* Algorithm for the Last Mile**:
   Similar to the first mile, the last mile segment, which covers the journey from the final transit stop to the destination, is optimized using the A* algorithm. This ensures that the final segment of the trip is efficient and direct, whether the traveler is walking, cycling, or using another mode of transport.

### **Demand-Responsive Transport (DRT) Integration**

OTP's support for [[Demand Response Transport]] **(DRT)** adds an additional layer of flexibility to its route planning capabilities. DRT services are designed to adapt to passenger demand, offering routes and schedules that are not fixed but instead respond to the needs of the users in real-time. This is particularly useful in areas with lower population density or during off-peak hours, where traditional public transport services may be limited.

 In OpenTripPlanner v1 (OTP1), there was a built-in analysis module that allowed for dedicated queries designed to analyse the coverage of the public transport system with tools like travel times from multiple entry points to single destinations, creating travel time surfaces.
With the introduction of OpenTripPlanner v2, the software has been focused on creating travel information for individual travellers. On the official website, they recommend using dedicated analysis software such as [[Conveyal R5]]. However, at the time of writing, it is unclear to me if rural transport has aspects not modded within R5 such as [[Demand Response Transport]]. On the other hand, R5 clearly has tools that are geared towards transport analysis.
# Running OTP
The basic workflow for working with OTP is first to load the street network and transit network, as mentioned. The street network is [[OpenStreetMap]], while the transit data can be either [[GTFS]] or [[NeTEx]]. Then, build a graph of connections in the data set. This can be done simultaneously for both networks, or since the transit network is more volatile, the street network can be built independently and merged.
Once the graph is built, the OTP server can be started. There are three main ways of interacting with the OTP server.  
1. Map-based web interface this facilitates a point and clik planning interface ![[OTP point and click.png]]
2. Web-based query interface. This is primarily for building template queries for the API.  Two dialects of the query language exist and are more or less similar but match the terminology of [[GTFS]] [[NeTEx]], respectively. The query interface is more or less interactive,  for the Transmodel (NeTEx related), the Norwegian developer EnTur has a really nice query builder at https://api.entur.io/graphql-explorer Basic for both API dialects that you first set some criteria for the trip and then some information elements you want returned![[OTP query builder.png]]
3. Standard API
   Each of the two "API" dialects has its own endpoints on your server, assuming the server is running on the local host; the defaults will be "http://localhost:8080/otp/gtfs/v1" for the GTFS dialect and  "http://localhost:8080/otp/transmodel/v3" for the newer tranmodel (NeTEx). The API allows you to write [[Python]] notebooks using [[JupyterLab]] to interface the server to calculate the travel time from all addresses to all schools with an arrival time of 8.00 in the morning. This can then be exported to [[GIS]], such as [[SemanticGIS/Processing Environments/QGIS/index]], for further analysis and visualisation. for an example notebook, see https://github.com/Esbern/transportation-analysis/blob/main/otp.ipynb
    
## Getting data into OTP
By default, the way OTP works is to have a configuration folder for each instance (spatial area , search defaults etc). This folder contains the configuration files stored as [[JSON]]  files as well as the data i.e [[OpenStreetMap]] and timetable data.
If we first look at getting [[OpenStreetMap]] data into OTP, the data needs to be stored as an "oms.pdf" file. These files can, for instance, be downloaded from https://download.geofabrik.de/. Here, we, for instance, can download Denmark. If we wish to work with a smaller area of the total country,  the "[[OSM.PBF]]" file can be spatially clipped using [[OSM.PBF#Tools for Manipulating OSM Files|OSM.PBFTools]] and [[Bounding Box]] or a polygon stored in [[GeoJSON]]. 

## Running OTP as a JAR file
The default distribution of OTP is as a "shaded" JAR file, i.e. a monolithic JAR file that contains all needed to run the program. For most uses, this is the best way of running OTP.  Ensure there is a Java runtime (JRE) or Java Development Kit (JDK) on the computer, or download  OPT v2.5 using at least Jave 21. There is a good simple start tutorial at https://docs.opentripplanner.org/en/latest/Basic-Tutorial/. However, note that the memory setting in the tutorial is probably too small for most uses, so increasing `-Xmx2G` to `-Xmx4G` giving the software 4G RAM is probably needed, especialy for larger nares (more complex road network

build the graph
java -Xmx2G -jar otp-shaded-2.7.0.jar --build --save ./data

load and serv the graph
java -Xmx2G -jar otp-shaded-2.7.0.jar --load --serve ./data

## Running OTP in docker
There is a docker image that can relatively easily be started in the case the folder i named Berlin 
> # `create directory for data and config`
> `mkdir berlin`
> # `download OSM`
> `curl -L https://download.geofabrik.de/europe/germany/berlin-latest.osm.pbf -o berlin/osm.pbf`  
> # `download GTFS`
> `curl -L https://vbb.de/vbbgtfs -o berlin/vbb-gtfs.zip`
> # `build graph and save it onto the host system via the volume`
> `docker run --rm -v ./berlin:/var/opentripplanner docker.io/opentripplanner/opentripplanner:latest --build --save`
> # `load and serve graph`
> `docker run -it --rm -p 8080:8080 -v ./berlin:/var/opentripplanner docker.io/c/opentripplanner:latest --load --serve`


