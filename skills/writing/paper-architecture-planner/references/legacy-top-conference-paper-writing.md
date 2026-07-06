---
name: top-conference-paper-writing
description: 顶会论文写作与改写规范，面向密码学、联邦学习与隐私计算方向。Use when the user asks to draft, revise, polish, de-AI, restructure, or review academic paper sections for top-conference style, especially abstracts, introductions, related work, preliminaries, problem definitions, threat/privacy/security models, federated learning settings, privacy-preserving protocols, secure aggregation, differential privacy, MPC, homomorphic encryption, TEE-based systems, security proofs, utility/privacy/efficiency evaluations, contribution lists, or Chinese-to-English academic writing guidance.
---

# Top Conference Paper Writing

## Core Workflow

Use this skill to turn paper drafts or writing plans into direct, rigorous top-conference style prose for cryptography, federated learning, and privacy-preserving computing papers. First identify the section type, then apply the relevant checklist below. Keep the writing task-driven: every paragraph must advance one clear purpose.

When revising user text:

1. Preserve the paper's technical claim unless evidence is missing or logically unsupported.
2. Make the narrative follow background -> problem -> limitation -> key insight -> construction/protocol -> proof/evaluation -> contribution.
3. Remove defensive, response-letter-like wording unless the user explicitly asks for rebuttal text.
4. Avoid vague claims, repeated motivation, undefined symbols, underspecified adversaries, and premature technical detail.
5. Prefer concise paragraphs with clear topic sentences and explicit links between motivation, assumptions, construction/protocol, privacy/security guarantees, model utility, and efficiency.

## Abstract

Write the abstract as 5-7 compact sentences:

1. Open with one precise sentence that states the research area and its importance or application value.
2. State the unresolved problem or pain point in current mainstream methods.
3. Introduce the proposed construction, protocol, algorithm, defense, or system in one sentence and name its core advantage.
4. Use 2-3 sentences to summarize the key technical ingredients, FL/privacy-computing setting, threat model, and how the pieces lead to the stated guarantee.
5. Summarize proof results, privacy leakage reduction, model utility, communication/computation overhead, implementation results, or benchmark performance with concrete metrics when available.
6. Optionally close with the contribution or application prospect.

Do not overload the abstract with proof or implementation details. Each claimed guarantee, privacy benefit, utility improvement, assumption, or performance benefit should later correspond to a formal definition, theorem, proof sketch, attack/defense evaluation, or system benchmark.

## Introduction

Structure the introduction as a narrowing argument:

1. Start from field consensus in 1-2 sentences, not generic background.
2. Move from broad area to the concrete problem, making each paragraph narrower than the previous one.
3. Acknowledge prior work before naming its remaining limitation.
4. Group related approaches into 2-3 categories and state their shared limitations instead of listing papers one by one.
5. Include one clear sentence explaining what existing methods cannot do; do not make readers infer it.
6. Present the key insight before technical mechanics: explain why the proposed direction should work, then explain how it is instantiated.
7. Introduce the proposed solution and connect it directly to the stated limitation.
8. End with a concise contribution list and paper organization when appropriate.

For cryptography, federated learning, and privacy-computing papers, prefer a motivating example, protocol overview, attack scenario, FL workflow, privacy leakage path, or comparison table when it can make the problem and improvement immediately visible. Use a pipeline figure only when the work is system-, training-, or protocol-flow-oriented.

Citation discipline:

- Support major factual claims with citations.
- Keep 1-2 relevant citations per introduction paragraph when the claim depends on prior work.
- Do not move a full Related Work survey into the introduction; keep only work needed for motivation.

## Related Work

Organize related work by technical route or problem dimension, not by chronology.

For each category:

1. Start with the category's shared idea.
2. Mention representative works.
3. Explain the common limitation that motivates this paper.
4. State whether this paper inherits from, improves on, or differs from the category.

Cover recent work from relevant venues when available, such as CRYPTO, EUROCRYPT, ASIACRYPT, TCC, CCS, USENIX Security, IEEE S&P, NDSS, PETS, NeurIPS, ICML, ICLR, and top systems/privacy venues where appropriate. End the section, or each major group, with a sentence that clarifies the paper's core distinction from all discussed directions.

## Technical Core

Make the technical section readable before it becomes formal:

1. Begin with an overview that states the construction, protocol, proof strategy, or system architecture and its core intuition in one sentence.
2. Explain motivation and intuition before formulas and implementation details.
3. Use a clear overview figure or protocol flow when there are multiple parties, phases, algorithms, or message exchanges.
4. Ensure every party, algorithm, oracle, phase, or message in the figure has a matching explanation.
5. Add standalone preliminaries/problem-definition subsections with inputs, outputs, assumptions, adversarial capabilities, security goals, and correctness requirements.
6. Define symbols at first use, keep notation consistent, and provide a notation table if many symbols appear.
7. Number formulas and explain the meaning of each key formula in text.
8. For every component, state why it is designed this way; cite borrowed primitives, assumptions, reductions, protocols, or system components.
9. Order subsections by logical dependency: preliminaries -> model -> construction -> correctness -> security -> efficiency/implementation.
10. Use algorithms, games, or pseudocode for complex procedures when it improves reproducibility or proof clarity.
11. Tie each construction choice to a theorem, proof step, complexity analysis, benchmark, or ablation-style evaluation when relevant.

