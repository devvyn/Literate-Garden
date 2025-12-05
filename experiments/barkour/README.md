# 🦴 Barkour Experiments

Playable manifestations of [Barkour: Tilly's Dream](../../../../barkour/GAME_VISION.md) - a bacon-powered parkour adventure starring a toothless Pekingese.

## About

This is the **experimental playground** for Barkour implementations. Fast iteration, playable prototypes, exploring "what if" scenarios without commitment to a single technical approach.

### The Vision
**Spiritual Center**: [`~/Documents/GitHub/barkour/`](../../../../barkour/)
**Core Idea**: Tilly (brownish-blonde Pekingese with black muzzle) discovers bacon gives her supernatural parkour abilities
**Essence**: Whimsical, heartwarming, nostalgic Flash-era platformer

## Experiments

### Interface Paradigm Branches

**Strategy**: Multiple interface expressions from single design skeleton
**Documentation**: [PARADIGM_EXPLORATION.md](./PARADIGM_EXPLORATION.md)
**Shared Architecture**: [shared/ARCHITECTURE.md](./shared/ARCHITECTURE.md)

Each subdirectory explores a different interface paradigm:

- **`prototypes/`** - Native desktop engines
  - **pygame-movement-01** ✅ Working baseline
  - Focus: PyGame, Pygame Zero, Arcade

- **`web/`** - Browser-based versions
  - **canvas-01** ⏳ Playable, needs testing
  - **phaser-01** 📋 Planned
  - Focus: Canvas API, Phaser.js framework

- **`pico8/`** - Fantasy console aesthetic
  - **barkour-01** 🌱 Just planted
  - Focus: Retro constraints, nostalgic feel
  - Matches "Flash-era aesthetic" from vision

- **`godot/`** - Open source engine (planned)
- **`unity/`** - Professional tooling (if needed)

- **`shared/`** - Common architecture
  - `barkour_config.json` - Single source of truth
  - `ARCHITECTURE.md` - Design skeleton
  - All paradigms share physics/mechanics

- **`docs/`** - Design explorations
  - Mechanics breakdowns
  - Level designs
  - Character concepts

## Garden Philosophy

From [Literate Garden README](../../README.md):

> **Make it playable, not perfect. Bud when it deserves structure.**

### Workflow
1. **Prototype rapidly** - Test ideas without heavy process
2. **Make it playable** - Focus on interaction over polish
3. **Decide fate**:
   - **Keep iterating** → Continue in garden
   - **Bud off** → Graduate to dedicated repo with governance
   - **Prune** → Document learnings, remove experiment

## Current Status

**Active Paradigms**:
- ✅ PyGame (prototypes/pygame-movement-01) - Working baseline
- ⏳ Canvas (web/canvas-01) - Physics implemented, needs testing
- 🌱 Pico-8 (pico8/barkour-01) - Just planted, waiting for installation

**Next to Explore**:
- Phaser.js (web framework approach)
- Godot (open source engine)

**Design Skeleton Status**: ✅ Established
- Shared config ensures all paradigms feel identical
- Accessibility patterns documented and inherited
- Ready for parallel development

## Getting Started

### Create a New Experiment

```bash
# For Python prototypes
cd prototypes/
python -m venv venv
source venv/bin/activate  # or: . venv/bin/activate
pip install pygame  # or: arcade, pygame-zero, etc.
# Create your experiment file
python tilly_movement_test.py
```

```bash
# For web prototypes
cd web/
# Create HTML file, link assets, open in browser
open prototype_name.html
```

### Testing Core Mechanics

Essential aspects to explore:
- **Bacon power-up feel** - How good does it feel to collect bacon?
- **Parkour movement** - Double jump, wall run, wall kick responsiveness
- **Power duration** - Tension between powered/unpowered states
- **Tilly's personality** - Does the character feel right?

## Budding Criteria

An experiment might be ready to bud into a dedicated repo when:
- ✅ Core parkour feel is **delightful**
- ✅ Power-up system creates **meaningful tension**
- ✅ Tilly's character comes through in **movement/animation**
- ✅ 2-3 levels demonstrate **progression concept**
- ✅ Technical foundation supports **full vision scope**

## Links

- **Vision Document**: [barkour/GAME_VISION.md](../../../../barkour/GAME_VISION.md)
- **Manifestations Tracker**: [barkour/MANIFESTATIONS.md](../../../../barkour/MANIFESTATIONS.md)
- **Literate Garden**: [../../README.md](../../README.md)

---

**Philosophy**: Every experiment teaches us something about what makes Barkour special.
