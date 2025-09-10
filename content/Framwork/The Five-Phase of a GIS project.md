---
title: The Five-Phase of a GIS project
draft: false
tags:
---
The methodology of `SemanticGIS` is built around three interconnected concepts:
1. A structuring of a [[GIS project]] into five well-defined phases
2. Documenting the [[GIS project]] through the use of a [[Design Rationale]]
3. Structuring the analytical process through the use of  a domains specific language.
This article focuses on the five phases of the [[GIS project]], these five phases are named after the primary intellectual task undertaken in each phase and function as a way to isolate the tasks, allowing for a focused and well-documented intellectual process.

## 1. Project Scoping

The first phase of any project is to define its **purpose, boundaries, and real-world context**. All projects exist within an organisational framework of rules, resources, and requirements. The first and most critical step is to understand this framework, as it defines the practical limits and directs the intellectual focus of your work.

---

### The Organisational Framework: Understanding Your Constraints

Before defining your specific research goals, you must identify and document the external factors that will shape your project. These are often non-negotiable constraints imposed by clients, employers, or legal bodies.

- **The Brief:** You must begin by analysing the project brief from the client (or teacher). This document dictates the entire structure of your project. Your first task is to determine which of two primary workflows it requires:
    
    - **Exploitative Workflow:** The brief poses an open-ended question (e.g., "Investigate the relationship between green space and property values"). Your process will be iterative, and the final output may not be known at the start.
        
    - **Reverse Engineering Workflow:** The brief demands hard deliverables (e.g., "Produce a map of all land parcels suitable for urban agriculture"). Here, your process is determined by working backward from the required output to identify the necessary data and analytical steps. 
	It is always a best practice to **reformulate the brief** in your own words, clarifying the workflow and deliverables, and have it approved by the client to ensure a shared understanding. Also note that a brief can seldom be answered through a  enticingly **Exploitative workflow** or a enticingly **Reverse Engineering Workflow:** often the two work in tandem. This articel presents the phases in the order of a **Exploitative workflow** since this is the simplest. At the end of the articel we wil discuss how to modify the proces for a more **Reverse Engineering Workflow:**
	
- **The Stakeholder Landscape**: Beyond the primary client (or teacher) who provides the brief, most projects have a wider network of **stakeholders**. You should identify who they are and what their interests or requirements might be.
	- **Who are they?** Stakeholders could include the **IT department** that controls data access and software, the **end-users** who will interact with your final map, a **communications team** that must approve public-facing materials, or even **community groups** affected by the analysis.
    - **Why does it matter?** A brilliant analysis that the IT department can't support or that the end-users find confusing is a failed project. Mapping these stakeholders early helps you anticipate needs and manage expectations.
        
- **Resources:** You need to assess the practical resources available. This includes the **time** allocated for the project, the **budget**, and your access to crucial, task-specific **data**, software, or expertise within the organisation. **The Technical Infrastructure** This is a more specific aspect of "Resources." It's not just about what you have access to, but what you are _required_ to use.
	- **What is it?** This includes constraints like a mandatory software ecosystem (e.g., "This organization works exclusively with ESRI products"), required database formats (e.g., "All data must be stored in the central PostgreSQL/PostGIS database"), or specific programming languages for scripts (e.g., "All automation must be done in Python 3.9").
	- **Why does it matter?** These constraints dictate your tool choices from the very beginning. Knowing them prevents you from building a solution in QGIS and R when the client can only support ArcGIS Pro and its proprietary tools.
	
- **Project Management:** Document any formal project management requirements. This includes **deadlines** and **milestones**, but also any specific formats for external documentation or reporting. While you must meet these external demands, your **`semanticGIS` Design Rationale remains your non-negotiable internal tool** for ensuring analytical rigor.
    
- **Legislation and Compliance:** You must identify any legal or regulatory constraints, such as privacy regulations (GDPR), data protection laws, or copyright on data that govern how you can acquire, store, and use information. In adition to the Legislation you should also consider  **Ethical Guidelines**. This goes beyond strict "Legislation and Compliance." Even if an analysis is legal, it may have significant ethical implications that you must consider.
	- **What is it?** This involves assessing the potential social impact of your work. For example, will a crime hotspot analysis unintentionally stigmatise a neighbourhood and reinforce social biases? Does a site suitability analysis for a new waste facility fairly consider the impact on all communities?
	- **Why does it matter?** As a researcher and consultant, you have a professional responsibility to "do no harm." Documenting your consideration of these ethical dimensions is a hallmark of a mature and responsible analytical process.
    
- **Design and Branding:** Identify any constraints on your final visualisations. Your client or organisation may have a **design manual** with specific rules for fonts, colours, and logos that you must follow.
    

---

### ## Defining Your Intellectual Core: Your Analytical Goals

Now that you have established the practical boundaries of your project, you can define its specific intellectual core. This involves translating the brief into a focused, actionable, and achievable research plan that fits within the identified constraints.

Your task is to:

- **Frame the Problem:** In your own words, write a clear statement of the research question or problem you will address.
    
- **Define Objectives:** List the specific, measurable goals you will achieve to answer that question.
    
- **Establish Scope:** Clearly define what is included and excluded from your analysis, including your geographical study area and any thematic or temporal limits.
    

The deliverable for this phase is a formal **project scope** that clearly outlines the external constraints and your specific analytical goals. This will be the first chapter in your Design Rationale.
    
### 1.2 Data Modelling:

   The project's **Universe of Discourse (UoD)** is the conceptual boundary of your analysis. It's the complete, informally defined list of **concepts** that are relevant to your scientific question. These concepts are the names we give to the raw **phenomena** we observe.
   The concepts within our UoD can be used to describe two fundamental things:
- **Objects**: These are concepts describing discrete, countable things that are understood to have a well-defined boundary. Examples include the concepts of a 'building', a 'lake', or a 'parcel of land'.
- **Properties**: These are concepts describing the measurable characteristics of our phenomena. A property, like 'temperature', can be conceptualised in two distinct ways:
	- **As an Attribute** of an Object: A single value attached to a discrete object. For example, `room_temperature` is an attribute of a specific 'room' object.
	- **As a Field**: A value that varies continuously across space. For example, the ambient `outdoor_temperature` across a landscape is a field.
        
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


## Exploitative workflow vs Reverse Engineering Workflow