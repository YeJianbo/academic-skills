---
name: nature-figure
description: "Create, revise, or audit scientific manuscript figures, multi-panel plots, and journal-ready SVG/PDF/TIFF exports. Use for 论文配图、科研绘图 and publication figure polishing. Supports R and Python; honor established user choices and otherwise use R. Not for dashboards or general infographics."
metadata:
  version: 2.0.0
  author: Community contribution, refactored into static/dynamic layers
---

# Nature Figure

Read [manifest.yaml](manifest.yaml) and its `always_load` files for figure requirements, data integrity, privacy, and visual design. Load only the backend fragment and references needed for the current figure.

## Choose the backend

Use the selection rule in [static/core/contract.md](static/core/contract.md). The current request and established user instructions, including AGENTS.md, determine the backend; this installation defaults to R. An explicit request to continue existing Python plotting code counts as choosing Python. Data originating in Python does not by itself choose a plotting backend. Proceed without asking the user to repeat an established choice.

The manifest maps `r` to ggplot2/patchwork/ComplexHeatmap and `python` to matplotlib/seaborn. Read the selected fragment; do not load the other one. Keep all drawing, previewing, exporting, and visual QA in the selected backend.

## Produce the figure

1. Inspect the source data and identify the question, variable meanings, panel plan, statistics, dimensions, and exports. Reuse manuscript context. Ask only about missing information that would change the scientific meaning; routine styling can proceed with stated assumptions.
2. Apply the core design guidance and the selected backend fragment. Do not fabricate results or modify data to improve the appearance.
3. Reuse the existing editable source, palette and icons; make local edits there. Export and inspect affected requested formats at intended size, then resolve clipping, unreadable labels, misleading encodings and unsupported statistical annotations. Reuse the current preview path; expand QA only when shared styles or layout affect other panels. Deliver the reproducible source and requested formats.

Use the on-demand references in the manifest for specific needs: figure planning, backend recommendations, R workflows, typography, layout recipes, and publication QA. Keep detailed design notes in working files when useful; no separate approval of a figure plan is required when the task is already authorized.
