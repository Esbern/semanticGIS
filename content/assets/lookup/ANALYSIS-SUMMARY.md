# Dataset-to-Leaf Analysis Complete

**Analysis Date:** April 18, 2026
**Status:** Analysis only - no new leaves created (per user request)

## Summary of Work Completed

### 1. Forward Matching: Leaves → Datasets

**Status:** ✅ Previously completed (second pass, 153/200 realisations matched)

- All 46 leaves updated with "Realised By Links" sections
- Unmatched realisations visible in each leaf for manual curation
- Markdown lint verified clean

### 2. Reverse Matching: Unmatched Datasets → Leaves

**Status:** ✅ Just completed

#### Results:

- **Total unmatched datasets:** 2,069
- **Matched to existing leaves:** 317 (15.3%)
- **Remaining unmatched:** 1,752 (84.7%)

#### Top leaves receiving matches:

1. **Groundwater Chemistry** - 78 datasets
2. **Nature Protection Areas** - 27 datasets  
3. **Protected Water Use Zones** - 23 datasets
4. **Fisheries Intensity** - 20 datasets
5. **Groundwater Bodies** - 19 datasets

**Output files generated:**

- `datasets-matched-to-leaves.json` (317 matches with confidence scores)
- `datasets-matched-to-leaves.md` (human-readable match table)
- `datasets-remaining-unmatched.json` (1,752 unmatched with metadata)
- `datasets-remaining-unmatched.md` (analysis table)

---

## Gap Analysis: Potential New Leaves

**Status:** ✅ Analysis complete - awaiting human consent before creation

### Top Categories of Unmatched Datasets (by cluster):

| Cluster | Count | Priority | Status |
| --------- | ------- | ---------- | -------- |
| **INSPIRE/Open Data Services** | 403 | Low | Infrastructure/platform issues, not subject-specific |
| **Other/Uncategorized** | 847 | Needs review | Diverse datasets, may group into multiple leaves |
| **Environmental Noise** | 98 | **HIGH** | EU Noise Directive requirement; 98 datasets ready to map |
| **Land Planning (PlanDK)** | 65 | **HIGH** | Critical INSPIRE theme; may need 2-3 separate leaves |
| **Water Source Protection** | 53 | **HIGH** | Drinking water infrastructure; distinct from existing water leaves |
| **Fisheries Data** | 58 | Medium-High | Partly covered; additional datasets available |
| **Forest Management** | 38 | Medium-High | Distinct from habitat-extent; management-focused |
| **Agricultural Practices** | 29 | Medium | Could extend existing Agriculture leaf |
| **Biodiversity Directives (Natura 2000)** | 48 | Medium-High | Complements existing Nature Protection Areas leaf |
| **Transport Infrastructure** | 21 | Medium | Rail, road, pipeline networks |
| **Emissions & Air Quality** | 18 | Medium | Regulatory; complements existing Atmospheric Deposition leaf |
| **Climate-Related Land Use** | 12 | Medium | Peatland management, forest restoration |
| **Cultural Heritage & Archaeology** | 13 | Low-Medium | Optional; not core geospatial data |
| **Greenland Datasets** | 17 | Low | Scope question: include Greenland data? |
| **Other Clusters** | <15 each | Low | Industrial facilities, waste, shipping, research monitoring |

---

## Recommended Priorities for New Leaves (Human Decision)

### Tier 1: Immediate Value (High priority)

1. **Environmental Noise & Air Transport** (98 datasets)
   - EU Noise Directive 2002/49/EC compliance
   - Noise mapping by source: rail, road, aviation
   - Sample datasets: "Støj fra jernbaner", "Støj fra større vejanlæg"

2. **Spatial Planning & Municipal Decisions** (65 datasets)
   - PlanDK registry datasets
   - Sample datasets: "Store husdyrbrug - PlanDK", "Administrative skel - PlanDK"
   - Consider: May warrant separate leaves for municipal/regional/national levels

3. **Drinking Water & Water Source Protection** (53 datasets)
   - Distinct from existing groundwater/freshwater leaves (focus on infrastructure)
   - Sample datasets: "VP3 - Dybe drikkevandsforekomster", "Sensitive Drinking Water Areas"

