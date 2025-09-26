# Dream Demos from the Literate Garden

> **Collaboration Signal:** This file captures the broad ideation state. If you add or revise concepts, please append your initials in parentheses next to the touched section header.

## Overview

The following concepts are crafted as award-aimed interactive experiences that balance artistic vision with production feasibility. Each entry contains:

- **Premise:** The atmospheric hook.
- **Core Systems:** Play patterns or mechanics that earn critical attention.
- **Suitability Notes:** Why the idea aligns with indie showcases (artistic or narrative strengths).
- **Feasibility Snapshot:** Technical and production considerations, highlighting available prototypes and any blockers.
- **Prototype Link:** For concepts selected for web exploration.

## Concept Roster

### Aurora Chord Pilgrimage (ACP)
- **Premise:** A synth-driven pilgrimage across frozen skylines where constellations respond to musical harmony.
- **Core Systems:**
  - Freeform constellation drawing that maps to chord progressions.
  - Traveling set pieces where harmony modulates weather and traversal difficulty.
  - Score based on emotional resonance rather than accuracy (dynamic NPC feedback).
- **Suitability Notes:**
  - Unique fusion of music theory and narrative pilgrimage invites festival juries.
  - Visual spectacle (auroras + starlines) photographs well for marketing.
- **Feasibility Snapshot:**
  - Web demo establishes our shader-free gradient and harmony feedback loop.
  - Full game would require bespoke audio middleware; vertical slice achievable with existing Web Audio pipelines.
- **Prototype Link:** [`web_demos/aurora_chord.html`](../web_demos/aurora_chord.html).

### Clockwork Canopy Atelier (CCA)
- **Premise:** An arboreal city whose clockwork flora must be tuned daily to keep the canopy alive.
- **Core Systems:**
  - Layered time-of-day puzzles where rotating branches reroute sunlight.
  - NPC artisans requesting custom gear-based flora adjustments.
  - Persistent ecology that responds to over/under tuning.
- **Suitability Notes:**
  - Steampunk-botanical art direction stands out in juried showcases.
  - Systems depth lets critics explore emergent problem solving.
- **Feasibility Snapshot:**
  - Demo highlights parallax canopy management and actionable data overlays.
  - Deeper simulation requires lightweight systems scripting; Marimo pipeline can iterate on economy balance logs.
- **Prototype Link:** [`web_demos/clockwork_canopy.html`](../web_demos/clockwork_canopy.html).

### Tidebound Cartographer (TBC)
- **Premise:** Charting a living coastline where tides reveal or erase the truth of ancient civilizations.
- **Core Systems:**
  - Tidal rhythm puzzles: align relics before they submerge.
  - Narrative mapping where each charted layer affects future expeditions.
  - Local co-op where one player controls tides, the other explores ruins.
- **Suitability Notes:**
  - Maritime myth + tactile mapping offers a refreshing aesthetic for juries seeking novel settings.
  - Cooperative asymmetry broadens audience reach and festival demo appeal.
- **Feasibility Snapshot:**
  - Demo simulates tide harmonics and reveals hidden glyphs tied to accuracy.
  - Extended development requires network sync for co-op; prototype focuses on single-user storytelling cues.
- **Prototype Link:** [`web_demos/tidebound_cartographer.html`](../web_demos/tidebound_cartographer.html).

### Resonant Loom Archivists (RLA)
- **Premise:** Historians weave literal time threads to record endangered cultures.
- **Core Systems:** Temporal weaving puzzles, oral history recordings, and branching archival choices.
- **Suitability Notes:** Strong narrative hook, but heavy VO budget.
- **Feasibility Snapshot:** Stalled at VO pipeline planning; see notes below.
- **Status:** **On hold.** Blocked by lack of performer network—open task for future collaborators.

### Nebula Market Tacticians (NMT)
- **Premise:** A zero-gravity bazaar where traders haggle via constellations.
- **Core Systems:** Market simulation, constellation-based dialog, and zero-g traversal.
- **Suitability Notes:** Wildly creative but requires complex physics.
- **Feasibility Snapshot:** Prototype scaffolding started in `notes/nmt_physics.md` (not yet created). **Pending.**

## Dead Ends & Open Threads
- **VO Casting Pipeline (RLA):** Paused after failing to secure budget and actor agreements. Next step would be drafting remote-recording workflow.
- **Zero-G Physics Sandbox (NMT):** Prototype math stalled at collision resolution for spinning vendors. Would benefit from dedicated physics contributor.

## Next Steps for Collaborators
1. Expand on existing web demos with narrative overlays or scoring logic.
2. Revive `RLA` once a dialogue pipeline is ready—consider speech-to-text to mock interactions.
3. For `NMT`, begin with 2D projected physics before venturing into 3D; reference the `docs/physics_research` folder if/when it exists.