Avoid dumping formulas before the reader knows what problem the definition, game, or algorithm solves.

## Federated Learning and Privacy Computing Setup

For FL and privacy-computing papers, make the system setting explicit before presenting the method:

1. Define parties and roles: clients, server/coordinator, aggregator, auditor, adversary, data owner, model owner, or evaluator.
2. State the FL regime: cross-device or cross-silo, horizontal or vertical FL, synchronous or asynchronous training, client sampling, number of clients, local epochs, aggregation rule, and non-IID setting.
3. Specify data assumptions: feature/label ownership, label availability, class imbalance, data heterogeneity, and whether raw data, gradients, updates, logits, embeddings, or intermediate activations are exposed.
4. Define the privacy target: data reconstruction resistance, membership/privacy leakage reduction, label privacy, gradient privacy, update confidentiality, secure aggregation, client anonymity, or inference confidentiality.
5. State the privacy/security tool precisely: differential privacy, secure aggregation, MPC, homomorphic encryption, secret sharing, zero-knowledge proofs, TEE, trusted setup, or hybrid protocol.
6. Clarify what is protected from whom. Distinguish honest-but-curious, malicious, colluding, adaptive, and external adversaries.
7. Separate privacy guarantee from empirical attack resistance. Do not present attack accuracy reduction as a formal privacy proof.

## Security Model and Proofs

For cryptography, FL security, and privacy-computing papers, do not treat proofs as appendix-only decoration:

1. State the threat model explicitly: adversary type, corruption model, capabilities, adaptivity, leakage, and trust assumptions.
2. Define correctness, security, privacy, soundness, zero-knowledge, robustness, utility preservation, or other guarantees before claiming them.
3. State assumptions precisely, such as DDH, LWE, ROM, standard model, random oracle, CRS, PKI, TEE, or honest-majority assumptions.
4. Present theorem statements near the construction and explain their meaning in plain language.
5. Give a proof roadmap in the main text when the full proof is long.
6. Make reductions traceable: identify the simulator, hybrids/games, failure events, and advantage bound.
7. Avoid claiming stronger security or privacy than the model proves.
8. Keep notation identical across definitions, algorithms, theorems, and proofs.

## Evaluation

Use evaluation only when appropriate to the paper type. For theory-heavy cryptography, efficiency and asymptotic analysis may be primary. For FL privacy, applied crypto, privacy systems, or security protocols, include reproducible implementation results and utility/privacy/efficiency tradeoff analysis.

Check that the evaluation section contains the relevant items:

1. Baselines from recent and classical schemes that solve the same problem under comparable assumptions.
2. Utility comparison: accuracy, AUC, F1, loss, convergence rounds, fairness across clients, or task-specific metrics.
3. Privacy/security comparison: adversary model, attacks, assumptions, leakage, trust setup, collusion threshold, privacy budget, and supported threat scenarios.
4. Complexity comparison: computation, communication, storage, rounds, setup cost, proof size, verification time, latency, throughput, and asymptotic bounds.
5. Implementation details: language/library, cryptographic backend, ML framework, security parameter, DP budget, curve/field/modulus choices, hardware, network setting, number of runs, and variance.
6. End-to-end cost and per-component breakdown when the construction has multiple phases.
7. Sensitivity analysis for security parameter, privacy budget, party/client count, malicious/colluding client ratio, dataset size, non-IID degree, model size, circuit size, batch size, or network latency when relevant.
8. Ablation-style analysis for optional optimizations, batching, preprocessing, compression, or protocol shortcuts.
9. Comparison under matched security levels and matched assumptions.
10. Attack evaluation when relevant: gradient inversion, membership inference, property inference, label inference, poisoning/backdoor robustness, or collusion analysis.
11. Failure cases, limitations, deployment constraints, or open assumptions.

Make sure every claimed contribution has proof, complexity, or empirical evidence. Do not introduce optimizations that never appear in analysis or evaluation.

## Writing Style

Write directly and progressively:

- Avoid circuitous setup and defensive phrasing.
- Avoid overusing "not X but Y", "rather than", "since", "however", "therefore", and "not only ... but also".
- Do not add unnecessary explanation merely to avoid a banned pattern.
- Keep transitions natural: do not jump from a broad possibility to a concrete setting without a bridge.
- Keep each paragraph assigned to one task.
- Avoid repeated motivation across sections.
- Delay dense technical details until the reader understands the intuition.
- Limit defensive statements to at most one in the introduction and one in the conclusion when truly needed.
- Do not write the paper as if it were responding to reviewers.

When polishing, improve logic before style. If a claim lacks evidence, mark the gap instead of making the prose sound stronger.
