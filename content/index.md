---
title: Welcome to Semantic GIS
tags:
---
# Welcome to Semantic GIS.
The motivation behind SemanticGIS is to make it easier to talk about **G**eographic **I**nformation **S**ystems. And thereby make it easier to learn and collaborate about GIS.  SemanticGIS is designed to aid especially beginners and casual users of GIS in developing a **structured geospatial thinking** and, at the same time, developing a framework for documenting their GIS work. The overall goal is to focus on the semantics of GIS and maintain a clear separation between **conceptual geospatial operations** and **tool-specific implementations**, thereby enabling users to create a clear conceptual solution to a problem before addressing the implementation details.
SemanticGIS consists of five interconnected parts.
1. A recommended workflow, organised around a 4-step "design rationale".
2. A website (semanticGIS.org) that organises teaching material according to the principles of SemanticGIS.
3. A so-called **D**omain **S**pecific **L**anguage for GIS, which is a formalised way of describing a pipeline of GIS operations to achieve a specific goal. 
4. A series of compilers that can translate the DSL into:
	1. Flowchart of the process for use, for instance, in the design rationale.
	2. A recipe for implementing the operations in a specific software like  QGIS or ArcGIS, 
	3. And, for advanced users, an executable Python script.
5. A series of websites that present national and regional datasets according to the principles of SemanticGIS. (semanticgis.dk and semanticgis.eu)
## Where to start
First of all, be warned, semanticGIS is very much a work in progress. The content is filled in as needed for teaching or research projects. A good place to start would be to read the section on design rationales and then the section on establishing a working environment. From there, the section "GIS 101" takes you through the main steps of a GIS project, and from there you hopefully have enough knowledge to explore semanticGIS.org based on your needs and interests. 
The GIS DSL is implemented as a Python library and can, in principle, be utilised in any Python IDE, but it has been designed to work in Notebook-inspired environments like Jupyter Lab or Google Colaboratory (Google Colab).
