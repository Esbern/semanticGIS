---
title: " Data Modelling"
draft: false
tags:
aliases:
  - Data Modelling
order: "2"
---
Think of the **Project Scope** you just completed as the plot outline for a story. This **Data Modelling** phase is where you write the detailed **"character sheets"** for the key players in that story.

The process is a step-wise refinement. You'll move from a vague idea of a character (e.g., "the main road") to a precise, unambiguous definition. This ensures every piece of data you use has a clear and well-defined role in your analysis.

---
## Step 1: Sketching Your Characters (The Universe of Discourse)

Your first task is to create a "cast list." This is your **Universe of Discourse (UoD)**—an initial list of all the key concepts, or "characters," in your story (e.g., 'building', 'forest', 'road').

To give these concepts a concrete form, you must define each one using one of three fundamental archetypes. These archetypes provide the basic **template** for how you will describe your data:

- **The Object Class**: The blueprint for discrete, countable "things" with a well-defined boundary and common properties. Examples include a 'Buildings' Object Class or a 'Lakes' Object Class.
    
- **The Property**: The measurable characteristics that describe your objects or the space they inhabit. This archetype has two distinct templates:
    - **As an Attribute**: A single value attached to a specific object. For example, `material = 'wood'` is an attribute of a specific bench.
    - **As a Field**: A value that varies continuously across space. For example, the ambient `outdoor_temperature` across a landscape.
        
With your preliminary UoD in hand, your primary action is to **search for existing datasets** that can represent your concepts. You'll use the terms from your UoD as keywords to search relevant metadata servers (see [[Tasks/Searching for data/index|Searching for data]]). This search leads to two possible outcomes:

1. **No suitable data is found**: This is rare but possible. Before deciding to record your own data, you should first reconsider your concepts and broaden your search. If you still find nothing, you must prepare for fieldwork by proceeding to [[Data Modelling#Step 2b Preforming a field pilot|Step 2b: Performing a Field Pilot]].
    
2. **Promising data is found**: This is the most common outcome. Your next step is to rigorously evaluate this data in [[Data Modelling#Step 2a Evaluating existing data|Step 2a]].
---
## Step 2a: Evaluating Existing Data

The goal here is to scrutinize the dataset's official "rulebook"—its **Domain of Discourse (DoD)**, which you'll typically find in its **metadata** or technical documentation. You must compare the dataset's formal rules with the informal intent of your UoD.

- **Your UoD** has the concept of a `'road'` for a traffic analysis.
    
- You find the `vejmidter` layer in the GeoDanmark dataset.
    
- Your investigation of the dataset's **DoD** reveals their definition includes _planned_ and _demolished_ roads. This is a critical mismatch; the data, in its raw form, is not fit for your purpose.
    
#### Your Three Choices

Based on your evaluation, you make a strategic decision. This decision formally defines your project's DoD and determines the tasks you'll perform in the next phase, [[Establishing the Data foundation|Establishing the Data Foundation]].

- ✅ **Accept**: The dataset's DoD is fit for your purpose. The dataset's DoD **becomes** your project's official DoD. In the next phase, you will simply perform a [[Establishing the Data foundation#Data Acquiring|data acquiring]] activity.
    
- 🔁 **Transform**: The dataset is valuable but needs modification. You will define **your own target DoD** (e.g., "roads where status = 'existing'"). Your project's DoD is this new, refined definition, and you will create a set of transformation rules to bridge the gap. In the next phase, you will perform a [[Establishing the Data foundation#Data Acquiring|data acquiring]] activity followed by a [[Establishing the Data foundation#Data Transforming|data transformation]] activity.
    
- ❌ **Reject**: The dataset is fundamentally incompatible, and transformation is not feasible. You must now define your own DoD from scratch and validate it by performing a [[Data Modelling#Step 2b Preforming a field pilot|Field Pilot (Step 2b)]]. In the next phase, you will perform [[Establishing the Data foundation#Data Schema Creation|data schema creation]] and [[Establishing the Data foundation#Data Recording|data recording]] activities.
---
## Step 2b: Performing a Field Pilot

The purpose of a field pilot is to convert your conceptual UoD into a robust, operational DoD by testing your definitions against real-world complexity. You will discover ambiguities and "edge cases" that force you to refine your rules.

The crucial difference between a pilot and the final data recording lies in the **goal**. The pilot is an **exploratory test** of your ontology, often using flexible tools like paper maps and notebooks. The final [[Field Surveys]] is a **systematic execution** of your finalized DoD using structured tools to produce clean, consistent data.

After the pilot, you will have a finalized DoD, ready to be implemented in the next phase via [[Establishing the Data foundation#Data Schema Creation|data schema creation]] and [[Establishing the Data foundation#Data Recording|data recording]].

