# Barkour - Interface Paradigm Exploration

**Date**: 2025-10-11
**Strategy**: Multiple expressions from single design skeleton

---

## Core Philosophy

Barkour's design skeleton (shared config + component structure) enables exploration of **different interface paradigms** while maintaining **identical core gameplay**. Each paradigm is a valid expression of the same game vision.

**Design Skeleton**: `shared/barkour_config.json` + `shared/ARCHITECTURE.md`

---

## Paradigm Branches

### Branch 1: PyGame (Desktop Native)
**Location**: `prototypes/pygame-movement-01/`
**Status**: ✅ Working prototype
**Paradigm**: Native desktop application

**Characteristics**:
- Direct pixel rendering
- Native window management
- Keyboard input via pygame events
- 60fps game loop with pygame.time.Clock
- Desktop-first experience

**Strengths**:
- Fast, responsive controls
- Native feel
- Easy debugging
- Direct hardware access

**Learnings**:
- Wall jump mechanics feel tight
- Bacon power-up timing (5s) works well
- Arrow key controls universal across layouts
- Super Meat Boy-like movement feel achieved

**Next Steps**:
- [ ] Add level progression
- [ ] Implement death/respawn
- [ ] Add particle effects
- [ ] Sound effects exploration

---

### Branch 2: Web Canvas (Browser Vanilla)
**Location**: `web/canvas-01/`
**Status**: ⏳ In progress (playable but needs testing)
**Paradigm**: Browser-based vanilla JavaScript

**Characteristics**:
- HTML5 Canvas API
- requestAnimationFrame game loop
- DOM keyboard events
- Runs in any modern browser
- No framework dependencies

**Strengths**:
- Zero install required
- Cross-platform by default
- Easy to share (just a URL)
- Inspect with browser DevTools

**Considerations**:
- Browser vsync timing
- Touch control additions needed
- Mobile performance
- Canvas scaling strategies

**Next Steps**:
- [ ] Test side-by-side with PyGame version
- [ ] Verify physics parity (same jump height, speed)
- [ ] Add touch controls for mobile
- [ ] Implement fullscreen mode

---

### Branch 3: Phaser.js (Web Framework)
**Location**: `web/phaser-01/` (planned)
**Status**: 📋 Not started
**Paradigm**: Web game framework

**Characteristics**:
- Phaser.js game framework
- Built-in physics engine
- Scene management
- Sprite/animation system
- Mobile-ready touch controls

**Why Explore**:
- Built-in physics might simplify code
- Scene system for menus/levels
- Asset management
- Production-ready tooling
- Large community, lots of examples

**Questions to Answer**:
- Does Phaser's physics match our custom physics?
- Is framework overhead worth the features?
- How does it handle our shared config pattern?
- Better or worse than vanilla Canvas?

**Next Steps**:
- [ ] Set up Phaser.js boilerplate
- [ ] Port player physics to Phaser
- [ ] Test power-up system integration
- [ ] Compare performance vs Canvas

---

### Branch 4: Godot (Open Source Engine)
**Location**: `godot/barkour-01/` (planned)
**Status**: 📋 Not started
**Paradigm**: Cross-platform game engine

**Characteristics**:
- Godot Engine (open source)
- Scene/node architecture
- GDScript (Python-like)
- Export to desktop/web/mobile
- Built-in animation/physics

**Why Explore**:
- Free and open source (MIT licensed)
- Strong 2D platformer support
- Export to multiple platforms from one codebase
- Visual scene editor
- Active community

**Questions to Answer**:
- Can we maintain shared config pattern?
- How to translate JSON config to Godot Resources?
- Does it feel as responsive as PyGame?
- Export size and performance?

**Next Steps**:
- [ ] Install Godot Engine
- [ ] Create scene structure
- [ ] Import shared config
- [ ] Implement player physics
- [ ] Test web export

---

### Branch 5: Unity (Industry Standard)
**Location**: `unity/barkour-01/` (planned)
**Status**: 📋 Not started
**Paradigm**: Professional game engine

**Characteristics**:
- Unity Engine
- C# scripting
- Component-based architecture
- Export to all platforms
- Massive asset ecosystem

**Why Explore**:
- Industry-standard tooling
- Strong physics system
- Professional workflows
- Export to consoles
- Large community

**Considerations**:
- Closed source
- Licensing for commercial use
- Larger learning curve
- Heavier editor

**Questions to Answer**:
- Overkill for a simple platformer?
- Does it respect our design skeleton?
- Performance vs simpler engines?
- Worth the complexity?

**Status**: Low priority (explore only if others prove limited)

---

### Branch 6: Pico-8 (Fantasy Console)
**Location**: `pico8/barkour-01/` (planned)
**Status**: 💡 Idea phase
**Paradigm**: Retro fantasy console aesthetic

