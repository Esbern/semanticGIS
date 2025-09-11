---
title: " Data Modelling"
draft: false
tags:
aliases:
  - Data Modelling
---
 
# Data Modelling: Defining the Characters in Your Story

Think of the **Project Scope** you just completed as the plot outline for a story. This Data Modelling phase is where you define the **characters** who will act in that story.

The process is a stepwise refinement. You'll move from a vague idea of a character (e.g., "the main road") to a precise, detailed "character sheet" that leaves no room for ambiguity. This ensures every piece of data you use has a clear and well-defined role to play in your analysis.

### Step 1: Sketching Your Characters (The Universe of Discourse)

Your first task is to create a "cast list" for your story. This is your **Universe of Discourse (UoD)**—an initial list of all the key concepts, or "characters," in your story (e.g., 'building', 'forest', 'road').

To give these concepts a concrete form, you must define each one using one of three fundamental archetypes. These archetypes provide the basic **template** for how you will describe your data:

- **The Object Class**: This is the archetype for the blueprint of discrete, countable "things." The template for an Object Class requires a well-defined boundary and a set of common properties. Examples include creating a 'Buildings' Object Class, a 'Lakes' Object Class, or a 'Benches' Object Class.
    
- **The Property**: This is the archetype for the measurable characteristics that describe the instances of your Object Class or the space they inhabit. This archetype has two distinct templates:
    - **As an Attribute**: A template for a single value attached to a specific object instance. For example, `material = 'wood'` is an attribute of a specific bench.
    - **As a Field**: A template for a value that varies continuously across space. For example, the ambient `outdoor_temperature` across a landscape is a field.
        
This initial sketch—defining your characters using these core archetypes—is the foundation for the next crucial step: finding data that can bring them to life.

With your preliminary ontology (the UoD) in hand, your first and most important action is to **search for existing datasets** that can represent your primary concepts (Object Classes and Properties Fields). You simply use each element in the list of primary concepts from your UoD as a search filter on the relevant metadata servers to find promising datasets.. A metadata server is a service (topicality websites) whee you can search for data for a detailed description including links to such servers see the article searching for data.   This search can result in two outcomes:
1. There are no existing datasets that matches the concept in your DoD. This is a rather unfortunate outcome and it is highly advisably to rethink the concept and broaden your search for data. If you still cant finde any existing dataset that matches your concept you need prepare for field work (step 2b below)
2. You finde data that matches the match the concept on your DoD. However you ar not home free jet remembering that "The devil, as always, is in the detail" your next step is to Evaluate the esisting data thor

### Step 2a: Evaluating existing data

With your preliminary ontology (the UoD) in hand, your first and most important action is to **search for existing datasets** that can represent your concepts. You've used the informal "character list" from your UoD as a search filter to find promising datasets. Your task  is now a deep, critical investigation of those potential datasets, remembering that "The devil, as always, is in the detail". The key of this step is to **scrutinise** and **evaluate** the details of the datasets you've found. We describe these formal, detailed specifications of a dataset in terms of a **Domain of Discourse (DoD)**. You can think of the DoD as the dataset's official "rulebook," which you'll typically find in its **metadata** or technical documentation.
Your **evaluation** involves comparing your intention behind the informal concepts (your UoD) with the precise rules (DoD) used in a given dataset.

**Let's look at a example:** 
- Your **UoD** has the concept of a `'road'` for a traffic analysis.
- You find the `vejmidter` layer in the GeoDanmark dataset.
- Your investigation of the dataset's **DoD** (its technical specification) reveals their definition of "road" includes not only existing roads but also _planned_ and _demolished_ roads.  This is a  critical departure from your concept of a road. . The dataset, in its raw form, is not fit for your specific purpose.  
#### Your three choices

Based on the findings of your investigation, you must now make a strategic decision. This decision will, in turn, formally define your project's DoD for that character.and how and whic activities you need to perferm in the next phase of the GIS project the "Establishing the Data foundation".  When evaluating a existing dataset you have three choices:
 - **Accept:** You determine the dataset's DoD is fit for your purpose. By choosing this, the dataset's DoD **becomes** your project's official DoD and in the ""Establishing the Data foundation" you can apply a simpel data acquiring activity.
 
- **Transform:** You find the data valuable but not exactly aligned for your needs. You decide to modify it (e.g., filter out "planned" roads). Your project's DoD is then defined by the original datas DoD plus your **transformation rules**. In the "Establishing the Data foundation" phase you   in attrition to the simpel data acquiring activity  you also need to undertake a data tranformation activity.

- **Reject:** You conclude that the dataset's DoD is fundamentally incompatible with your project's needs, and no reasonable transformation is possible. You are now faced with the need to preform a datacolection activity in the "Establishing the Data foundation" phase but you first need to 

---

## 2. The Decision: Defining Your Project's DoD

Based on the findings of your investigation, you must now make a strategic decision. This decision will, in turn, formally define your project's DoD for that character.

You have three choices:

- **Accept:** You determine the dataset's DoD is fit for your purpose. By choosing this, the dataset's DoD **becomes** your project's official DoD.
    
- **Transform:** You find the data valuable but flawed for your needs. You decide to modify it (e.g., filter out "planned" roads). Your project's DoD is then defined by the **transformation rules** you create.
    
- **Reject:** You conclude that the dataset's DoD is fundamentally incompatible with your project's needs, and no reasonable transformation is possible. You must then either search for other data or move to **Path B: Creating New Data**.

---
