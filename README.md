# Literate Garden

A self-incubating marimo-based research system integrated with multi-agent collaboration framework.

## Philosophy

**Make it playable, not perfect. Bud when it deserves structure.**

This is an **experimental greenhouse** for rapid prototyping, not a production system:
- **No spec-driven development** for experiments in the garden
- Focus on **playable prototypes** that users can interact with
- **Budding mechanism**: Successful experiments graduate to dedicated repos with appropriate governance
- **Literate programming**: Marimo documents make experiments tangible and explorable

## Getting Started

1. Install dependencies (using `uv`):
   ```bash
   uv pip install marimo openai requests pydantic
   ```

2. Set OpenAI API key (optional, enables AI-assisted task generation):
   ```bash
   export OPENAI_API_KEY="your-key-here"
   ```

3. Launch the notebook:
   ```bash
   marimo run starter_seed.py --headless
   ```
   Visit the printed URL to explore the interactive document.

## Garden Metaphor

### 🌱 Seeds → Growth → Budding → Pruning

- **Seeds**: Initial ideas and experiments (marimo documents)
- **Growth**: Rapid iteration without heavy process overhead
- **Budding**: Successful experiments split off into new repos with stricter governance
- **Pruning**: Failed experiments documented and removed

### Experiment Workflow

1. **Start a seed**: Create a new marimo document in the garden
2. **Make it playable**: Focus on minimal interaction, not perfection
3. **Iterate fast**: No mandatory specs, tests, or reviews
4. **Decide fate**:
   - **Keep growing** → Continue iterating in garden
   - **Bud off** → Graduate to dedicated repo with appropriate rules
   - **Prune** → Document what didn't work and remove

## Budding Protocol

### When to Graduate an Experiment

Questions to ask:
1. **Is it playable?** Can users meaningfully interact with it?
2. **Is there momentum?** Will this continue being developed?
3. **Does it need structure?** Would specs/testing help it grow?
4. **Is the garden cramped?** Is this too complex for quick iteration?

If yes to most → Time to bud into a dedicated repo.

### Evolution Paths

Budded projects can adopt different governance:
- **Spec-driven**: GitHub spec-kit, formal requirements (AAFC Herbarium style)
- **Library**: Comprehensive testing, semantic versioning (Python Toolbox style)
- **Scientific**: Curator validation, constitutional governance
- **Experimental continue**: Keep iterating in garden if still exploring

## Multi-Agent Coordination

### Authority Domains
- **Human**: What's worth prototyping, playability threshold, when to bud
- **Code Agent**: Rapid implementation, make prototypes playable quickly
- **Chat Agent**: Pattern recognition, budding recommendations, suggest evolution paths

### Bridge System (Optional)
Use if coordinating across portfolio:
```bash
./.bridge/send-message.sh code chat NORMAL "Prototype ready for review" message.md
./.bridge/receive-messages.sh
```

See `CLAUDE.md` for full details.

## Active Experiments

### 🎮 Game Demo Gallery (NEW!)

**Four parallel visions unified** — Interactive showcase of award-ready indie game concepts:

```bash
marimo run game_demos_gallery.py
```

Explore 17 festival-targeted concepts across four collections:
- **🌸 Bloom** — Synesthetic mechanics, emotional resonance
- **⚙️ Clockwork** — Systems depth, emergent behavior
- **🏛️ Palimpsest** — Narrative layering, memory themes
- **🎨 Patterns** — Reusable interaction patterns

See [experiments/README.md](experiments/README.md) for details.

---

## Project Structure

```
Literate-Garden/
├── starter_seed.py           # Original agentic seed document
├── game_demos_gallery.py     # Interactive showcase (NEW!)
├── experiments/              # Four unified collections (NEW!)
│   ├── bloom/
│   ├── clockwork/
│   ├── palimpsest/
│   └── patterns/
├── CLAUDE.md                 # Agent coordination instructions
├── .bridge/                  # Meta-project integration
└── README.md                 # This file
```

## Integration with Portfolio

Related projects:
- **Meta-Project**: Coordination infrastructure and bridge system
- **AAFC Herbarium**: Scientific data extraction patterns
- **Python Toolbox**: Shared utility functions

All inherit coordination protocols from `~/devvyn-meta-project/`.

