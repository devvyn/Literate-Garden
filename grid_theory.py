"""grid_theory.py

Pushing deeper into grids: what makes a grid generative?

Observations so far:
- Trackers: 64 rows × 4 channels, effects per cell
- Marimo: cells in dependency graph
- Spreadsheets: infinite grid, formulas per cell
- Pixel art: fixed canvas, colors per cell

These are all "grids" but feel very different. Why?
What's the theory of generative grids?

Provenance: Deepening tracker_as_dsl
Connects to: tracker_as_dsl, protracker_deep_dive, game_demos_gallery
"""

import marimo

__generated_with__ = "0.9.16"
app = marimo.App(width="medium")


@app.cell
def strategic_layer():
    """The deeper questions about grids."""

    questions = [
        "What are the dimensions of a grid? (not just rows/cols)",
        "What goes in a cell? (value, formula, effect, behavior?)",
        "How do cells relate? (neighbors, dependencies, sequences?)",
        "What makes constraints generative vs restrictive?",
        "Can we design a 'grid algebra' like convergence algebra?",
    ]

    hypothesis = """
    A generative grid has:

    1. CELLS with semantic content (not just values)
    2. RELATIONSHIPS between cells (not just position)
    3. CONSTRAINTS that force creativity (not paralyze)
    4. PATTERNS that can be named and reused
    5. TIME or SEQUENCE (implicit or explicit flow)

    The magic happens when constraints + relationships + patterns
    create emergent behavior the designer didn't explicitly encode.
    """

    return questions, hypothesis


@app.cell
def execution_layer():
    """Build a grid taxonomy and theory."""
    from dataclasses import dataclass
    from typing import List, Dict, Any, Optional, Callable
    from enum import Enum

    class CellSemantics(Enum):
        """What does a cell contain?"""
        VALUE = "value"           # Just data (spreadsheet number)
        FORMULA = "formula"       # Computation (spreadsheet formula)
        EFFECT = "effect"         # Transformation (tracker effect)
        BEHAVIOR = "behavior"     # Action/rule (game entity)
        PIXEL = "pixel"           # Visual atom (pixel art)
        NOTE = "note"             # Temporal event (music)

    class RelationType(Enum):
        """How do cells relate?"""
        POSITIONAL = "positional"     # Grid neighbors (pixel art)
        SEQUENTIAL = "sequential"     # Time order (tracker rows)
        DEPENDENCY = "dependency"     # DAG edges (marimo, spreadsheet)
        CHANNEL = "channel"           # Parallel streams (tracker channels)
        LAYER = "layer"               # Z-stacking (photoshop, game)

    class ConstraintType(Enum):
        """What limits the grid?"""
        DIMENSION = "dimension"       # Fixed size (64 rows)
        PALETTE = "palette"           # Limited options (4 channels, 16 colors)
        CAPACITY = "capacity"         # Resource limit (128KB demo)
        GRAMMAR = "grammar"           # Valid combinations (effect syntax)
        PHYSICS = "physics"           # Rules of interaction (game mechanics)

    @dataclass
    class GridType:
        """A taxonomy entry for a grid-based tool."""
        name: str
        cell_semantics: List[CellSemantics]
        relations: List[RelationType]
        constraints: List[ConstraintType]
        time_model: str  # "implicit", "explicit", "none"
        pattern_reuse: str  # "copy", "reference", "none"
        emergence_type: str  # what emerges from the grid

    # Catalog known grid types
    grid_taxonomy = [
        GridType(
            name="ProTracker",
            cell_semantics=[CellSemantics.NOTE, CellSemantics.EFFECT],
            relations=[RelationType.SEQUENTIAL, RelationType.CHANNEL],
            constraints=[ConstraintType.DIMENSION, ConstraintType.PALETTE, ConstraintType.CAPACITY],
            time_model="explicit",
            pattern_reuse="reference",
            emergence_type="music from rows + effects"
        ),
        GridType(
            name="Spreadsheet",
            cell_semantics=[CellSemantics.VALUE, CellSemantics.FORMULA],
            relations=[RelationType.POSITIONAL, RelationType.DEPENDENCY],
            constraints=[ConstraintType.GRAMMAR],
            time_model="none",
            pattern_reuse="copy",
            emergence_type="computation from formulas"
        ),
        GridType(
            name="Marimo",
            cell_semantics=[CellSemantics.BEHAVIOR, CellSemantics.VALUE],
            relations=[RelationType.DEPENDENCY],
            constraints=[ConstraintType.GRAMMAR],
            time_model="implicit",
            pattern_reuse="none",
            emergence_type="reactive flow from dependencies"
        ),
        GridType(
            name="Pixel Art Editor",
            cell_semantics=[CellSemantics.PIXEL],
            relations=[RelationType.POSITIONAL, RelationType.LAYER],
            constraints=[ConstraintType.DIMENSION, ConstraintType.PALETTE],
            time_model="none",
            pattern_reuse="copy",
            emergence_type="image from color adjacency"
        ),
        GridType(
            name="Game of Life",
            cell_semantics=[CellSemantics.VALUE],
            relations=[RelationType.POSITIONAL],
            constraints=[ConstraintType.PHYSICS],
            time_model="explicit",
            pattern_reuse="reference",
            emergence_type="lifeforms from neighbor rules"
        ),
        GridType(
            name="Drum Machine",
            cell_semantics=[CellSemantics.NOTE],
            relations=[RelationType.SEQUENTIAL, RelationType.CHANNEL],
            constraints=[ConstraintType.DIMENSION, ConstraintType.PALETTE],
            time_model="explicit",
            pattern_reuse="reference",
            emergence_type="rhythm from hits + silence"
        ),
    ]

    # Analyze what makes grids generative
    def generativity_score(grid: GridType) -> Dict[str, int]:
        """Heuristic: what correlates with generative grids?"""
        score = {}
        score["constraint_pressure"] = len(grid.constraints)
        score["relation_richness"] = len(grid.relations)
        score["semantic_depth"] = len(grid.cell_semantics)
        score["has_time"] = 1 if grid.time_model != "none" else 0
        score["pattern_power"] = 2 if grid.pattern_reuse == "reference" else (1 if grid.pattern_reuse == "copy" else 0)
        score["total"] = sum(score.values())
        return score

    scores = [(g.name, generativity_score(g)) for g in grid_taxonomy]
    scores.sort(key=lambda x: -x[1]["total"])

    findings = [
        f"Analyzed {len(grid_taxonomy)} grid types",
        f"Most generative: {scores[0][0]} (score: {scores[0][1]['total']})",
        f"Pattern reuse via 'reference' (not copy) appears in top grids",
        "Explicit time + constraints + patterns = high generativity",
        "Spreadsheets score lower: weak time model, copy-only patterns",
    ]

    return GridType, CellSemantics, RelationType, ConstraintType, grid_taxonomy, scores, findings


