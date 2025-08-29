---
title: Spatial SQL
draft: false
tags:
---


# Spatial SQL: Working with Spatial Data in Databases

**Spatial SQL** is an extension of [[SQL]] that allows you to perform queries and operations on geographic data. Both **[[GeoPackage]]** and **[[PostGIS]] (for [[PostgreSQL]])** support spatial SQL, enabling powerful spatial queries that manipulate geographic features such as points, lines, and polygons. In desktop GIS environments like **QGIS**, spatial SQL combines traditional attribute-based queries with spatial operations, providing a flexible way to analyze and manipulate spatial data.

## Spatial SQL in GeoPackage and PostGIS

Both GeoPackage and PostGIS allow you to run spatial SQL queries. The same SQL syntax and spatial functions, such as `ST_Intersects` and `ST_DWithin`, are used across both platforms. The key difference is in the environment:
- **[[GeoPackage]]** is serverless, designed for smaller datasets, and is ideal for single-user, offline use cases.
- **[[PostGIS]]** is a server-based extension for [[PostgreSQL]], supporting larger datasets, scalability, and multi-user environments.

Despite these differences, the examples presented here work in both environments.

### Example Tables

The following tables are used for the examples in this note and mirror the **Towns** and **LandUsePlans** tables from the SQL note.

#### Towns Table (with spatial geometries)

| TownID | TownName     | Population | Area (sq km) | Geometry                    |
|--------|--------------|------------|--------------|-----------------------------|
| 1      | Copenhagen   | 794128     | 88.25        | POINT(12.5683 55.6761)      |
| 2      | Aarhus       | 285273     | 91.00        | POINT(10.2039 56.1629)      |
| 3      | Odense       | 180760     | 304.34       | POINT(10.4034 55.4038)      |
| 4      | Aalborg      | 120194     | 139.95       | POINT(9.9217 57.0467)       |
| 5      | Esbjerg      | 71683      | 221.00       | POINT(8.4543 55.4765)       |

#### LandUsePlans Table (with spatial geometries)

| PlanID | TownID | PlanType    | AreaCovered (sq km) | Geometry                     |
|--------|--------|-------------|---------------------|------------------------------|
| 101    | 1      | Residential | 40.00               | POLYGON((...))               |
| 102    | 2      | Commercial  | 20.00               | POLYGON((...))               |
| 103    | 3      | Industrial  | 60.00               | POLYGON((...))               |
| 104    | 4      | Residential | 30.00               | POLYGON((...))               |
| 105    | 5      | Commercial  | 100.00              | POLYGON((...))               |

---

## Attribute Queries in SQL

Like standard SQL, spatial SQL can perform attribute-based queries on relational data. For instance, selecting towns based on population size is a simple attribute query that works in both a GeoPackage and a PostGIS database.

### Example: Select Towns by Population

```sql
SELECT TownName, Population
FROM Towns
WHERE Population > 150000;
```

This query returns all towns with populations over 150,000. **Result:**

| TownName     | Population |
|--------------|------------|
| Copenhagen   | 794128     |
| Aarhus       | 285273     |
| Odense       | 180760     |

## Spatial Operations in [[SemanticGIS/Processing Environments/QGIS/index]] vs. Spatial SQL

In [[SemanticGIS/Processing Environments/QGIS/index]], spatial operations can be carried out using **native tools**, such as:
- **Select by Location**: Finding features based on spatial relationships (e.g., "find all towns within a certain polygon").
- **Buffering**: Creating buffer zones around points, lines, or polygons.

These native QGIS tools can be combined with **attribute queries**, but they often involve running separate steps for filtering by attributes and then performing spatial operations.

In contrast, **spatial SQL** allows both attribute filtering and spatial operations in a single query. This is more efficient for complex analyses because you can combine multiple logical and spatial conditions at once.

### Example: Spatial SQL with Attribute and Spatial Conditions

To find towns that are within a specific polygon (spatial condition) and have a population greater than 150,000 (attribute condition), you can use:

```sql
SELECT Towns.TownName, Towns.Population
FROM Towns
JOIN LandUsePlans ON Towns.TownID = LandUsePlans.TownID
WHERE ST_Within(Towns.Geometry, LandUsePlans.Geometry)
AND Towns.Population > 150000;
```

**Result:**

| TownName     | Population |
|--------------|------------|
| Odense       | 180760     |

### Spatial Queries in QGIS Using GeoPackage

In QGIS, you can run spatial SQL queries on GeoPackage databases using the **DB Manager** or **Virtual Layers**. For example, you could find all towns within a specific buffer zone around a landmark.

```sql
SELECT TownName, Population
FROM Towns
WHERE ST_DWithin(Towns.Geometry, ST_MakePoint(10.4034, 55.4038), 50000);
```

This query finds all towns within 50 kilometers of Odense, using the `ST_DWithin` spatial function, which works in both GeoPackage and PostGIS.

---

## Combining Attribute and Spatial SQL in QGIS

QGIS provides tools to execute both attribute and spatial queries. However, by using spatial SQL, you can combine these operations more seamlessly and with greater flexibility.

### Example: Finding Towns with Spatial and Attribute Conditions

Suppose you want to find all towns that intersect a specific land-use plan and have a population greater than 100,000. You could run this spatial SQL query:

```sql
SELECT Towns.TownName, LandUsePlans.PlanType
FROM Towns
JOIN LandUsePlans ON Towns.TownID = LandUsePlans.TownID
WHERE ST_Intersects(Towns.Geometry, LandUsePlans.Geometry)
AND Towns.Population > 100000;
```

**Result:**

| TownName   | PlanType    |
|------------|-------------|
| Copenhagen | Residential |
| Odense     | Industrial  |
| Aarhus     | Commercial  |

### Benefits of Spatial SQL Over Native Tools

- **Efficiency**: Combines both spatial and attribute queries in a single step.
- **Flexibility**: Allows more complex conditions using SQL operators such as `AND` and `OR`.
- **Reusability**: Spatial SQL queries can be saved, reused, and modified more easily than workflows created through native GIS tools.

---

## Reference to Further Notes

For more advanced geospatial queries, refer to the following notes:
- **[[PostGIS|PostGIS and SQL for Geospatial Processing]]**: This note covers how spatial SQL is extended in PostGIS and the advanced geospatial functions it provides.
- **[Working with QGIS and Spatial SQL]**: A deeper look into using QGIS’s DB Manager and Virtual Layers for running SQL queries on spatial data, particularly with GeoPackage databases.

---

