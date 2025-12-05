# Barkour - Universal Design Skeleton

**Purpose**: Define the common architecture that works across **all platforms**
**Platforms**: Pico-8, PyGame, Web (Canvas/Phaser), Apple TV, Godot, Unity, Mobile

---

## Philosophy

**One game, many expressions**

Every platform implements:
1. Same physics (scaled appropriately)
2. Same core mechanics (wall jumps, bacon power-ups)
3. Same level structure (ground → clouds)
4. Same input model (universal controls)
5. Same game feel (tight, responsive platforming)

**Platform differences allowed**:
- Visual style (pixel art vs HD sprites)
- Screen resolution (128x128 vs 1920x1080)
- Additional features (leaderboards, replays)
- Platform-specific optimizations

---

## Core Configuration (`barkour_config.json`)

### Universal Format

```json
{
  "game": {
    "title": "Barkour: Tilly's Dream",
    "version": "0.1.0",
    "base_resolution": [800, 600],
    "target_fps": 60
  },

  "physics": {
    "gravity": 0.5,
    "base_jump_strength": -12,
    "base_movement_speed": 5,
    "acceleration": 0.5,
    "friction": 0.8,
    "max_fall_speed": 15,
    "wall_slide_speed": 2,
    "wall_jump_push": 8,
    "wall_jump_strength": -13
  },

  "powerup": {
    "duration_ms": 5000,
    "speed_multiplier": 1.5,
    "jump_multiplier": 1.2,
    "wall_jump_multiplier": 1.3
  },

  "levels": {
    "vertical_tower": {
      "type": "vertical_progression",
      "height": 512,
      "sections": [
        {"name": "ground", "y_range": [384, 512], "difficulty": "tutorial"},
        {"name": "buildings", "y_range": [256, 384], "difficulty": "medium"},
        {"name": "rooftops", "y_range": [128, 256], "difficulty": "hard"},
        {"name": "clouds", "y_range": [0, 128], "difficulty": "victory"}
      ],
      "platforms": [...],
      "walls": [...],
      "bacon": [...]
    }
  }
}
```

---

## Platform Scaling Rules

### Resolution Scaling

**Base resolution**: 800x600 (PyGame, Web)
**Scale factor**: `platform_width / 800`

**Examples**:
- **Pico-8**: 128px / 800 = 0.16x scale
- **Web**: 800px / 800 = 1.0x scale
- **Apple TV**: 1920px / 800 = 2.4x scale
- **Mobile**: 375px / 800 = 0.47x scale

**Apply scaling**:
```python
scale = platform_width / config.base_resolution[0]
player_width = config.player.width * scale
gravity = config.physics.gravity * scale
```

### Physics Scaling

**For small screens** (Pico-8, mobile):
- Reduce gravity proportionally
- Reduce jump strength proportionally
- Reduce movement speed proportionally
- Add acceleration/friction for smooth feel

**For large screens** (Apple TV, desktop):
- Keep physics values from config
- Optionally increase for more dramatic feel

---

## Universal Component Structure

### 1. PowerUpManager

**Responsibilities**:
- Track powered state (true/false)
- Manage timer countdown (milliseconds)
- Apply multipliers to player stats

**Interface**:
```python
class PowerUpManager:
    def __init__(self, config):
        self.duration = config.powerup.duration_ms
        self.powered = False
        self.timer = 0

    def collect_bacon(self):
        self.powered = True
        self.timer = self.duration

    def update(self, dt_ms):
        if self.powered:
            self.timer -= dt_ms
            if self.timer <= 0:
                self.powered = False

    def is_powered(self):
        return self.powered

    def get_speed_multiplier(self):
        return config.powerup.speed_multiplier if self.powered else 1.0

    def get_jump_multiplier(self):
        return config.powerup.jump_multiplier if self.powered else 1.0
```

### 2. Player

**State**:
- position (x, y)
- velocity (dx, dy)
- size (width, height)
- grounded (bool)
- wall_contact (None, "left", "right")
- can_wall_jump (bool)

