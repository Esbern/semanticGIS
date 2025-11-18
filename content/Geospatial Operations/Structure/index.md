---
title: Structure
draft: false
tags:
aliases:
  - structure
---
 Structue i information relecant to how data is stiores that somtime is needed to be exlpiclly statet  we have raster and vedtor but also sets (unordered) and lista (ordered= both of which must contain momogenius ellements  finaly we also have vector_points vector_lines and vestor_polygons  as well as taster continius and raster_categorical-
  
his is where the payoff happens. When the student calls `visualize.map()`, the system looks at the `MeasurementScale` and refuses to generate a bad map.

**Scenario:** Student tries to map "Soil Type" (Nominal) using a "High-to-Low" Red gradient.

- **Current GIS:** Draws it. It looks like Soil Type A is "hotter" or "more" than Soil Type B. Misleading.
    
- **semanticGIS:**
    
    - _Check:_ `scale` is `NOMINAL`.
        
    - _Check:_ `style` is `sequential_gradient`.
        
    - _Action:_ **Warning:** _"You are applying a sequential gradient to Nominal data. This implies an order where none exists. Switched to default Qualitative palette (Paired)."_
        

**Scenario:** Student tries to map "Population" (Ratio) using unique random colors.

- **semanticGIS Action:** **Warning:** _"You are mapping Ratio data as distinct categories. You lose the magnitude. Switched to default Sequential palette (Viridis)."_
    

### The "Aggregation Guardrail"

This handles your `aggregate` module logic.

**Scenario:** Student tries to calculate the **Mean** of an Ordinal field (e.g., "Risk Level: 1, 2, 3, 4, 5").

- _Math:_ (1+5)/2=3.
    
- _Logic:_ The "average" of Low Risk and Extreme Risk is not necessarily Medium Risk. The distance between 1 and 2 might be different than 4 and 5.
    
- **semanticGIS:**
    
    - `aggregate.summarize(field="Risk", stat="mean")`
        
    - _Error:_ "Statistical Error: You cannot calculate the Mean of Ordinal data. Use Median or Mode."
        

### Application to `Raster`

We can map these scales to our previously discussed Raster types:

- **`RasterCategorical`**:
    
    - Subtype: **Nominal** (Land Use)
        
    - Subtype: **Ordinal** (Suitability Raster 1-10)
        
- **`RasterContinuous`**:
    
    - Subtype: **Interval** (Temp Surface)
        
    - Subtype: **Ratio** (Elevation relative to absolute datum, Slope, Rainfall)
        

### Strategic Verdict