# Barkour Pico-8 - Playtesting Notes

**Date**: 2025-10-12
**Version**: 0.1.0 (first playtest)

---

## Physics & Movement

### ✅ What Works

**Movement Feel** (after physics adjustments):
- "Movement physics feel pretty decent no complaints here"
- Acceleration/friction feel smooth
- Jump height proportional to 128x128 screen
- Edge boundaries prevent falling off

**Wall Kick Mechanic**:
- "The wall kick is cute and fun"
- Wall slide particle effect well-received ("I liked the cloud that appears")
- Visual feedback clear and satisfying

### Physics Values (Final)
```lua
grav=0.3       -- gentler than PyGame
jump=-6        -- half of PyGame (-12)
spd=2          -- slower for small screen
accel=0.5      -- smooth ramp-up
friction=0.8   -- smooth slow-down
wjump=-7       -- wall jump strength
wpush=4        -- wall jump push
```

**Verdict**: ✅ Core mechanics work in Pico-8's constraints

---

## Level Design Feedback

### 🎯 Key Request

**"It's now the levels that I'm more interested in exploring"**

**Specific needs**:
1. **More variation** - Current single-screen level too simple
2. **Sense of progress** - Need progression/advancement feeling
3. **Exploration** - Want to discover/explore spaces

### Current Limitations

**Single Screen Level**:
- 5 platforms
- 3 walls
- 3 bacon pieces
- No vertical/horizontal progression
- No secrets or discovery
- No sense of "going somewhere"

**Missing Elements**:
- Multiple connected screens/rooms
- Vertical progression (climb upward toward goal)
- Hidden bacon pieces (reward exploration)
- Environmental variety (different platform layouts)
- Difficulty progression (easy → challenging)
- Visual landmarks (know where you are)

---

## Next Steps: Level Design Exploration

### Option 1: Vertical Tower (Recommended)

**Concept**: Climb a tall tower (multiple screens high)

**Structure**:
```
Screen 4: ☁️ CLOUDS (final goal)
   ↑
Screen 3: 🏰 High platforms
   ↑
Screen 2: 🧱 Wall jump gauntlet
   ↑
Screen 1: 🌱 Ground (tutorial area)
```

**Implementation**:
- Camera follows player (Pico-8 `camera()` function)
- Map is taller than 128px (e.g., 128x512)
- Use Pico-8 map editor to design rooms
- Bacon pieces at key challenge points
- Top = "you reached the clouds!" victory

**Why this works**:
- ✅ Clear progression (upward = progress)
- ✅ Variation (each screen different layout)
- ✅ Exploration (side paths for bacon)
- ✅ Matches vision ("ground → rooftops → clouds")

### Option 2: Horizontal Scrolling

**Concept**: Side-scrolling level (left to right)

**Structure**:
```
[Start] → [Easy jumps] → [Wall kick section] → [Bacon hunt] → [Goal]
```

**Why this works**:
- ✅ Classic platformer progression
- ✅ Can add secrets above/below main path
- ✅ Room for environmental variety

### Option 3: Open World (Advanced)

**Concept**: Interconnected rooms, Metroidvania-style

**Why defer this**:
- Complex for first Pico-8 experiment
- Better after establishing core level feel
- Save for if Pico-8 becomes primary paradigm

---

## Pico-8 Level Design Tools

### Map Editor

**Access**: ESC to cycle modes → Map editor (grid icon)

**Features**:
- 128x64 tile map (8x8 tiles)
- Can design multiple screens
- Copy/paste sections
- Visual level design

### Camera System

**Code**:
```lua
-- Follow player vertically
camera(0, max(0, p.y - 64))

-- Or horizontally
camera(max(0, p.x - 64), 0)
```

### Map Collision

**Read tiles for collision**:
```lua
function solid(x,y)
  local tile=mget(x/8, y/8)
  return tile==1 or tile==2  -- tiles 1,2 are solid
end
```

---

## Recommended Next Implementation

### Phase 1: Vertical Tower Prototype (2-3 hours)

**Goal**: Prove vertical progression works in Pico-8

**Tasks**:
1. Design 4-screen vertical tower in map editor
2. Implement camera following
3. Place bacon strategically (reward wall kicks)
4. Add "victory" at top (cloud sprite?)
5. Test progression feel

**Success Criteria**:
- Feels like progressing upward
- Bacon placement encourages exploration
- Victory moment satisfying
- Want to replay for faster time

### Phase 2: Polish & Variety (1-2 hours)

**Add**:
- Different platform arrangements per screen
- 1-2 "hidden" bacon pieces (side paths)
- Simple background parallax (clouds moving)
- Victory fanfare (Pico-8 music)
- Timer (speedrun element)

---

## Design Questions for Next Session

1. **Progression Style**:
   - Linear climb (one path up)?
   - Branching paths (choose route)?
   - Secrets/optional challenges?

2. **Difficulty Curve**:
   - Start easy (tutorial jumps)?
   - End hard (wall kick gauntlet)?
   - Bacon as difficulty gates?

3. **Victory Condition**:
   - Reach the top?
   - Collect all bacon?
   - Time trial?

4. **Environmental Theme**:
   - Ground → buildings → rooftops → clouds?
   - Single tower aesthetic?
   - Color palette shifts per screen?

---

## Pico-8 Paradigm Evaluation

### ✅ Confirmed Strengths

1. **Physics translate well** - Proportional scaling works
2. **Aesthetic matches vision** - Retro, whimsical feel
3. **Particle effects charming** - Wall slide clouds work
4. **Constraints are productive** - Forces focused design

### 🎯 Next to Validate

1. **Level design in 128x128** - Can we create compelling progression?
2. **Map editor workflow** - Does visual design speed up iteration?
3. **Multi-screen feel** - Does camera following work well?
4. **Replayability** - Do small levels encourage speedruns?

### Decision Point

**After level prototype**:
- If level design works → Pico-8 strong candidate for primary paradigm
- If too constrained → Consider Phaser/Godot for bigger levels
- Both can coexist → Pico-8 for "arcade mode", other for "story mode"

---

## Feedback Collection Template

**For next playtest session**:

1. **Progression Feel** (1-5): Do you feel like you're advancing?
2. **Exploration Reward** (1-5): Is finding bacon satisfying?
3. **Difficulty Curve** (1-5): Does it ramp up nicely?
4. **Victory Moment** (1-5): Does reaching the top feel good?
5. **Replay Desire** (1-5): Want to try again for better time?

**Open questions**:
- What was your favorite moment?
- What felt frustrating?
- What would you add/change?

---

**Next Session**: Build vertical tower level, test progression feel

**Created**: 2025-10-12
**Updated**: 2025-10-12
