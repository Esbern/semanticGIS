---
title: "## Observing reality"
draft: false
tags:
---
## Observing reality

### The Prerequisite: A Well-Defined Ontology

Before any practical observation begins, you must complete the most critical conceptual step: defining your project's ontology. This process establishes your domain of discourse and results in a formal classification schema. This goes beyond simply listing categories; it involves the often complex task of determining what constitutes a single, discrete feature. For instance, is a 'group on a bench' a single entity for a study on public space, or are the individual people the features of interest for a demographic study? The choices you make here are fundamental.

The answers to these questions must be driven directly by your scientific question. An analysis of foot traffic requires mapping individuals, while a study of park utilisation might define 'a group using a bench' as the relevant feature. A theoretical schema, however, rarely survives contact with reality. This is why a pilot study 🧪 is essential. It is an iterative process where you test your definitions in the field, discovering ambiguities and refining your schema against the complexities of the real world. This crucial step ensures your final ontology is not just theoretically sound but practically robust and perfectly aligned with your research goal.

  

### The Four Modes of Observation

#### 1. Counting: Generating Point Features

This is the most fundamental act of observation: noting the presence and frequency of discrete phenomena. It answers the question, "How many are there, and where?" In this method, we treat the location as the constant frame of reference and count the entities within it.

- Geospatial Translation: This directly creates point data. Each observation could be a single point (e.g., tree_location) or a point with a quantitative attribute (e.g., intersection_point with an attribute cyclist_count = 152).
    

#### 2. Tracing: Following an entity through time

This method focuses on capturing dynamics and flow. It answers the question, "Where does it go, and what path does it take?" Here, we treat the entity being studied as the constant and record its changing location over time.

- Geospatial Translation: This naturally produces line data. The resulting LineString represents the trajectory of an object, like a wildlife GPS track, a pedestrian's route, or a stream's path.
    

#### 3. Delineating: Generating Area & Surface Features

This is the method for applying your pre-defined ontology to the landscape. It involves observing a continuous space and partitioning it into discrete, homogeneous units based on your schema. It answers the question, "What is this area like, and where are its boundaries?"

- Geospatial Translation: This is the primary method for creating polygon data (e.g., land cover maps, soil type polygons) or raster data through remote sensing image classification. Each polygon or group of cells represents a distinct class from your ontology.
    

####  4. Mapping: Locating and Characterising Discrete Entities

This method focuses on creating an inventory of individual, well-defined objects within an area at a specific point in time. Much like counting, it provides a snapshot, but instead of a simple tally, it registers the precise location and properties of each entity.

The core of this method isn't about creating boundaries from scratch (as in Delineation), but about locating objects that are already conceptually discrete (a tree, a building, a light pole, a parcel of land).

- Core Question: "Where are the individual things, and what are they like?"
    
- Geospatial Translation: This method produces a feature layer (typically points or polygons) where each feature corresponds to a single entity in reality. For example, it could result in a point layer of trees with attributes for species and height, or a polygon layer of building footprints with an attribute for land_use.
    

### Synthesis: Connecting Method to Provenance

Your choice of observation method and details of it, such as time of day the observations were made, are core elements of the design rationale as they define the origin and nature of your data as well as the basis for a discussion of the sustainability of the data for answering a given task.

|   |   |   |   |
|---|---|---|---|
|Observation Method|Core Question|Focus|Output|
|Counting|How many are there?|Tallying occurrences at a location|A numerical attribute|
|Tracing|Where does it go?|Following a single entity over time|Line Features|
|Delineating|What are the zones?|Partitioning a continuous surface|Polygon/Raster Features|
|Mapping|What and where are the things?|Inventorying discrete entities|Point/Polygon Features|

  

---

## Representing observations: The Spatial Table

Once we have performed our observations—whether by counting, tracing, delineating, or mapping—we need a systematic way to store this information. The universal structure for organizing data is the table. In GIS, we use a special kind of table that has a "spatial awareness."

At its core, all vector-based geospatial data is stored in tables where each row represents a single observed feature (like a specific tree, a single road, or one park) and each column represents an attribute (a characteristic of that feature).

---

### The Anatomy of a Spatial Table

A spatial table has three key components:

1. Rows (or Records): Each row in the table corresponds to a single, discrete feature that was observed in the real world. If you have a dataset of trees, each row represents one individual tree.
    
2. Attribute Columns (or Fields): These are the standard columns you would find in any table. Each column describes a specific property of the features. For our trees, we might have columns for species, height_meters, and condition.
    
3. The Geometry Column: This is the special column that makes a table spatial. It stores the "where" information for each feature. For each row, the geometry column contains the coordinate data that defines the feature's shape—whether it's a point (for a tree), a line (for a road), or a polygon (for a park).
    

Let's look at a simple example of a tree inventory:

|   |   |   |   |   |
|---|---|---|---|---|
|feature_id|species|height_meters|condition|geometry|
|1|Oak|15.2|Good|POINT (55.7 12.5)|
|2|Birch|11.8|Fair|POINT (55.8 12.4)|
|3|Oak|18.5|Good|POINT (55.7 12.6)|

In GIS software, this fundamental structure—a table containing a geometry column—is often referred to as a layer or a feature class. But it's crucial to remember that underneath these labels is the simple, powerful concept of a spatial table.

### The Power of the Table: The Relational Model

The true power of organizing our observations into a spatial table lies in its simple, predictable structure. This clean format isn't just for storage; it's a foundation for action. It allows us to perform powerful operations directly on our data, such as filtering the table to show only the trees in 'Good' condition or combining it with other tables to discover new insights.

These fundamental operations—selecting, transforming, and combining data—are not just ad-hoc tricks. They are formalised in a branch of mathematics known as relational algebra. The relational data model, which you'll find at the heart of nearly all modern database systems and GIS software, is the practical implementation of these mathematical principles. 🧠

Therefore, by structuring our observations into a simple table, we unlock the ability to perform complex, repeatable, and logically sound analysis. It's this robust, formalised approach that elevates GIS from a simple map-making tool to a true analytical science. 
