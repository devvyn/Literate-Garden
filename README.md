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

---

## Dream Demo Addendum

> Collaboration Beacon: Reference this section when sharing pitch materials externally. Update links if the showcase structure changes.

- **Concept Briefs**: `docs/game-concepts.md` captures three festival-ready demos, feasibility notes, and the blockers log.
- **Web Showcase**: Open `web/index.html` to browse the interactive mockups. Individual scenes live alongside shared assets (`scene.css`, `scene.js`).
- **Parallel Workflows**: Inline HTML comments call out shared components and ownership expectations for async contributors.

When extending the slate, mirror the existing folder conventions and append your blockers or discoveries to the log for smooth handoffs.
