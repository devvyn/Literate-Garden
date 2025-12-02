# Tidal Echo Composer

**Genre:** Rhythmic Puzzle / Environmental Music Game
**Core Loop:** Observe → Manipulate → Listen → Compose → Discover
**Estimated Scope:** 16-20 weeks with 3-person team
**Created:** 2025-09-29

---

## Concept Overview

Players inherit a mysterious coastal archive where ancient songs have been carved into tidal rocks. As water levels rise and fall, different musical phrases become exposed or submerged. By controlling tidal forces (moon phase, weather, time acceleration), players compose multi-layered soundscapes and unlock hidden narratives about a lost maritime culture.

### The Hook

**"What if the tide was an instrument, and the coastline your score?"**

This game uniquely combines:
- **Environmental puzzle-solving** (manipulate natural systems)
- **Music composition** (layer revealed melodies)
- **Narrative archaeology** (discover story through songs)
- **Rhythmic timing** (tidal cycles create musical tempo)

---

## Suitability Analysis

### Festival Fit
- ⭐⭐⭐⭐⭐ **IGF Excellence in Audio** - Core mechanic is auditory
- ⭐⭐⭐⭐ **IndieCade** - Novel intersection of music + environment
- ⭐⭐⭐⭐ **A MAZE.** - Experimental systems-based gameplay

### Audience Appeal
- **Primary:** Fans of Sayonara Wild Hearts, Incredibox, Sound Shapes, Gris
- **Secondary:** Puzzle game enthusiasts, world-building explorers
- **Educational:** Music theory, oceanography, archaeology

### Market Positioning
- **USP:** First game to make tidal simulation a music-composition tool
- **Similar:** Auditorium (audio puzzles), GRIS (music + environment), Unpacking (narrative discovery)
- **Differentiation:** Systemic music generation from physical simulation

---

## Technical Feasibility

### Core Systems Required

#### 1. Tidal Simulation
- **Complexity:** Moderate
- **Tech:** Sin wave-based water level simulation with multiple influencing factors
- **Challenge:** Making it intuitive yet scientifically satisfying
- **Solution:** Simplified model—moon phase + weather + time modifiers

#### 2. Dynamic Music System
- **Complexity:** High
- **Tech:** Layered audio stems that activate based on water level thresholds
- **Challenge:** Smooth transitions between musical states
- **Challenge:** Preventing cacophony when too many layers active
- **Solution:** Harmonic locking (ensure compatible keys), volume ducking

#### 3. Rock Revelation Mechanic
- **Complexity:** Moderate
- **Tech:** Shader-based water masking reveals carved symbols/notation
- **Challenge:** Readability of partially-submerged glyphs
- **Solution:** Glowing highlights on revealed sections, particle effects

#### 4. Time Manipulation UI
- **Complexity:** Low
- **Tech:** Time slider affecting simulation speed (1x to 100x)
- **Challenge:** Preventing disorientation during fast-forward
- **Solution:** Visual ripple effects, audio pitch-shifting for feedback

### Technology Stack

**Engine:** Unity with FMOD audio middleware (or Godot + custom audio)
**Rendering:** 2.5D with parallax water layers
**Shaders:** Water caustics, refraction, foam
**Audio:** Stem-based system (16-24 tracks), procedural ambience

### Performance Considerations
- **Target:** 60fps on mid-range devices
- **Audio Latency:** <10ms for responsive feedback
- **Memory:** ~150MB for all audio stems (compressed)
- **Mobile:** Simplified shaders, reduce parallax layers

---

## Gameplay Loop

### Discovery Phase
1. **Arrive at new coastal section**
2. **Observe tidal patterns** and visible rock formations
3. **Listen** to ambient sounds (waves, wind, partial melodies)

### Manipulation Phase
4. **Adjust tidal controls:**
   - Moon phase (new → full: low → high baseline tide)
   - Weather (storm → calm: waves → stillness)
   - Time of day (affects ambient lighting and some tide heights)
   - Time acceleration (1x → 100x: explore patterns quickly)

### Composition Phase
5. **Find harmonic sweet spots:**
   - Specific tide levels reveal certain rock carvings
   - Each carving plays a musical phrase when exposed
   - Goal: Find combinations that create beautiful compositions

