# Legacy CS De-Vibe Notes

This file preserves the earlier de-vibe checklist before it was integrated with the broader anti-AI and naturalization workflow.

## Original Scope

Act as a strict top-conference reviewer for CS papers and identify typical AI-generated "vibe paper" features. Improve academic rigor, logical depth, and natural scholarly expression.

## Original Diagnostic Areas

### 1. Motivation and System Design

- Diagnose stiff introductions, overly long module names, inconsistent abbreviations, and excessive bolding of module names.
- Fix by simplifying component names, keeping abbreviations consistent across text and figures, and removing unnecessary boldface.

### 2. Theorems and Lemmas

- Diagnose decorative theory, proofs weakly connected to the method, and restated existing theory without contribution.
- Fix by checking whether each theorem or lemma serves the method, aligning proof notation with definitions, and replacing unnecessary theory with logical derivation.

### 3. Mathematical Rigor

- Diagnose fragmented formulas, undefined symbols, and poor formula layout.
- Fix by defining every variable at first use and combining scattered equations into a coherent derivation.

### 4. Algorithms

- Diagnose unnecessary pseudocode that only describes standard procedures such as SGD, Adam, or simple data loops.
- Fix by keeping only pseudocode that captures the core contribution, such as a custom loss, sampling strategy, protocol, or attack/defense routine.

### 5. Structure and Lists

- Diagnose excessive bullet lists and false parallelism where the ideas should be causal or progressive.
- Fix by turning fragmented bullets into coherent paragraphs with explicit logical progression.

### 6. Experimental Analysis

- Diagnose experiment sections that only describe metric changes without connecting back to the motivation.
- Fix by explaining why each component works and tying ablations back to the motivating hypothesis.

### 7. Linguistic De-noising

- Diagnose semicolon and dash overuse, awkward placement of therefore, and inflated words such as elegantly, crucial, and theoretically.
- Fix by removing emotional or promotional modifiers and using direct technical verbs.
