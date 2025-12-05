# AGENTS — Literate Garden (Root Scope)

Scope: Entire repository unless a deeper `AGENTS.md` overrides.

## Purpose
We are in a **4× parallel development branch** meant to produce merge-friendly, self-explaining artifacts for multiple agents working simultaneously. Keep instructions additive and avoid rewriting sibling agent notes—side-by-side guidance is encouraged.

## Breadcrumb Protocol (use on every file you touch)
- Add a short **Agent Breadcrumbs** block (markdown section or comment) noting lane, date, and intent.
- Prefer structured tags like `AGENT_TODO[lane]: ...` or `AGENT_NOTE[lane]: ...`; avoid deleting prior tags from other agents.
- When introducing new context, link to or create a context node under `agents/context/` instead of embedding long narratives inline.

## Parallel Lanes (pick one when you add breadcrumbs)
- **Lane A — Telemetry & Gallery**: instrumentation, marimo UI, feedback capture.
- **Lane B — Budding & Governance**: extraction playbooks, graduation checklists, repo handoff.
- **Lane C — Pattern SDK**: reusable mechanics, shared assets, templates.
- **Lane D — Narrative Layering**: timeline overlays, diegetic journaling, lore coherence.

## Merge Hygiene
- Avoid sweeping rewrites; append new sections to preserve provenance.
- Prefer new cells/sections over edits when touching marimo docs.
- If two instructions conflict, add an inline note describing the tension and keep both.

## Quick Pointers
- Instruction index lives in `README.md` under **Agent Mesh**.
- Context hierarchy starts at `agents/context/lanes.md`; add siblings for new lanes.
- Experiments folder has its own scoped instructions (`experiments/AGENTS.md`).

## Agent Breadcrumbs (Lane B — Budding & Governance)
- 2025-10-06: Established root scope instructions + breadcrumb protocol for 4× branch; refer agents to context nodes for depth.