**Methods**:
```python
class Player:
    def handle_input(self, input_state):
        # Universal input (works for keyboard, touch, gamepad)
        if input_state.left:
            self.accelerate_left()
        elif input_state.right:
            self.accelerate_right()
        else:
            self.apply_friction()

        if input_state.jump_pressed:
            if self.grounded:
                self.ground_jump()
            elif self.can_wall_jump:
                self.wall_jump()

    def update(self, dt, gravity, platforms, walls):
        # Apply gravity
        self.apply_gravity(gravity)

        # Move
        self.x += self.dx
        self.y += self.dy

        # Collision detection
        self.check_platform_collision(platforms)
        self.check_wall_collision(walls)

    def check_wall_collision(self, walls):
        # Returns wall contact direction
        # Updates can_wall_jump state
```

### 3. Bacon

**State**:
- position (x, y)
- collected (bool)
- bob_offset (for animation)

**Methods**:
```python
class Bacon:
    def update(self, time):
        # Bob animation (sin wave)
        self.bob_offset = sin(time * 2) * 2

    def check_collection(self, player):
        if not self.collected:
            if self.overlaps(player):
                self.collected = True
                return True
        return False

    def render_position(self):
        return (self.x, self.y + self.bob_offset)
```

### 4. Level

**State**:
- platforms (list)
- walls (list)
- bacon_pieces (list)
- camera_offset (for scrolling)

**Methods**:
```python
class Level:
    def __init__(self, config, level_name):
        level_data = config.levels[level_name]
        self.platforms = self.load_platforms(level_data)
        self.walls = self.load_walls(level_data)
        self.bacon = self.load_bacon(level_data)

    def update_camera(self, player_y):
        # Vertical scrolling (tower climb)
        self.camera_y = clamp(player_y - screen_height/2, 0, max_height)

    def get_visible_objects(self):
        # Return only objects in camera view (optimization)
```

---

## Universal Input Model

### Input Abstraction Layer

**All platforms map to this**:
```python
class InputState:
    left: bool          # Move left
    right: bool         # Move right
    jump: bool          # Jump button held
    jump_pressed: bool  # Jump button just pressed
    jump_released: bool # Jump button just released
```

### Platform Mappings

**Desktop (PyGame, Web)**:
- Arrow keys: left/right
- Space or Up arrow: jump
- Accessible across all keyboard layouts ✅

**Mobile (Touch)**:
- Virtual d-pad: left/right
- Touch anywhere right side: jump
- Or tilt controls

**Apple TV (Remote)**:
- Remote d-pad: left/right
- Remote center button: jump
- Gamepad if connected

**Pico-8**:
- Arrow keys: left/right
- Z or X: jump

**Gamepad (Universal)**:
- D-pad or stick: left/right
- A button: jump

---

## Universal Game Loop

**Every platform implements**:

```python
def game_loop():
    # 1. Initialize
    config = load_config("barkour_config.json")
    scale = calculate_scale(platform_resolution, config.base_resolution)
    player = Player(config, scale)
    level = Level(config, "vertical_tower", scale)
    powerup_manager = PowerUpManager(config)

    # 2. Main loop (60 FPS target)
    while running:
        dt = get_delta_time()

        # 3. Input
        input_state = get_input()
        if input_state.quit:
            break

        # 4. Update
        player.handle_input(input_state)
        player.update(dt, config.physics, level.platforms, level.walls)
        powerup_manager.update(dt)

        # Check bacon collection
        for bacon in level.bacon:
            if bacon.check_collection(player):
                powerup_manager.collect_bacon()

        # Check victory
        if player.y < level.victory_threshold:
            show_victory()

        # 5. Camera
        level.update_camera(player.y)

        # 6. Render
        clear_screen()
        render_level(level, level.camera_y)
        render_player(player, powerup_manager.is_powered())
        render_ui(powerup_manager, player.y)
        present_frame()

        # 7. Timing
        wait_for_next_frame(config.fps)
```

---

## Platform-Specific Adaptations

### Pico-8

**Constraints**:
- 128x128 display
- 16 colors
- Limited tokens

