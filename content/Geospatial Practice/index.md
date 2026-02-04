---
title: Geospatial Practice
draft: false
tags:
aliases:
  - Geospatial Practice
---
At the heart of semanticGIS is a desire to establish **geospatial practices** that focus on a structured, transparent, and well-documented process. This practice is built on two interacting components:

1.  **The Lifecycle (The 5 Phases):** A linear progression from question to result, moving from [[Geospatial Practice/Project Scoping/index|Scoping]] to [[Geospatial Practice/Dissemination and Communication/index|Dissemination]].
2.  **The Discipline (Project Stewardship):** A continuous, parallel layer of governance. [[Geospatial Practice/Project Stewardship/index|Project Stewardship]] runs alongside every phase, ensuring your work remains organized, documented, and reproducible via the [[Geospatial Practice/Project Stewardship/Design rationale|Design Rationale]].

Especially if you are new to doing geospatial analysis, it is advisable to study other projects and domain-specific considerations; therefore, this part of the website also contains links to a series of [[Geospatial Practice/Analytical Modelling/Common Analytical Patterns/index|Application Domains & Frameworks]] that highlight how the five phases can be implemented in different contexts.

---

## The Five Phases of the GIS-Project

Within the SemanticGIS framework, we recommend that you organise your geospatial practice into the following five phases.

#### **1. [[Geospatial Practice/Project Scoping/index|Project Scoping]]**
This is the foundational phase where you move from a vague idea (topic) to an actionable question. You define your research questions, establish clear objectives, identify your area of interest, and outline the project's scope and limitations.

#### **2. [[Geospatial Practice/Data Modelling/index|Data Modelling]]**
Before you collect any data, you design your conceptual **ontology**—the formal "rulebook" that defines the objects, features, and relationships you will be working with. This crucial step ensures your data will be consistent and fit for purpose.

#### **3. [[Geospatial Practice/Establishing the Data Foundation/index|Establishing the Data Foundation]]**
Here, you acquire and prepare your data. Whether you're conducting fieldwork, downloading existing datasets, or digitising historical maps, every action is guided by your data model and **actively recorded** in your Design Rationale.

#### **4. [[Geospatial Practice/Analytical Modelling/index|Analytical Modelling]]**
This is where you develop the methods to answer your research questions. In semanticGIS, we adopt a **Documentation Driven Development (DDD)** approach:
* **Think First:** You first write the "documentation"—defining the logical pipeline (the abstract recipe) in clear, human-readable terms.
* **Code Later:** Only once this logic is sound do you "compile" it—often using AI as an assistant—into concrete Python code or QGIS operations. This ensures that your analysis is driven by your scientific intent, not by syntax errors or software limitations.

#### **5. [[Geospatial Practice/Dissemination and Communication/index|Dissemination and Communication]]**
The final phase involves sharing your work. This includes not only your final maps and reports but the **Design Rationale** and the **Analytical Recipe** itself. By publishing your process (Provenance), you empower others to understand, critique, and confidently build upon your findings, fostering a culture of open and reproducible science.

---

## The Parallel Layer: Project Stewardship

While the **Five Phases** describe the *lifecycle* of your analysis (the chronological journey from question to answer), **[[Geospatial Practice/Project Stewardship/index|Project Stewardship]]** describes the *governance* of your project.

Think of Stewardship as the **continuous discipline** (or "Staff Function") that runs parallel to all five phases. It is the "hygiene" that keeps your project healthy.

* **In Phase 1 (Scoping):** Stewardship means setting up your folder structure and initializing your **Design Rationale**.
* **In Phase 3 (Data):** Stewardship means recording the provenance (source/date) of every file you download.
* **In Phase 5 (Dissemination):** Stewardship means ensuring your final package is archived correctly so it can be opened in 5 years.

**Rule of Thumb:** The Five Phases are about *getting the result*. Project Stewardship is about *ensuring the result is trustworthy and durable*.

---

## A Note on AI and Documentation Driven Development

SemanticGIS embraces the modern reality of AI-assisted coding. By adopting **Documentation Driven Development**, we shift the focus from memorising syntax to designing logic.

* **The Human's Role:** You are the **Architect**. You write the "Abstract Script" (the documentation) which defines _what_ happens to the data and _why_.
* **The AI's Role:** The AI acts as the **Compiler**. It takes your rigorous documentation and helps translate it into the specific Python syntax or software steps required.

This parallel to "Think First, Click Later" ensures that you remain in control of the process, even when using advanced tools to accelerate the execution.

## Exploratory Workflow vs. Prescriptive Workflow

Note that the execution of the five phases is not 100% linear like a [waterfall model](https://en.wikipedia.org/wiki/Waterfall_model). Within SemanticGIS, there is considerable **iterative refinement**—or "backflow"—from one phase to the previous.

The nature of this flow depends on your approach:

* **[[Geospatial Practice/Project Scoping/index#^Prescriptive-Workflow|Prescriptive Workflow]]**: The project workflow is identified by "reverse engineering" the required outputs. You know exactly what map you need (deductive reasoning), and you work backward to define the necessary data and analysis.
* **[[Geospatial Practice/Project Scoping/index#^Exploratory-Workflow|Exploratory Workflow]]**: You begin with a rich dataset or a broad question and use the analysis phase to discover patterns or relationships (inductive reasoning), allowing the final output to emerge from the data itself.