@app.cell
def design_new_grid(grid_taxonomy):
    """Design a new grid type based on theory."""

    proposed_grid = """
    ## Proposed: Behavior Tracker

    Apply tracker theory to game/simulation behaviors.

    | Property | Choice | Rationale |
    |----------|--------|-----------|
    | Cell semantics | BEHAVIOR + EFFECT | Actions, not just notes |
    | Relations | SEQUENTIAL + CHANNEL + DEPENDENCY | Time + parallelism + triggers |
    | Constraints | DIMENSION (64 ticks) + PALETTE (verb vocabulary) | Force economy |
    | Time model | Explicit | Tick-based like tracker |
    | Pattern reuse | Reference | Name patterns, compose |
    | Emergence | Interactive systems from simple rules |

    ### Example Notation

    ```
    Tick | Entity:Player | Entity:Enemy | Entity:World
    -----|---------------|--------------|-------------
    00   | spawn(10,5)   | -            | -
    01   | move(→)       | -            | -
    02   | move(→)       | spawn(20,5)  | -
    03   | -             | chase(Player)| -
    04   | jump(5)       | chase(Player)| gravity(0.5)
    05   | -             | -            | spawn_coin(15,3)
    ...  | ...           | ...          | ...
    ```

    ### What Emerges

    - **Rhythm**: actions at fixed ticks create game feel
    - **Patterns**: reusable behavior sequences (patrol, attack, idle)
    - **Constraints**: limited verbs force creativity
    - **Composition**: patterns combine like tracker patterns
    """

    return proposed_grid,


@app.cell
def reflection_layer(findings, scores):
    """What did we learn about grids?"""

    insights = [
        "Generativity = constraints + patterns + time + rich relations",
        "Trackers score highest because they maximize all factors",
        "Spreadsheets lack time and pattern references → less generative feel",
        "'Reference' patterns (not copy) enable composition, key insight",
        "Cell semantics matter: BEHAVIOR/EFFECT > VALUE",
    ]

    next_steps = [
        "Build minimal Behavior Tracker prototype",
        "Test: can 64 ticks + 4 entity channels make a playable game?",
        "Study drum machine UX for pattern composition",
        "Compare: Pico-8 (code) vs Behavior Tracker (grid) for same game",
        "Extract grid theory into reusable framework",
    ]

    return insights, next_steps


@app.cell
def display(hypothesis, proposed_grid, findings, scores, insights, next_steps):
    """Render exploration."""
    import marimo as mo

    scores_md = "\n".join(f"- **{name}**: {s['total']} (time:{s['has_time']}, patterns:{s['pattern_power']}, constraints:{s['constraint_pressure']})"
                         for name, s in scores[:4])

    output = mo.md(f"""
# Grid Theory

## Hypothesis

{hypothesis}

## Generativity Scores

{scores_md}

## Findings

{chr(10).join(f"- {f}" for f in findings)}

{proposed_grid}

## Insights

{chr(10).join(f"- {i}" for i in insights)}

## Next Steps

{chr(10).join(f"- {s}" for s in next_steps)}
""")

    return output,


if __name__ == "__main__":
    app.run()
