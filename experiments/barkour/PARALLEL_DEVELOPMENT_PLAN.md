# Barkour: Parallel Development Plan

**Objective**: Demonstrate simultaneous cross-platform game development using shared configuration and specialized agents.

**Target**: 10 platform implementations from single source of truth

---

## Architecture Overview

```
barkour/
├── shared/
│   ├── barkour_config.json      # Physics, timing, gameplay constants
│   ├── level_data.json          # Level geometry (platform-agnostic)
│   ├── ARCHITECTURE.md          # Shared design decisions
│   └── assets/
│       ├── tilly_reference.png  # Art reference (adapt per platform)
│       └── bacon_reference.png
│
├── implementations/
│   ├── pygame/          # Tier 1: Full parity
│   ├── web-canvas/
│   ├── phaser/
│   ├── love2d/
│   ├── godot/
│   ├── raylib/
│   ├── pico8/           # Tier 2: Constrained
│   ├── mono8/
│   ├── tic80/
│   └── terminal/        # Tier 3: Transformed
│
└── tools/
    ├── config_validator.py      # Ensure config consistency
    ├── level_converter.py       # Export levels to platform formats
    └── comparison_runner.py     # Side-by-side testing
```

---

## Shared Configuration Schema

```json
{
  "meta": {
    "version": "1.0.0",
    "name": "Barkour",
    "description": "Bacon-powered parkour platformer"
  },

  "display": {
    "logical_width": 320,
    "logical_height": 240,
    "target_fps": 60
  },

  "physics": {
    "gravity": 0.5,
    "terminal_velocity": 12,
    "ground_friction": 0.85,
    "air_friction": 0.95
  },

  "player": {
    "walk_speed": 3.0,
    "run_speed": 5.0,
    "jump_force": -10,
    "double_jump_force": -8,
    "coyote_time_frames": 6,
    "jump_buffer_frames": 4,
    "hitbox": {"width": 12, "height": 16}
  },

  "bacon": {
    "float_amplitude": 4,
    "float_speed": 0.1,
    "collect_radius": 16,
    "boost_multiplier": 1.5,
    "boost_duration_frames": 180
  },

  "levels": {
    "tile_size": 16,
    "reference": "level_data.json"
  }
}
```

---

## Agent Assignments

### Core Agents (Tier 1 Platforms)

| Agent ID | Platform | Specialty | Dependencies |
|----------|----------|-----------|--------------|
| `pygame-agent` | PyGame | Python, SDL | None (baseline) |
| `canvas-agent` | Web Canvas | Vanilla JS, Canvas API | None |
| `phaser-agent` | Phaser.js | Phaser 3 framework | canvas-agent patterns |
| `love-agent` | LÖVE2D | Lua, love.* API | pico8-agent patterns |
| `godot-agent` | Godot | GDScript, Node2D | None |
| `raylib-agent` | Raylib | C, minimal deps | None |

### Constrained Agents (Tier 2 Platforms)

| Agent ID | Platform | Specialty | Dependencies |
|----------|----------|-----------|--------------|
| `pico8-agent` | Pico-8 | Lua subset, 128×128 | love-agent |
| `mono8-agent` | Mono-8 | MonoScript, 160×144 | pico8-agent |
| `tic80-agent` | TIC-80 | Lua/JS, 240×136 | pico8-agent |

### Experimental Agent (Tier 3)

| Agent ID | Platform | Specialty | Dependencies |
|----------|----------|-----------|--------------|
| `terminal-agent` | ASCII/Curses | ncurses, Unicode | None |

---

## Phase Execution

### Phase 0: Foundation (Pre-work)
**Duration**: Complete before parallel sprint

- [ ] Finalize `barkour_config.json` schema
- [ ] Create `level_data.json` with 3 test levels
- [ ] Document platform adaptation rules in `ARCHITECTURE.md`
- [ ] Build `config_validator.py`
- [ ] Establish PyGame as reference implementation

**Owner**: Human (you) + general agent

---

### Phase 1: Parallel Sprint — Tier 1
**Parallelism**: 6 agents simultaneously

```
┌─────────────────────────────────────────────────────────────┐
│  PARALLEL EXECUTION BLOCK                                    │
├─────────────┬─────────────┬─────────────┬─────────────┬─────┤
│ pygame-agent│ canvas-agent│ phaser-agent│ love-agent  │ ... │
│ (validate)  │ (complete)  │ (new)       │ (new)       │     │
├─────────────┼─────────────┼─────────────┼─────────────┼─────┤
│ godot-agent │ raylib-agent│             │             │     │
│ (new)       │ (new)       │             │             │     │
└─────────────┴─────────────┴─────────────┴─────────────┴─────┘
```

**Each agent delivers**:
1. Player movement (walk, run, jump, double-jump)
2. Bacon collection with boost mechanic
3. Level 1 playable
4. Basic collision detection
5. Score display

**Sync point**: All 6 must reach "Level 1 playable" before Phase 2

---

### Phase 2: Parallel Sprint — Tier 2
**Parallelism**: 3 agents simultaneously

```
┌─────────────────────────────────────────────────────────────┐
│  PARALLEL EXECUTION BLOCK                                    │
├─────────────────┬─────────────────┬─────────────────────────┤
│ pico8-agent     │ mono8-agent     │ tic80-agent             │
│ (adapt assets)  │ (new runtime)   │ (Pico-8 port)           │
└─────────────────┴─────────────────┴─────────────────────────┘
```

**Adaptation rules for constrained platforms**:
- Pico-8: Scale levels to 128×128 viewport, 8×8 sprites
- Mono-8: 4-shade dithering, 160×144 viewport
- TIC-80: Direct Pico-8 port with resolution bump

