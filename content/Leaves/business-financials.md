---

title: Economics and Employment
type: leaf
draft: true
sphere: Socio_Technical
subsphere: Socio_technical_socioeconomic
concept: >-
  Cognised economic scale, financial performance, and workforce characteristics
  of firms and establishments
question: >-
  What are the economic and employment characteristics of a firm or
  establishment?
threads: []
tags: []
---

> **Cognised existence:** Economics and employment describe the measurable scale of a firm's activity — revenue, profit, assets, employment, and workforce intensity. The concept exists whether you read it from a company's filed annual report or from an aggregated statistical table. The granularity and access differ dramatically between sources.

**Question:** What are the economic and employment characteristics of a firm or establishment?

## What are Economics and Employment?

Economics and employment are not the firm itself (that's [[Leaves/firms|Firms]]). They are the *measurable scale and performance* of the firm or establishment — how much money flows in, how many people work there, how large the asset base is, and how labor is distributed over time. Understanding which sources carry what level of detail, and what reporting obligations apply, is critical for avoiding false zeroes (missing ≠ zero).

---

## Realisations

Instead of hardcoding implementation schemas here, SPHERE separates semantic meaning from dataset implementation. See the following realisations for how to access this data:

- **[[Realisations/CVR_CentraleVirksomhedsregister_business_financials|CVR (CentraleVirksomhedsregister) — Per-Entity Reports]]**
- **[[Realisations/Danmarks_Statistik_business_financials|Danmarks Statistik — Aggregated Statistics]]**

---

## Combining Realisations

| Need | Best Realisation | Why |
| --- | --- | --- |
| Per-company financial detail | CVR | Individual annual accounts |
| Employment by area | CVR or DST | CVR for per-entity, DST for aggregated time series |
| Sectoral benchmarking | DST | Aggregated averages and totals by NACE |
| Spatial financial heatmap | CVR + DAR | Geocode entities, aggregate by grid/area |
| Long-term economic trends | DST | Multi-year time series by sector and region |

## Classical Theme References

| Standard | Theme | Link |
| --- | --- | --- |
| INSPIRE | Production and Industrial Facilities | [[Classical Classifications/INSPIRE/production-and-industrial-facilities\\\|Production and Industrial Facilities]] |
