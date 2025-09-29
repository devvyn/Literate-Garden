# Recursive Garden Architect

**Genre:** Zen Builder / Fractal Exploration
**Core Loop:** Plant → Zoom → Observe → Prune → Discover
**Estimated Scope:** 14-18 weeks with 3-person team
**Created:** 2025-09-29

---

## Concept Overview

Players tend a garden where **every plant is a microcosm** of the whole garden. Zoom into any flower and discover an entire miniature garden within its petals. The game explores self-similarity, emergence, and the meditative practice of tending to systems that echo themselves infinitely.

### The Hook

**"What if every flower contained the entire garden, and every garden fit inside a flower?"**

By making players custodians of a fractal ecosystem, we create a unique gameplay loop where:
- Local actions have global consequences
- Pattern recognition becomes survival
- Zooming becomes exploration
- Simplicity generates complexity

---

## Suitability Analysis

### Festival Fit
- ⭐⭐⭐⭐ **IGF Nuovo** - Mathematical elegance meets accessible gameplay
- ⭐⭐⭐⭐ **A MAZE.** - Experimental mechanics with artistic depth
- ⭐⭐⭐ **IndieCade** - Meditative design, educational potential

### Audience Appeal
- **Primary:** Fans of Opus Magnum, Townscaper, Islanders, Mini Metro
- **Secondary:** Math/fractals enthusiasts, meditation game players
- **Educational:** Strong potential for STEM education (fractal geometry, systems thinking)

### Market Positioning
- **USP:** First game to make fractals directly interactive and playable
- **Similar:** Cloud Gardens (zen building), Everything (scale jumping), Manifold Garden (impossible geometry)
- **Differentiation:** Recursive depth isn't just visual—it's mechanically meaningful

---

## Technical Feasibility

### Core Systems Required

#### 1. Fractal Generation Engine
- **Complexity:** High
- **Tech:** L-systems or IFS (Iterated Function Systems) for plant generation
- **Challenge:** Real-time generation at multiple depth levels without lag
- **Solution:** Procedural generation with LOD, cache common patterns

#### 2. Infinite Zoom Interface
- **Complexity:** Moderate
- **Tech:** Logarithmic camera scaling, dynamic asset loading
- **Challenge:** Smooth transitions between scales without jarring jumps
- **Solution:** Interpolated zoom with particle effects masking load times

#### 3. Recursive State Management
- **Complexity:** High
- **Tech:** Tree data structure where each node contains entire subtree
- **Challenge:** Changes propagate both up and down the hierarchy
- **Solution:** Event system with "dirty flags" for selective updates

#### 4. Pattern Evolution System
- **Complexity:** Moderate
- **Tech:** Cellular automata or reaction-diffusion for organic growth
- **Challenge:** Keeping patterns interesting without becoming chaotic
- **Solution:** Designer-tuned rulesets with player-adjustable parameters

### Technology Stack