### Tier 2: Moderate Value (Medium priority)

4. **Natura 2000 & EU Biodiversity Directives** (48 datasets)
   - Complements "Nature Protection Areas" leaf
   - Sample: "Natura 2000 Bird Protection Areas", EU habitat directive datasets

5. **Forest Ecosystems & Management** (38 datasets)
   - Distinct from "Habitat Extent" (focus on management/forestry)
   - Sample: "Forest Type Map", "Management units", "Urørt skov"

6. **Fisheries Monitoring & Management** (58 datasets)
   - Partly overlaps existing "Fisheries Intensity" leaf
   - Could extend existing leaf with additional VP/NP datasets

7. **Agricultural & Land Use Practices** (29 datasets)
   - Ecological condition, crop rotation, soil management
   - Could extend existing "Agricultural Land Management" leaf

### Tier 3: Optional/Low Priority

8. **Air Quality & Emissions Inventories** (18 datasets)
   - Regulatory reporting (PM10, NOx); could extend "Atmospheric Deposition" leaf

9. **Industrial Facilities & Contamination Risk** (10 datasets)
   - Could extend "Spill and Pollution Incidents" leaf

10. **Transport Infrastructure Networks** (21 datasets)
    - Rail corridors, pipelines, utility lines

---

## What Requires Human Review

### 1. INSPIRE/Service Issue (403 datasets)

Many unmatched entries are **metadata about INSPIRE web services** rather than actual datasets:

- "DK INSPIRE AM Areas for Groundwater Protection - **service**"
- "DK INSPIRE PS Natura 2000 - **service**"

**Action needed:** Determine if these should be:

- Excluded from analysis (metadata artifacts)?
- Merged with parent dataset entries?
- Handled differently?

### 2. Large "Other" Category (847 datasets)

Nearly 50% of unmatched datasets remain uncategorized. Likely causes:

- Diverse theme combinations not captured by keyword clustering
- Multi-language variations (Danish/English)
- Technical/platform datasets (versions, updates)

**Action needed:** Manual sampling to identify patterns

### 3. Greenland Datasets (17)

- **Question:** Should SemanticGIS cover Greenlandic data?
- If yes, may need separate organizational structure or scope clarification

---

## Files Available for Review

All analysis outputs in: `/DanishData/content/assets/lookup/`

- **datasets-matched-to-leaves.md** – Human-readable matches (317 datasets mapped to 46 leaves)
- **datasets-remaining-unmatched.md** – Top 100 unmatched datasets with best-match suggestions
- **gap-analysis-potential-new-leaves.md** – Detailed cluster analysis with recommendations

---

## Next Steps (Awaiting Your Guidance)

**Option A: Review & Create New Leaves**

1. Review gap analysis and prioritized recommendations
2. For each approved new leaf:
   - Define: concept, question, primary_collection
   - Map realisations from unmatched datasets list
   - Follow existing leaf template in `DanishData/content/Leaves/`
3. Notify when new leaves created; re-run matching script
4. Update leaves with "Realised By Links" sections

**Option B: Refine Matching Heuristics**

1. Tune F1 threshold or keyword matching logic
2. Handle INSPIRE service metadata separately
3. Improve language normalization for Danish/English

**Option C: Manual Curation**

1. Review `datasets-remaining-unmatched.json` manually
2. Create mapping spreadsheet of dataset → recommended leaf
3. Batch create new leaves based on manual analysis

**No action** until you confirm which path forward.

---

## Bidirectional Coverage Summary

| Direction | Status | Details |
| ----------- | -------- | --------- |
| **Leaves → Datasets** | ✅ 153/200 | Realisations matched to concrete datasets |
| **Datasets → Leaves** | ✅ 317/2069 | Unmatched datasets analyzed; gaps identified |
| **Visibility** | ✅ Complete | Leaves have "Realised By Links" sections; unmatched lists in audit artifacts |
| **New Leaves** | ⏸️ Pending | Gap analysis complete; awaiting human consent |
