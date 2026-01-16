# Barkour Spec Validation Paths

**Goal**: Validate that the formal specification produces identical behavior across implementations.

---

## Current State Assessment

### Existing Implementations

| Platform | Location | Status | Config Source |
|----------|----------|--------|---------------|
| PyGame | `prototypes/pygame-movement-01/` | Working | Hardcoded constants |
| Web Canvas | `web/canvas-01/` | Playable | `shared/barkour_config.json` |
| Pico-8 | `pico8/barkour-01/` | Skeleton | None yet |

### Discovered Discrepancies

| Parameter | PyGame Code | Old Config | New Spec | Notes |
|-----------|-------------|------------|----------|-------|
| Boost duration | 5000ms | 5000ms | 3000ms (180 frames) | **CONFLICT** |
| Walk speed | - | 5 | 3.0 | Spec distinguishes walk/run |
| Run speed | 5 | 5 | 5.0 | Match |
| Jump force | -12 | -12 | -12 | Match |
| Gravity | 0.5 | 0.5 | 0.5 | Match |
| Coyote time | Not impl? | Not defined | 6 frames | **NEW** |
| Jump buffer | Not impl? | Not defined | 4 frames | **NEW** |
| Variable jump | Not impl? | Not defined | Yes | **NEW** |

**Key Finding**: Spec adds mechanics (coyote time, jump buffer, variable jump) that don't exist in current implementations.

---

## Validation Path 1: Conformance Audit

**Objective**: Determine if existing implementations can achieve certification.

### Steps
1. Read PyGame `main.py` completely
2. Compare each mechanic against `MECHANICS.yaml`
3. Document gaps and conflicts
4. Determine: update implementations → spec, or spec → implementations?

### Expected Outcome
- List of spec compliance gaps
- Decision on which direction to reconcile
- Updated spec OR updated implementations

### Effort: Low (2-4 hours)

---

## Validation Path 2: Test Harness MVP

**Objective**: Create minimal test runner that validates mechanics.

### Approach
```python
# test_harness.py
import yaml
from implementations.pygame import BarkourGame

def test_jump_apex():
    """Spec: apex_height = 144 pixels"""
    game = BarkourGame()
    game.spawn_player(160, 240)  # on ground
    initial_y = game.player.y

    game.press('jump')
    for _ in range(24):  # time_to_apex
        game.advance_frame()

    apex_height = initial_y - game.player.y
    assert abs(apex_height - 144) <= 2, f"Apex {apex_height} != 144"
```

### Requirements
1. PyGame implementation exposes test harness API
2. Load spec from YAML
3. Run mechanics tests programmatically

### Effort: Medium (1-2 days)

---

## Validation Path 3: Side-by-Side Recording

**Objective**: Visual proof that implementations behave identically.

### Approach
1. Record input sequence on PyGame
2. Replay same inputs on Web Canvas
3. Compare trajectories frame-by-frame
4. Generate visual diff

### Tools Needed
- Input recorder (log keypresses with frame timestamps)
- Trajectory exporter (player x,y per frame)
- Comparison script (compute deviation)

### Effort: Medium (1-2 days)

---

## Validation Path 4: Fresh Implementation from Spec

**Objective**: Prove spec is sufficient for implementation without reference code.

### Approach
1. Give spec to a fresh agent (no access to existing code)
2. Agent implements on new platform (e.g., LÖVE2D or Godot)
3. Compare behavior to PyGame reference
4. Measure: how much clarification was needed?

### Success Criteria
- Agent asks ≤3 clarifying questions
- Resulting implementation passes mechanics tests
- Jump/physics feel identical to reference

### Effort: High (1-3 days)

---

## Validation Path 5: Constrained Platform Port

**Objective**: Validate adaptation rules work for Pico-8/Mono-8.

### Approach
1. Implement Barkour on Pico-8 following spec
2. Apply documented adaptation rules for 128×128
3. Verify core mechanics still pass (scaled)
4. Human feel test: "Same game?"

### Effort: Medium-High (2-4 days)

---

## Recommended Validation Sequence

### Phase A: Quick Wins (Today)
1. **Path 1**: Audit PyGame against spec (find all gaps)
2. Reconcile boost duration conflict (5s → 3s or vice versa)
3. Document missing mechanics (coyote, buffer, variable jump)

### Phase B: Prove Testability (This Week)
4. **Path 2**: Build minimal test harness
5. Run 5-10 core mechanics tests against PyGame
6. Fix any failures, update spec if needed

### Phase C: Prove Portability (Next)
7. **Path 3**: Record and compare PyGame vs Web Canvas
8. **Path 4**: Fresh implementation on new platform

### Phase D: Prove Scalability (Later)
9. **Path 5**: Pico-8 implementation with adaptations

---

## Immediate Actions

### 1. Resolve Boost Duration Conflict
```
Current: 5000ms (5 seconds)
Spec: 3000ms (3 seconds / 180 frames)

Decision needed:
  A) Update spec to match existing (5000ms = 300 frames)
  B) Update implementations to match spec (3000ms)
  C) Playtest both, choose what feels better
```

### 2. Add Missing Mechanics to Implementations
```
Not in current code:
  - Coyote time (6 frames after leaving platform)
  - Jump buffer (4 frames before landing)
  - Variable jump height (early release = lower)

Options:
  A) Add to PyGame/Canvas to match spec
  B) Remove from spec (simpler implementations)
  C) Mark as "optional enhancements" in spec
```

### 3. Create Test Harness Interface
```python
# Required API for certification testing
class TestableGame:
    def spawn_player(self, x, y): ...
    def get_player_state(self) -> dict: ...
    def advance_frame(self): ...
    def press(self, action): ...
    def release(self, action): ...
```

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Spec completeness | All mechanics testable | mechanics_tests.yaml coverage |
| Implementation parity | <5% deviation | Trajectory comparison |
| Fresh implementation success | ≤3 questions asked | Agent interaction log |
| Certification achievable | Bronze within 4 hours | Time to pass all tests |

---

## Open Questions for Resolution

1. **Frame vs Time**: Spec uses frames, implementations use milliseconds. Standardize?
2. **Physics Granularity**: Fixed timestep mandatory, or allow delta-time with conversion?
3. **Missing Mechanics**: Add coyote/buffer to implementations, or remove from spec?
4. **Boost Duration**: 3s (spec) or 5s (implementations)?

---

*This document tracks validation progress. Update as paths are completed.*
