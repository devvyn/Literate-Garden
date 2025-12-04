# Claude Agent Instructions - Literate Garden

**Context Level**: 3 (Sub-Project)
**Inherits From**:
- `~/.claude/CLAUDE.md` (User preferences: uv, fd, macOS tooling)
- `~/devvyn-meta-project/CLAUDE.md` (Bridge v3.0, Multi-Agent Framework v2.1)

**Project Type**: Agentic self-incubating research system
**Framework**: Literate programming + Multi-agent collaboration
**Last Updated**: 2025-09-29

## Project Context

### Purpose: Experimental Playground for Rapid Prototyping
Literate Garden is a **prototyping greenhouse** where ideas grow quickly with minimal process overhead:

- **Not spec-driven**: Quick experiments don't need formal specifications
- **Playable prototypes**: Focus on making ideas tangible and interactive
- **Budding mechanism**: Successful experiments graduate to dedicated repos with appropriate governance
- **Literate programming**: Code and narrative in executable marimo documents for rapid iteration

### The Garden Metaphor
- **Seeds**: Initial ideas and experiments
- **Growth**: Rapid iteration without heavy process
- **Pruning**: Failed experiments are documented and removed
- **Budding**: Successful prototypes split off into new repositories with stricter rules

### Human Context: Devvyn Murphy
- **Philosophy**: Make things playable, then decide if they deserve more structure
- **Work Style**: Values directness, resists premature process overhead
- **Domain**: Scientific data extraction, research automation, experimental tooling

## Authority Domains (Multi-Agent Framework v2.1)

### Human Domain
- **What's worth prototyping**: Idea selection and priority
- **What's playable enough**: Quality threshold for "usable prototype"
- **When to bud**: Decision to graduate experiment to dedicated repo
- **Domain expertise**: Scientific validity when relevant

### Code Agent Domain
- **Rapid implementation**: Make prototypes playable quickly
- **Minimal viable functionality**: Get to interactive state fast
- **Technical feasibility**: "Can this work?" assessments
- **Budding mechanics**: Help extract successful experiments to new repos

### Chat Agent Domain
- **Pattern recognition**: "This experiment resembles X project"
- **Budding recommendations**: When prototypes deserve their own repos
- **Cross-pollination**: Connect experiments to portfolio patterns
- **Evolution paths**: Suggest appropriate governance for budded projects

## Integration with Meta-Project

### Bridge System v3.0
This project is coordinated through the meta-project bridge system:

```bash
# Send coordination requests from this project
cd ~/devvyn-meta-project
./scripts/bridge-send.sh code chat HIGH "Literate Garden Update" message.md

# Check for messages about this project
./scripts/bridge-receive.sh code
```

### Inherited Protocols
- **Atomic operations**: Use provided scripts for all bridge communication
- **Quality standards**: TLA+ formal verification, comprehensive testing
- **Tool preferences**: uv for Python, fd for file search
- **Coordination patterns**: Clear authority domains, systematic handoffs

## Project Structure

### Core Files
- `starter_seed.py` - Executable marimo document (the "seed crystal")
- `README.md` - User-facing documentation
- `CLAUDE.md` - This file (agent coordination instructions)

### Environment
- **Language**: Python 3.11+
- **Package Manager**: `uv` (inherited preference)
- **Core Dependencies**: marimo, openai, requests, pydantic
- **AI Model**: gpt-4o-mini for task generation
- **Philosophy**: Local-first, agentic expansion, reproducible research

## Agentic Loop Architecture

### Observe → Reflect → Extend
The project implements a self-incubation cycle:

1. **Observe**: Read current state of starter_seed.py
2. **Reflect**: Generate reflections via `reflect_and_propose()` and `codex_propose()`
3. **Extend**: Add new marimo cells preserving provenance

### Extension Protocol
When extending this project:

```python
@app.cell
def new_feature(...):
    """
    Provenance: Added by Claude Code on 2025-09-29
    Purpose: [describe the enhancement]
    """
    # Implementation
    return outputs
```

**IMPORTANT**:
- Append new cells, don't overwrite existing narrative
- Preserve provenance in docstrings
- Maintain self-documenting style

## Common Tasks

### Running the Seed
```bash
# Install dependencies using uv
uv pip install marimo openai requests pydantic

# Run in headless mode
marimo run starter_seed.py --headless

# Edit interactively
marimo edit starter_seed.py
```

### Extending Functionality
1. Read current cycle output from last run
2. Identify gaps or enhancement opportunities
3. Add new marimo cells following extension protocol
4. Test with `marimo run` to validate
5. Commit changes preserving narrative flow

