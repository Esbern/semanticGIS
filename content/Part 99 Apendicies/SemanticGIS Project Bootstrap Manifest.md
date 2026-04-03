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
3. Create Design_Rationale.md, copilot-instructions.md, .gitignore, and .env.example.
4. Add DATAFORDELER_API_KEY placeholder to .env.example and ensure .env is gitignored.
5. Ask me 5 scoping questions before any data download or analysis code.
6. Keep public source manifests external (semanticgis.dk), and keep local sanctuary focused on sanitized project outputs.

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
4. Create .gitignore and .env.example (with DATAFORDELER_API_KEY placeholder) and do not create/commit .env.
5. Create a minimal copilot-instructions.md using the intent-first template.
6. Ask me 5 scoping questions and draft 01_Scoping/Project_Outline.md.
7. Stop and wait for approval before data download or analysis code.

Rules:
- Keep public source manifests external on semanticgis.dk.
- Keep local 03_Sanctuary focused on sanitized project outputs.
- Never commit real credentials.
```

## Template Repository Recommendation

Yes. A GitHub template repository is the most stable way to bootstrap many similar projects.

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
