---
title: SQL
draft: false
tags:
---

# SQL: Structured Query Language

**SQL (Structured Query Language)** is the standard language used to interact with relational databases. It allows users to retrieve, manipulate, and manage data through various commands and clauses. SQL operates on the foundation of **first-order predicate logic**, making it a powerful tool for querying data stored in relational tables. SQL is not a general-purpose programming language like Python. Strictly speaking, SQL is a **declarative, domain-specific language** designed to handle **data retrieval and manipulation** in relational databases rather than a full-fledged programming language. In this way, SQL is the de facto standard for querying and manipulating data in a [[Relational Database (Concept)|Relational Database]] and for filtering data in [[Concepts/Framework/GIS]] like [[QGIS]].

## Example Tables

We’ll use the following tables for the examples throughout this note. These tables represent data relevant to geography and planning in Danish towns.

### Towns Table

| TownID | TownName     | Population | Area (sq km) |
|--------|--------------|------------|--------------|
| 1      | Copenhagen   | 794128     | 88.25        |
| 2      | Aarhus       | 285273     | 91.00        |
| 3      | Odense       | 180760     | 304.34       |
| 4      | Aalborg      | 120194     | 139.95       |
| 5      | Esbjerg      | 71683      | 221.00       |

### LandUsePlans Table

| PlanID | TownID | PlanType        | AreaCovered (sq km) |
|--------|--------|-----------------|---------------------|
| 101    | 1      | Residential     | 40.00               |
| 102    | 2      | Commercial      | 20.00               |
| 103    | 3      | Industrial      | 60.00               |
| 104    | 4      | Residential     | 30.00               |
| 105    | 5      | Commercial      | 100.00              |

### Queries and Results

### 1. Basic Predicate with WHERE

Let’s start by selecting towns with a population greater than 150,000:

```sql
SELECT TownName, Population
FROM Towns
WHERE Population > 150000;
```

**Result:**

| TownName     | Population |
|--------------|------------|
| Copenhagen   | 794128     |
| Aarhus       | 285273     |
| Odense       | 180760     |

### 2. Combining Predicates with AND

Next, we’ll select towns with a population greater than 150,000 and an area of less than 100 sq km:

```sql
SELECT TownName, Population, Area
FROM Towns
WHERE Population > 150000 
AND Area < 100;
```

**Result:**

| TownName     | Population | Area (sq km) |
|--------------|------------|--------------|
| Copenhagen   | 794128     | 88.25        |
| Aarhus       | 285273     | 91.00        |

### 3. Combining Predicates with OR

Now, we’ll select towns that either have a population greater than 150,000 **or** an area greater than 100 sq km:

```sql
SELECT TownName, Population, Area
FROM Towns
WHERE Population > 150000 
OR Area > 100;
```

**Result:**

| TownName     | Population | Area (sq km) |
|--------------|------------|--------------|
| Copenhagen   | 794128     | 88.25        |
| Aarhus       | 285273     | 91.00        |
| Odense       | 180760     | 304.34       |
| Aalborg      | 120194     | 139.95       |
| Esbjerg      | 71683      | 221.00       |

### 4. Using AND and OR with Parentheses

We can combine **AND** and **OR** to create more complex conditions. For example, select towns with a population greater than 150,000 and either a residential or industrial land use plan:

```sql
SELECT Towns.TownName, Towns.Population, LandUsePlans.PlanType
FROM Towns
JOIN LandUsePlans ON Towns.TownID = LandUsePlans.TownID
WHERE Population > 150000 
AND (PlanType = 'Residential' OR PlanType = 'Industrial');
```

**Result:**

| TownName   | Population | PlanType    |
|------------|------------|-------------|
| Odense     | 180760     | Industrial  |

### 5. Spatial Query Example

Let’s incorporate spatial data. Suppose we want to find towns where the area covered by land-use plans is greater than 50 sq km. This could be particularly useful in urban planning where large-scale developments are planned.

```sql
SELECT Towns.TownName, LandUsePlans.PlanType, LandUsePlans.AreaCovered
FROM Towns
JOIN LandUsePlans ON Towns.TownID = LandUsePlans.TownID
WHERE LandUsePlans.AreaCovered > 50;
```

**Result:**

| TownName   | PlanType    | AreaCovered (sq km) |
|------------|-------------|---------------------|
| Odense     | Industrial  | 60.00               |
| Esbjerg    | Commercial  | 100.00              |



### 6. Joining Tables: Combining Towns and LandUsePlans

Let’s join the **Towns** and **LandUsePlans** tables to show the names of the towns along with their corresponding land use plans. We’ll use the `TownID` field, which is the foreign key in the **LandUsePlans** table, to join it with the **Towns** table.

```sql
SELECT Towns.TownName, Towns.Population, LandUsePlans.PlanType, LandUsePlans.AreaCovered
FROM Towns
JOIN LandUsePlans ON Towns.TownID = LandUsePlans.TownID;
```

**Result:**

| TownName     | Population | PlanType    | AreaCovered (sq km) |
|--------------|------------|-------------|---------------------|
| Copenhagen   | 794128     | Residential | 40.00               |
| Aarhus       | 285273     | Commercial  | 20.00               |
| Odense       | 180760     | Industrial  | 60.00               |
| Aalborg      | 120194     | Residential | 30.00               |
| Esbjerg      | 71683      | Commercial  | 100.00              |

### 7. Joining Tables with Filtering

We can also combine the join with a `WHERE` clause to filter the results. For example, let’s find towns with residential land-use plans:

```sql
SELECT Towns.TownName, Towns.Population, LandUsePlans.PlanType, LandUsePlans.AreaCovered
FROM Towns
JOIN LandUsePlans ON Towns.TownID = LandUsePlans.TownID
WHERE LandUsePlans.PlanType = 'Residential';
```

**Result:**

| TownName     | Population | PlanType    | AreaCovered (sq km) |
|--------------|------------|-------------|---------------------|
| Copenhagen   | 794128     | Residential | 40.00               |
| Aalborg      | 120194     | Residential | 30.00               |

## Variants of SQL
There are especially two variants of SQL you come across when working with geospatial data, namely the simplified version used to filter a feature class based on some attributes and the addition of spatial operators found in spatial SQL.


###   Simplified SQL for filtering in desktop GIS

In many desktop GIS applications like QGIS, SQL is often used to filter features based on attributes. For example, to filter out all towns where the population is greater than 100,000 for further analysis in QGIS:

```sql
SELECT TownName, Population
FROM Towns
WHERE Population > 100000;
```

**Result:**

| TownName     | Population |
|--------------|------------|
| Copenhagen   | 794128     |
| Aarhus       | 285273     |
| Odense       | 180760     |
| Aalborg      | 120194     |

Here’s an additional example where the two tables, **Towns** and **LandUsePlans**, are joined. This will show how a **JOIN** works to combine data from related tables based on a common key.


### Spatial SQL
While this note introduces SQL and its use in relational and spatial contexts, a separate note will cover the specifics of how SQL can be extended to support geospatial data management, including **OGC Simple Features** and their implementation in **[[PostGIS]]**, which enables more advanced spatial queries and operations.