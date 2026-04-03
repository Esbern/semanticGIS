# SemanticGIS Project folder

The projects in this folder are for experiments (for example, bars and restaurants in Copenhagen).
Each project should be its own repository and should not be committed into the top-level SemanticGIS repository.

## Recommended workflow

1. Keep raw experiment code and local working files inside `projects/<project_name>/`.
2. Publish website-facing notes in `content/projects/`.
3. Publish website-facing assets in `content/assets/projects/<project_name>/`.
4. Link only to files under `content/` from website pages so links are stable in Quartz builds.

## Why this works

- `projects/` can stay independent and messy while prototyping.
- `content/` is the canonical, versioned source for semanticgis.org.
- Broken links are reduced because Quartz indexes `content/` directly.
