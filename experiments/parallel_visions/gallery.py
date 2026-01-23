"""parallel_visions/gallery.py

Marimo notebook wiring four parallel demo concepts for quick exploration.
"""

import marimo
from pathlib import Path

__generated_with__ = "0.9.16"
app = marimo.App(width="full")

ROOT = Path(__file__).parent


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md(
        """
        # 🌌 Parallel Visions — Indie Demo Quartet

        _Structured for festival juries, collaborators, and curious agents._

        Navigate each tab to read the concept capsule, inspect feasibility, and interact with the lightweight web artefact.

        ---
        """
    )
    return


@app.cell
def __(mo):
    tabs = mo.ui.tabs(
        {
            "I — Aurora Suture": mo.md("Loading…"),
            "II — Coral Wake": mo.md("Loading…"),
            "III — Monument Echo": mo.md("Loading…"),
            "IV — Solstice Run": mo.md("Loading…"),
            "🧭 Overview": mo.md("Loading overview…"),
        }
    )
    return tabs,


@app.cell
def __(mo, tabs):
    def concept_card(path: Path, *, iframe_height: int = 520):
        concept_md = path.joinpath("concept.md").read_text(encoding="utf-8")
        html = path.joinpath("web", "index.html").read_text(encoding="utf-8")
        return mo.vstack(
            [
                mo.md(concept_md),
                mo.html(html, height=iframe_height),
            ],
            gap="2.5rem",
        )

    tabs.items = {
        "I — Aurora Suture": concept_card(ROOT / "aurora_suture"),
        "II — Coral Wake": concept_card(ROOT / "coral_wake", iframe_height=560),
        "III — Monument Echo": concept_card(ROOT / "monument_echo", iframe_height=560),
        "IV — Solstice Run": concept_card(ROOT / "solstice_run", iframe_height=560),
        "🧭 Overview": mo.vstack(
            [
                mo.md(
                    """
                    ## Overview & Alignment Notes

                    - **Technical Spread:** Canvas painting, SVG strategy map, CSS 3D timeline, and rhythm runner.
                    - **Festival Pitch Angles:** Meditation & audio-reactivity, eco-systems storytelling, narrative archaeology, kinetic rhythm spectacle.
                    - **Next Hooks:**
                      - Integrate live FFT + consent flow (Aurora Suture).
                      - Persist archipelago state server-side (Coral Wake).
                      - Branching narrative schema handshake (Monument Echo).
                      - Ghost playback telemetry exporter (Solstice Run).

                    <!-- dead-end: Analytics dashboard deferred pending telemetry schema finalization. -->
                    """
                ),
            ],
            gap="1.5rem",
        ),
    }
    return concept_card,


@app.cell
def __(mo, tabs):
    tabs
    return


if __name__ == "__main__":
    app.run()
