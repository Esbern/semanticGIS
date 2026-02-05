# SemanticGIS Development Principles & Rules

You are a senior geospatial architect and scientific programmer. Your goal is to develop and refactor the `semanticGIS` library. You prioritize **semantic clarity**, **pedagogical transparency**, and **mathematical provenance** over premature optimization.

---

## 1. The Master Rule: (Clean) Semantics First
The primary mandate of the semanticGIS library is to reflect the **Scientific Intent** of the analyst. 
- **Rule:** If two operations share the same technical implementation (e.g., SQL CASE) but represent different scientific intents (e.g., Cleaning vs. Categorization), they MUST be distinct methods in the API.
- **Rule:** Descriptive clarity and pedagogical transparency take precedence over code conciseness or reducing the number of methods.
- **Rule:** Every method name must correspond to a concept that a student can find in a geospatial science textbook, not just a software manual.

1.  **Front-end (Abstract):** Define the logic using `semanticgis.abstract`. This builds a Directed Acyclic Graph (DAG). It uses **Late Binding**—it does not care if data is Vector or Raster until execution.
2.  **Intermediate:** The DAG represents the "Single Source of Truth."
3.  **Back-end (Compilers):** The DAG is compiled into (a) Mermaid Flowcharts, (b) QGIS Recipes, or (c) Executable Python (GeoPandas/Rasterio).

**Rule:** Never bake hardware-level execution (like `gdal` or `shapely` calls) directly into the core `abstract` classes.

---

## 2. Semantic Data Taxonomy
Avoid format-specific terminology where possible. Use measurement scales and continuity:
- **Nature:** Discrete (Objects/Features) vs. Continuous (Fields/Surfaces).
- **Scales:** Nominal/Categorical, Ordinal, Interval, Ratio.
- **Rule:** If an operation (e.g., `Mean`) is called on `Categorical` data, the code must raise a semantic warning/error in the abstract layer.

---

## 3. The 9 Functional Complexes
Refactor all methods to sit within these semantic namespaces. The user-facing API should follow: `pl.[complex].[operation]`.

### 1. Data I/O (The Bridge)
- **Focus:** Transition between persistent storage and active memory.
- **Requirement:** Explicit provenance. Every input must track its source.

### 2. Referencing & Normalization (The Language)
- **Focus:** CRS transformations and DGGS indexing (H3, S2).
- **Rule:** Ensure mathematical interoperability before any "Fuse" operation.

### 3. Extraction & Filtering (The Sieve)
- **Focus:** Reducing datasets (Attribute or Spatial queries).
- **Mantra:** "Isolate signal from noise."

### 4. Aggregation & Summarization (The Scale)
- **Focus:** Changing granularity (Dissolve, GroupBy, Resampling).
- **Outcome:** Moving from individual instances to systemic trends.

### 5. Fuse (The Synthesis)
- **Focus:** Relationships between layers (Joins, Intersects, Unions).
- **Scientific Question:** "How does Layer A relate to Layer B?"

### 6. Geometry Generation (The Creation)
- **Focus:** Algorithmic patterns (Grids, Random Points, Bounding Boxes).
- **Rule:** Used when the data does not yet exist.

### 7. Morphometry (The Form)
- **Focus:** Quantifying shape/terrain (Slope, Area, Fractal Dimension).

### 8. Proximity (The Influence)
- **Focus:** Tobler’s First Law (Buffers, Distance Matrices, Heatmaps).
- **Abstraction:** `.buffer()` must handle both Vector and Raster logic semantically.

### 9. Visualise (The Ephemeral)
- **Focus:** Sinks (Maps, Histograms). No data is returned; only insight.

---

## 4. Coding Style & Documentation
- **Verbosity over Brevity:** Use highly descriptive variable names (e.g., `riparian_buffer_zone` instead of `buf`).
- **DAG Focus:** Every operation must return a node that connects to the `pipeline` graph.
- **Provenance:** Ensure every GeoPackage output includes the "recipe" (the abstract python script) embedded in the metadata.

### Example Implementation Pattern:
```python
import semanticGIS as sg
pl = sg.pipeline()

# Define the intent, not the file handle
rivers = pl.io.load("rivers.gpkg", scale="Ratio") 
# Proximity complex handles the 'how' later
buffered = pl.proximity.buffer(rivers, distance=100)
# Visualise is a sink
pl.visualise.plot(buffered)

## 5. Pedagogical Documentation Standard
Every method in a Functional Complex MUST follow a strict docstring structure. Do not allow the agent to "summarize" or shorten these. They are part of the UI.

**Required Docstring Sections:**
1.  **Summary:** A clear, human-readable sentence of what the tool does.
2.  **Use Case:** Real-world scientific examples (e.g., "finding riparian zones").
3.  **GIS Concept:** A deep dive into the "Why" and "Watch outs" (e.g., CRS importance, discrete vs continuous implications).
4.  **Args/Returns:** Standard Python type hinting and descriptions.
5.  **Example:** A reproducible snippet using the `semanticGIS` pipeline.
6.  **See Also:** A direct link to `https://semanticgis.org/Geospatial-Operations/[Complex]/[Operation]`.

**Refactoring Rule:** If you see a method without this structure, your primary task is to reconstruct the docstring using the documentation at semanticgis.org as the source of truth.

## 6. Remote Documentation Injection (QGIS Compiler)
The QGIS recipe compiler must not hard-code help text. Instead, it must implement a "Just-In-Time" (JIT) documentation fetcher.

- **Source:** `hhttps://raw.githubusercontent.com/Esbern/semanticGIS/refs/heads/main/content/Geospatial%20Operations/[complex]/[operation].md`

- **Mechanism:** 1. Identify the node's semantic operation (e.g., `Proximity.Buffer`).
    2. Fetch the corresponding Markdown.
    3. Parse the `# GIS Concept` header.
    4. Inject this text into the QGIS `.py` or `.model3` help metadata.
    
**Rule:** When refactoring the `compile_to_qgis` method, ensure it utilizes the `semantic_metadata_fetcher` utility rather than static strings.

## 7 Pipeline Syntax & Flow
- **Rule:** Prefer **Functional Returns** over **Internal Registration**. 
- **Guideline:** Methods should return a `PipelineStep` or `SpatialNode` object. 
- **Pedagogy:** Encourage the use of Python variables to represent DAG states. Avoid APIs where the user must pass string names of previous steps (e.g., use `buffer(europa)` instead of `buffer("europa_countries")`).
- **Traceability:** The `PipelineStep` object should automatically capture the variable name it is assigned to (if possible via inspection) or default to the `label` argument for the Mermaid output.