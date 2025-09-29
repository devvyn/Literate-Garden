# Memory Constellation Navigator

**Genre:** Contemplative Puzzle / Narrative Exploration
**Core Loop:** Connect → Rotate → Discover → Understand
**Estimated Scope:** 12-16 weeks with 2-person team
**Created:** 2025-09-29

---

## Concept Overview

Players inherit a celestial archive where memories have been encoded as scattered star fields. To unlock each memory, they must:

1. **Connect nodes** in 3D space using gravitational threads
2. **Rotate their viewpoint** to find the "memory angle"
3. **Align the constellation** to reveal hidden imagery/text
4. **Piece together** narrative fragments into coherent stories

### The Hook

**"What if memories could only be seen from the right angle?"**

Combining constellation-drawing with forced perspective puzzles creates a unique mechanic where the *camera becomes the key*.

---

## Suitability Analysis

### Festival Fit
- ⭐⭐⭐⭐ **IGF Nuovo Award** - Novel perspective-based mechanic
- ⭐⭐⭐⭐ **IndieCade** - Artistic + contemplative design
- ⭐⭐⭐ **Day of the Devs** - Visually distinctive, emotionally resonant

### Audience Appeal
- **Primary:** Fans of Monument Valley, Gorogoa, The Witness
- **Secondary:** Narrative exploration enthusiasts
- **Accessibility:** Low dexterity requirements, adjustable difficulty

### Market Positioning
- **Unique Selling Point:** First game to combine 3D constellation-building with forced perspective narrative
- **Similar Games:** Monument Valley (perspective), Gorogoa (layering), Manifold Garden (impossible spaces)
- **Differentiation:** Adds emotional narrative discovery to spatial puzzles

---

## Technical Feasibility

### Core Systems Required

#### 1. Node Connection System
- **Complexity:** Moderate
- **Tech:** Three.js raycasting for click-to-connect
- **Challenge:** Preventing unwanted connections in dense star fields
- **Solution:** Distance thresholds + visual feedback (glow on hover)

#### 2. 3D Camera Controls
- **Complexity:** Low
- **Tech:** OrbitControls or custom arcball rotation
- **Challenge:** Intuitive control on both mouse and touch
- **Solution:** Smooth interpolation + momentum damping

#### 3. Perspective Detection
- **Complexity:** Moderate
- **Tech:** Calculate angle between camera look vector and target constellation normal
- **Challenge:** Defining "correct" angle tolerance
- **Solution:** Cone-based tolerance (5-10 degrees), visual feedback when approaching

#### 4. Hidden Image Reveal
- **Complexity:** Low-Moderate
- **Tech:** Shader-based alpha blending or texture swap on alignment
- **Challenge:** Creating compelling reveal animations
- **Solution:** Particle effects + fade-in with audio cue

### Technology Stack

**Engine:** Three.js (web) or Godot (standalone)
**Rendering:** WebGL with bloom post-processing for star glow
**Audio:** Spatial audio for connection feedback, ambient soundscape
**Narrative:** JSON-based story fragments with localization support

### Performance Considerations
- **Target:** 60fps on mid-range devices
- **Optimization:** Level of detail (LOD) for distant stars
- **Memory:** ~50-100 nodes per level, instanced geometry
- **Mobile:** Simplified post-processing, reduced particle counts

---

## Gameplay Loop (Single Memory)

1. **Entry:** Player presented with scattered stars and a cryptic hint
2. **Exploration:** Free rotation reveals different patterns
3. **Connection Phase:**
   - Click/tap nodes to draw gravitational threads
   - Visual feedback: threads glow, stars pulse
   - Wrong connections can be undone
4. **Alignment Phase:**
   - Rotate constellation to find the "memory angle"
   - Audio cues intensify as correct angle approaches
   - Visual shimmer effect when close
5. **Revelation:**
   - Hidden image fades in (photo, sketch, symbol)
   - Text fragment appears (diary entry, conversation snippet)
   - Constellation locks and becomes part of the archive
6. **Integration:**
   - New connections to other memories may appear
   - Meta-puzzle: How do memories relate?

---

## Narrative Framework

### Theme: "The Architecture of Memory"

Each constellation represents a moment from the protagonist's past that has been fragmented by trauma, time, or intentional forgetting. The player is an archivist (or the protagonist themselves) reconstructing these memories.

### Story Structure

**Act I: Fragments (Memories 1-5)**
- Simple, isolated memories (childhood, first love, family)
- Teaches core mechanics
- Establishes emotional baseline

**Act II: Connections (Memories 6-12)**
- Memories begin to overlap and contradict
- Meta-puzzle: Some stars belong to multiple constellations
- Introduces unreliable narrator concept

**Act III: Reconstruction (Memories 13-20)**
- Player must choose which version of events to "lock in"
- Branching narrative based on constellation choices
- Revelation of why memories were fragmented

### Emotional Beats
- **Nostalgia** → **Confusion** → **Understanding** → **Acceptance/Grief/Hope**

---

## Prototype Scope (Web Demo)

### Must-Have Features
- [x] 3D star field with 15-20 nodes
- [x] Click-to-connect line drawing
- [x] Free camera rotation (mouse drag)
- [x] Single "correct angle" detection
- [x] Hidden image reveal on alignment
- [x] Basic audio feedback

