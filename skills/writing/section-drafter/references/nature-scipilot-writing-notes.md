# Nature / SciPilot Writing Notes for Section Drafting

This reference extracts reusable writing-process ideas from the local `scipilot-writing-skill` and Nature-style guidance. Use it as a process reference, not as a default venue style. The default domain remains computer science: cryptography, federated learning, privacy computing, security, and privacy-preserving machine learning.

## What to Borrow

1. **Contract before writing**: identify task type, text carrier, target venue, domain, language direction, and edit depth before drafting.
2. **Evidence-strength discipline**: claim strength must match proof, experiment, or analysis strength.
3. **Section playbooks**: every section has a job, information flow, required evidence, and common failure modes.
4. **Draft quality loop**: write Draft 0, self-check for logic and overclaiming, then produce Draft 1.
5. **Format hygiene**: preserve LaTeX commands, citation keys, labels, formulas, and terminology.

## What Not to Borrow Blindly

1. Do not force Nature/Science broad-audience style onto CS conference papers.
2. Do not move methods to the end unless targeting a Nature-family journal.
3. Do not use biomedical reporting rules such as CONSORT/STROBE unless the paper actually requires them.
4. Do not replace CS-style explicit contribution lists when the venue expects them.

## Section Moves Worth Reusing

### Abstract

Use the information flow:

`Background -> Gap -> Approach -> Key evidence -> Implication`

For CS/privacy papers, evidence may be:

- theorem or security guarantee,
- leakage/attack reduction,
- utility result,
- communication/computation improvement,
- deployment-scale benchmark.

### Introduction

Use CARS as a high-level rhetorical skeleton:

1. Establish the territory: why the problem matters in FL/privacy/security.
2. Establish the niche: what current methods cannot guarantee or cannot scale to.
3. Occupy the niche: what this paper contributes and why the key insight works.

For CS papers, keep a clear contribution list when appropriate.

### Methods / Technical Core

For CS, translate "Methods reproducibility" into:

- problem definition,
- threat/privacy model,
- protocol or algorithm details,
- assumptions,
- implementation details,
- complexity and reproducibility information.

### Results / Evaluation

Use the Results discipline:

1. state what the table/figure answers,
2. report key numbers,
3. avoid replaying every cell,
4. connect the result to the claim,
5. keep causal/security claims within the evaluated model.

## Drafting Gate

Before returning a section draft, check:

- Does each paragraph have one job?
- Does the first sentence announce that job?
- Does every strong claim have proof, analysis, or experimental evidence?
- Are missing citations, numbers, theorem labels, and figure references explicitly marked?
- Is the target venue style compatible with the output?
