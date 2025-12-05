# Barkour - Pico-8 Paradigm

**Interface Paradigm**: Retro fantasy console
**Status**: 🌱 Just planted
**Created**: 2025-10-11

---

## Why Pico-8?

From GAME_VISION.md:
> "Nostalgic Flash-era aesthetic... whimsical, heartwarming, slightly absurd"

**Pico-8's constraints might be perfect for capturing this:**
- 128x128 pixel display → Forces charming simplicity
- 16-color palette → Nostalgic, retro feel
- Built-in sprite editor → Fast iteration on Tilly's animations
- Cart file format → Easy to share and play
- Constraint-based design → Creativity through limitation

---

## Installation

### Option 1: Buy Pico-8 ($15)
**Recommended** - Supports creator Zep, includes full IDE

1. Go to https://www.lexaloffle.com/pico-8.php
2. Purchase license ($15)
3. Download for macOS
4. Install to `/Applications/PICO-8.app`
5. Run from terminal: `/Applications/PICO-8.app/Contents/MacOS/pico8`
6. Or create alias: `alias pico8='/Applications/PICO-8.app/Contents/MacOS/pico8'`

### Option 2: Education License
Free for educators/students: https://www.lexaloffle.com/pico-8.php?page=schools

### What You Get
- Fantasy console IDE (code, sprites, maps, music, sfx)
- Export to HTML/binary
- Built-in BBS for sharing carts
- Huge community and examples
- Excellent documentation

---

## Quick Start

```bash
# Launch Pico-8
pico8

# In Pico-8, load the cart
> LOAD BARKOUR.P8

# Run the cart
> RUN

# Edit code/sprites
> [ESC] to switch modes

# Save changes
> SAVE
```

---

## Design Constraints → Creative Opportunities

### Display: 128x128 pixels
**Challenge**: Small viewport
**Opportunity**: Focus on tight, focused levels
**Barkour**: Vertical platforming in compact spaces

### Colors: 16 fixed colors
**Challenge**: Limited palette
**Opportunity**: Strong visual identity, forced cohesion
**Barkour Colors** (from GAME_VISION):
- Tilly beige → Pico-8 color 4 (brownish)
- Tilly muzzle → Pico-8 color 0 (black)
- Bacon pink → Pico-8 color 14 (pink)
- Sky blue → Pico-8 color 12 (light blue)
- Ground brown → Pico-8 color 4 (brown)

### Sprites: 8x8 pixels, 256 total
**Challenge**: Tiny sprite resolution
**Opportunity**: Charming pixel art aesthetic
**Barkour Sprites**:
- Tilly: 8x8 (perfect for 128x128 world)
- Bacon: 4x4 (cute and tiny)
- Platforms: 8x8 tiles
- Walls: 8x8 tiles

### Sound: 4 channels, 64 sounds
**Challenge**: Limited music/sfx
**Opportunity**: Every sound meaningful
**Barkour Sounds** (planned):
- Bacon collect (happy chime)
- Jump (soft boop)
- Wall jump (satisfying thunk)
- Power-up activation (fanfare)
- Background music (whimsical tune)

### Code: 8192 tokens
**Challenge**: Limited code space
**Opportunity**: Forces elegant solutions
**Barkour**: Core mechanics only, no bloat

---

## Shared Config → Pico-8 Translation

### Physics Parameters

**Shared Config** → **Pico-8 Equivalent**:
```
gravity: 0.5              → grav=0.5
base_jump_strength: -12   → jump=-12
base_movement_speed: 5    → spd=5
wall_slide_speed: 2       → wslide=2
wall_jump_push: 8         → wpush=8
wall_jump_strength: -13   → wjump=-13
```

### World Scaling

**Shared config uses 800x600 world**
**Pico-8 uses 128x128 display**

**Scale factor: 128/800 = 0.16** (roughly 1/6th size)

**Translation**:
- Player (40x40) → 6x6 pixels in Pico-8
- Bacon (30x20) → 5x3 pixels (round to 8x8 sprite for visibility)
- Platforms scale down proportionally

**Alternative**: Don't scale - design new level layouts for 128x128

---

## Pico-8 Specific Features to Leverage

### 1. Sprite Animation
**Built-in frame animation**:
```lua
-- Tilly idle: sprites 1-2
-- Tilly run: sprites 3-6
-- Tilly jump: sprite 7
-- Tilly wall slide: sprite 8
```

### 2. Map Editor
**128x64 tile map**:
- Design levels visually in map editor
- Read tiles at runtime for collision
- Fast iteration on level design

### 3. Particle System
```lua
-- Wall slide particles
add_particle(x,y,dx,dy,color,life)
```

### 4. Camera System
```lua
-- Follow player (if level > 128x128)
camera(player.x-64, player.y-64)
```

### 5. Persistent Data
```lua
-- High scores, unlocked levels
cartdata("barkour_v1")
dset(0, score)
```

---

## Development Workflow

### Phase 1: Core Mechanics (2-3 hours)
1. ✅ Set up cart structure
2. [ ] Draw Tilly sprite (8x8)
3. [ ] Implement player movement (arrow keys)
4. [ ] Add gravity and jumping
5. [ ] Test if it "feels good"

