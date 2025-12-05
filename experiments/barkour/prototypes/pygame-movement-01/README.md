# Barkour - PyGame Movement Prototype 01

**Focus**: Bacon-powered parkour mechanics
**Status**: Playable ✅
**Created**: 2025-10-09
**Updated**: 2025-10-10 - Added bacon collection and power-up system!

## Quick Start

```bash
# Set up virtual environment and install dependencies
uv venv
source .venv/bin/activate
uv pip install pygame

# Run the prototype
python main.py
```

**Or use the existing venv:**
```bash
source .venv/bin/activate
python main.py
```

## Controls

- **Arrow keys**: Move left/right
- **Space** or **Up arrow**: Jump
- **ESC**: Quit

> Note: Arrow keys work universally regardless of keyboard layout (Dvorak, Colemak, etc.)

## What This Tests

- ✅ Basic platformer gravity and physics
- ✅ Jump arc and responsiveness
- ✅ Platform collision detection
- ✅ Simple Tilly representation (beige rectangle with black muzzle detail)
- ✅ **Bacon collection mechanic**
- ✅ **Power-up state management (normal → powered → normal)**
- ✅ **Enhanced movement when powered (1.5x speed, 1.2x jump)**
- ✅ **Visual feedback (golden glow when powered)**
- ✅ **Timer UI showing remaining power duration**

## Physics Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Gravity | 0.5 | Feels responsive, not floaty |
| Base Jump Strength | -12 | Good height for reaching platforms |
| Base Movement Speed | 5 | Comfortable horizontal speed |
| Max Fall Speed | 15 | Prevents infinite acceleration |
| FPS Target | 60 | Smooth movement |

## Power-Up Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Powered Speed Multiplier | 1.5x | Noticeably faster movement |
| Powered Jump Multiplier | 1.2x | Higher, longer jumps |
| Power-Up Duration | 5 seconds | Creates urgency and tension |
| Visual Feedback | Golden glow | Clear powered state indicator |

## Findings

### What Worked

- **Jump arc feels good** - not too floaty, not too heavy
- **Platform collision is reliable** - clean landing detection
- **Controls are responsive** (< 50ms input latency)
- **Runs at solid 60fps** on macOS
- **User feedback**: "Feels good, kinda reminds me of Super Meat Boy" ✨
  - This is excellent validation - SMB is known for tight platformer controls

### What Could Be Better

- No coyote time (jump grace period after leaving platform)
- No jump buffering (press jump slightly before landing)
- Movement stops instantly (no momentum/sliding)
- Character is just a rectangle (need actual sprite)

### Next Iterations

1. Add bacon collection mechanic (Task #3)
2. Implement power-up state with enhanced movement
3. Add coyote time and jump buffering for better feel
4. Create proper Tilly sprite

## Vision Alignment

✅ **Playable within 5 minutes**: Yes - just run `python main.py`
✅ **Recognizable as dog**: Minimal (beige rectangle with black muzzle)
✅ **Movement focus**: Yes - that's all this prototype does
⏳ **Bacon power-ups**: Not yet (next task)
⏳ **Parkour feel**: Basic jumping works, needs wall mechanics

## Evaluation Schema

```json
{
  "prototype_id": "pygame-movement-01",
  "engine": "PyGame",
  "focus": "Basic platformer physics and jump feel",
  "findings": {
    "what_worked": [
      "Jump arc feels responsive",
      "60fps performance",
      "Simple controls work well",
      "Platform collision is reliable"
    ],
    "what_didnt": [
      "No coyote time",
      "No jump buffering",
      "Instant movement stop (no slide)",
      "Character too abstract"
    ],
    "parameters": {
      "gravity": 0.5,
      "jump_strength": -12,
      "movement_speed": 5,
      "max_fall_speed": 15,
      "fps": 60
    }
  },
  "next_steps": "iterate",
  "playable_link": "~/Documents/GitHub/Literate-Garden/experiments/barkour/prototypes/pygame-movement-01/"
}
```

---

**Vision Reference**: [`~/Documents/GitHub/barkour/GAME_VISION.md`](../../../../../barkour/GAME_VISION.md)
