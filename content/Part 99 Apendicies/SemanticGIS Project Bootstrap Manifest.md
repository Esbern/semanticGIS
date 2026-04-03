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

## Quick Access

If you want to start from a ready GitHub template instead of an empty folder, use:

- [[projects/using-semanticgis-template|Using the SemanticGIS Project Template]]

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
  semantic_id: [project_semantic_id]
  title: [project_title]
  intent: |
    [Describe the scientific and practical intent of the project in 2-4 lines.]
  epistemic_mode: [heuristic | teleological]

structure:
  root_files:
    - Design_Rationale.md
    - copilot-instructions.md
    - README.md
    - .gitignore
    - .env.example
  folders:
    - 01_Scoping
    - 02_Modelling
    - 03_Sanctuary/raw
    - 03_Sanctuary/processed
    - 04_Analytics
    - 05_Outputs

secrets_and_env:
  required_env_vars:
    - DATAFORDELER_API_KEY
  rules:
    - Never commit real secrets to Git.
    - Keep only placeholder values in .env.example.
    - Add .env to .gitignore.
  starter_env_example: |
    # Copy this file to .env and fill with real values locally.
    DATAFORDELER_API_KEY=replace_with_real_key

git_hygiene:
  required_gitignore_entries:
    - .env
    - .venv/
    - __pycache__/
    - *.pyc
    - *.log
    - .DS_Store
    - 03_Sanctuary/raw/**
  note: Keep raw/sensitive local material out of version control unless explicitly sanitized.

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
    - Never print, persist, or commit real API keys.

starter_data_hints:
  candidate_sources:
    - [source_manifest_1]
    - [source_manifest_2]
  first_task_prompt: |
    Create the project structure, initialize Design_Rationale.md,
    and propose a first scoping interview aligned with the project intent.
```

## How users can use it with AI

Use this manifest as a structure contract, and use the template repository as the default start path.

## Getting Started (Recommended)

### Option A: GitHub template + clone (default)

1. Open https://github.com/Esbern/semanticGIS-template
2. Click **Use this template**
3. Create a new repository
4. Clone the new repository locally
5. Copy `.env.example` to `.env` and set local values (for example `DATAFORDELER_API_KEY`)
6. Start Phase 1 scoping with AI

### Option B: No Git workflow (ZIP)

1. Open https://github.com/Esbern/semanticGIS-template
2. Click **Code** -> **Download ZIP**
3. Unpack into a local project folder
4. Copy `.env.example` to `.env` and set local values
5. Start Phase 1 scoping with AI

### Minimal AI start instruction

```text
Use this folder as a SemanticGIS project scaffold.
Before any data download or analysis code:
1. Summarize project intent in 5 bullets.
2. Ask 5 scoping questions.
3. Confirm credentials are loaded from .env and never committed.
Then stop and wait for approval.
```

## Template Repository

Current SemanticGIS template repository:

- Local parent path: `projects/semanticGIS-template`
- GitHub: https://github.com/Esbern/semanticGIS-template

Recommended baseline in the template repository:

- the full scaffold from this bootstrap manifest
- `.gitignore` with secret and local-runtime exclusions
- `.env.example` with placeholders only
- starter `README.md` describing setup and env variables
- optional CI checks (lint/test) if your team uses them

Suggested user flow:

1. Click "Use this template" on GitHub
2. Create new project repository from template
3. Clone locally
4. Copy `.env.example` to `.env` and fill local key values
5. Start Phase 1 scoping with AI

This gives consistent project structure, better stewardship, and safer default secret handling.

## Notes for Copenhagen party-zone case

A pragmatic first pass can start from CVR business entities and then refine with:

- opening-hour proxies
- noise-sensitive receptors
- temporal behavior patterns
- local policy constraints