### Coordinating with Other Agents
```bash
# Example: Request research methodology review from Chat agent
cd ~/devvyn-meta-project
./scripts/bridge-send.sh code chat NORMAL \
  "Literate Garden: Review reflection algorithm" \
  reflection_analysis.md
```

### Integration with Portfolio
This project relates to:
- **AAFC Herbarium**: Scientific data extraction patterns
- **Python Toolbox**: Shared utility functions
- **Meta-Project**: Coordination infrastructure

## Quality Standards

### Prototype Quality (Intentionally Relaxed)
- **Playability over polish**: Can someone interact with this?
- **Literate enough**: Narrative explains what's being tried
- **Provenance when useful**: Track why experiments were tried
- **No mandatory testing**: Unless it helps rapid iteration

### Documentation Quality (Minimal)
- **Self-documenting experiments**: Marimo narrative shows intent
- **Track failed experiments**: Brief note on what didn't work and why
- **README lists active experiments**: Quick overview of what's growing
- **CLAUDE.md tracks budding**: Document when experiments graduate

### Budding Quality (Strict When Graduating)
When an experiment is ready to become a real project:
- Document what was learned in the garden
- Define appropriate governance for the new repo
- Clean up prototype code if needed
- Preserve garden provenance in new repo's history

## Warning Signs

**Escalate to Chat agent if:**
- Agentic loops produce circular or unhelpful tasks
- Integration with other projects creates conflicts
- Research methodology needs strategic reevaluation
- Framework patterns should be generalized to portfolio

**Escalate to Human if:**
- Scientific validity of research approach is unclear
- Domain expertise needed for task proposals
- Quality standards for research outputs need definition
- Strategic priority conflicts arise

## Tool Preferences (Inherited)

### Python Package Management
```bash
# Always use uv (inherited preference)
uv pip install <package>
uv pip list
uv pip freeze > requirements.txt
```

### File Operations
```bash
# Use fd for file search (aliased as find)
fd "*.py" .
fd --hidden "CLAUDE.md"

# Use rg for text search
rg "def codex_propose" starter_seed.py
```

### Bridge Operations
```bash
# Always use atomic scripts from meta-project
cd ~/devvyn-meta-project
./scripts/bridge-send.sh <from> <to> <priority> <title> <file>
./scripts/bridge-receive.sh <agent>
```

### Resource Provisioning
```bash
# Request software/datasets for experiments (via meta-project)
cd ~/devvyn-meta-project
./scripts/resource-request.sh \
  --source "magnet:?xt=..." \
  --purpose "PICO-8 for barkour prototyping"

# Resources downloaded to: ~/infrastructure/shared-resources/
# Pattern doc: knowledge-base/patterns/collective-resource-provisioning.md
```

**Example**: Barkour experiments needed PICO-8 fantasy console. Requested via torrent, now available to all projects in `shared-resources/`.

## Session Startup Checklist

**Every time you work on Literate Garden:**

1. ✅ **Context Inheritance**: Aware of meta-project protocols
2. ✅ **Bridge Sync**: Check for coordination messages
   ```bash
   cd ~/devvyn-meta-project && ./scripts/bridge-receive.sh code
   ```
3. ✅ **Authority Domains**: Know your domain vs human/chat domains
4. ✅ **Provenance**: Track all changes with timestamps and attribution
5. ✅ **Marimo State**: Run `marimo run starter_seed.py --headless` to verify

## Budding Protocol

### When to Bud (Graduate an Experiment)
Ask these questions:
1. **Is it playable?** Can users actually interact with it meaningfully?
2. **Is there momentum?** Will this continue being developed?
3. **Does it need structure?** Would formal specs/testing help it grow?
4. **Is the garden cramped?** Is this experiment too complex for quick iteration?

### How to Bud
```bash
# 1. Create new repo with appropriate governance
cd ~/Documents/GitHub/
mkdir new-project-name
cd new-project-name
git init

# 2. Extract prototype from garden
cp ~/Documents/GitHub/Literate-Garden/experiments/prototype.py ./

# 3. Create appropriate CLAUDE.md for new project
# (May include spec-driven development, testing requirements, etc.)

# 4. Document the budding in garden
cd ~/Documents/GitHub/Literate-Garden
# Add note about what budded and why
```

### Evolution Paths After Budding
- **Spec-driven project**: Apply GitHub spec-kit, formal requirements
- **Scientific project**: Add curator validation, constitutional governance
- **Library project**: Add comprehensive testing, semantic versioning
- **Experimental continue**: Keep iterating in garden if still exploring

---

**Project Status**: Active experimental greenhouse. NOT production-ready; NOT spec-driven. Optimized for rapid prototyping and playability discovery.

**Garden Rules**: Make it playable, not perfect. Bud when it deserves structure. Prune what doesn't work.