### Resolution Phase
6. **Record your composition** (optional)
7. **Unlock narrative fragment** when puzzle "solved"
8. **Progress to next coastal section**

### Meta-Game
- **Archive:** All unlocked songs can be replayed/remixed
- **Secrets:** Hidden rocks only revealed at extreme tides
- **Community:** Share your compositions (export as audio file)

---

## Narrative Framework

### Theme: "Songs the Sea Remembers"

An ancient coastal civilization encoded their history, myths, and knowledge into rock carvings designed to be revealed by specific tidal conditions. You play as an archaeologist-musician reconstructing their lost culture through song.

### Story Structure

**Prologue: The First Tide**
- Tutorial: Learn basic tidal controls
- Discovery: First simple 2-layer melody
- Hook: "If this rock holds a song, what secrets lie in the others?"

**Act I: Fragments (Sections 1-5)**
- Simple puzzles, 2-3 musical layers
- Themes: Daily life, work songs, children's rhymes
- Emotional tone: Curious, nostalgic

**Act II: Depths (Sections 6-10)**
- Complex puzzles, 4-6 musical layers
- Themes: Love, loss, warnings, prophecies
- Emotional tone: Melancholic, urgent

**Act III: Storm (Sections 11-15)**
- Extreme tidal manipulation required
- Themes: Disaster, exodus, hope
- Emotional tone: Dramatic, cathartic

**Epilogue: The Final Song**
- All sections' melodies can be interwoven
- Player creates ultimate composition
- Revelation: Why the civilization disappeared
- Multiple endings based on compositional choices?

---

## Prototype Scope (Web Demo)

### Must-Have Features
- [x] Tidal simulation with adjustable parameters (moon, time)
- [x] 3-5 rock carvings that reveal/hide with water level
- [x] Each rock plays distinct musical loop when exposed
- [x] Visual water that rises/falls
- [x] Time acceleration slider

### Nice-to-Have
- [ ] Weather system affecting tide
- [ ] Particle effects (foam, spray)
- [ ] Save/replay compositions
- [ ] Multiple coastal sections

### Explicitly Out of Scope for Demo
- Full campaign (15 sections)
- High-fidelity audio stems
- Complex shader water rendering
- Narrative text integration

---

## Production Roadmap

### Phase 1: Prototype (6 weeks)
- Core tidal simulation
- Basic music layering system
- 2 coastal sections functional
- Art style proof-of-concept

### Phase 2: Vertical Slice (8 weeks)
- 5 complete coastal sections
- Refined audio stems (collaborate with composer)
- Narrative integration
- UI/UX polish

### Phase 3: Content Production (10 weeks)
- Remaining 10 coastal sections
- Full musical score composed
- All narrative fragments written
- Achievement system

### Phase 4: Polish (4 weeks)
- Performance optimization
- Accessibility (visual metronome for hearing-impaired)
- Localization preparation
- Festival build

**Total Timeline:** 28 weeks (7 months) with 3-person team
**Budget Estimate:** $50k-70k (includes professional composer)

---

## Collaboration Hooks

### For Composers
- **Brief:** 15 interconnected musical themes (shared motifs)
- **Style:** Ambient, organic, evocative of ocean and ancient mystery
- **Tech Requirements:** Deliver as stems (melody, harmony, bass, percussion separate)
- **Reference:** Austin Wintory's "ABZÛ", Darren Korb's "Transistor"

### For Audio Programmers
- **Challenge:** Real-time stem mixing without clicks/pops
- **Challenge:** Smooth crossfades as rocks revealed/hidden
- **Solution:** FMOD Studio or Wwise for state-based music
- **Stretch Goal:** Procedural wave sounds (synthesized, not samples)

### For Narrative Designers
- **Task:** 15 short stories/poems encoded in rock carvings
- **Constraint:** Each must work independently AND as part of larger arc
- **Format:** 50-150 words per fragment, evocative language
- **Theme:** Lost maritime culture, emphasis on music as memory

### For Visual Artists
- **Art Direction:** Stylized realism—not photorealistic but grounded
- **Key Assets:** Rock formations (with carved glyphs), dynamic water, sky gradients
- **Animation:** Subtle: waves, light caustics, glowing glyphs
- **Color Palette:** Blues, greens, sunset oranges, bioluminescent accents

---

## Known Blockers & Open Questions

