# GitHub Token Saver Notes

Source: `C:\Users\YeJianbo\.skills-manager\external-references\token_saver`

The external project provides a Claude Code package for reducing token use. This local skill adapts the workflow ideas to Codex and the user's CS academic workflow.

## Useful Ideas Imported

- Token discipline: shortest useful answer, no repeated caveats, summarize tool output, stop when the goal is satisfied.
- Subagent economy: use subagents only when they reduce total context, improve model fit, or isolate noisy research.
- Compact task: compress broad prompts into goal, constraints, success criteria, first action.
- Entry finder: find starting files first; read at most a few files before reassessing.
- Minimal research: state hypothesis, minimal checks, and stop condition before broad research.
- Review compress: summarize long review/log/diff into severity-ordered findings.
- Handoff brief: preserve next-step state without carrying long logs.

## Not Imported Directly

- Claude lifecycle hooks: not portable to this Codex Desktop skill workflow.
- Broad shell denial rules: replaced by softer guidance because Codex already has repository-specific developer rules.
- Python entry-finder helper scripts: useful for Claude projects, but this local workflow already uses `rg`, skill routing, and Codex tools. Add scripts later only if repeated file-entry discovery becomes expensive.

## Local Adaptation

- Academic survey stores evidence in files instead of chat context.
- Venue selection keeps live official search but logs search trace compactly.
- AGY/Claude/DeepSeek calls receive narrow task packets.
- Review outputs use findings-first format consistent with the user's AGENTS.md.
