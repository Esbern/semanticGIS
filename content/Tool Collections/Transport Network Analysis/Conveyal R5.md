---
title: 
draft: false
tags:
---
**Conveyal R5** (R5: Rapid Realistic Routing on Real-world and Reimagined networks) is an advanced routing and accessibility analysis engine designed to support large-scale transportation and urban planning projects. While there is a commercial service available at [Conveyal](https://conveyal.com/), the core analysis engine, **R5**, is open source available at [GitHub](https://github.com/conveyal/r5), providing powerful capabilities for transportation researchers, planners, and developers. R5 is particularly suited for tasks that require analysing travel times and accessibility across entire metropolitan areas or regions, making it an invaluable tool for urban planning and public transit optimization.


**Open Source Tools for R5**

  
1. **R5py (Python Interface)**:
   R5py is a Python interface to the R5 engine, allowing users to easily integrate R5 into their Python-based workflows. It provides access to the full range of R5’s capabilities, including fast and scalable travel time analysis, making it a powerful tool for transportation research and urban planning in Python environments. More information can be found on the [R5py documentation page](https://r5py.readthedocs.io/en/stable/).

2. **R5r (R Interface)**:
   R5r is an R package that provides an interface to the R5 engine within the R programming environment. This package is designed for users who prefer R for their data analysis tasks, offering a seamless way to perform accessibility and travel time analyses. The package is well-documented and can be explored further on its [CRAN page](https://cran.r-project.org/web/packages/r5r/vignettes/r5r.html).


**R5 as an Analysis Engine vs. Routing Software for Individual Journeys**

One of the key distinctions between **R5** and other routing software like [[OpenTripPlanner]] (OTP) is the focus on large-scale analysis rather than individual journey planning:

• **Analysis-Oriented Routing**:

R5 is optimised for performing large-scale, many-to-many or many-to-one travel time analyses. For example, it can quickly calculate the travel time from numerous departure locations to a single destination, such as a school or medical facility, across a city. This capability is crucial for urban planners who need to assess the accessibility of public services or analyse the impact of transportation infrastructure changes on a large population.

• **Focus on Speed and Scalability**:

Unlike individual journey planners like OTP, where detailed route criteria such as accessibility, the number of transfers, or exact arrival times are essential, R5 prioritizes speed and scalability. It excels at providing travel time estimates within a given time window, which is more relevant for analysis than precise timings for specific journeys.

• **Time Window Analysis**:

R5 allows for the analysis of travel times within a time window, rather than requiring a specific departure or arrival time. This flexibility is important for understanding accessibility patterns and the potential variability in travel times due to factors like traffic or transit schedules.

• **Many-to-One Analysis**:

R5 is particularly effective for many-to-one analyses, which aim to determine travel times from multiple origins to a single destination. This type of analysis is beneficial for evaluating the accessibility of public services or understanding regional mobility patterns.
![[travel time surface.png]]