**Adaptations**:
- Scale everything by 0.16x
- Use simpler rendering (rectangles instead of sprites initially)
- Store level data in code (not JSON)
- Camera follows player vertically

**Config translation**:
```lua
-- From barkour_config.json
cfg = {
  grav = 0.5 * 0.16,        -- scaled
  jump = -12 * 0.16,        -- scaled
  spd = 5 * 0.16,           -- scaled
  accel = 0.5,              -- keep for smooth feel
  friction = 0.8            -- keep for smooth feel
}
```

### PyGame (Desktop)

**Strengths**:
- Full config support
- High resolution
- Fast iteration

**Adaptations**:
- Use config directly (no scaling needed)
- Load sprites if available
- Window resizing support
- Debug overlays

### Web (Canvas/Phaser)

**Strengths**:
- Cross-platform by default
- Touch + keyboard support
- Easy sharing

**Adaptations**:
- Responsive canvas sizing
- Touch controls for mobile
- High DPI support
- Web-specific optimizations (requestAnimationFrame)

### Apple TV

**Strengths**:
- Big screen
- Gamepad support
- Living room gaming

**Adaptations**:
- Scale up 2-3x for TV viewing distance
- Remote + gamepad input
- Couch-friendly UI (large text)
- Achievement integration

### Mobile (iOS/Android)

**Strengths**:
- Portable
- Touch native
- Wide audience

**Adaptations**:
- Scale down for phone screens
- Touch controls (virtual d-pad)
- Tilt controls optional
- Portrait or landscape support
- Save/resume state

---

## Level Data Format (Universal)

### JSON Structure

```json
{
  "level_id": "vertical_tower",
  "type": "vertical_scroll",
  "dimensions": {
    "width": 128,
    "height": 512
  },
  "victory_condition": {
    "type": "reach_y",
    "threshold": 50
  },
  "platforms": [
    {
      "id": "ground_floor",
      "x": 0,
      "y": 480,
      "width": 128,
      "height": 16,
      "type": "solid"
    }
  ],
  "walls": [
    {
      "id": "tutorial_wall",
      "x": 5,
      "y": 380,
      "width": 4,
      "height": 80,
      "type": "wall_jumpable"
    }
  ],
  "bacon": [
    {
      "id": "easy_bacon",
      "x": 60,
      "y": 450,
      "difficulty": "easy"
    }
  ],
  "camera": {
    "type": "follow_player_vertical",
    "offset_y": -64,
    "bounds": [0, 0, 128, 512]
  }
}
```

### Platform Loading

**Each platform loads same JSON**:
```python
# PyGame
level_data = json.load(open("levels/vertical_tower.json"))

# Pico-8
-- Convert JSON to Lua tables manually or with tool

# Web
fetch('levels/vertical_tower.json').then(r => r.json())

# Apple TV
let levelData = try JSONDecoder().decode(from: levelFile)
```

---

## Testing Parity

### Physics Verification

**Test**: Jump from platform A to platform B
**Expected**: Same arc, same landing point (accounting for scale)
**How**: Record jump trajectory, compare across platforms

**Automated test**:
```python
def test_jump_parity():
    config = load_config()

    # Simulate jump in reference implementation
    reference = simulate_jump(config, start_pos, jump_input)

    # Simulate in platform implementation
    platform = platform_simulate_jump(config, start_pos, jump_input)

    # Compare (allowing for floating point errors)
    assert positions_match(reference, platform, tolerance=0.1)
```

### Feel Verification

**Test**: Wall jump sequence
**Expected**: Same satisfying "kick off wall" feel
**How**: Player feedback, side-by-side video comparison

**Checklist**:
- [ ] Jump height consistent?
- [ ] Wall slide speed consistent?
- [ ] Wall jump push distance consistent?
- [ ] Power-up multipliers consistent?
- [ ] Bacon collection range consistent?

---

## Asset Pipeline (Future)

### Shared Assets

**Location**: `shared/assets/`

