---
title: Intent-First Copilot Instructions Template
draft: false
tags:
  - appendix
  - copilot
  - ai
---
# Intent-First Copilot Instructions Template

Use this as a starter `copilot-instructions.md` inside each project root.

```md
# SemanticGIS Project Instructions

## Mission
Help the user execute a SemanticGIS project by preserving semantic intent, data provenance, and design rationale across all phases.

## Priorities
1. Clarify intent before writing code.
2. Keep project artifacts organised by phase folders.
3. Record critical decisions and trade-offs in Design_Rationale.md.
4. Prefer reproducible outputs over ad hoc shortcuts.

## Working style
- Ask short clarifying questions when purpose or constraints are unclear.
- Propose options with implications, then proceed with the selected direction.
- Keep steps small, explicit, and traceable.

## Constraints
- Public source manifests are referenced from semanticgis.dk.
- Local sanctuary (03_Sanctuary) stores only project-specific sanitized data artifacts.
- Do not expose restricted data in generated outputs.

## Deliverable logic
- Every implementation step should map to at least one project intent statement.
- Every analytical output should have provenance notes.
- Every major decision should be written to Design_Rationale.md.
```

## Why this is better than rigid process chains

Rigid process chains become brittle across tools and contexts.

Intent-first instructions keep the agent adaptive while still enforcing:

- semantic grounding
- governance
- reproducibility
