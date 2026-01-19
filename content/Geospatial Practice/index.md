---
title: Geospatial Practice
draft: false
tags:
aliases:
  - Geospatial Practice
---
At the heart of semanticGIS is a desire to establish **geospatial practices** that focus on a structured, transparent, and well-documented process. This semanticGIS **geospatial practice** consists of:

1. Structuring your [[GIS project|GIS project]] into **five** well-defined phases as described in the section [[Geospatial Practice/index#The five phases of the GIS-project|The five phases of the GIS-project]] below.
    
2. A set of recommendations for good [[Geospatial Practice/Project Stewardship/index|Project Stewardship]], where the use of a [[Geospatial Practice/Project Stewardship/Design rationale|Design Rationale]] is the most important.
    

Especially if you are new to doing geospatial analysis, it is advisable to study other projects and domain-specific considerations; therefore, this part of the website also contains links to a series of [[Geospatial Practice/Analytical Patterns/index|Application domains & Frameworks]] that highlight how the five phases can be implemented in different contexts.

## The five phases of the GIS-project

Within the SemanticGIS framework, we recommend that you organise your geospatial practice into the following five phases.

#### **1. [[Geospatial Practice/Project Scoping/index|Project Scoping]]**

This is the foundational phase where you move from a vague idea (topic) to an actionable question. You define your research questions, establish clear objectives, identify your area of interest, and outline the project's scope and limitations.

#### **2. [[Geospatial Practice/Data Modelling/index|Data Modelling]]**

Before you collect any data, you design your conceptual **ontology**—the formal "rulebook" that defines the objects, features, and relationships you will be working with. This crucial step ensures your data will be consistent and fit for purpose.

#### **3. [[Geospatial Practice/Establishing the Data Foundation/index|Establishing the Data Foundation]]**

Here, you acquire and prepare your data. Whether you're conducting fieldwork, downloading existing datasets, or digitising historical maps, every action is guided by your data model and meticulously documented in your Design Rationale.

#### **4. [[Geospatial Practice/Analytical Modelling/index|Analytical Modelling]]**

This is where you develop the methods to answer your research questions. In semanticGIS, we emphasize the **Abstract-First** approach here: you first design the _logical pipeline_ (the abstract recipe) that converts your data into results, and only then do you "compile" that logic into concrete software operations. This ensures your analysis is driven by scientific intent, not software limitations.

#### **5. [[Geospatial Practice/Dissemination and Communication/index|Dissemination and Communication]]**

The final phase involves sharing your work. This includes not only your final maps and reports but the **Design Rationale** and the **Analytical Recipe** itself. By publishing your process (Provenance), you empower others to understand, critique, and confidently build upon your findings, fostering a culture of open and reproducible science.

## Exploratory Workflow vs. Prescriptive Workflow

Note that the execution of the five phases is not 100% linear like a [waterfall model](https://en.wikipedia.org/wiki/Waterfall_model). Within SemanticGIS, there is considerable **iterative refinement**—or "backflow"—from one phase to the previous.

The nature of this flow depends on your approach:

- **[[Geospatial Practice/Project Scoping/index#^Prescriptive-Workflow|Prescriptive Workflow]]**: The project workflow is identified by "reverse engineering" the required outputs. You know exactly what map you need (deductive reasoning), and you work backward to define the necessary data and analysis.
    
- **[[Geospatial Practice/Project Scoping/index#^Exploratory-Workflow|Exploratory Workflow]]**: You begin with a rich dataset or a broad question and use the analysis phase to discover patterns or relationships (inductive reasoning), allowing the final output to emerge from the data itself.