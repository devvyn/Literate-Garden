# Barkour Spec Audit Results

**Date**: 2025-01-15
**Auditor**: Claude Opus 4.5

---

## Summary

| Metric | Count |
|--------|-------|
| **Matching** | 9 |
| **Mismatches** | 1 |
| **New in Spec** | 3 |

---

## Matching Values (No Action)

These values are consistent across spec, PyGame, and config:

| Parameter | Value |
|-----------|-------|
| Gravity | 0.5 px/frame² |
| Terminal velocity | 15 px/frame |
| Run speed | 5.0 px/frame |
| Jump force | -12 px/frame |
| Wall slide speed | 2 px/frame |
| Wall jump horizontal | 8 px/frame |
| Wall jump vertical | -13 px/frame |
| Boost speed multiplier | 1.5× |
| Boost jump multiplier | 1.2× |

---

## Mismatch: Boost Duration

| Source | Value |
|--------|-------|
| Spec | 180 frames (3000ms / 3 seconds) |
| PyGame | 5000ms (5 seconds) |
| Config | 5000ms (5 seconds) |

### Resolution Options

**Option A: Update spec to match implementation**
- Change spec to 300 frames (5000ms)
- Rationale: Preserves existing gameplay feel
- Risk: Spec now documents what exists, not what's ideal

**Option B: Update implementation to match spec**
- Change PyGame/config to 3000ms
- Rationale: Spec is authoritative, 3s is more intense
- Risk: Changes gameplay feel players may prefer

**Recommendation**: **Option B** — The spec defines desired behavior. 3 seconds creates more tension and encourages collecting more bacon. Implementation should conform.

---

## New in Spec (Implementation Gaps)

### 1. Walk Speed (3.0 px/frame)

**Current state**: Implementation only has run speed (5.0)

**Spec intent**: Walk when pressing direction, run when holding shift

**Resolution Options**:
- A: Add walk/run distinction to implementations
- B: Remove walk speed from spec (always run)

**Recommendation**: **Option B** — Keep it simple. Most platformers don't distinguish walk/run. Update spec to remove walk speed, use 5.0 as sole movement speed.

### 2. Coyote Time (6 frames)

**Current state**: Not implemented in PyGame or Web Canvas

**Spec intent**: Allow jump for 6 frames after leaving platform edge

**Resolution Options**:
- A: Implement in all platforms
- B: Mark as optional/enhancement
- C: Remove from spec

**Recommendation**: **Option A** — Coyote time is a standard platformer feel improvement. Implementation is ~10 lines of code. Worth adding.

### 3. Jump Buffer (4 frames)

**Current state**: Not implemented

**Spec intent**: Allow jump input slightly before landing to execute on land

**Resolution Options**:
- A: Implement in all platforms
- B: Mark as optional/enhancement
- C: Remove from spec

**Recommendation**: **Option A** — Jump buffer is equally standard. Combined with coyote time, creates responsive feel. Implementation is ~10 lines.

---

## Validation Paths Forward

### Path 1: Reconcile Spec ← Implementations (Quick)
1. Change spec boost duration: 180 → 300 frames
2. Remove walk speed from spec
3. Mark coyote/buffer as "recommended" not "required"
4. Re-run audit to confirm all MATCH

**Outcome**: Existing implementations are Bronze-certifiable as-is

### Path 2: Reconcile Implementations → Spec (Correct)
1. Update PyGame boost: 5000ms → 3000ms
2. Update config boost: 5000ms → 3000ms
3. Add coyote time to PyGame
4. Add jump buffer to PyGame
5. Re-run audit to confirm all MATCH
6. Port changes to Web Canvas

**Outcome**: Implementations conform to spec vision

### Path 3: Parallel Test (Validate Spec Sufficiency)
1. Freeze spec as-is
2. Fresh agent implements on LÖVE2D (no access to existing code)
3. Compare LÖVE2D behavior to PyGame
4. Measure: how many clarifications needed?

**Outcome**: Proof that spec is implementable from scratch

---

## Recommended Action Plan

### Immediate (Today)
1. **Decision**: Choose Path 1 or Path 2
2. **Update**: Implement chosen reconciliation
3. **Audit**: Re-run to confirm MATCH status

### Short Term (This Week)
4. Add test harness API to PyGame
5. Run 5 mechanics tests from spec
6. Document any test failures

### Medium Term (Next Week)
7. Implement same changes in Web Canvas
8. Side-by-side comparison recording
9. Begin Path 3 validation (fresh implementation)

---

## Decision Required

> **Which reconciliation direction?**
>
> - [ ] Path 1: Spec follows implementations (faster, preserves current feel)
> - [ ] Path 2: Implementations follow spec (correct, may change feel)

Awaiting human decision before proceeding.
