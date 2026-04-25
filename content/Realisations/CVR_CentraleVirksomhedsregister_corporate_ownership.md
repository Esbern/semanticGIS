---
title: "CVR (CentraleVirksomhedsregister) — Ownership Entities Realisation of Ownership and Governance"
type: realisation
draft: false
leaf: Ownership and Governance
dataset: CVR
tags:
  - realisation/cvr_centralevirksomhedsregister
  - leaf/corporate-ownership
---

**Leaf:** [[Leaves/corporate-ownership|Ownership and Governance]]
**Dataset:** CVR (CentraleVirksomhedsregister) — Ownership Entities

The sole authoritative realisation in Denmark. [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/index|CVR]] records ownership through a rich set of relation entities.

#### Spatial Access Path

```
ejerforhold / reelejerrelation / legalejerrelation
  │  FK: CVREnhedsId → target Virksomhed
  ▼
Virksomhed
  │  FK: → Adressering → DAR join chain
  │       adresse → husnummer → adgangspunkt.position
  ▼
adgangspunkt.position (point geometry via DAR)
```

**No native geometry.** Ownership is a graph structure. To map it spatially, join through the owned/owning entity to its address, then through the [[Leaves/addresses|Addresses]] join chain to coordinates.

#### Ownership Graph Structure

```
Person A ──owns 60%──► Company B ──owns 100%──► Company C
                                  ──owns 40%──► Company D

Person E ──board member──► Company B
```

Analysis typically requires **recursive traversal** or graph queries. Ownership chains can run through multiple intermediate entities (holding companies, foundations, foreign entities).

#### Key Entities

| Entity | Role |
| --- | --- |
| **[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/ejerforhold\\\|ejerforhold]]** | Direct ownership relationships |
| **[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/reelejerrelation\\\|reelejerrelation]]** | Beneficial (real) ownership — who ultimately controls the entity |
| **[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/legalejerrelation\\\|legalejerrelation]]** | Legal ownership chain |
| **[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/andendeltager\\\|andendeltager]]** | Other participants in ownership structures |
| **[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/fuldtansvarligdeltagerrelation\\\|fuldtansvarligdeltagerrelation]]** | Fully liable participant relations |
| **[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/ledelse\\\|ledelse]]** | Management and board members |
| **[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/ledelserelation\\\|ledelserelation]]** | Management role assignments |
| **[[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/kapitalforhold\\\|kapitalforhold]]** | Capital share structure |

#### Key Attributes

| Attribute | Description | Notes |
| --- | --- | --- |
| `ejerandel` | Ownership share (%) | May be a range rather than exact figure |
| `stemmeandel` | Voting share (%) | May differ from ownership share |
| `rollebeskrivelse` | Role description | Danish: "Direktion", "Bestyrelse", "Stifter" |
| `CVREnhedsId` | Identifier linking to the owned entity | Stable join key |

#### Legal vs Beneficial Ownership

| Layer | Entity | What it captures |
| --- | --- | --- |
| **Legal ownership** | `legalejerrelation` | Formal registered owner on paper |
| **Beneficial ownership** | `reelejerrelation` | Natural person who ultimately controls or benefits |
| **Management** | `ledelse` / `ledelserelation` | Directors, board members, executive roles |

For compliance and AML analysis, beneficial ownership is the critical chain. For corporate structure mapping, all three layers matter.

#### Access

- **GraphQL**: [[Data Portals/Datafordeleren/graphql|Datafordeleren GraphQL]] — ownership relation entities are queryable with nested fields
- **File Download**: Download multiple relation entities and join locally by `CVREnhedsId`
- **Note**: Some ownership data (especially involving natural persons) has access restrictions via [[Datasets by Collection/Grunddatamodellen/CentraleVirksomhedsregister/cvrperson|CVRPerson]]

## Temporal Model

Ownership is **bitemporal**. Ownership stakes change over time through acquisitions, mergers, and restructuring. Historical ownership analysis requires careful `virkningFra`/`virkningTil` filtering. Each ownership relation entity carries independent registration and effect periods.
