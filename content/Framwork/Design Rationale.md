---
title: Design Rationale
draft: false
tags:
---
#### Note on Terminology

Within`semanticGIS`, we use the concept of design rationale as a practical tool to help you structure and reflect on your GIS project work. Traditionally, the term is used in software and product design to describe decisions after they have been made (see [Wikipedia](https://en.wikipedia.org/wiki/Design_rationale)), we’re adapting it here for you to actively plan, document, and justify your decisions as you proceed. Think of it as a blend between a traditional _design rationale_ and a _research design_.

Like a research design, your rationale will help you plan your work step by step—defining your problem, identifying key concepts, selecting data, and choosing appropriate analytical methods. At the same time, like a traditional design rationale, you’ll be asked to reflect on your decisions, explain why you made them, and consider possible alternatives. This will strengthen your ability to communicate your work clearly to clients, collaborators, or your future self.

## 1  Project Phases and Structure of Your Design Rationale

Within `semanticGIS`, the design rationale and hence also the GIS project is organised into four key phases that provide a clear way to document and justify your thinking and decision-making within the GIS project:


### 1.1 Project scoping
   This phase consists of two main activities: Problem Framing and specification of the project's Universe of Discourse. 
   In  **Problem Framing**, you interpret and define the problem, i.e. your conceptualisation of the issue. It should describe how you understand the task in your own words and clarify key terms and goals—especially in relation to how a client/teacher might phrase them. 
   The project's **Universe of Discourse (UoD)** is the conceptual boundary of your analysis. It's the complete, informally defined list of **concepts** that are relevant to your scientific question. These concepts are the names we give to the raw **phenomena** we observe.
   The concepts within our UoD can be used to describe two fundamental things:
- **Objects**: These are concepts describing discrete, countable things that are understood to have a well-defined boundary. Examples include the concepts of a 'building', a 'lake', or a 'parcel of land'.
- **Properties**: These are concepts describing the measurable characteristics of our phenomena. A property, like 'temperature', can be conceptualised in two distinct ways:
	- **As an Attribute** of an Object: A single value attached to a discrete object. For example, `room_temperature` is an attribute of a specific 'room' object.
	- **As a Field**: A value that varies continuously across space. For example, the ambient `outdoor_temperature` across a landscape is a field.
        
	This distinction concerns the nature of the phenomena the concepts refer to, rather than their eventual digital representation. The UoD serves as a **controlled vocabulary** for all the concepts—including objects and their properties (whether as attributes or fields)—that you will address in your project.
    
### 1.2 Data Modelling:
   Before we can discuss this step, we need to address some shortcomings in the relationship between the UoD and data. While the UoD is an informally defined list of **concepts** relating to the project, and this might be enough for simple one-off data collection, it has some clear shortcomings. In practice, it is often necessary to go beyond the informal, everyday meaning of terms like 'building' and introduce a precise, unambiguous definition. The translation of the vocabulary of the UoD into precise, unambiguous definitions is called the Domain of Doscource (DoD). The DoD provides an explicit set of rules, criteria, and thresholds that bridge the gap between the abstract concept and its concrete representation in data. For example, within our DoD, a 'building' might be defined as "a permanent, roofed structure with a footprint greater than 25 square meters," and a 'forest' might be defined by "a canopy cover greater than 30% with a minimum mapping unit of 0.5 hectares." The DoD answers the question: "_What precise rules qualify something as an instance of our concept for this specific analysis?_"  The distinction between the UoD and DoD is not just of academic interest. In relation to data acquisition, it is a highly relevant and important distinction. In the official Danish topographical dataset "GeoDanmark", there is a representation of the concept of roads (vejmidter).  If you are working on a project that includes creating a traffic map, you probably would have the term road in your UoD and think that it matches the term road as in the GeoDanmark dataset. However, when you study the DoD of GeoDanmark, you will see that the operational definition of road includes not only existing roads, but also planned roads and roads under demolition.  Likewise, if you compare a satellite image of Denmark with the location of forest according to GeoDanmark, you will see that there are forest without trees, again due to how forists are defined in the DoD of GeoDanmark.  You now have three possibilities: 
	   1. Accept the definition of roads and forists as given in the DoD of GeoDanmark (For existing datasets, the DoD is often named metadata or specification)
	   2. Investigate if it is possible to transform the GeoDanmark dataset to match how you whish to define the terms in your DoD
	   3. If and only if the first two options fail, you can consider collecting your own data, matching the definition of the terms. Data collection, as described in the section [[Tasks/Recording new data/index|Recording new data]], is a time-consuming task and should be avoided if it is possible to use existing data.
	   
### 1.3 Data Sourcing and Preparation
   Having defined your **Domain of Discourse (DoD)** and chosen your data strategy in the previous step, you must now execute that strategy to assemble a complete, clean, and project-ready database. This phase is the practical work of preparing the specific inputs for your analysis. 
   The specific actions you take here are determined by the strategy you chose.
    1. **Adopting an Existing Dataset**
       If you determined that an existing dataset's DoD is fit for your purpose, this is the most straightforward path.
	       1. **Acquire the Data**: Download the dataset from the official provider.
	       2. **Document Provenance**: Immediately record the source, download date, version number, and a link to the original metadata in your project documentation. This is critical for reproducibility.
	       3. **Initial Quality Check**: Load the data into your GIS environment to ensure it is not corrupt, covers your study area, and has the expected attributes.
	    The outcome of this strategy is a "raw" dataset that is documented and ready for analysis.
	 2. **Transforming an Existing Dataset**
	    This is the most common strategy in practice. It involves acquiring a raw dataset and modifying it to conform precisely to your project's DoD.
		 1. **Acquire and Check**: Perform all the steps from Strategy 1 first.
		 2. **Develop a Transformation Recipe**: Document the exact sequence of steps you will take to adapt the data. This recipe might include:
			 -  **Filtering rows**: Selecting a subset of features that match your definition (e.g., selecting only roads with `status = 'existing'`).
			 - **Modifying attributes**: Renaming or recalculating fields to match your schema.
			 - **Geometric operations**: Clipping the data to your study area boundary.
		 3. **Execute and Document**: Run the transformation process, saving the output as a _new_ derived dataset. Your documented recipe ensures this process is transparent and can be repeated.
		The outcome is a new, processed dataset that is perfectly aligned with your DoD.
	3. **Recording New Data**
	   This is the most resource-intensive strategy and should only be undertaken when no suitable data exists.
		   1. **Finalise Methodology through a Pilot Study**: Before full-scale recording, you should conduct a pilot study to test your DoD and recording methodology in the field. This iterative process identifies practical issues and allows you to refine your ontology into a final, robust set of rules.
		   2. **Record the Data**: Carry out the whole data recording process (e.g., fieldwork, digitising from imagery) according to your finalised methodology.
		   3. **Quality Assurance**: Implement a quality control process to check for errors, inconsistencies, and missing values as the data is being created.
		The outcome is an entirely new, bespoke dataset, created from scratch to match your DoD.
	Regardless of the path taken, this phase concludes when you have a **final, documented project database**. This clean dataset is the official input for the next step, the **Analytical Approach**.
	
### 1.4 Analytical Approach
In this phase, you deconstruct the problem into spatial operations and analytical steps. Document which GIS methods and tools you use (e.g., buffering, density analysis, spatial joins), and why you selected these over alternatives. Discuss how your operations align with the problem as defined in your conceptual ontology.
    
### 1.5 Dissemination and Communication
Finally, you explain how you choose to present your findings. Consider who your audience is (e.g., the public, policymakers, clients), and how your choice of maps, visuals, or text will shape their understanding. Justify your medium (e.g., interactive map, printed report) and design choices in terms of clarity, accessibility, and impact.

A key purpose of the design rationale is to clearly explain the consequences or artifacts created by different choices. By explicitly documenting the trade-offs and potential impacts of various decisions, the rationale helps avoid unintended consequences and ensures that all stakeholders understand the implications of the project’s design.

Moreover, the design rationale is essential for **documentation and feedback**. It provides a structured record that can be referenced throughout the project’s lifecycle, making it easier to review decisions, provide feedback, and make adjustments as needed. It also serves as a valuable resource for future projects, offering insights into the decision-making process and the outcomes of past choices.

In alignment with the concept developed by W.R. Kunz and Horst Rittel, the design rationale in a GIS project provides an argumentation-based structure that supports the collaborative and often complex process of designing geospatial systems. It ensures that decisions are not only recorded but also justified, considering all alternatives and trade-offs, ultimately leading to more robust and well-founded project outcomes.

By maintaining a clear and detailed design rationale, GIS professionals can enhance the transparency, consistency, and effectiveness of their projects, ensuring that the reasoning behind every decision is well-documented and understood.


## 2 Example Design Rationale: Identifying Entertainment Zones in Copenhagen

Below is a sample design rationale for a fictive project where the client (in this case, your teacher) has asked for a data-driven identification and visualisation of Copenhagen's party/entertainment zones. This example follows the four phases outlined above.

---
### 2.1 Project scoping

The project task is to identify party/entertainment zones in Copenhagen using data-driven GIS methods. Since the term “party/entertainment zone” is open to interpretation, I have chosen to define it as areas characterised by a high concentration of social, cultural, and nightlife activities. This includes bars, restaurants, music venues, cinemas, and event spaces. I would like to include some seasonality in the investigation since there are some clear summer-related areas, such as public parks and swimming zones. 

Entities relevant to this  include:
- Point locations of venues (bars, clubs, theatres, etc.)
- Potential locations for informal party activity (Parks, swimming zones)
- Observations of formal and informal party activity.
- Public transportation nodes (metro stations, bus stops)
- Street network data (for walkability analysis relative to public transport)
- 
Example of detail consideration on bars:
To make the analysis meaningful, we need to be precise about what we include under each category. For instance, when working with point locations of venues, we must consider how to define a "bar." Do we include only standalone bars, or do bars inside clubs, theatres, and cinemas count as well? If a bar is only accessible to ticket holders (e.g., in a theatre or amusement park), should it be included? In this project, I have decided to include bars that are publicly accessible, whether they are standalone or part of a larger establishment. Bars within clubs or theatres are only counted if they serve the general public. Bars in amusement gardens with entrance fees are included, as they contribute significantly to the entertainment landscape. Finally, we also need to look at temporality some establishments might only be open at weekends or in the summer period. Careful attention must also be paid to avoid double-counting venues (e.g., not counting a club and its bar as two separate entities unless they function independently).

---
### 2.2 Data Modelling 
In this case, our ontology of a bare is rather vague and it can match up with bars in at least three alternative datasets:

1. **The Danish register for firms CVR** that use standard NACE codes NACE code 563020 = Beverage serving activities.  
   This is probably the most reliable dataset, but it might have some bios due to its official purpose for taxation.
2. **Open Street map:** the ontology is here based on key and tags in the case of a bar we could use the key amenity with the tag 'bar' or  'pub' Tag = bar: is used to map a **bar**: a purpose-built commercial establishment that sells alcoholic drinks to be consumed on the premises. They are characterised by a noisy and vibrant atmosphere, similar to a party. They usually do not sell food to be eaten as a meal. The music is usually loud and you often have to stand. Sometimes it has a dancefloor, but it's not the main attraction.
   Tag = bar :A **pub** or **public house** is an establishment that sells alcoholic drinks that can be consumed on the premises. Pubs commonly sell food which also can be eaten on the premises. They are characterised by a traditional appearance and a relaxed atmosphere. You can usually sit down and there is usually no loud music to disturb conversation. A pub would be a good location to meet after a day's mapping for OpenStreetMap.
3. **Google Maps place API:** the term bar is defined as "a physical establishment that serves alcohol, which is categorized by Google Maps based on its business information and reviews"
In this case, any of the definitions (DoD) could be used and we can continue to the next phase of sourcing the data

---

### 2.3 Data Sourcing and Preparation

The following is an example of the considerations you might make in this case, looking at data for bars.

As mentioned, there are at  least three alternatives to source for this data.ther the ontology of bar matches:
1. The Danish register for firms CVR that use standard NACE codes (available in English).  
2. Open Street map: the ontology is here based on tags and values in the case of a bar we could use the tag amenity with the tag ('bar', 'pub')
3. Google Maps place API: I considered using commercial venue data (e.g., Google Places), but decided against it due to licensing restrictions.

Both 1 and 2 are plausible and free, but before deciding on which dataset to use for representing bars, I conducted a quick comparison of available sources:

To acquire OSM data, I used QuickOSM and searched for the tag `amenity` within the extent of Copenhagen Municipality. Although the initial query included locations outside the municipality boundary, I clipped the resulting layer using the official administrative boundary of Copenhagen. I then filtered the features where `amenity` was in ('bar', 'pub'), which resulted in 534 potential bar locations.

From the CVR (Danish Central Business Register), I downloaded a list of all active business units (p-enheder) in Copenhagen and filtered them using the NACE code `563020`, which corresponds to bars. This gave me 680 businesses, but these lacked spatial coordinates—only address information was available. I joined these with a geocoded address dataset and filtered out those located outside Copenhagen, resulting in 552 mappable bars.

To manage the risk of data loss and ensure a clean workflow, I saved the layers as CVR_bar and OSM_bar, converted both to EPSG:25832 and removed unnecessary attributes. A visual comparison showed better alignment between Google Maps and OSM than between Google Maps and CVR, which influenced my final decision.

Although the CVR data might be more authoritative in terms of business registry, it lacked up-to-date changes and required extensive processing. Based on completeness, alignment, and ease of use, I chose to continue with the OSM dataset. Ideally, 
I would validate this through field mapping, but time constraints prevented this step.

Other datasets not described in detail:
    
- Parks and other leisure areas.
    
-  Noise complaint records (as a proxy for nightlife activity) Copenhagen noise complaint data, police reports. This might also need some fieldwork.
    
- Rejseplanen’s GTFS feed for public transport locations or OSM trafic data
    
- Official GeoDanmark or OpenStreetMap street network data for walkability analysis
    

---

### 2.4 Analytical Approach

The problem was deconstructed into a set of GIS operations:

1. 1.Venue Density Analysis: I used kernel density estimation on entertainment POIs to identify spatial clusters. In considering how to model the spatial distribution of bars, I evaluated two main options: analyzing counts per cell in a regular grid or applying a kernel density function. While a grid-based approach (e.g., 250x250m cells) offers clarity and ease of interpretation, I found that kernel density estimation better captured the gradual influence of multiple venues on an area's ambiance.
   I selected a quartic kernel function with a search radius of 500 meters, based on the assumption that a bar can contribute to the perceived liveliness of an area up to 500 meters away. This distance approximates a 5–7 minute walk and reflects how clusters of venues influence urban atmosphere. A uniform kernel was considered, but the quartic kernel was preferred for its smoother decay of influence with distance, better reflecting the nature of urban entertainment clustering.
    
Not so-detailed discussion.
2. **Noise Hotspot Mapping**: Noise complaint points were aggregated by 100x100m grid to reveal concentration areas.
    
3. **Walkability Analysis**: A service area analysis was performed around public transport nodes to highlight accessible zones.
    
4. **Zoning Filter**: Entertainment clusters were cross-referenced with zoning layers to exclude incompatible land use areas.
    

These steps were combined in a weighted overlay to generate a final raster surface representing entertainment potential. Alternative approaches were considered (e.g., DBSCAN clustering), but kernel density provided better control over smoothing and visibility.

---

### 2.5 Dissemination and Communication

The results are presented in two main formats:

- An interactive web map (built using QGIS and Leaflet) to allow clients to explore the zones in detail.
    
- A summary report with static maps and charts tailored to a policymaker audience. One key element of this report is a map showing the result of the venue density analysis. For this map, I chose a light gray background to avoid visual interference with the color gradient used to represent bar density. The density scale runs from blue (indicating low or "boring" levels of activity) to red (indicating a high-intensity party zone).
    
**Summery report map in detail:**
To enhance interpretability, I decreased the opacity for low-density values so that only significant concentrations are emphasized. A detailed description of the methodology is included directly on the map, stating that it shows bar density based on a 500-meter radius quartic kernel function.

The map is included as an appendix to ensure it can be printed at A4 size like the rest of the report. This choice also allowed me to select a round and readable map scale of 1:5000. Both a scale bar and a numeric ratio (e.g., 1:5000) have been included and placed in the water area outside Copenhagen to avoid covering relevant data.

Finally, a source credit—'CC BY 4.0 Klimadatastyrelsen & OSM'—has been added to acknowledge the background map and venue data. No additional legend or title was added, as the map is meant to be interpreted in the context of the report’s discussion.

Visual design choices emphasized clarity and accessibility: using simple symbology, consistent color schemes, and minimal text. The interactive map allows filtering by type of entertainment, while the report provides a narrative interpretation of key findings. I chose this dual format to meet both public and professional expectations.
![[partyzones.png]]
---