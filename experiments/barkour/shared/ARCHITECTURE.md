# Barkour - Shared Architecture

This document defines the **unified design skeleton** shared across all Barkour implementations (PyGame, Web Canvas, Phaser.js, etc.).

## Philosophy

All implementations share:
- **Same game logic** (physics, power-ups, collision rules)
- **Same configuration** (`barkour_config.json`)
- **Same component structure** (PowerUpManager, Player, Bacon, Level)
- **Same game loop pattern** (update → collision → render)

Each implementation can:
- Use platform-specific rendering
- Leverage platform-specific features
- Optimize for their environment

**Result**: Core gameplay feels identical across platforms, but each uses the best tools for their context.

---

## Core Components

### 1. PowerUpManager
**Responsibility**: Manage bacon power-up state

**State**:
```
- powered: boolean
- timer: number (milliseconds remaining)
- duration: number (from config)
```

**Methods**:
```
- collect_bacon(): activate power-up, reset timer
- update(dt): decrement timer, deactivate when expired
- is_powered(): return current state
- get_time_remaining(): return seconds left
```

---

### 2. Player
**Responsibility**: Tilly's physics, movement, and abilities

**State**:
```
- position: {x, y}
- velocity: {x, y}
- size: {width, height} (from config)
- on_ground: boolean
- touching_wall: "left" | "right" | null
- can_wall_jump: boolean
- wall_jump_cooldown: number
- power_manager: reference to PowerUpManager
```

**Methods**:
```
- update(keys, platforms, walls):
  - Apply gravity (reduced when wall sliding)
  - Handle input (movement, jump)
  - Check wall collision
  - Update position
  - Check platform collision

- get_movement_speed(): base or powered speed
- get_jump_strength(): base or powered jump
- get_wall_jump_strength(): base or powered wall jump

- draw(screen): render player with power-up effects
```

**Physics Rules** (from config):
- Normal gravity: `config.physics.gravity`
- Wall slide: max fall speed = `config.physics.wall_slide_speed`
- Ground jump: velocity.y = `get_jump_strength()`
- Wall jump:
  - velocity.x = `±config.physics.wall_jump_push`
  - velocity.y = `get_wall_jump_strength()`

---

### 3. Bacon
**Responsibility**: Collectible power-up with animation

**State**:
```
- position: {x, y}
- size: {width: 30, height: 20}
- collected: boolean
- bob_offset: number (for animation)
```

**Methods**:
```
- update(): increment bob_offset for float animation
- get_rect(): return collision box (with bob animation)
- draw(screen): render bacon with stripes
```

**Animation**:
```
bob_y = y + sin(bob_offset) * 5
```

---

### 4. Level
**Responsibility**: Static geometry from config

**Data** (loaded from `config.levels.demo`):
```
- platforms: array of {x, y, width, height}
- walls: array of {x, y, width, height}
- bacon_spawns: array of {x, y}
```

---

## Game Loop

All implementations follow this pattern:

```
1. INITIALIZATION
   - Load config
   - Create power_manager
   - Create player(config.player.start_x, config.player.start_y, power_manager)
   - Create platforms from config.levels.demo.platforms
   - Create walls from config.levels.demo.walls
   - Create bacon from config.levels.demo.bacon

2. GAME LOOP (60fps from config)
   while running:
     dt = get_delta_time()

     # INPUT
     keys = get_input_state()

     # UPDATE
     player.update(keys, platforms, walls)
     power_manager.update(dt)
     for bacon in bacons:
       bacon.update()

     # COLLISION
     for bacon in bacons:
       if not bacon.collected and player.collides(bacon):
         bacon.collected = True
         power_manager.collect_bacon()

     # RENDER
     clear_screen(config.colors.sky_blue)
     draw_platforms(platforms, config.colors.ground_brown)
     draw_walls(walls, config.colors.wall_gray)
     draw_bacon(bacons)
     draw_player(player)
     draw_ui(power_manager)
     display_frame()
```

---

## Configuration Usage

### PyGame Example
```python
import json

with open('shared/barkour_config.json') as f:
    config = json.load(f)

# Use config values
GRAVITY = config['physics']['gravity']
SCREEN_WIDTH = config['game']['screen']['width']
platforms = [pygame.Rect(**p) for p in config['levels']['demo']['platforms']]
```

### Web/JavaScript Example
```javascript
fetch('shared/barkour_config.json')
  .then(r => r.json())
  .then(config => {
    // Use config values
    const GRAVITY = config.physics.gravity;
    const canvas = createCanvas(config.game.screen.width, config.game.screen.height);
    const platforms = config.levels.demo.platforms.map(p => new Platform(p));
  });
```

---

