---
title: SemanticGIS Project Bootstrap Manifest
draft: false
tags:
  - appendix
  - bootstrap
  - ai
---
# SemanticGIS Project Bootstrap Manifest

Use this document when a user starts from an empty folder in VS Code and asks an AI agent to create a SemanticGIS project.

## Why this is intent-first

This manifest tells the agent:

- what the project is trying to achieve
- what structure must exist
- what artifacts must be produced

It does not over-prescribe an exact toolchain sequence.

## Bootstrap manifest template

```yaml
manifest_version: 1.0
manifest_type: semanticgis_project_bootstrap

project:
  semantic_id: cph_partyzones_v1
  title: Copenhagen Party Zones
  intent: |
    Identify and communicate party-zone patterns in Copenhagen,
    balancing nightlife accessibility, resident impact, and governance constraints.
  epistemic_mode: heuristic

structure:
  root_files:
    - Design_Rationale.md
    - copilot-instructions.md
    - README.md
  folders:
    - 01_Scoping
    - 02_Modelling
    - 03_Sanctuary/raw
    - 03_Sanctuary/processed
    - 04_Analytics
    - 05_Outputs

phase_outputs:
  01_Scoping:
    - Project_Outline.md
    - Stakeholder_Map.md
    - Research_Questions.md
  02_Modelling:
    - Ontology.md
    - NOIR_Attribute_Catalog.md
    - Data_Model_Diagram.md
  03_Sanctuary:
    - Sanctuary_Index.md
    - processed/README.md
  04_Analytics:
    - Analytical_Recipe.md
    - analysis_plan.md
  05_Outputs:
    - Output_Narrative.md
    - Visualisation_Spec.md

agent_brief:
  behavior:
    - Ask clarifying questions when intent is ambiguous.
    - Prefer semantic alignment over tool convenience.
    - Record assumptions in Design_Rationale.md.
  constraints:
    - Keep public-source manifests external (semanticgis.dk).
    - Keep local sanctuary focused on sanitized project data.
    - Avoid exposing restricted or personal data in outputs.

starter_data_hints:
  candidate_sources:
    - semanticgis.dk Datafordeleren source manifests
    - CVR for business entities
    - DAR for address grounding
  first_task_prompt: |
    Create the project structure, initialize Design_Rationale.md,
    and propose a first scoping interview for party-zone analysis.
```

## How users can use it with AI

Prompt pattern:

```text
I want to run a SemanticGIS project. Use the attached bootstrap manifest.
Create the folder structure and required files, then guide me through Phase 1 scoping.
```

## Copy-Paste First Prompt (Empty Folder)

Use this prompt as-is when starting from an empty folder:

```text
Start a SemanticGIS project in this empty folder.
Use the following pages as canonical references:
- SemanticGIS Project Bootstrap Manifest
- Intent-First Copilot Instructions Template
- Introduction: The SemanticGIS Manifesto

Task:
1. Summarize project intent in 5 bullets.
2. Create the project scaffold exactly as defined in the bootstrap manifest.
3. Create Design_Rationale.md and copilot-instructions.md.
4. Ask me 5 scoping questions before any data download or analysis code.
5. Keep public source manifests external (semanticgis.dk), and keep local sanctuary focused on sanitized project outputs.

After scaffolding and questions, stop and wait for my confirmation.
```

If the AI cannot access website content directly, paste the manifest content into the chat first and then run the same prompt.

## One-Shot Beginner Prompt (GitHub + Scaffold)

Use this prompt when users want the AI to handle setup end-to-end:

```text
I want to create a SemanticGIS project as described at semanticgis.org.

Read these canonical references first:
1. SemanticGIS Project Bootstrap Manifest
2. Intent-First Copilot Instructions Template
3. Introduction: The SemanticGIS Manifesto

Then do the following:
1. Initialize this folder as a Git repository.
2. Ask whether I want a new GitHub repository created and connected.
3. Create the SemanticGIS folder scaffold and root files from the bootstrap manifest.
4. Create a minimal copilot-instructions.md using the intent-first template.
5. Ask me 5 scoping questions and draft 01_Scoping/Project_Outline.md.
6. Stop and wait for approval before data download or analysis code.

Rules:
- Keep public source manifests external on semanticgis.dk.
- Keep local 03_Sanctuary focused on sanitized project outputs.
```

### Feasibility note

This is feasible in practice, with one caveat: some AI sessions cannot reliably fetch website pages.

Fallback strategy:

1. Copy the bootstrap manifest text into the chat.
2. Copy the intent-first instructions template into the chat.
3. Run the same one-shot prompt.

## Notes for Copenhagen party-zone case

A pragmatic first pass can start from CVR business entities and then refine with:

- opening-hour proxies
- noise-sensitive receptors
- temporal behavior patterns
- local policy constraints
