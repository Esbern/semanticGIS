---
title: Five-Phase Process
draft: false
tags:
---
## 1  Project Phases and Structure of Your Design Rationale

Within `semanticGIS`, the [[GIS project]] and hence also the [[Design Rationale]] is organised into five key phases that provide a transparent and reproducible way to manage your thinking and decision-making within the GIS project.
The five phases are named after the primary activity undertaken in each phase. and present ways of isolating the theas activities  

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