**Characteristics**:
- Pico-8 fantasy console
- Lua scripting
- 128x128 pixel display
- 16-color palette
- Built-in sprite/map editor
- Constraint-based design

**Why Explore**:
- Matches nostalgic Flash-era aesthetic from vision
- Constraints force creative solutions
- Built-in shareability (cart files)
- Charming retro feel
- Perfect for "whimsical parkour" vibe

**Questions to Answer**:
- Can we maintain shared config in Lua?
- Do 128x128 constraints work for level design?
- Does it capture Tilly's personality?
- Can we export to web?

**Next Steps**:
- [ ] Prototype Tilly sprite in Pico-8 editor
- [ ] Test wall jump physics in 128x128
- [ ] Explore 16-color palette for Tilly/bacon
- [ ] Evaluate if constraints enhance or limit vision

---

## Shared Architecture Guarantee

**All paradigms share**:
1. Same physics parameters (gravity, jump strength, speed)
2. Same power-up duration (5 seconds)
3. Same level layouts (when applicable)
4. Same collision rules
5. Same accessibility principles (arrow keys, keyboard-first)

**Verification Strategy**:
- Record gameplay video of each paradigm
- Same level, same task (e.g., "collect all bacon, reach top")
- Compare side-by-side
- Should feel identical (except visual style)

---

## Evaluation Criteria

For each paradigm, evaluate:

### Technical
- **Setup time**: How long to get playable?
- **Iteration speed**: How fast can we test changes?
- **Performance**: Smooth 60fps?
- **Physics accuracy**: Matches shared config?
- **Code clarity**: Easy to understand/maintain?

### Design
- **Control feel**: Responsive and tight?
- **Visual polish**: Can we achieve whimsical aesthetic?
- **Accessibility**: Arrow keys work? Keyboard-first?
- **Platform reach**: Where can it run?

### Workflow
- **Debugging ease**: Easy to find/fix bugs?
- **Asset pipeline**: How to add sprites/sounds?
- **Build/deploy**: How to share with testers?
- **Version control**: Git-friendly?

### Vision Alignment
- **Tilly's personality**: Can we capture her charm?
- **Parkour feel**: Does movement feel joyful?
- **Nostalgic aesthetic**: Flash-era whimsy achievable?
- **Emotional impact**: Does it make you smile?

---

## Discovery Process

### Phase 1: Establish Baselines (Current)
- ✅ PyGame: Working prototype
- ⏳ Canvas: Playable, needs testing
- Verify these two feel identical

### Phase 2: Framework Exploration (Next 1-2 weeks)
- 🎯 Phaser.js: Test framework approach
- 🎯 Pico-8: Test constraint-based design
- Compare against baseline

### Phase 3: Engine Evaluation (If needed)
- Godot: Test open-source engine
- Unity: Test professional tooling (if others fall short)

### Phase 4: Decision Point
- Which paradigm best serves the vision?
- Do we need multiple paradigms for different platforms?
- What's the path to "budding" (releasing first version)?

---

## Success Metrics

**A paradigm succeeds when**:
1. ✅ Implements core mechanics (movement, wall jump, bacon)
2. ✅ Shares config with other paradigms
3. ✅ Physics feel identical to baseline
4. ✅ Arrow key controls work universally
5. ✅ Captures whimsical, heartwarming vibe
6. 🎯 Makes tester say "This feels good!"

**The winning paradigm** (or paradigms):
- Best serves Tilly's dream vision
- Sustainable to maintain
- Reaches intended audience
- Brings joy to players

---

## Parallel Development Strategy

### Git Branch Structure
```
main
  ├── experiments/barkour/prototypes/pygame-movement-01/  (PyGame)
  ├── experiments/barkour/web/canvas-01/                  (Canvas)
  ├── experiments/barkour/web/phaser-01/                  (Phaser - planned)
  ├── experiments/barkour/godot/barkour-01/               (Godot - planned)
  └── experiments/barkour/pico8/barkour-01/               (Pico-8 - planned)

All share:
  └── experiments/barkour/shared/
      ├── barkour_config.json
      └── ARCHITECTURE.md
```

### Workflow
1. Make change to shared config
2. Test change in 2+ paradigms
3. Verify physics parity maintained
4. Document findings in paradigm README
5. Commit changes across all paradigms

---

## Notes

**Philosophy**: Barkour is an **idea** that can take many **forms**. The design skeleton ensures the idea stays consistent while we explore which form best expresses it.

**Literate Garden Alignment**: This exploration matches the garden's "make it playable, not perfect" ethos. We're growing multiple plants from the same seed to see which thrives.

**Budget Decision**: Multiple paradigms running in parallel. We'll let the best expression reveal itself through play, not through premature optimization.

---

**Created**: 2025-10-11
**Status**: Exploration in progress
**Current Focus**: Phaser.js and Pico-8 as next branches
