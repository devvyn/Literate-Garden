# Literate Garden

This project is a minimal marimo-based seed for agentic, self-incubating projects. Run the document to generate reflections and proposed tasks for the next iteration.

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

## Indie Demo Concept Showcase

The `docs/` and `web/` directories now outline award-ready demo concepts and the interaction patterns they emphasize.

- Read `docs/game_concepts.md` for suitability and feasibility breakdowns across the slate.
- Open `web/index.html` in a browser to explore the interactive pattern library.
- COLLAB NOTE: Keep cross-discipline updates flowing—drop renderer discoveries into `docs/rendering.md` and networking findings into `TODO-networking.md` so async contributors stay aligned.
