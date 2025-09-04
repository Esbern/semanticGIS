---
title: Design Rationale
draft: false
tags:
---
## Note on Terminology

Within `semanticGIS` we  use the concept of design rationale as a practical tool to help you structure and reflect on your GIS project work. While the term is traditionally used in software and product design to describe decisions after they’re made, we’re adapting it here for you to actively plan, document, and justify your decisions as you go. Think of it as a blend between a traditional _design rationale_ and a _research design_.

Like a research design, your rationale will help you plan your work step by step—defining your problem, identifying key concepts, selecting data, and choosing appropriate analytical methods. At the same time, like a traditional design rationale, you’ll be asked to reflect on your decisions, explain why you made them, and consider possible alternatives. This will strengthen your ability to communicate your work clearly to clients, collaborators, or your future self.

Simularaly  we introduce a specific distinction between the **Universe of Discourse (UoD)** and the **Domain of Discourse (DoD)** to enforce clarity in the analytical design process.

- The **Universe of Discourse (UoD)** refers to the **conceptual realm** of real-world phenomena we are interested in. It consists of the common-sense, often informally defined entities relevant to our scientific question. For example, the UoD might include concepts like 'forests', 'buildings', or 'suitable habitats'. It answers the question: "_What general concepts are we investigating?_"
    
- The **Domain of Discourse (DoD)** represents the **specific operational model** used to formally define and represent entities from the UoD within our analysis. It provides the explicit set of rules, criteria, and thresholds that bridge the gap between the abstract concept and its concrete representation in data. For example, within our DoD, a 'building' might be defined as "a permanent, roofed structure with a footprint greater than 25 square meters," and a 'forest' might be defined by "a canopy cover greater than 30% with a minimum mapping unit of 0.5 hectares." The DoD answers the question: "_What precise rules qualify something as an instance of our concept for this specific analysis?_"
    
This distinction is not merely academic; it is fundamental to analytical transparency. The UoD sets the stage, while the DoD defines the exact terms of the analysis, controlling what is included or excluded from the resulting datasets.

**Project Phases and Structure of Your Design Rationale**

Within `semanticGIS` the design rationale and hence also the GIS project is organised into four key phases that provide a clear way to document and justify your thinking and decision-making within the GIS project:

1. **Problem Framing and Conceptual Ontology**: This phase includes how you interpret and define the problem i.e. your conceptualisation of the issue. It should describe how you understand the task in your own words and clarify key terms and goals—especially in relation to how a client/teacher might phrase them. It also includes the identification of relevant entities (e.g., bars, music venues, noise complaints) that exist in your conceptualisation of the issue--Universe of Discourse.  This helps form the foundation for the rest of the project.
    
2. **Data Selection (Domain of Discourse)**: Here, you identify how you represent the entities and concepts outlined in your problem framing as datasets. This includes evaluating the suitability of existing data, deciding whether data transformation-and filtering  are needed, or whether new data collection is necessary. Justify your choices and reflect on potential trade-offs and consequences. If new data collection is needed alternative methods are discussed and evaluated.
    
3. **Analytical Approach**: In this phase, you deconstruct the problem into spatial operations and analytical steps. Document which GIS methods and tools you use (e.g., buffering, density analysis, spatial joins), and why you selected these over alternatives. Discuss how your operations align with the problem as defined in your conceptual ontology.
    
4. **Dissemination and Communication**: Finally, you explain how you choose to present your findings. Consider who your audience is (e.g., the public, policymakers, clients), and how your choice of maps, visuals, or text will shape their understanding. Justify your medium (e.g., interactive map, printed report) and design choices in terms of clarity, accessibility, and impact.

A key purpose of the design rationale is to clearly explain the consequences or artifacts created by different choices. By explicitly documenting the trade-offs and potential impacts of various decisions, the rationale helps avoid unintended consequences and ensures that all stakeholders understand the implications of the project’s design.

Moreover, the design rationale is essential for **documentation and feedback**. It provides a structured record that can be referenced throughout the project’s lifecycle, making it easier to review decisions, provide feedback, and make adjustments as needed. It also serves as a valuable resource for future projects, offering insights into the decision-making process and the outcomes of past choices.

In alignment with the concept developed by W.R. Kunz and Horst Rittel, the design rationale in a GIS project provides an argumentation-based structure that supports the collaborative and often complex process of designing geospatial systems. It ensures that decisions are not only recorded but also justified, considering all alternatives and trade-offs, ultimately leading to more robust and well-founded project outcomes.

By maintaining a clear and detailed design rationale, GIS professionals can enhance the transparency, consistency, and effectiveness of their projects, ensuring that the reasoning behind every decision is well-documented and understood.


**Example Design Rationale: Identifying Entertainment Zones in Copenhagen**

Below is a sample design rationale for a fictive project where the client (in this case, your teacher) has asked for a data-driven identification and visualisation of Copenhagen's party/entertainment zones. This example follows the four phases outlined above.

---

## 1. Problem Framing and Conceptual Ontology

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

## 2. Data Selection (Domain of Discourse)

The following is an example of the considerations you might make in this case, looking at data for bars.

There are at least three alternatives to source for this data.
1. The Danish register for firms CVR that use standard NACE codes (available in English).  
   This is probably the most reliable dataset, but it might have some bios due to its official purpose for taxation.
2. Open Street map: This is clearly the simplest and has the advantage of being unofficial but, at the same time, probably not as updated for Clouser.
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

## 3. Analytical Approach

The problem was deconstructed into a set of GIS operations:

1. 1.Venue Density Analysis: I used kernel density estimation on entertainment POIs to identify spatial clusters. In considering how to model the spatial distribution of bars, I evaluated two main options: analyzing counts per cell in a regular grid or applying a kernel density function. While a grid-based approach (e.g., 250x250m cells) offers clarity and ease of interpretation, I found that kernel density estimation better captured the gradual influence of multiple venues on an area's ambiance.
   I selected a quartic kernel function with a search radius of 500 meters, based on the assumption that a bar can contribute to the perceived liveliness of an area up to 500 meters away. This distance approximates a 5–7 minute walk and reflects how clusters of venues influence urban atmosphere. A uniform kernel was considered, but the quartic kernel was preferred for its smoother decay of influence with distance, better reflecting the nature of urban entertainment clustering.
    
Not so-detailed discussion.
2. **Noise Hotspot Mapping**: Noise complaint points were aggregated by 100x100m grid to reveal concentration areas.
    
3. **Walkability Analysis**: A service area analysis was performed around public transport nodes to highlight accessible zones.
    
4. **Zoning Filter**: Entertainment clusters were cross-referenced with zoning layers to exclude incompatible land use areas.
    

These steps were combined in a weighted overlay to generate a final raster surface representing entertainment potential. Alternative approaches were considered (e.g., DBSCAN clustering), but kernel density provided better control over smoothing and visibility.

---

## 4. Dissemination and Communication

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