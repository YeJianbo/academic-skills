# Figure contract before plotting

For a new figure or a structural redesign, establish the scientific claim, evidence and relevant design constraints below. Reuse an existing figure contract and editable source. A label, color, spacing or export adjustment needs only the changed requirements and affected checks; do not rebuild the full contract before every edit.

## Backend selection

Honor an explicit choice in the current request, then an established choice in the conversation or applicable AGENTS.md. Otherwise use R. A request to modify or continue existing Python plotting code is an explicit Python workflow; a CSV, NumPy output, or Python data-processing script alone is not. State the selected backend and proceed; do not ask the user to repeat a choice or confirm the R default.

When the user asks for a backend recommendation, consult `references/backend-selection.md`, explain the relevant trade-off, and proceed with the recommendation within the requested scope.

## The selected backend is exclusive

Once Python or R is selected, every plotting script, preview image, SVG/PDF/TIFF/PNG export, QA render, and visual workaround must be produced by that same backend. Do not use Python to draw a preview for an R figure, and do not use R to draw a preview for a Python figure, even if the selected runtime or packages are missing locally. The non-selected language may only be used for non-visual file inspection or data conversion when it does not open a graphics device, import plotting libraries, create image/vector files, or change the final visual appearance.

## Missing runtime/package rule

After the backend is selected, check the selected runtime early (`Rscript`/R for R; Python and required plotting packages for Python). If the selected runtime or required packages are unavailable, stop before rendering and report the exact blocker. You may provide a selected-backend script and installation commands, or ask permission to install dependencies, but you must not fall back to the other language to make a substitute figure.

## The five-point contract

1. **Core conclusion**: write the one-sentence claim the figure must defend.
2. **Evidence chain**: map each planned panel to the claim, and drop panels that do not carry a unique piece of evidence.
3. **Archetype**: classify the figure as `quantitative grid`, `schematic-led composite`, `image plate + quant`, or `asymmetric mixed-modality figure`.
4. **Backend**: use the selected Python or R track exclusively for all figure drawing, previewing, exporting, and visual QA. Do not cross-render with the other language.
5. **Journal/export contract**: set final dimensions, editable text, source data, statistics, image-integrity notes, and export formats before styling.

The highest-priority rule is: **the chart serves the scientific logic**. Aesthetic polish, template matching, and complex layout are subordinate to making the core conclusion clear, defensible, and reviewable.

For the full method to convert a request into core conclusion, evidence hierarchy, panel map, and review-risk checks, open `references/figure-contract.md`.