### Blockers
1. **Audio Licensing:** Need original music (samples too expensive)
   - *Mitigation:* Budget for composer, or use Creative Commons with attribution
2. **Tidal Realism vs. Playability:** Real tides are slow and complex
   - *Mitigation:* Embrace abstraction, prioritize feel over accuracy
3. **Puzzle Difficulty:** How to guide players without being prescriptive?
   - *Mitigation:* Visual hints (glows), optional tutorial mode

### Open Questions
- **Save System:** Should players save compositions mid-puzzle?
- **Social Features:** Online sharing of compositions via audio export?
- **VR Potential:** Would standing on shore in VR enhance immersion?
- **Accessibility:** How to make music puzzles work for deaf players?
  - *Idea:* Visual waveform representations, vibration patterns

### COLLABORATION NOTE: Stalling Point
**Blocker:** Need to prototype audio stem layering before committing to full production
**Next Steps:**
1. Create test scene with 4 audio stems
2. Implement crossfade system
3. Verify no performance issues with 10+ simultaneous tracks
4. If successful, proceed to full prototype

**Estimated Resolution Time:** 1-2 days for audio tech validation

---

## Technical Deep Dive: Tidal Simulation Algorithm

```javascript
// COLLAB NOTE: Simplified tidal model for gameplay purposes
// Not scientifically accurate, but feels right

class TidalSimulator {
    constructor() {
        this.baseLevel = 0.5;     // 0 = low tide, 1 = high tide
        this.moonPhase = 0.5;     // 0 = new moon, 1 = full moon
        this.weatherFactor = 0.5; // 0 = storm, 1 = calm
        this.timeOfDay = 0;       // 0-24 hours
        this.timeSpeed = 1;       // Simulation speed multiplier
    }

    // COLLAB NOTE: Calculate current tide level
    // Combines multiple sinusoidal waves for complexity
    getTideLevel() {
        // Primary tidal cycle (12.42 hour period, influenced by moon)
        const primaryTide = Math.sin(this.timeOfDay * Math.PI / 6.21);

        // Secondary tidal cycle (longer period for spring/neap tides)
        const secondaryTide = Math.sin(this.timeOfDay * Math.PI / 24);

        // Moon phase influence (full moon = higher highs and lower lows)
        const moonInfluence = this.moonPhase * 0.3;

        // Weather influence (storm = more chaotic, calm = smoother)
        const weatherChaos = (1 - this.weatherFactor) *
                            Math.sin(this.timeOfDay * Math.PI * 3) * 0.1;

        // Combine all factors
        let tideLevel = this.baseLevel +
                       (primaryTide * 0.3) +
                       (secondaryTide * 0.1) +
                       (primaryTide * moonInfluence) +
                       weatherChaos;

        // Clamp to valid range
        return Math.max(0, Math.min(1, tideLevel));
    }

    // COLLAB NOTE: Update simulation (called each frame)
    update(deltaTime) {
        // Advance time based on speed multiplier
        this.timeOfDay += (deltaTime / 1000) * this.timeSpeed;

        // Wrap time to 24-hour cycle
        if (this.timeOfDay >= 24) {
            this.timeOfDay -= 24;
        }
    }

    // COLLAB NOTE: Player controls
    setMoonPhase(phase) {
        this.moonPhase = Math.max(0, Math.min(1, phase));
    }

    setWeather(factor) {
        this.weatherFactor = Math.max(0, Math.min(1, factor));
    }

    setTimeSpeed(speed) {
        this.timeSpeed = speed;
    }
}

// FUTURE ENHANCEMENT: Add seasonal variation, wind direction, etc.
```

---

## Festival Submission Strategy

### Primary Target: IGF Excellence in Audio (October 2025)
- **Submission Package:** 30-minute demo, 3 complete coastal sections
- **Emphasis:** Novel music composition mechanic, audio as core gameplay
- **Press Kit:** Video showing tidal manipulation → music creation

### Secondary Targets
- **IndieCade (June 2026):** Innovation in Game Design
- **A MAZE. (April 2026):** Experimental Games Showcase
- **SXSW Gaming (March 2026):** Indie Game Competition

---

**Status:** Design complete, audio tech validation required before prototype
**Next Step:** Build simplified web demo with placeholder audio
**Estimated Time:** 8-10 hours for functional MVP
**Critical Path:** Secure composer collaboration before full production