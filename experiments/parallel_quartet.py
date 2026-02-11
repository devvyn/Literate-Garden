"""parallel_quartet.py

Four-way concept sheet + interactive snippets captured in a marimo notebook.

Each tab mirrors a distinct creative branch (ambient, tactical, narrative,
systemic) with embedded HTML prototypes authored alongside feasibility notes.
"""

import marimo

__generated_with__ = "0.9.16"
app = marimo.App(width="full")


@app.cell
def __():
    import marimo as mo
    from pathlib import Path
    from base64 import b64encode
    return Path, b64encode, mo


@app.cell
def __(Path, b64encode, mo):
    base = Path("experiments/parallel_quartet/web")

    def load_html(version: str) -> mo.Markdown:
        """Load the inline HTML prototype for a given version."""
        html_path = base / version / "index.html"
        # Collaboration Note: Keep html artifacts small so they embed cleanly here.
        content = html_path.read_text()
        encoded = b64encode(content.encode("utf-8")).decode("ascii")
        iframe = f"<iframe title='{version} prototype' src='data:text/html;base64,{encoded}' " \
                  "style=\"width:100%;height:520px;border:none;border-radius:18px;box-shadow:0 16px 40px rgba(0,0,0,0.35);\"></iframe>"
        return mo.md(iframe)

    versions = {
        "Version A": {
            "title": "Aurora Loom — Ambient Bloomcraft",
            "logline": "Conduct auroral threads in a synesthetic canopy studio.",
            "loop": [
                "Drift across the canopy, sketching ribbons that bloom into bioluminescent particles",
                "Modulate palette mood via scroll to reframe emotional tone mid-session",
                "Reset / capture compositions for festival showcases or streaming overlays",
            ],
            "feasibility": [
                "WebGL-free canvas particles perform smoothly on kiosk hardware",
                "Adds audio-reactive shader layer in UE/Unity for full build",
                "Small 2-person pod can deliver vertical slice in 4 weeks",
            ],
            "audience": "Lounge/festival chill zones, synesthetic art-stream communities.",
            "html": load_html("version_a"),
        },
        "Version B": {
            "title": "Rift Relay — Tactical Harmonics",
            "logline": "Tune relay nodes to shepherd energy across a fractured frontline.",
            "loop": [
                "Toggle modular nodes to create a viable path",
                "Propagate waveform to test coverage and discover unexpected synergies",
                "Iterate builds quickly, priming the concept for deckbuilder expansion",
            ],
            "feasibility": [
                "Pure DOM/JS logic demonstrates clarity of core puzzle loop",
                "Hybrid board-builder could live in Godot with netcode for co-op",
                "Systems designer + UI dev can ship demo sprint in ~5 weeks",
            ],
            "audience": "Tactics fans, roguelike deckbuilder players, puzzle showcase juries.",
            "html": load_html("version_b"),
        },
        "Version C": {
            "title": "Glass Archives — Echo Weaving",
            "logline": "Slide through eras of a lighthouse to align overlapping vows.",
            "loop": [
                "Scrub timeline slider to reveal layered narrative beats",
                "Annotate pivotal echoes for later curation",
                "Queue exhibition markers to export into festival decks",
            ],
            "feasibility": [
                "Slider-based narrative works as install booth or web anthology",
                "Next sprint wires export + VO layering via web audio",
                "Solo narrative designer can extend scenes over a two-week cycle",
            ],
            "audience": "Narrative-first players, museum installations, alt-control festivals.",
            "html": load_html("version_c"),
        },
        "Version D": {
            "title": "Verdant Circuit — Eco Resonance",
            "logline": "Balance a singing biosphere by seeding spores into a living reactor.",
            "loop": [
                "Drop seeds, watch diffusion field respond in real time",
                "Pulse evolution cycle to maintain equilibrium",
                "Stream emergent patterns, highlight systemic tension arcs",
            ],
            "feasibility": [
                "Lightweight canvas sim scales to desktop + tablet web",
                "Full game would migrate to GPU compute (Unity ECS / Bevy) for richness",
                "One engineer + one artist deliver milestone demo in 6 weeks",
            ],
            "audience": "Cozy sim streamers, strategy curious players, eco-education showcases.",
            "html": load_html("version_d"),
        },
    }

    def describe(version: dict) -> mo.ui.accordion:
        """Render a description block with loop + feasibility."""
        return mo.ui.accordion({
            "Concept": mo.md(
                f"""
                ### {version['title']}
                _{version['logline']}_

                **Core Loop Highlights**
                - """ + "\n                - ".join(version["loop"]) + "\n\n"
                """
            ),
            "Suitability & Feasibility": mo.md(
                """
                **Technical & Production Outlook**
                - """ + "\n                - ".join(version["feasibility"]) + "\n\n"
                f"**Audience Appeal:** {version['audience']}" + "\n\n"
                """
            ),
            "Interactive Slice": version["html"],
        }, multiple=False, expanded_indices=[0])

    return describe, mo, versions


@app.cell
def __(describe, mo, versions):
    hero = mo.md(
        """
        # 🌌 Parallel Dream Demos

        Four simultaneous prototypes charting distinct festival-ready directions. Each
        tab pairs a playable slice with my feasibility read so collaborators can pick up
        the branch that resonates.
        """
    )

    tabs = {
        key: mo.vstack([
            describe(versions[key])
        ])
        for key in versions
    }

    gallery = mo.ui.tabs(tabs)
    mo.vstack([hero, gallery])
    return


@app.cell
def __(mo):
    mo.md(
        """
        ---
        _Status:_ No blockers encountered. Audio hooks and export plumbing flagged for
        follow-up agents in respective HTML comments.
        """
    )
    return
