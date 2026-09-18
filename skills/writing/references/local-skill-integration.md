# Local Skill Integration

This file records local skills that can support the writing workflow. Keep them as external collaborators; do not duplicate their full content into `writing`.

## Primary Writing Workflow

For computer science writing, select the owner for the actual request from the following roles. This is not a mandatory sequence; existing paragraphs can go directly to polish, and an authorized complete draft continues through the requested scope:

1. `paper-architecture-planner`
2. `section-drafter`
3. `section-writing-polish`
4. `academic-paper-de-vibe`

## External Local Skills

### `scipilot-writing-skill`

Path: `C:\Users\YeJianbo\.codex\skills\scipilot-writing-skill`

Use as an optional reference when the user asks for:

- Nature/Science/Cell/PNAS/IEEE journal-style tuning.
- SCI-style section playbooks beyond the CS conference norm.
- cover letter, rebuttal, table/figure captions, or broad journal submission writing.
- lint-like self-check ideas: AI fingerprints, mechanical connectors, overclaiming, LaTeX hygiene, Word/Markdown residue.

Do not use it as the default writer for cryptography, federated learning, or privacy-computing papers. The local CS workflow remains primary.

### `nature-figure`

Path: `C:\Users\YeJianbo\.codex\skills\nature-figure`

Use when the task is figure creation, figure polishing, multi-panel manuscript figures, Nature-style figure QA, SVG/PDF/TIFF export, or Python/R publication plotting. It is a figure workflow, not a prose-writing workflow.

### `scipilot-figure-skill`

Path: `C:\Users\YeJianbo\.codex\skills\scipilot-figure-skill`

Use when the user needs data visualization advice, chart selection, figure design, avoidance of common plotting errors, or Nature/Science/IEEE/Elsevier/PNAS-grade scientific figures. Use it for data-to-figure reasoning; use `nature-figure` for scientific figure production and QA, following the established user backend or the R default.

### `codex-paper-figure-skill`

Path: `C:\Users\YeJianbo\.codex\skills\codex-paper-figure-skill`

Use only when its figure-specific workflow is a better match than the two SciPilot/Nature figure skills. Check its own `SKILL.md` before using.

### `review`

Path: `C:\Users\YeJianbo\.codex\skills\review`

Use after drafting and polishing when the user asks for self-review, external-review simulation, method review, security/privacy proof audit, experiment/reproducibility audit, citation check, or rebuttal strategy.

Preferred routing:

- `cs-paper-reviewer`: whole-paper pre-submission review and simulated reviewer critique; it integrates the useful multi-reviewer and editorial-synthesis framework from `academic-paper-reviewer`.
- `security-privacy-auditor`: threat model, privacy claim, security proof, leakage, and assumption audit.
- `evaluation-reproducibility-auditor`: FL/privacy experiments, baselines, attack evaluation, utility/privacy/efficiency tradeoff, and reproducibility.
- `rebuttal-revision-planner`: reviewer-comment taxonomy, response strategy, and revision plan.

For normal prose de-vibe, keep using `academic-paper-de-vibe`.

### `top-conference-paper-writing`

Path: `C:\Users\YeJianbo\.codex\skills\top-conference-paper-writing`

This is a legacy duplicate of earlier top-conference writing guidance. Do not route new tasks to it by default. Its useful content is preserved under:

`paper-architecture-planner/references/legacy-top-conference-paper-writing.md`

## Routing Rules

1. If the user asks to plan or write a CS paper, stay inside `writing`.
2. If the user asks for Nature/Science/Cell style prose, consult `scipilot-writing-skill` and adapt only compatible process rules.
3. For figures, use `scipilot-figure-skill` when chart-selection advice is needed and `nature-figure` for production and QA.
4. If the user asks for post-draft review, route to `review` or `academic-paper-de-vibe` depending on whether they want reviewer critique or prose/logic cleanup.
5. Keep economics and medical writing resources as references only; do not use them by default.
