# Literate Garden

This project is a minimal marimo-based seed for agentic, self-incubating projects. Run the document to generate reflections and
proposed tasks for the next iteration.

## Getting Started

1. Install dependencies:
   ```bash
   pip install marimo
   ```
2. Launch the notebook:
   ```bash
   marimo run starter_seed.py --headless
   ```
   Visit the printed URL in your browser to explore the document.

## Workflow

Each cycle of the notebook produces:
- Reflections on the current state.
- A prioritized list of next tasks (e.g., refactoring or documentation).

Extend the project by appending new cells and preserving the narrative in `starter_seed.py`.

---

## Award-Oriented Game Demo Vault

Three interactive slices live under [`web_demos/`](web_demos):

- **Aurora Chord Pilgrimage** — sketch musical constellations and trigger chord pulses.
- **Clockwork Canopy Atelier** — tune solar angle and gear cadence to balance a mechanical forest.
- **Tidebound Cartographer** — manipulate tides to reveal glyphs and log shoreline scans.

Each demo is self-contained HTML (open directly in a browser). Shared styling and utilities live in [`web_demos/styles/common.css`](web_demos/styles/common.css) and [`web_demos/scripts/common.js`](web_demos/scripts/common.js).

Refer to [`docs/game_concepts.md`](docs/game_concepts.md) for feasibility notes, open questions, and collaboration breadcrumbs.
