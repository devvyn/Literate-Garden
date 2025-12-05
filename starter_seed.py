"""starter_seed.py

A marimo "seed" for agentic, self-incubating projects with hooks for
Codex-style agents.

This document is both narrative and executable. Its purpose is to:
  1. Declare the project’s purpose and working style
  2. Establish a reproducible environment
  3. Encode the agentic loop of "observe → reflect → extend"
  4. Generate tasks and notes that become future iterations
"""

import marimo
from textwrap import dedent

__generated_with__ = "0.9.16"
app = marimo.App()


# CELL 1 — Introduction
@app.cell
def introduction():
    intro_text = dedent(
        """
    # 🌱 Agentic Project Seed

    Welcome! This is a self-incubating marimo document designed to be
    the genesis of a project. Think of it as a seed crystal dropped
    into solution: over time, structures will accrete, iterate, and 
    self-improve.
    
    ## Principles
    - Literate programming: code and commentary in one.
    - Agentic growth: the system proposes its own next steps.
    - Self-documenting: outputs are logged as part of the narrative.
    
    Begin by running this document. Each cycle produces:
    1. Reflections on the current state
    2. A prioritized task list
    3. Hooks for external agents (e.g. Codex) to act
    """
    )
    return intro_text


# CELL 2 — Environment declaration
@app.cell
def environment_declaration():
    env = {
        "language": "Python 3.11+",
        "package_manager": "uv / pip",
        "core_dependencies": ["marimo", "openai", "requests", "pydantic"],
        "openai_model": "gpt-4o-mini",
        "env_var": "OPENAI_API_KEY",
        "philosophy": "Local-first, agentic expansion, reproducible research",
    }
    return env


# CELL 3 — Agentic loop scaffold
@app.cell
def agentic_loop():
    import datetime
    import random

    def reflect_and_propose(notes: str):
        """Reflect on notes and propose next tasks."""
        timestamp = datetime.datetime.utcnow().isoformat()
        reflections = [
            f"🕒 Reflection at {timestamp}",
            f"Input notes: {notes}",
            "Proposal: Extend functionality iteratively.",
        ]
        tasks = [
            "✅ Refactor code for clarity",
            "📖 Add more documentation",
            f"⚙️ Explore feature #{random.randint(1,100)}",
        ]
        return reflections, tasks
    return reflect_and_propose

# CELL 4 — Codex task generator
@app.cell
def codex_task_generator():
    import os
    from typing import List

    def codex_propose(notes: str, model: str = "gpt-4o-mini") -> List[str]:
        """Use an OpenAI model to propose next tasks."""
        try:
            from openai import OpenAI, OpenAIError
        except Exception as e:  # pragma: no cover - graceful degradation
            return [f"OpenAI package not installed: {e}"]

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return ["Set OPENAI_API_KEY to enable Codex suggestions."]

        client = OpenAI(api_key=api_key)
        prompt = (
            "Given the project notes:\n"
            f"{notes}\nGenerate three follow-up coding tasks."
        )
        try:
            response = client.responses.create(model=model, input=prompt)
        except Exception as e:  # pragma: no cover - network failures
            return [f"OpenAI request failed: {e}"]

        text = response.output_text.strip()
        return [line.strip("-• ") for line in text.splitlines() if line.strip()]

    return codex_propose


# CELL 5 — First cycle
@app.cell
def first_cycle(agentic_loop):
    reflections, tasks = agentic_loop("Seed document freshly run.")
    return reflections, tasks


# CELL 6 — Codex-assisted suggestions
@app.cell
def codex_demo(codex_task_generator):
    suggestions = codex_task_generator("Seed document freshly run.")
    return suggestions


# CELL 7 — Display
@app.cell
def display(introduction, environment_declaration, first_cycle, codex_demo):
    from pprint import pprint

    print(introduction)
    print("\n---\nEnvironment:\n")
    pprint(environment_declaration)

    print("\n---\nCycle 1 reflections and tasks:\n")
    pprint(first_cycle[0])
    pprint(first_cycle[1])

    print("\n---\nCodex suggestions:\n")
    pprint(codex_demo)


# CELL 8 — Self-extension hook
@app.cell
def extension_protocol():
    protocol = dedent(
        """
    ## 🔄 Extension Protocol

    To extend this project:
    1. Read the reflections and tasks from the last cycle.
    2. Propose modifications or new cells.
    3. Commit changes back into this marimo document.

    Agents may add new cells with:
    ```python
    @app.cell
    def new_feature(...):
        ...
    ```

    Set `OPENAI_API_KEY` to enable Codex-powered task suggestions.
    Each cycle should preserve provenance: append, don’t overwrite.
    """
    )
    return protocol


# CELL 9 — Agent breadcrumbs for parallel lanes
@app.cell
def agent_breadcrumbs():
    breadcrumbs = dedent(
        """
    ## Agent Breadcrumbs (Lane D — Narrative Layering)
    - 2025-10-06: Leave space for layered timeline + diegetic journal prototype as a new cell appended below.

    ## Agent Breadcrumbs (Lane A — Telemetry & Gallery)
    - 2025-10-06: When wiring telemetry, prefer additive cells that stream signals without mutating earlier loops.
    """
    )
    return breadcrumbs