**Engine:** Unity (C#) or Godot (GDScript) for recursive systems
**Rendering:** Instanced rendering for thousands of plants
**Shaders:** Custom shaders for fractal detail and bloom
**Audio:** Generative music that scales with zoom level (Brian Eno-inspired)

### Performance Considerations
- **Target:** 60fps on mid-range devices
- **Optimization:**
  - Only render 3-4 depth levels at once
  - Use impostors (billboards) for distant/shallow recursion
  - Lazy evaluation: don't compute hidden branches
- **Memory:** ~200MB for full garden state

---

## Gameplay Loop

### Macro Level (Full Garden View)
1. **Survey:** See overall garden health and balance
2. **Identify:** Spot overgrown or dying regions
3. **Navigate:** Choose a plant to zoom into

### Micro Level (Inside a Plant)
4. **Tend:** Plant new seeds, water, prune unwanted growth
5. **Observe:** Watch how changes affect the mini-garden within
6. **Recurse:** Zoom even deeper (gardens within gardens within gardens)

### Emergence
7. **Cascade:** Changes at micro level propagate to macro
8. **Discover:** Unexpected patterns emerge from simple rules
9. **Balance:** Find sustainable equilibrium across all scales

### Challenge Modes
- **Survival:** Keep garden alive against entropy/disease
- **Puzzle:** Achieve specific fractal patterns
- **Sandbox:** Pure creative expression, no failure state
- **Speedrun:** Reach certain patterns in minimal time

---

## Narrative Framework

### Theme: "As Above, So Below"

The game is framed as an ancient gardening practice where monks tended sacred fractal gardens to contemplate infinity, interconnection, and the nature of self-similarity in the universe.

### Story Structure (Optional Campaign Mode)

**Act I: The Seed**
- Tutorial: Plant your first garden, learn basic tending
- Philosophy: "From one seed, infinite gardens grow"

**Act II: The Pattern**
- Challenges: Maintain specific fractal dimensions
- Philosophy: "What you do to the smallest affects the largest"

**Act III: The Equilibrium**
- Master Challenge: Create a self-sustaining fractal ecosystem
- Philosophy: "True harmony exists at every scale"

### Meditative Mode
- No win/loss conditions
- Ambient music and sound
- Minimal UI
- Pure contemplative garden tending

---

## Prototype Scope (Web Demo)

### Must-Have Features
- [x] 2-3 depth levels of recursion
- [x] Smooth zoom animation between levels
- [x] Plant/remove flora at any level
- [x] Visual indication of fractal self-similarity
- [x] Basic L-system plant generation

### Nice-to-Have
- [ ] 5+ depth levels
- [ ] Multiple plant species with different fractal rules
- [ ] Audio that changes with zoom level
- [ ] Save/load garden states

### Explicitly Out of Scope for Demo
- Full campaign/puzzle mode
- Advanced shaders and particle effects
- Mobile touch optimization
- Multiplayer/shared gardens

---

## Production Roadmap

### Phase 1: Prototype (6 weeks)
- Fractal generation engine
- Infinite zoom mechanic
- Basic plant placement
- 3 depth levels functional

### Phase 2: Vertical Slice (8 weeks)
- 5 depth levels
- Multiple plant types
- Audio system
- Tutorial sequence
- First 5 puzzle challenges

### Phase 3: Content (8 weeks)
- 20 puzzle challenges
- Sandbox mode polish
- All plant species
- Meditation mode

### Phase 4: Polish (4 weeks)
- Performance optimization
- UI/UX refinement
- Accessibility features
- Platform-specific builds

**Total Timeline:** 26 weeks (6.5 months) with 3-person team
**Budget Estimate:** $40k-60k

---

## Collaboration Hooks

### For Mathematicians/Fractal Artists
- **Consultation Needed:** Aesthetically pleasing L-system rulesets
- **References:** Mandelbrot Set, Julia Sets, Romanesco broccoli
- **Tools:** L-Studio or Structure Synth for rule design

### For Audio Designers
- **Concept:** Music that scales with zoom (deeper = lower frequencies?)
- **Generative:** Algorithm that creates infinite ambient soundscape
- **Reference:** Brian Eno's "Music for Airports", Disasterpeace's "Fez"

### For UI/UX Designers
- **Challenge:** How to indicate current recursion depth?
- **Challenge:** How to make zoom intuitive on keyboard, mouse, AND touch?
- **Inspiration:** Google Earth zoom, PowerPoint's zoom feature

### For Game Designers
- **Open Question:** How to create meaningful puzzles from fractal rules?
- **Open Question:** Should time pass differently at different scales?
- **Open Question:** Multiplayer possibilities? (shared fractal gardens)

---

## Known Blockers & Open Questions

### Blockers
1. **Performance:** Recursive systems are computationally expensive
   - *Mitigation:* Aggressive LOD, only compute visible branches
2. **Cognitive Load:** Infinite recursion can be overwhelming
   - *Mitigation:* Limit initial depth to 3, unlock deeper levels gradually
3. **Tutorial:** How to teach fractal concepts without math jargon?
   - *Mitigation:* Show, don't tell—let players discover patterns

### Open Questions
- **Failure States:** Should gardens ever "die"? Or is this pure sandbox?
- **Progression:** What unlocks? New plant types? Deeper recursion?
- **Accessibility:** How do colorblind players distinguish plant types?
- **VR Potential:** Would this be transformative in VR?

### COLLABORATION NOTE: Paused Development
**Reason:** Need to validate fractal generation performance before full prototype
**Next Steps:**
1. Build stress test with 10,000 instances
2. Measure frame times on target hardware
3. If <60fps, simplify plant models or reduce depth

---

## Technical Deep Dive: L-System Implementation

```javascript
// COLLAB NOTE: Simplified L-system for fractal plant generation
// This is a Lindenmayer system—string rewriting for organic growth

class LSystem {
    constructor(axiom, rules, depth) {
        this.axiom = axiom;      // Starting symbol (e.g., "F")
        this.rules = rules;      // Rewrite rules (e.g., F -> "FF+[+F-F-F]-[-F+F+F]")
        this.depth = depth;      // Recursion depth
    }

    generate() {
        let result = this.axiom;

        // Apply rules 'depth' times
        for (let i = 0; i < this.depth; i++) {
            result = this.applyRules(result);
        }

        return result;
    }

    applyRules(input) {
        let output = "";
        for (let char of input) {
            // Replace each symbol according to rules
            output += this.rules[char] || char;
        }
        return output;
    }

    // COLLAB NOTE: Convert L-system string to 3D geometry
    // F = move forward and draw
    // + = rotate right
    // - = rotate left
    // [ = push state (branch)
    // ] = pop state (return from branch)
    toGeometry(string) {
        let position = { x: 0, y: 0 };
        let angle = 90; // Start facing up
        let stack = [];
        let lines = [];

        const angleIncrement = 25; // degrees
        const stepLength = 1;

        for (let char of string) {
            switch(char) {
                case 'F':
                    // Move forward and draw line
                    const newX = position.x + Math.cos(angle * Math.PI / 180) * stepLength;
                    const newY = position.y + Math.sin(angle * Math.PI / 180) * stepLength;
                    lines.push([
                        { x: position.x, y: position.y },
                        { x: newX, y: newY }
                    ]);
                    position = { x: newX, y: newY };
                    break;
                case '+':
                    angle += angleIncrement;
                    break;
                case '-':
                    angle -= angleIncrement;
                    break;
                case '[':
                    // Save current state before branching
                    stack.push({ pos: {...position}, ang: angle });
                    break;
                case ']':
                    // Restore state after branch
                    const state = stack.pop();
                    position = state.pos;
                    angle = state.ang;
                    break;
            }
        }

        return lines;
    }
}

// Example: Simple fractal tree
const tree = new LSystem(
    "F",                                      // Axiom (start)
    {
        "F": "FF+[+F-F-F]-[-F+F+F]"          // Rule (branch + recurse)
    },
    3                                         // Depth (iterations)
);

// FUTURE ENHANCEMENT: Add parameters for:
// - Stochastic rules (randomness in growth)
// - Context-sensitive rules (F depends on neighbors)
// - Parametric rules (F(1.5) for variable lengths)
```

---

## Festival Submission Strategy

### Primary Target: IGF Nuovo (October 2025)
- **Submission Package:** 20-minute demo, 3 puzzle levels + sandbox
- **Press Kit:** GIF showing infinite zoom reveal
- **Pitch:** "M.C. Escher meets Zen garden simulator"

### Secondary Targets
- **A MAZE. (April 2026):** Experimental games showcase
- **IndieCade (June 2026):** Innovation in Game Design
- **Ars Electronica (September 2026):** Prix Ars category (digital art)

---

**Status:** Design complete, web prototype requires L-system implementation
**Next Step:** Build simplified 2D fractal garden demo
**Estimated Time:** 6-8 hours for MVP
**Blocker:** Performance validation needed before committing to full 3D