---

### Phase 3: Integration & Polish
**Sequential, human-directed**

1. Run `comparison_runner.py` across all 9 implementations
2. Identify physics divergence (frame timing, collision)
3. Tune per-platform until "feel" matches
4. Record side-by-side video comparison
5. Write retrospective on what transferred vs. what diverged

---

### Phase 4: Experimental
**Optional, interest-driven**

- `terminal-agent`: ASCII Barkour
- Playdate port (if hardware available)
- Vector-8 wireframe experiment

---

## Agent Task Templates

### Template: New Platform Implementation

```markdown
## Task: Implement Barkour on [PLATFORM]

### Context
- Read `shared/barkour_config.json` for all constants
- Read `shared/level_data.json` for level geometry
- Reference `implementations/pygame/` as canonical behavior

### Deliverables
1. Project structure matching platform conventions
2. Game loop at 60fps (or platform standard)
3. Player controller:
   - Walk/run with friction
   - Jump with coyote time and jump buffering
   - Double jump
4. Bacon collectible:
   - Floating animation
   - Collection detection
   - Speed boost on collect
5. Level rendering:
   - Platforms from level_data.json
   - Collision with platforms
6. HUD:
   - Score (bacon count)
   - Boost indicator

### Validation
- [ ] Player jump height matches PyGame reference
- [ ] Bacon boost duration is exactly 3 seconds
- [ ] Coyote time allows jump 6 frames after leaving platform
- [ ] Level 1 completable with same route as PyGame

### DO NOT
- Invent new mechanics
- Change physics values
- Add features not in config
```

---

### Template: Constrained Platform Adaptation

```markdown
## Task: Adapt Barkour to [CONSTRAINED PLATFORM]

### Context
- Source: `implementations/pygame/` (or nearest Tier 1)
- Target constraints: [RESOLUTION], [COLORS], [SPRITES]
- Config: `shared/barkour_config.json` (scale appropriately)

### Adaptation Rules
1. **Resolution scaling**:
   - Logical 320×240 → [TARGET]
   - Scale factor: [FACTOR]
   - Adjust hitboxes proportionally

2. **Asset adaptation**:
   - Redraw sprites at target resolution
   - Reduce colors to platform palette
   - Document which details were cut

3. **Physics preservation**:
   - Multiply velocities by scale factor
   - Gravity and friction ratios unchanged
   - Frame timing identical (60fps or platform standard)

### Deliverables
- Platform-native implementation
- `ADAPTATION_NOTES.md` documenting changes
- Side-by-side screenshot comparison

### Validation
- [ ] Jump arc visually proportional to Tier 1
- [ ] Bacon boost feels identical in duration
- [ ] Level 1 completable (may need layout tweaks)
```

---

## Coordination Protocol

### Daily Sync Format
```
AGENT: [agent-id]
STATUS: [in_progress | blocked | complete]
COMPLETED:
  - [what shipped]
BLOCKERS:
  - [what's stuck]
DIVERGENCE:
  - [where physics/feel differs from reference]
```

### Escalation Triggers
1. **Physics divergence >5%**: Escalate to human for ruling
2. **Platform limitation discovered**: Document in `ADAPTATION_NOTES.md`
3. **Config schema inadequate**: Propose schema change via bridge

### Integration Checkpoints
| Checkpoint | Criteria | Validator |
|------------|----------|-----------|
| `movable` | Player moves with correct speed | `config_validator.py` |
| `jumpable` | Jump height within 5% of reference | Manual frame count |
| `collectible` | Bacon boost duration exact | Timer check |
| `playable` | Level 1 completable | Human playtest |
| `shippable` | All 3 levels, no crashes | Full playthrough |

---

## Success Metrics

### Quantitative
- [ ] 10 platforms implemented
- [ ] All pass `config_validator.py`
- [ ] Jump height variance <5% across platforms
- [ ] Boost duration variance <1 frame across platforms

### Qualitative
- [ ] "Feels like the same game" on blind test
- [ ] Platform idioms respected (not just ports)
- [ ] Constrained platforms feel intentional, not broken

### Showcase Deliverables
- 10-way split-screen video (Level 1 speedrun)
- Blog post: "One Game, Ten Platforms, One Config"
- Open-source release of shared architecture

---

## Risk Registry

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Frame timing variance | High | Medium | Use delta-time, not frame count |
| Collision edge cases | Medium | High | Canonical test cases in config |
| Agent drift (adding features) | Medium | Medium | Strict task templates |
| Platform blocks progress | Low | High | Drop to 9 platforms |
| Config schema inadequate | Medium | Medium | Iterate schema in Phase 0 |

---

## Appendix: Platform Quick Reference

| Platform | Language | Resolution | Colors | FPS | Difficulty |
|----------|----------|------------|--------|-----|------------|
| PyGame | Python | Any | Any | 60 | Easy |
| Web Canvas | JS | Any | Any | 60 | Easy |
| Phaser.js | JS | Any | Any | 60 | Easy |
| LÖVE2D | Lua | Any | Any | 60 | Easy |
| Godot | GDScript | Any | Any | 60 | Medium |
| Raylib | C | Any | Any | 60 | Medium |
| Pico-8 | Lua | 128×128 | 16 | 30/60 | Medium |
| TIC-80 | Lua/JS | 240×136 | 16 | 60 | Medium |
| Mono-8 | MonoScript | 160×144 | 4 | 60 | Medium |
| Terminal | Python | 80×24 | 16 | 30 | Hard |

---

**Plan Status**: Ready for execution
**Next Action**: Validate Phase 0 prerequisites are complete