**Structure**:
```
shared/assets/
  sprites/
    tilly/
      tilly_idle.png      (40x40 base)
      tilly_run_01.png
      tilly_jump.png
      tilly_wall_slide.png
    bacon/
      bacon.png           (30x20 base)
  sounds/
    jump.wav
    wall_jump.wav
    bacon_collect.wav
    power_up.wav
  music/
    ground_theme.mp3
    clouds_theme.mp3
```

### Platform Conversion

**PyGame**: Use PNG directly
**Web**: Convert to spritesheet
**Pico-8**: Downscale to 8x8, reduce colors to 16
**Apple TV**: Use @2x or @3x versions

**Tool** (future):
```bash
# Convert assets for platform
./scripts/convert_assets.sh --platform pico8
# Output: pico8/assets/ with converted files
```

---

## Documentation Per Platform

### Platform README Template

```markdown
# Barkour - [Platform Name]

**Status**: [Active/Prototype/Experimental]
**Shared Config**: `../shared/barkour_config.json`
**Architecture**: `../shared/ARCHITECTURE.md`

## Platform-Specific Notes

**Resolution**: [width x height]
**Scale Factor**: [X]
**Physics**: [Same as base / Scaled by X]
**Input**: [Keyboard/Touch/Gamepad details]

## Running

[Platform-specific run instructions]

## Development

[Platform-specific dev notes]

## Parity Status

- [ ] Physics match base
- [ ] Input works universally
- [ ] Levels match design
- [ ] Power-ups work correctly
- [ ] Victory condition works
```

---

## Version Control Strategy

### Shared Files

**Never change without coordination**:
- `shared/barkour_config.json`
- `shared/ARCHITECTURE.md`
- `shared/levels/*.json`

**Process**:
1. Propose change in `shared/proposals/`
2. Test in one platform
3. Verify doesn't break others
4. Update all platforms
5. Commit together

### Platform Files

**Independent development allowed**:
- Platform-specific code
- Platform-specific optimizations
- Platform-specific features (leaderboards, etc.)

**But must maintain**:
- Config compliance
- Physics parity
- Level structure parity

---

## Decision Framework

### When to Keep Parity

**Core mechanics**: Must match across all platforms
- Physics (gravity, jumps, movement)
- Power-up behavior (duration, multipliers)
- Level structure (platforms, walls, bacon)
- Victory conditions

### When to Diverge

**Platform capabilities**: Can differ based on constraints
- Visual style (pixel art vs HD)
- Sound/music quality
- UI polish (menus, transitions)
- Platform features (achievements, replays)

**Example**: Pico-8 has simple rectangles, Apple TV has HD sprites - both valid, both Barkour

---

## Success Criteria

**A platform implementation succeeds when**:

1. ✅ Loads from shared config
2. ✅ Physics feel identical to baseline (PyGame)
3. ✅ Levels match structure from config
4. ✅ Wall jumps work and feel good
5. ✅ Bacon power-ups behave correctly
6. ✅ Victory condition triggers at right time
7. ✅ Input works universally (keyboard layouts, etc.)
8. ✅ Player says "this is Barkour!"

---

## Next Steps

### Immediate (This Week)

1. **Extract Pico-8 level data to JSON**
   - Convert vertical tower to `shared/levels/vertical_tower.json`
   - Pico-8 loads from this data

2. **Update PyGame to use new acceleration/friction**
   - Port Pico-8's smooth movement to PyGame
   - Verify feel matches

3. **Test Web Canvas with vertical tower**
   - Load level from JSON
   - Verify camera follows player

### Short Term (Next 2 Weeks)

4. **Apple TV prototype**
   - Use SwiftUI or SpriteKit
   - Load shared config
   - Test with remote input

5. **Mobile prototype** (iOS or Android)
   - Touch controls
   - Test on phone screen size

### Long Term (Future)

6. **Asset pipeline**
   - Create Tilly sprites
   - Auto-convert for platforms

7. **Level editor**
   - Visual tool to edit JSON
   - Preview across platforms

---

**Philosophy**: Build once (config + architecture), deploy everywhere (platforms)

**Created**: 2025-10-12
**Status**: Living document, evolves with development
