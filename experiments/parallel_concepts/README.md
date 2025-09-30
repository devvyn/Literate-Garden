# Parallel Game Concept Demos

<!-- Shared context: This README introduces four parallel concept slices for Marimo capture. -->

Each concept below pairs a concise pitch with feasibility notes and links to a minimal web-ready artefact. Every artefact is intentionally lightweight so multiple collaborators can iterate without stepping on each other.

## Version A — **Echoes in Neon** (Cyberpunk Rhythm Reflex)
- **Concept Flair:** Pilot a courier weaving through neon alleys where beats manifest as light pulses. Players tap cues to stay in rhythm while dodging obstacles that sync to the soundtrack.
- **Suitability / Feasibility:**
  - *Technical Scope:* Moderate — core loop is timing-based, using lightweight input detection and beat scheduling. Extendable with procedural track authoring.
  - *Gameplay Loop:* Hear beat → react via arrow keys → earn momentum boosts or stumble.
  - *Audience Appeal:* Rhythm-action fans, streamers attracted by synthwave aesthetics.
- **Demo:** [`version_a_echoes_in_neon.html`](./version_a_echoes_in_neon.html)

## Version B — **Botanical Bard** (Cozy Narrative Composer)
- **Concept Flair:** Tend a living poem garden where each plant is a stanza that grows based on player-selected moods and inspirations.
- **Suitability / Feasibility:**
  - *Technical Scope:* Lightweight — seeded text templates and unlockable descriptors; scalability via AI-assisted stanza generation.
  - *Gameplay Loop:* Choose tone → sprout stanza → curate arrangement → share garden snapshots.
  - *Audience Appeal:* Cozy gamers, creative writers, social sharers seeking mindful play.
- **Demo:** [`version_b_botanical_bard.html`](./version_b_botanical_bard.html)

## Version C — **Astral Weaver** (Tactical Pattern Puzzle)
- **Concept Flair:** Align constellations on a holographic loom to channel cosmic energy. Players rotate fragments to weave paths between stellar anchors.
- **Suitability / Feasibility:**
  - *Technical Scope:* Mid-high — tile rotation logic with solvable procedural generation.
  - *Gameplay Loop:* Rotate tiles → connect anchors → trigger chain reactions → unlock lore snippets.
  - *Audience Appeal:* Puzzle aficionados craving tactile sci-fi aesthetics.
- **Demo:** [`version_c_astral_weaver.html`](./version_c_astral_weaver.html)

## Version D — **Quantum Jam Session** (Live Audio Sandbox)
- **Concept Flair:** Improvise in a zero-gravity lounge where orbital nodes emit harmonics. Players layer loops, modulate filters, and sculpt soundscapes.
- **Suitability / Feasibility:**
  - *Technical Scope:* Moderate — Web Audio graph with loopers and lightweight visualizers.
  - *Gameplay Loop:* Activate orbiting nodes → tweak parameters → capture live mixdowns.
  - *Audience Appeal:* Music experimenters, ambient creators, streamers who mix live.
- **Demo:** [`version_d_quantum_jam.html`](./version_d_quantum_jam.html)

> **Collaboration Note:** Each HTML file contains inline comments marking extension hooks (`<!-- EXTENSION HOOK -->`) so new agents can bolt on features without guesswork.
