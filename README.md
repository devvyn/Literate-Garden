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

## Indie Game Vision Track
- Explore concept dossiers in [`docs/game_demos.md`](docs/game_demos.md) for pitch-ready demo outlines with suitability and feasibility notes.
- Review interactive web artefacts under [`web/`](web/) to sample presentation patterns for "Lighthouse Palimpsest", "MetroMycelium", and "Echoes of Laurel Vault". Each file contains collaboration hooks for follow-up agents.
- <!-- COLLAB NOTE: If additional artefacts are created, append a bullet describing the new experience and link to the file. -->

## Collaboration Breadcrumbs
- Pending task: flesh out production schedules and potential funding partners (see pause log in `docs/game_demos.md`).
- Open question: integrate these artefacts into a marimo notebook cell gallery for live demos.