### Nice-to-Have
- [ ] Particle effects on connection
- [ ] Shader-based bloom/glow
- [ ] Multiple difficulty levels
- [ ] Tutorial overlay

### Explicitly Out of Scope for Demo
- Full narrative integration
- Multiple levels/memories
- Save system
- Mobile touch optimization

---

## Production Roadmap (Full Game)

### Phase 1: Prototype (4 weeks)
- Core mechanics validation
- 3 complete memory puzzles
- Art style proof-of-concept
- Playtest with 20+ users

### Phase 2: Vertical Slice (6 weeks)
- 5 polished memories (Act I complete)
- Final art direction locked
- Audio system implemented
- UI/UX polish

### Phase 3: Production (10 weeks)
- Remaining 15 memories designed and implemented
- Narrative branching system
- Achievement/completion tracking
- Localization preparation

### Phase 4: Polish (4 weeks)
- Performance optimization
- Accessibility features (colorblind mode, difficulty adjust)
- Bug fixing and playtesting
- Festival build preparation

**Total Timeline:** 24 weeks (6 months) with 2-person team
**Budget Estimate:** $30k-50k (if paying team members)

---

## Collaboration Hooks

### For Artists
- **Style Reference:** Volumetric star fields (Interstellar), minimalist UI (Journey)
- **Asset Needs:** Hidden images (15-20 hand-drawn illustrations or photos)
- **Technical Format:** PNG with alpha, 1024x1024px, black and white preferred

### For Writers
- **Narrative Brief:** 20 memory fragments, each 50-150 words
- **Tone:** Introspective, emotionally authentic, avoiding melodrama
- **Structure:** Each memory needs a visual symbol and text component

### For Audio Designers
- **Soundscape:** Ambient space-like tones, minimal but evocative
- **Feedback:** Connection sounds (click, hum), alignment cue (rising tone)
- **Music:** Generative/adaptive system that evolves with progress

### For Programmers
- **Technical Challenges:** Perspective detection algorithm refinement
- **Optimization:** Instanced rendering for 1000+ stars in later levels
- **Feature Requests:** VR support (natural fit for mechanic)

---

## Known Blockers & Open Questions

### Blockers
1. **Narrative Depth vs Accessibility:** Risk of being too obtuse or too obvious
   - *Mitigation:* Extensive playtesting, optional hint system
2. **Camera Control on Mobile:** Touch-based 3D rotation can be awkward
   - *Mitigation:* Gyroscope option, simplified 2.5D mode
3. **Replayability:** Once solved, memories lose their mystery
   - *Mitigation:* Multiple valid solutions? Speedrun mode? Daily challenges?

### Open Questions for Next Iteration
- Should players be able to create their own memory constellations? (UGC potential)
- Could this work in VR for deeper immersion?
- What happens if we invert the mechanic (destroy constellations to forget)?
- Can we add a multiplayer mode (collaborative memory reconstruction)?

---

## Festival Submission Strategy

### Primary Target: IGF Nuovo (October 2025)
- **Submission Package:** 15-minute demo, 3 complete memories
- **Press Kit:** Trailer emphasizing unique perspective mechanic
- **Narrative Hook:** "Monument Valley meets Eternal Sunshine"

### Secondary Targets
- **IndieCade (June 2025):** Night Games track for contemplative design
- **Day of the Devs (November 2025):** Curated showcase opportunity
- **A MAZE. (April 2026):** Experimental games focus

---

## Technical Deep Dive: Perspective Detection Algorithm

```javascript
// COLLAB NOTE: This is the core magic of the game
// Future iterations should refine tolerance and feedback curves

function checkAlignment(camera, constellation) {
    // Calculate camera's look direction
    const lookDir = new THREE.Vector3(0, 0, -1);
    lookDir.applyQuaternion(camera.quaternion);

    // Get constellation's "correct" normal vector
    const targetNormal = constellation.correctViewAngle;

    // Calculate angular difference
    const angle = lookDir.angleTo(targetNormal);
    const angleDegrees = THREE.MathUtils.radToDeg(angle);

    // TUNABLE PARAMETER: Tolerance cone (currently 8 degrees)
    const tolerance = 8.0;

    if (angleDegrees <= tolerance) {
        // Perfect alignment - trigger reveal
        return { aligned: true, proximity: 1.0 };
    } else if (angleDegrees <= tolerance * 2) {
        // Close - provide feedback (audio pitch, visual shimmer)
        const proximity = 1.0 - ((angleDegrees - tolerance) / tolerance);
        return { aligned: false, proximity: proximity };
    } else {
        // Far away
        return { aligned: false, proximity: 0.0 };
    }
}

// FUTURE ENHANCEMENT: Could use more sophisticated alignment scoring
// - Multi-axis constraints (not just angle, but also rotation around axis)
// - Time-based alignment (must hold position for 2 seconds)
// - Partial reveals based on how close you are
```

---

**Status:** Design complete, ready for web prototype implementation
**Next Step:** Build interactive Three.js demo
**Estimated Time:** 4-6 hours for MVP