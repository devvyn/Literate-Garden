# Barkour: Formal Game Specification

**Version**: 1.0.0
**Status**: Complete Draft

---

## What Is This?

This directory contains the **formal specification** for Barkour, a bacon-powered parkour platformer. The specification defines the game's behavior with enough precision that any competent implementation — human or AI, on any compatible platform — produces an experience indistinguishable from the designer's intent.

**The specification is the source of truth. Code is derivative.**

---

## Document Structure

```
spec/
├── META.yaml                 # Version, authors, certification rules
├── MECHANICS.yaml            # Layer 1: Core rules (IMMUTABLE)
├── PRESENTATION.yaml         # Layer 2: Visual/audio (ADAPTABLE)
├── LEVELS/
│   ├── level_schema.yaml     # Level format definition
│   ├── level_01.yaml         # Tutorial level
│   ├── level_02.yaml         # (planned)
│   └── level_03.yaml         # (planned)
├── TESTS/
│   ├── mechanics_tests.yaml  # Automated physics verification
│   ├── visual_tests.yaml     # Screenshot comparison tests
│   └── feel_tests.yaml       # Human validation protocol
├── BINDINGS/
│   ├── pygame.yaml           # Reference implementation mapping
│   ├── pico8.yaml            # (planned)
│   └── ...
└── REFERENCE/
    ├── assets/               # Canonical art/audio
    └── trajectories/         # Recorded physics traces
```

---

## Specification Layers

### Layer 1: Mechanics (MECHANICS.yaml)
**Immutable** — These values define the game's feel and must be identical across all implementations.

- Physics constants (gravity, friction, terminal velocity)
- Jump mechanics (force, coyote time, buffer, variable height)
- Wall mechanics (slide speed, jump force, cooldown)
- Bacon boost (duration, multipliers, stacking)
- Collision rules

**Implementations must match these exactly within specified tolerance.**

### Layer 2: Presentation (PRESENTATION.yaml)
**Adaptable** — These values can be adjusted for platform constraints while preserving gameplay.

- Visual style (sprites, colors, animations)
- Audio (sound effects, music)
- UI layout (HUD, menus)
- Camera behavior

**Constrained platforms may adapt these following documented rules.**

### Layer 3: Platform Bindings (BINDINGS/*.yaml)
**Per-implementation** — Maps abstract spec to platform specifics.

- Input mapping (which button is "jump")
- Rendering API usage
- Audio implementation
- File structure

---

## Certification Levels

| Level | Badge | Requirements |
|-------|-------|--------------|
| **Bronze** | ✓ | Pass all automated mechanics tests |
| **Silver** | ✓✓ | Bronze + pass visual tests + complete all levels |
| **Gold** | ✓✓✓ | Silver + pass human feel tests + speedrun replay validity |

### How to Certify

1. Implement Barkour on your target platform
2. Create a platform binding (BINDINGS/your_platform.yaml)
3. Expose the test harness interface
4. Run `mechanics_tests.yaml` — must pass 100%
5. Run `visual_tests.yaml` — must meet similarity threshold
6. Conduct `feel_tests.yaml` with 3+ human testers
7. Submit certification report

---

## Key Mechanics Summary

### Movement
- Walk speed: **3.0** px/frame
- Run speed: **5.0** px/frame
- Ground friction: **0.85** (when no input)
- Air friction: **0.95**

### Jump
- Jump force: **-12** px/frame
- Apex height: **144** logical pixels
- Time to apex: **24** frames (400ms)
- Coyote time: **6** frames (100ms)
- Jump buffer: **4** frames (67ms)
- Variable height: yes (early release = lower)

### Wall
- Wall slide max speed: **2** px/frame
- Wall jump horizontal: **8** px/frame
- Wall jump vertical: **-13** px/frame
- Wall jump cooldown: **6** frames

### Bacon Boost
- Duration: **180** frames (3000ms) — **EXACT, non-negotiable**
- Speed multiplier: **1.5×**
- Jump multiplier: **1.2×**
- Stacking: refresh timer (not additive)

### Physics
- Gravity: **0.5** px/frame²
- Terminal velocity: **15** px/frame
- Coordinate system: top-left origin, Y-down
- Resolution: **320×240** logical pixels (scale to display)

---

## For Implementers

### Quick Start
1. Read `MECHANICS.yaml` — implement physics exactly as specified
2. Read `PRESENTATION.yaml` — implement visuals within adaptation rules
3. Load `LEVELS/level_01.yaml` — test your implementation
4. Run `TESTS/mechanics_tests.yaml` — verify correctness

### Critical Tolerances
- Position: ±1 pixel
- Velocity: ±0.01 px/frame
- Frame timing: **±0 frames** (exact for coyote, buffer, boost)

### Common Mistakes
- Using variable timestep without conversion
- Applying friction before movement
- Checking collision in wrong order
- Boost duration off by 1 frame
- Coyote time counted from wrong event

---

## For Designers

### Editing the Spec
- Layer 1 changes require **version bump** and **recertification**
- Layer 2 changes are non-breaking
- Document all changes in META.yaml changelog

### Adding Levels
- Follow `level_schema.yaml` format
- Include validation checklist (reachability proof)
- Test on reference implementation first

### Tuning Feel
- All feel-related values are in MECHANICS.yaml
- Changes propagate to all certified implementations
- Consider backward compatibility (existing speedruns)

---

## Philosophy

> "Create game specifications so precise that any competent implementation produces an experience indistinguishable from the designer's intent."

This specification embodies:
- **Completeness**: Every observable behavior is specified
- **Precision**: Numerical values with exact semantics
- **Testability**: Every requirement has a verification procedure
- **Platform abstraction**: Behavior specified, not mechanism

The goal is not to constrain creativity, but to **define the contract** between designer and implementer so clearly that implementation becomes engineering, not interpretation.

---

## Related Documents

- `../SPECIFICATION_PHILOSOPHY.md` — Why specification-driven development
- `../PARALLEL_DEVELOPMENT_PLAN.md` — Multi-platform implementation strategy
- `../shared/barkour_config.json` — Legacy config (superseded by this spec)
- `../shared/ARCHITECTURE.md` — Implementation patterns

---

## License

Specification: CC BY-SA 4.0
Reference assets: To be determined

---

*Specifications are eternal. Implementations are ephemeral.*
