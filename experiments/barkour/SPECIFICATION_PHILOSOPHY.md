# Specification-Driven Game Development

**Vision**: Create game specifications so precise that any competent implementation — human or AI, on any compatible platform — produces an experience indistinguishable from the designer's intent.

---

## The Problem with Code-First Development

Traditional approach:
```
Idea → Reference Implementation → Port → Port → Port
                ↓
         (drift accumulates)
                ↓
      "Close enough" on each platform
```

Each port interprets the reference. Subtle differences compound. The "feel" diverges.

---

## The Specification-First Alternative

```
Idea → Formal Specification → Implementation A
                           → Implementation B
                           → Implementation C
                           ↓
                 (all validate against spec)
                           ↓
              Identical behavior guaranteed
```

The specification is the source of truth. Implementations are **proofs** that the spec is realizable.

---

## What Makes a Specification "Impeccable"

### 1. Completeness
Every observable behavior is specified. No implementation decisions left to interpretation.

**Bad**: "The player should jump high enough to reach platforms."
**Good**: "Jump apex = initial_y - (jump_force² / (2 × gravity)) = 100 units above ground."

### 2. Precision
Numerical values with exact semantics. Units defined. Frame timing explicit.

**Bad**: "Coyote time gives the player a grace period after leaving a platform."
**Good**: "For 6 frames (100ms at 60fps) after last_grounded, jump input is valid."

### 3. Testability
Every requirement has a verification procedure.

```yaml
requirement: "Bacon boost increases speed by 50%"
test:
  given: player.speed = 3.0
  when: bacon.collected
  then: player.speed = 4.5 for 180 frames
  tolerance: ±0 frames, ±0.01 speed
```

### 4. Platform Abstraction
Specifies behavior, not mechanism. Platforms implement differently but achieve same result.

**Bad**: "Call `pygame.sprite.collide_rect()` for collision."
**Good**: "Collision occurs when player.hitbox overlaps bacon.hitbox by ≥1 pixel."

### 5. Graceful Degradation Rules
Explicit guidance for constrained platforms.

```yaml
constraint: resolution < 160×144
adaptation:
  - scale: hitboxes proportionally
  - preserve: timing ratios
  - allow: sprite simplification
  - require: jump arc ratio unchanged
```

---

## Specification Layers

### Layer 1: Core Mechanics (immutable)
Physics, timing, game rules. Must be identical everywhere.

```yaml
mechanics:
  gravity:
    value: 0.5
    unit: pixels/frame²
    non_negotiable: true

  jump:
    force: -10
    unit: pixels/frame
    coyote_time: 6 frames
    buffer_time: 4 frames
    non_negotiable: true
```

### Layer 2: Presentation (adaptable)
Visuals, audio, UI. Can vary by platform within constraints.

```yaml
presentation:
  player_sprite:
    reference: assets/tilly.png
    minimum_size: 8×8 pixels
    required_states: [idle, walk, jump, fall]
    adaptation: may simplify detail, must preserve silhouette

  bacon_sprite:
    reference: assets/bacon.png
    required: visually distinct from background
    animation: floating, 0.5-2 second period
```

### Layer 3: Platform Binding (per-implementation)
How abstract concepts map to platform specifics.

```yaml
# pico8_binding.yaml
platform: pico-8
resolution: 128×128
scale_factor: 0.4

input_mapping:
  jump: btn(4)  # O button
  left: btn(0)
  right: btn(1)

rendering:
  clear: cls()
  sprite: spr(n, x, y)
```

---

## Verification Framework

### Automated Tests
```python
class SpecificationTest:
    def test_jump_apex(self, implementation):
        """Player reaches exact apex height."""
        impl.spawn_player(x=50, y=ground)
        impl.press(JUMP)
        impl.advance_frames(apex_frame)

        expected_apex = ground - (JUMP_FORCE ** 2) / (2 * GRAVITY)
        assert impl.player.y == expected_apex, f"Apex mismatch: {impl.player.y} vs {expected_apex}"

    def test_coyote_time(self, implementation):
        """Jump valid for exactly 6 frames after leaving ground."""
        impl.spawn_player_on_platform()
        impl.walk_off_edge()

        for frame in range(6):
            impl.advance_frames(1)
            impl.press(JUMP)
            assert impl.player.vy < 0, f"Coyote jump failed at frame {frame}"
            impl.reset()

        impl.walk_off_edge()
        impl.advance_frames(7)
        impl.press(JUMP)
        assert impl.player.vy >= 0, "Coyote time extended beyond spec"

    def test_bacon_boost(self, implementation):
        """Boost duration exactly 180 frames."""
        impl.collect_bacon()

        for frame in range(180):
            assert impl.player.boost_active, f"Boost ended early at frame {frame}"
            impl.advance_frames(1)

        assert not impl.player.boost_active, "Boost extended beyond spec"
```

