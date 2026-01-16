# Literate Garden

Interactive marimo experiments. Run them, hack them, make new ones.

## The Cycle

```bash
marimo run garden_cycle.py
```

The orchestrator harvests findings and next_steps from all notebooks and displays them. Then ask Claude Code to propose new experiments based on what you see. No API keys required - Claude Code does the generation when you ask.

## Experiments

### Agent Strata
Proof that marimo's reactive graph naturally implements agent call stacking.

```bash
marimo run agent_strata.py
```

Four layers: Strategic → Tactical → Execution → Reflection. Changes propagate reactively through the stack.

### Game Demo Gallery
17 indie game concepts across four collections: Bloom, Clockwork, Palimpsest, Patterns.

```bash
marimo run game_demos_gallery.py
```

### Research Notebooks
Deep dives spawned from podcasts and curiosity:

```bash
marimo run kubernetes_operators_exploration.py   # K8s operator patterns
marimo run protracker_deep_dive.py               # MOD tracker music analysis
```

### Greene Graph
Network analysis of Robert Greene's intellectual influences.

```bash
python build_greene_graph.py
```

## Setup

```bash
uv pip install marimo openai requests pydantic networkx
```

## Making New Experiments

Just create a `.py` file with marimo cells. No templates, no process.

```python
import marimo
app = marimo.App()

@app.cell
def your_experiment():
    # do interesting things
    return result,
```

When something outgrows this playground and needs its own repo, move it.
