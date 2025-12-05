# Installing Pico-8

## Quick Start

**1. Buy Pico-8** ($15)
   - Go to: https://www.lexaloffle.com/pico-8.php
   - Click "Buy Pico-8" button
   - Purchase via Stripe/PayPal
   - Download macOS version

**2. Install**
   - Unzip downloaded file
   - Drag `PICO-8.app` to `/Applications/`
   - Done!

**3. Run**
   ```bash
   # From Applications
   open /Applications/PICO-8.app

   # Or from terminal
   /Applications/PICO-8.app/Contents/MacOS/pico8
   ```

**4. Create Shell Alias** (optional)
   ```bash
   # Add to ~/.zshrc
   echo 'alias pico8="/Applications/PICO-8.app/Contents/MacOS/pico8"' >> ~/.zshrc
   source ~/.zshrc

   # Now you can run:
   pico8
   ```

---

## Loading Barkour Cart

Once Pico-8 is installed:

```bash
# Option 1: Launch with cart
pico8 ~/Documents/GitHub/Literate-Garden/experiments/barkour/pico8/barkour-01/barkour.p8

# Option 2: Load in Pico-8 console
pico8
# Then in console:
> CD ~/Documents/GitHub/Literate-Garden/experiments/barkour/pico8/barkour-01/
> LOAD BARKOUR.P8
> RUN
```

---

## Basic Pico-8 Commands

**In Console**:
```
LOAD BARKOUR.P8    -- load cart
SAVE BARKOUR.P8    -- save cart
RUN                -- run game
REBOOT             -- restart pico-8

DIR                -- list files
CD <path>          -- change directory
```

**In Game**:
- Arrow keys: Move
- Z or X: Jump / Wall jump
- ESC: Exit to console

**While Editing**:
- ESC: Switch between modes (code/sprite/map/sfx/music)
- CTRL+R: Run from editor
- CTRL+S: Save

---

## Learning Pico-8

**Official Manual**:
https://www.lexaloffle.com/dl/docs/pico-8_manual.html

**Keyboard Shortcuts**:
- CTRL+R: Run game
- CTRL+S: Save cart
- ESC: Toggle editor mode
- TAB: Toggle console

**Helpful Commands**:
```
HELP            -- show help
SPLORE          -- browse community carts
EXPORT          -- export to HTML/binary
```

---

## Why $15 is Worth It

**You get**:
- Full fantasy console IDE
- Code editor with syntax highlighting
- Sprite editor (128 sprites, 8x8 each)
- Map editor (128x64 tiles)
- Sound effect editor (64 sfx)
- Music editor (64 patterns)
- Export to standalone HTML/binary
- BBS account for sharing carts
- Lifetime updates
- All future features

**Community Benefits**:
- 10,000+ games on BBS to learn from
- Active forums and Discord
- Tons of tutorials
- Regular game jams
- Supportive creator (Zep)

**Educational Value**:
- Learn game dev constraints
- Understand optimization
- Practice creative limitation
- Build complete games quickly

---

## Free Alternative (Limited)

**Education Edition**: https://www.lexaloffle.com/pico-8.php?page=schools

Free for students/educators, but:
- Web-based only
- No export
- No sprite editor
- Limited features

**Recommendation**: If you're serious about Barkour in Pico-8, buy the full version.

---

## Next Steps After Installation

1. **Load barkour.p8**
2. **Press CTRL+R to run**
3. **Play with arrow keys + Z**
4. **Press ESC to edit**
5. **Try sprite editor (switch with ESC)**
6. **Draw Tilly sprite in slot 1**
7. **Save with CTRL+S**

---

## Troubleshooting

**"Can't find pico8 command"**:
- Did you create the alias?
- Try full path: `/Applications/PICO-8.app/Contents/MacOS/pico8`

**"Cart won't load"**:
- Make sure file is named `.p8` (not `.p8.txt`)
- Check you're in the right directory (`CD` command)

**"Game runs too fast/slow"**:
- Pico-8 targets 60fps automatically
- Check Activity Monitor for CPU issues
- Try closing other apps

---

**Ready?** Let's make Tilly jump! 🐕🥓
