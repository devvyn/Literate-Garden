"""tracker_as_dsl.py

Exploring tracker effect commands as a domain-specific language.

MOD trackers encode music as compact row-based patterns with effect commands.
Can this "tracker notation" inspire DSLs for other creative domains?

Provenance: Inspired by garden_cycle harvest
Connects to: protracker_deep_dive, game_demos (Patterns collection)
"""

import marimo

__generated_with__ = "0.9.16"
app = marimo.App(width="medium")


@app.cell
def strategic_layer():
    """What are we trying to understand?"""
    questions = [
        "What makes tracker notation so effective for composition?",
        "Can we design a 'tracker-like' notation for game behaviors?",
        "How did tracker composers think in patterns vs linear composition?",
        "Do constraints (4 channels, limited effects) boost creativity?",
    ]

    hypothesis = """
    Tracker notation works because:
    1. Fixed grid (64 rows, 4 channels) creates rhythm naturally
    2. Effect commands are a micro-DSL (0xy = arpeggio, 4xy = vibrato)
    3. Patterns are reusable - compose by arranging, not rewriting
    4. Constraints force economy of expression

    This could apply to game mechanics, animation, dialogue, etc.
    """

    return questions, hypothesis


@app.cell
def execution_layer(questions):
    """Build a minimal tracker-like DSL interpreter."""
    from dataclasses import dataclass
    from typing import List, Dict, Callable, Any

    @dataclass
    class TrackerRow:
        """Single row in a pattern."""
        note: str | None      # e.g., "C-4", "D#5", None for continue
        instrument: int | None
        effect: str | None    # e.g., "0xy", "4xy", "Cxx"
        effect_param: int

    @dataclass
    class Pattern:
        """64-row pattern, single channel for simplicity."""
        rows: List[TrackerRow]

    class TrackerInterpreter:
        """Minimal interpreter for tracker-like patterns."""

        def __init__(self):
            self.effects: Dict[str, Callable] = {
                "0": self._arpeggio,    # 0xy: cycle note, note+x, note+y
                "4": self._vibrato,     # 4xy: oscillate pitch by y at speed x
                "C": self._volume,      # Cxx: set volume to xx
                "F": self._speed,       # Fxx: set tempo
            }
            self.state = {"note": None, "volume": 64, "tick": 0}

        def _arpeggio(self, x, y):
            return f"arpeggio: root, +{x}, +{y} semitones"

        def _vibrato(self, x, y):
            return f"vibrato: speed={x}, depth={y}"

        def _volume(self, x, y):
            vol = x * 16 + y
            self.state["volume"] = vol
            return f"volume → {vol}"

        def _speed(self, x, y):
            tempo = x * 16 + y
            return f"tempo → {tempo} ticks/row"

        def execute_row(self, row: TrackerRow) -> List[str]:
            """Execute a single row, return actions taken."""
            actions = []

            if row.note:
                self.state["note"] = row.note
                actions.append(f"play {row.note}")

            if row.effect:
                effect_type = row.effect[0].upper()
                x = (row.effect_param >> 4) & 0xF
                y = row.effect_param & 0xF

                if effect_type in self.effects:
                    result = self.effects[effect_type](x, y)
                    actions.append(result)

            return actions

    # Example: a tiny pattern
    pattern = Pattern(rows=[
        TrackerRow("C-4", 1, "C", 0x40),   # Play C-4, volume 64
        TrackerRow(None, None, "0", 0x37), # Arpeggio +3, +7 (major chord)
        TrackerRow(None, None, "0", 0x37),
        TrackerRow(None, None, "0", 0x37),
        TrackerRow("E-4", 1, "4", 0x42),   # Play E-4, vibrato
        TrackerRow(None, None, "4", 0x42),
        TrackerRow("G-4", 1, "C", 0x30),   # Play G-4, volume 48
        TrackerRow(None, None, "F", 0x06), # Tempo 6
    ])

    interpreter = TrackerInterpreter()
    execution_log = []
    for i, row in enumerate(pattern.rows):
        actions = interpreter.execute_row(row)
        if actions:
            execution_log.append(f"Row {i:02d}: {', '.join(actions)}")

    findings = [
        f"Executed {len(pattern.rows)} rows with {len(execution_log)} actions",
        "Effect commands are essentially function calls: 0xy → arpeggio(x, y)",
        "Pattern + interpreter = declarative music programming",
        "The grid constraint (rows/ticks) creates implicit rhythm",
    ]

    return Pattern, TrackerRow, TrackerInterpreter, pattern, execution_log, findings


@app.cell
def game_dsl_sketch(findings):
    """Sketch: what would a 'game tracker' look like?"""

    game_tracker_idea = """
    ## Game Tracker Notation (sketch)

    Instead of notes + effects, we have entities + behaviors:

    ```
    Row | Entity | Action  | Param
    ----|--------|---------|------
    00  | player | spawn   | x=10,y=5
    01  | player | move    | dx=1
    02  | player | move    | dx=1
    03  | enemy  | spawn   | x=20,y=5
    04  | enemy  | chase   | target=player
    05  | player | jump    | force=10
    06  | -      | wait    | frames=30
    07  | bullet | spawn   | from=player
    ```

    Pattern-based: define movement patterns, reuse them.
    Effect commands: behaviors like chase(speed), patrol(path), etc.
    Constraint: fixed tick rate forces rhythmic game feel.
    """

    game_dsl_questions = [
        "What's the 'note' equivalent for games? (spawn? state change?)",
        "What's the 'channel' equivalent? (entity type? layer?)",
        "Can rhythm constraints make games feel more musical?",
    ]

    return game_tracker_idea, game_dsl_questions


@app.cell
def reflection_layer(findings, game_dsl_questions):
    """What did we learn?"""

    insights = [
        "Tracker DSL power comes from: grid + effects + patterns + constraints",
        "Effect commands are a micro-language embedded in the grid",
        "Reusable patterns reduce cognitive load - compose by arranging",
        "The fixed tick/row rate creates emergent rhythm",
    ]

    next_steps = [
        "Build a playable 'game tracker' prototype",
        "Study how tracker composers structure patterns (verse/chorus/bridge)",
        "Try mapping game mechanics to effect command style (Axy, Bxy, etc.)",
        "Research other grid-based creative tools (pixel art, drum machines)",
    ]

    return insights, next_steps


@app.cell
def display(hypothesis, execution_log, game_tracker_idea, findings, insights, next_steps):
    """Display exploration results."""
    import marimo as mo

    log_md = "\n".join(f"- `{line}`" for line in execution_log)

    output = mo.md(f"""
# Tracker as DSL

## Hypothesis

{hypothesis}

## Execution Log

{log_md}

## Game Tracker Sketch

{game_tracker_idea}

## Findings

{chr(10).join(f"- {f}" for f in findings)}

## Insights

{chr(10).join(f"- {i}" for i in insights)}

## Next Steps

{chr(10).join(f"- {s}" for s in next_steps)}
""")

    return output,


if __name__ == "__main__":
    app.run()
