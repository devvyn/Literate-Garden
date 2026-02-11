"""parallel_visions_showcase.py

Marimo notebook presenting four parallel indie game demo explorations.
Each tab embeds a lightweight HTML prototype plus design/feasibility notes.
"""

import html
import pathlib

import marimo

__generated_with__ = "0.9.16"
app = marimo.App(width="wide")


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md(
        """
        # ✨ Parallel Visions

        Four simultaneous explorations demonstrating range across aesthetics and systems.
        Click through each tab to explore the embedded micro-prototype, concept recap,
        and collaboration breadcrumbs.
        """
    )
    return


@app.cell
def __(mo):
    base = pathlib.Path("experiments/parallel_visions")

    def embed_html(relative):
        content = (base / relative).read_text(encoding="utf-8")
        iframe = f"""
        <iframe
          title="{relative}"
          srcdoc='{html.escape(content, quote=True)}'
          style="width:100%;height:520px;border:1px solid rgba(0,0,0,0.08);border-radius:18px;"
        ></iframe>
        """
        return mo.Html(iframe)

    version_data = {
        "🌞 Solarpunk Harmonics": {
            "summary": "Synesthetic gardening sim with responsive light music canvas.",
            "suitability": "Web-ready canvas loop, accessibility-first color design, cozy vibes.",
            "path": "version_a_solarpunk/web/index.html",
        },
        "🕶️ Quantum Relay Heist": {
            "summary": "Dual-timeline tactics puzzle staging entangled operatives.",
            "suitability": "Deterministic grid logic, neon noir presentation, streamer replayability.",
            "path": "version_b_quantum_heist/web/index.html",
        },
        "🍄 Mycelial Memory Opera": {
            "summary": "Choral narrative weaving memory fragments via resonance nodes.",
            "suitability": "Node graph storytelling, choral sampling hooks, emotional showcase.",
            "path": "version_c_mycelial_opera/web/index.html",
        },
        "⚡ Cloudforged Ritual": {
            "summary": "Co-op ritual strategy with drag-and-drop weather pylons.",
            "suitability": "Tactile planning, co-op readiness, systemic forecast cues.",
            "path": "version_d_cloudforged_ritual/web/index.html",
        },
    }

    tabs = {}
    for label, data in version_data.items():
        tabs[label] = mo.vstack(
            [
                mo.md(
                    f"""
                    ## {label}

                    **Concept Pulse:** {data['summary']}

                    **Festival Fit:** {data['suitability']}

                    _Embedded prototype below. Inspect inline comments for handoff context._
                    """
                ),
                embed_html(data["path"]),
            ]
        )

    demo_tabs = mo.ui.tabs(tabs)
    return demo_tabs,


@app.cell
def __(demo_tabs):
    demo_tabs
    return


if __name__ == "__main__":
    app.run()