### Phase 2: Wall Jumps (1-2 hours)
6. [ ] Detect wall collision
7. [ ] Wall slide physics
8. [ ] Wall jump input
9. [ ] Compare feel to PyGame version

### Phase 3: Bacon Power (1 hour)
10. [ ] Draw bacon sprite
11. [ ] Collection detection
12. [ ] 5-second power-up timer
13. [ ] Speed/jump multipliers

### Phase 4: Polish (2-3 hours)
14. [ ] Add sound effects
15. [ ] Particle effects
16. [ ] Background music
17. [ ] Level design in map editor

### Evaluation (30 min)
18. [ ] Does it capture Tilly's charm?
19. [ ] Does movement feel joyful?
20. [ ] Is the aesthetic right?
21. [ ] Decision: continue or pivot?

---

## Code Structure Template

```lua
-- barkour.p8
-- bacon-powered parkour!

-- === init ===
function _init()
  -- player state
  p={
    x=64,y=64,      -- position
    dx=0,dy=0,      -- velocity
    w=6,h=6,        -- size
    grounded=false,
    wall=nil,       -- "l"/"r"/nil
    powered=false,
    ptimer=0        -- power timer
  }

  -- config (from shared)
  grav=0.5
  jump=-12
  spd=5
  wslide=2
  wpush=8
  wjump=-13

  -- bacon
  bacon={
    {x=40,y=80},
    {x=90,y=60}
  }
end

-- === update (60fps) ===
function _update()
  -- input
  local moving=false
  if btn(⬅️) then
    p.dx=-spd
    moving=true
  end
  if btn(➡️) then
    p.dx=spd
    moving=true
  end
  if not moving then
    p.dx=0
  end

  -- gravity
  if p.wall and p.dy>0 then
    -- wall slide
    p.dy=min(p.dy+grav,wslide)
  else
    p.dy+=grav
  end

  -- jump
  if btnp(❎) or btnp(⬆️) then
    if p.grounded then
      -- ground jump
      p.dy=jump
    elseif p.wall then
      -- wall jump
      p.dx=p.wall=="l" and wpush or -wpush
      p.dy=wjump
      p.wall=nil
    end
  end

  -- move
  p.x+=p.dx
  p.y+=p.dy

  -- collision (simplified)
  -- todo: real collision with map

  -- bacon collection
  for b in all(bacon) do
    if not b.collected then
      if abs(p.x-b.x)<8 and abs(p.y-b.y)<8 then
        b.collected=true
        p.powered=true
        p.ptimer=300 -- 5 sec * 60 fps
        sfx(0) -- bacon sound
      end
    end
  end

  -- power-up timer
  if p.powered then
    p.ptimer-=1
    if p.ptimer<=0 then
      p.powered=false
    end
  end
end

-- === draw ===
function _draw()
  cls(12) -- sky blue

  -- todo: draw map

  -- bacon
  for b in all(bacon) do
    if not b.collected then
      spr(2,b.x,b.y) -- bacon sprite
    end
  end

  -- player
  local col=p.powered and 10 or 4
  spr(1,p.x,p.y) -- tilly sprite

  -- ui
  if p.powered then
    print("🥓 power!",2,2,10)
    print(flr(p.ptimer/60).."s",2,8,10)
  end
end
```

---

## Pico-8 Learning Resources

**Official**:
- Manual: https://www.lexaloffle.com/dl/docs/pico-8_manual.html
- Cheat sheet: https://www.lexaloffle.com/bbs/?tid=28207

**Community**:
- BBS (games/tutorials): https://www.lexaloffle.com/bbs/?cat=7
- Platformer tutorial: https://mboffin.itch.io/gamedev
- Awesome list: https://github.com/pico-8/awesome-PICO-8

**Example Platformers**:
- Celeste (famous Pico-8 → full game): https://www.lexaloffle.com/bbs/?tid=2145
- Endless Tower: https://www.lexaloffle.com/bbs/?tid=3959

---

## Success Criteria

**Pico-8 paradigm succeeds if**:
1. [ ] Tilly's sprite captures her personality (8x8 pixels)
2. [ ] Movement feels as tight as PyGame version
3. [ ] Wall jumps work in 128x128 constraints
4. [ ] Aesthetic matches "nostalgic Flash-era" vision
5. [ ] Bacon power-up brings joy
6. [ ] Makes you smile when you play it

**If successful**: Consider Pico-8 as primary or co-primary paradigm
**If not**: Great learning, move to Phaser.js branch

---

## Notes

**Pico-8 Philosophy**: "Constraints as creativity catalyst"

This might be the perfect match for Barkour:
- Small scope → Focus on what matters (Tilly's charm)
- Retro aesthetic → Matches nostalgic vision perfectly
- Fast iteration → Literate Garden ethos
- Shareability → Easy to get feedback

**Hypothesis**: The 128x128 constraint will force us to distill Barkour to its purest essence - which might be exactly what we need.

---

**Created**: 2025-10-11
**Next Session**: Install Pico-8, draw Tilly, test movement feel
