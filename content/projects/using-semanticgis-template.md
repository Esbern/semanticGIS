---
title: Using the SemanticGIS Project Template
draft: false
tags:
  - projects
  - template
  - bootstrap
  - ai
---
# Using the SemanticGIS Project Template

Use this guide when you want to start a new SemanticGIS project with the standard scaffold, secure credential handling, and intent-first workflow.

## Template repository

- GitHub template: https://github.com/Esbern/semanticGIS-template

## Why use the template

- consistent project structure across teams and cohorts
- safer defaults for credentials (`.env` ignored, `.env.example` committed)
- faster AI onboarding with fewer setup mistakes
- better project stewardship and reproducibility

## Recommended start flow

1. Open the template repository on GitHub.
2. Click **Use this template**.
3. Create a new repository for your project.
4. Clone the new repository locally.
5. Copy `.env.example` to `.env` and set local values.
6. Start your Phase 1 scoping with AI.

## Included scaffold

The template includes:

- `Design_Rationale.md`
- `copilot-instructions.md`
- `.gitignore`
- `.env.example`
- `01_Scoping/`
- `02_Modelling/`
- `03_Sanctuary/raw/`
- `03_Sanctuary/processed/`
- `04_Analytics/`
- `05_Outputs/`

## Security baseline

- never commit real API keys
- keep `.env` local only
- keep local sensitive/raw material out of Git unless sanitized intentionally

## Canonical references

- [[Part 99 Apendicies/SemanticGIS Project Bootstrap Manifest|SemanticGIS Project Bootstrap Manifest]]
- [[Part 99 Apendicies/Intent-First Copilot Instructions Template|Intent-First Copilot Instructions Template]]
- [[Introduction|Introduction: The SemanticGIS Manifesto]]

## Suggested AI prompt

```text
Start a SemanticGIS project from this repository template.
Use the bootstrap manifest and intent-first instructions as canonical guidance.
Before any data download or analysis code:
1. Summarize project intent in 5 bullets.
2. Ask me 5 scoping questions.
3. Confirm credentials are read from .env and never committed.
Then stop and wait for approval.
```
