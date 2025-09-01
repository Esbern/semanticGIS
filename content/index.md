---
title: Welcome to Semantic GIS
tags:
---
# Semantic GIS: Think First, Click Later.

Geospatial analysis is more than a series of clicks; it's a scientific process. Yet, our workflows often become opaque, hard to reproduce, and locked into a single software tool. How do you document your reasoning? How can you share your methodology in a way that anyone can understand and replicate?

**SemanticGIS provides a framework for structured geospatial thinking.** We advocate for a clear separation between the _'what'_ (your conceptual plan) and the _'how'_ (the tool-specific implementation). This begins not with code, but with a clear, four-step **Design Rationale**.

---

## The Core of Our Method: The 4-Step Design Rationale 🧠

This four-step process guides you from a vague question to a well-documented and defensible result. It ensures you have a solid plan before you write a single line of code or click a single button.

1. **Problem Framing & Conceptual Ontology:** First, define the problem in your own words. What are the key goals? What are the important real-world entities involved (e.g., specific businesses, noise complaints, administrative zones)? This step is about building a clear conceptual foundation for your project.
    
2. **Data Selection:** Next, decide how to represent those real-world entities as digital data. You'll identify suitable datasets, justify your choices, and consider any necessary transformations or filtering. This is where you connect your abstract concepts to concrete spatial data.
    
3. **Analytical Approach:** Now, you design the specific sequence of operations to answer your question. You deconstruct your problem into a formal **"recipe"**—a simple, human-readable script that defines each analytical step (e.g., buffer, spatial join, density analysis). This script becomes the unambiguous, tool-agnostic plan for your analysis. You can write this "**recipe**" in any tool you chose as either a text or a graphical workflow.  This is also where the `semanticgis` Python library comes in.
    
4. **Dissemination & Communication:** Finally, you plan how to present your findings. Who is the audience? What is the best way to communicate the results—an interactive map, a static report, a presentation? This ensures your hard work has the intended impact.
    

---

## From Recipe to Result: Our Tools for Transparency 🚀

Once you've defined your **Analytical Approach** (Step 3) as a `semanticgis` recipe, our tools can automatically translate it into multiple formats:

- A **visual flowchart** to clearly illustrate your methodology in reports and presentations.
- A **step-by-step guide** for executing the workflow in desktop software like QGIS.
- A fully **executable Python script** for automated processing and advanced analysis.
    
## Where to Start

SemanticGIS is an actively developing project. A great place to begin is by reading the full documentation on the **[[Design Rationale]]**. From there, the "GIS 101" section will walk you through a complete project using these principles.