## Platform-Specific Adaptations

### PyGame
- Uses pygame.Rect for collisions
- Uses pygame.draw for rendering
- Direct pixel manipulation

### Web Canvas
- Uses DOM Canvas API
- requestAnimationFrame for game loop
- Touch events for mobile

### Phaser.js
- Uses Phaser.Physics for collisions
- Uses Phaser.Sprite for rendering
- Built-in input management

**All share**: same config, same logic, same feel.

---

## Accessibility-Driven Design

Barkour inherits accessibility patterns from the meta-project knowledge base, specifically from the AAFC Herbarium project's accessibility-first design.

**Pattern Source**: `~/devvyn-meta-project/.kb-context/patterns/accessibility-driven-design.md`

### Universal Keyboard Input

**Principle**: Use only layout-agnostic keys that work across all keyboard layouts (QWERTY, Dvorak, Colemak, AZERTY, etc.)

**Implementation**:
- **Arrow keys only** for movement - no WASD
- **Space** for jump (universal across layouts)
- **Arrow Up** as alternative jump key
- **Escape** for pause/menu (future)

**Rationale**:
- Developer uses Dvorak layout where WASD doesn't correspond to expected positions
- Arrow keys work identically on all keyboard layouts worldwide
- More accessible to international users with different layouts
- Easier to port to mobile (touch controls map naturally to arrows)

**Code Example** (from pygame-movement-01/main.py:191-195):
```python
# Movement input
if keys[pygame.K_LEFT]:
    self.velocityX = -movementSpeed
elif keys[pygame.K_RIGHT]:
    self.velocityX = movementSpeed
else:
    self.velocityX = 0
```

**Documentation Note**: "Arrow keys work universally regardless of keyboard layout (Dvorak, Colemak, etc.)"

### Keyboard-First Design

**Principle**: Design for keyboard first, then add other input methods (mouse, touch, gamepad) as enhancements.

**Implementation**:
- Complete gameplay possible with keyboard only (no mouse required)
- All game states navigable via keyboard
- Future menu systems will be keyboard-navigable
- Touch/gamepad controls map to keyboard equivalents

**Benefits**:
- Accessible to keyboard-only users
- Screen reader compatible (keyboard events are detectable)
- Platform-agnostic (works on any device with a keyboard)
- Power users can play efficiently

### Future Accessibility Considerations

When adding new features, follow these patterns:

**Input Controls**:
- Use arrow keys for primary navigation
- Use Space/Enter for primary actions
- Use Escape for cancel/back
- Avoid layout-specific keys (WASD, HJKL on QWERTY)
- Document all controls

**Visual Feedback**:
- Don't rely on color alone (use text + icons + color)
- Ensure contrast ratios meet WCAG AA standards
- Provide text alternatives for visual information

**Multi-Platform**:
- Keyboard controls should map naturally to:
  - Touch (on-screen d-pad = arrow keys)
  - Gamepad (d-pad/stick = arrow keys, button A = space)
  - Mobile (tilt/swipe = arrow key equivalents)

**Testing**:
- Verify all functionality accessible via keyboard only
- Test with different keyboard layouts if possible
- Ensure focus indicators are visible (for menus)

### Cross-Project Pattern Inheritance

**AAFC Herbarium** → **Barkour**

| Pattern | AAFC Usage | Barkour Application |
|---------|-----------|-------------------|
| Universal keyboard input | Review interface uses arrow keys for navigation | Game uses arrow keys for movement (no WASD) |
| Keyboard-first workflow | Complete review workflow keyboard-only | Complete gameplay keyboard-only |
| No layout assumptions | Works with Dvorak, Colemak, etc. | Arrow keys universal across layouts |
| Expert-first design | Power users optimize via keyboard | Players can use efficient arrow key controls |

**Pattern Source**: Multi-agent collaboration framework v2.1 (Inclusive Collaboration Design)

---

## Testing Parity

To verify implementations match:

1. **Same physics parameters** → Same jump height, speed, feel
2. **Same level layout** → Platforms/walls in same positions
3. **Same power-up duration** → 5 seconds across all versions
4. **Same collision rules** → Bacon collection feels identical

**Goal**: Player can't tell which version they're playing (except for graphics style).

---

## Future Enhancements

When adding new features, update:
1. `barkour_config.json` - add config parameters
2. This `ARCHITECTURE.md` - document the pattern
3. All implementations - maintain parity

Example: Adding double-jump
- Config: `"double_jump_enabled": true`
- Architecture: Update Player component docs
- Implementations: Each adds double-jump following same rules

---

**Last Updated**: 2025-10-10
**Implementations**: PyGame ✅, Web Canvas (in progress), Phaser.js (planned)