### Visual Diff Testing
```yaml
visual_tests:
  - name: jump_arc_comparison
    procedure:
      1. Record player jump trajectory on reference implementation
      2. Record same input sequence on test implementation
      3. Overlay trajectories
    pass_criteria: trajectories match within 2px at all points

  - name: level_layout
    procedure:
      1. Render level 1 on both implementations
      2. Compare platform positions
    pass_criteria: all platforms within 1 tile of reference
```

### Feel Testing (Human Validation)
```yaml
feel_tests:
  - name: blind_platform_test
    procedure:
      1. Player completes level 1 on implementation A
      2. Immediately plays level 1 on implementation B
      3. Asked: "Same game, or different?"
    pass_criteria: >80% report "same game"

  - name: speedrun_validity
    procedure:
      1. Record speedrun on reference implementation
      2. Replay inputs on test implementation
    pass_criteria: same outcome (success/failure, final time ±0.5s)
```

---

## Specification Document Structure

```
GAME_SPEC/
├── META.yaml                 # Name, version, authors, license
├── MECHANICS.yaml            # Layer 1: Core rules
├── PRESENTATION.yaml         # Layer 2: Visual/audio requirements
├── LEVELS/
│   ├── level_schema.yaml     # Level format definition
│   ├── level_01.yaml
│   ├── level_02.yaml
│   └── level_03.yaml
├── TESTS/
│   ├── mechanics_tests.yaml  # Automated verification
│   ├── visual_tests.yaml
│   └── feel_tests.yaml
├── BINDINGS/
│   ├── pygame.yaml
│   ├── pico8.yaml
│   ├── godot.yaml
│   └── ...
└── REFERENCE/
    ├── assets/               # Canonical art/audio
    ├── trajectories/         # Recorded physics traces
    └── implementation/       # Reference code (informative, not normative)
```

---

## Specification Evolution

### Versioning
```yaml
version: 1.2.0
changelog:
  1.2.0:
    - Added wall-jump mechanic
    - Increased coyote_time from 4 to 6 frames
  1.1.0:
    - Added double-jump
    - Reduced bacon boost from 4s to 3s
  1.0.0:
    - Initial release
```

### Breaking vs Non-Breaking Changes
- **Breaking**: Changes to Layer 1 (mechanics) — requires re-certification of all implementations
- **Non-breaking**: Changes to Layer 2/3 — implementations may update at leisure

### Deprecation
```yaml
deprecated:
  - feature: triple_jump
    removed_in: 2.0.0
    reason: "Reduced skill ceiling too much"
    migration: "Use wall-jump for height"
```

---

## Implementation Certification

### Certification Levels

| Level | Requirements | Badge |
|-------|--------------|-------|
| **Bronze** | Passes all automated mechanics tests | ✓ Spec-Compliant |
| **Silver** | Bronze + visual diff within tolerance | ✓✓ Verified |
| **Gold** | Silver + passes feel tests | ✓✓✓ Certified |

### Certification Process
```
1. Submit implementation + platform binding
2. Run automated test suite
3. Generate visual diff report
4. (Gold only) Human feel testing
5. Issue certification with version lock
```

### Recertification Triggers
- Spec version update (breaking)
- Platform major version change
- Implementation refactor

---

## Why This Matters

### For Designers
Specifications become **transferable design knowledge**. A well-specified game can be implemented by anyone, anywhere, anytime — and produce the intended experience.

### For Developers
Clear contracts. No guessing what "jump should feel good" means. Implementation becomes engineering, not interpretation.

### For AI Agents
Unambiguous task definition. An agent with a Gold-certified implementation has **proven** it understood the spec.

### For Players
Consistent experience across platforms. "Barkour on Pico-8" and "Barkour on Godot" are the same game, not cousins.

### For Preservation
Games specified this way survive platform death. The spec is eternal; implementations are ephemeral.

---

## Relation to Fantasy Consoles

The fantasy console specs (Pico-8, Vector-8, Mono-8) define **platforms**.
Game specs (Barkour) define **experiences**.

Together:
```
Platform Spec (Mono-8)     Game Spec (Barkour)
        ↓                          ↓
        └──────────┬───────────────┘
                   ↓
        Barkour-on-Mono-8 Implementation
                   ↓
            Certification Testing
                   ↓
              Gold Badge ✓✓✓
```

---

## Open Questions

1. **Tolerance thresholds**: How much variance is acceptable before "different game"?
2. **Floating point**: Mandate fixed-point for determinism, or allow platform float?
3. **RNG**: Require seeded determinism, or allow "statistically equivalent"?
4. **Audio precision**: Frame-accurate sound triggers, or "perceptually simultaneous"?
5. **Input latency**: Specify maximum input-to-response time?

---

## Next Steps

1. **Formalize Barkour spec** as proof-of-concept
2. **Build test harness** that runs against any implementation
3. **Certify PyGame implementation** as Gold reference
4. **Document certification for Pico-8** (constrained platform)
5. **Extract patterns** for specification authoring guide

---

**This document describes the destination. The parallel development plan describes the journey.**
