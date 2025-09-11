---
title: Establishing the Data foundation
draft: false
tags:
aliases:
  - Establishing the Data foundation
order: "3"
---
Until now we have been focused on intellectual process of ensure a sound conceptual foundation for our project, we now come to a more practical phases of the GIS project where we in addition to intellectual processes also need to grab some tools and shovel some bytes and thus establish the data foundation of our project.

---
We now need to introduce the concept of a project document. This is not the  Design rational it is a software specific document, In both QGIS and ArcGIS Pro this is called the a project file. In Python it is typically a declaration block in the code. In the project document we establish a named connection between the processing environment (the GIS software) and the data structures that hold the date we intend to use in the project. 

## Data Acquiring
now we need to establish the physical database and populate it with the data we need for the project.

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

## Data Transforming
## Data Schema Creation
## Data Recording