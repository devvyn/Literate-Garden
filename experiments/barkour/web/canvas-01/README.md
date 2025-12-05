# Barkour - Web Canvas Version

**Same game, different platform!** This uses the exact same design skeleton as the PyGame version.

## Quick Start

```bash
# From the experiments/barkour directory
python3 -m http.server 8000

# Then open in browser:
# http://localhost:8000/web/canvas-01/
```

## Shared Architecture

This implementation uses:
- **`../shared/barkour_config.json`** - Same config as PyGame
- **Same component structure**:
  - `PowerUpManager` - Identical power-up logic
  - `Player` - Same physics, wall jumps, everything
  - `Bacon` - Same bob animation
  - Level data from config

**Result**: Gameplay feels identical to PyGame version, but runs in your browser!

## What's Different?

**Same**:
- Physics (gravity, speeds, jump heights)
- Power-up duration (5 seconds)
- Level layout (platforms, walls, bacon positions)
- Game loop logic
- Wall jump mechanics

**Different**:
- Rendering (HTML5 Canvas instead of PyGame)
- Input (DOM events instead of pygame.key)
- Game loop (requestAnimationFrame instead of clock.tick)

## Testing Parity

To verify both versions feel the same:
1. Play PyGame version, note jump height
2. Play web version, compare jump height
3. Should be **identical** - both use `config.physics.base_jump_strength: -12`

## Browser Requirements

- Modern browser (Chrome, Firefox, Safari, Edge)
- JavaScript enabled
- Keyboard for controls (arrow keys + space)

## Future: Phaser.js Version

Next up: same architecture, but using Phaser framework for:
- Built-in physics engine
- Better sprite/animation system
- Mobile touch controls
- Sound management

**All three will share the same skeleton!**

---

**Created**: 2025-10-10
**Version**: 0.1.0 (matches PyGame version)
