"""behavior_tracker.py

A tracker-style grid system for game behaviors.

Like ProTracker sequences notes + effects, this sequences actions + modifiers.
64 ticks × N entity channels. Patterns are reusable. Constraints force creativity.

Run: marimo run behavior_tracker.py

Provenance: Built from grid_theory.py proposal
Connects to: tracker_as_dsl, protracker_deep_dive, game_demos_gallery
"""

import marimo

__generated_with__ = "0.9.16"
app = marimo.App(width="full")


@app.cell
def define_vocabulary():
    """The behavior vocabulary - like tracker effect commands."""
    from dataclasses import dataclass, field
    from typing import Dict, Any, Optional, List, Callable
    from enum import Enum

    class BehaviorType(Enum):
        """Core behavior verbs."""
        NOP = "."           # No operation (continue previous)
        SPAWN = "spawn"     # Create entity at position
        MOVE = "move"       # Move in direction
        JUMP = "jump"       # Vertical impulse
        CHASE = "chase"     # Move toward target
        FLEE = "flee"       # Move away from target
        SHOOT = "shoot"     # Emit projectile
        DIE = "die"         # Remove entity
        WAIT = "wait"       # Explicit pause
        SAY = "say"         # Display text
        FLAG = "flag"       # Set a flag/trigger

    @dataclass
    class Behavior:
        """A single behavior command."""
        verb: BehaviorType
        params: Dict[str, Any] = field(default_factory=dict)

        def __repr__(self):
            if self.verb == BehaviorType.NOP:
                return "."
            p = ",".join(f"{v}" for v in self.params.values())
            return f"{self.verb.value}({p})" if p else self.verb.value

    # Shorthand constructors
    def nop(): return Behavior(BehaviorType.NOP)
    def spawn(x, y): return Behavior(BehaviorType.SPAWN, {"x": x, "y": y})
    def move(dx, dy): return Behavior(BehaviorType.MOVE, {"dx": dx, "dy": dy})
    def jump(force): return Behavior(BehaviorType.JUMP, {"force": force})
    def chase(target): return Behavior(BehaviorType.CHASE, {"target": target})
    def flee(target): return Behavior(BehaviorType.FLEE, {"target": target})
    def shoot(dx, dy): return Behavior(BehaviorType.SHOOT, {"dx": dx, "dy": dy})
    def die(): return Behavior(BehaviorType.DIE)
    def wait(): return Behavior(BehaviorType.WAIT)
    def say(text): return Behavior(BehaviorType.SAY, {"text": text})
    def flag(name): return Behavior(BehaviorType.FLAG, {"name": name})

    return (BehaviorType, Behavior, nop, spawn, move, jump,
            chase, flee, shoot, die, wait, say, flag)


@app.cell
def define_pattern_structure(Behavior, nop):
    """Patterns: the reusable building blocks."""
    from dataclasses import dataclass, field
    from typing import List, Dict

    @dataclass
    class Channel:
        """A single entity's behavior track."""
        name: str
        entity_type: str  # "player", "enemy", "item", "world"
        rows: List[Behavior] = field(default_factory=list)

    @dataclass
    class Pattern:
        """A pattern = N ticks × M channels, like tracker pattern."""
        name: str
        length: int  # number of ticks
        channels: List[Channel] = field(default_factory=list)

        def get_tick(self, tick: int) -> Dict[str, Behavior]:
            """Get all behaviors for a given tick."""
            result = {}
            for ch in self.channels:
                if tick < len(ch.rows):
                    result[ch.name] = ch.rows[tick]
                else:
                    result[ch.name] = nop()
            return result

        def __repr__(self):
            header = f"Pattern: {self.name} ({self.length} ticks, {len(self.channels)} channels)"
            return header

    @dataclass
    class Song:
        """A song = sequence of pattern references, like tracker song."""
        name: str
        patterns: Dict[str, Pattern] = field(default_factory=dict)
        sequence: List[str] = field(default_factory=list)  # pattern names in order
        loop_point: int = 0  # where to loop back to

    return Channel, Pattern, Song


@app.cell
def define_world(Behavior, BehaviorType):
    """The world state that behaviors act upon."""
    from dataclasses import dataclass, field
    from typing import Dict, List, Set, Tuple, Optional
    import math

    @dataclass
    class Entity:
        """A game entity with position and state."""
        name: str
        entity_type: str
        x: float
        y: float
        vx: float = 0.0
        vy: float = 0.0
        alive: bool = True
        flags: Set[str] = field(default_factory=set)
        speech: str = ""

    @dataclass
    class World:
        """The game world state."""
        width: int = 32
        height: int = 16
        entities: Dict[str, Entity] = field(default_factory=dict)
        gravity: float = 0.0
        tick: int = 0
        messages: List[str] = field(default_factory=list)
        flags: Set[str] = field(default_factory=set)

        def add_entity(self, name: str, entity_type: str, x: float, y: float):
            self.entities[name] = Entity(name, entity_type, x, y)

        def get_entity(self, name: str) -> Optional[Entity]:
            return self.entities.get(name)

        def remove_entity(self, name: str):
            if name in self.entities:
                self.entities[name].alive = False

        def apply_physics(self):
            """Apply gravity and velocity to all entities."""
            for e in self.entities.values():
                if not e.alive:
                    continue
                e.vy += self.gravity
                e.x += e.vx
                e.y += e.vy
                # Clamp to world bounds
                e.x = max(0, min(self.width - 1, e.x))
                e.y = max(0, min(self.height - 1, e.y))
                # Floor collision
                if e.y >= self.height - 1:
                    e.y = self.height - 1
                    e.vy = 0

        def distance(self, e1: str, e2: str) -> float:
            a, b = self.entities.get(e1), self.entities.get(e2)
            if not a or not b:
                return float('inf')
            return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

        def direction_to(self, from_name: str, to_name: str) -> Tuple[int, int]:
            a, b = self.entities.get(from_name), self.entities.get(to_name)
            if not a or not b:
                return (0, 0)
            dx = 1 if b.x > a.x else (-1 if b.x < a.x else 0)
            dy = 1 if b.y > a.y else (-1 if b.y < a.y else 0)
            return (dx, dy)

    return Entity, World


@app.cell
def define_interpreter(Behavior, BehaviorType, World, Entity):
    """The interpreter that executes behaviors."""
    from typing import Dict

    class BehaviorInterpreter:
        """Executes behaviors against world state."""

        def __init__(self, world: World):
            self.world = world

        def execute(self, entity_name: str, behavior: Behavior):
            """Execute a single behavior for an entity."""
            entity = self.world.get_entity(entity_name)
            verb = behavior.verb
            params = behavior.params

            if verb == BehaviorType.NOP:
                pass  # No operation

            elif verb == BehaviorType.SPAWN:
                x, y = params.get("x", 0), params.get("y", 0)
                # Determine entity type from channel name
                etype = "player" if "player" in entity_name.lower() else "enemy"
                self.world.add_entity(entity_name, etype, x, y)
                self.world.messages.append(f"T{self.world.tick}: {entity_name} spawned at ({x},{y})")

            elif verb == BehaviorType.MOVE:
                if entity and entity.alive:
                    dx, dy = params.get("dx", 0), params.get("dy", 0)
                    entity.x += dx
                    entity.y += dy

            elif verb == BehaviorType.JUMP:
                if entity and entity.alive:
                    force = params.get("force", 3)
                    entity.vy = -force  # negative = up

            elif verb == BehaviorType.CHASE:
                if entity and entity.alive:
                    target = params.get("target", "")
                    dx, dy = self.world.direction_to(entity_name, target)
                    entity.x += dx * 0.5
                    entity.y += dy * 0.5

            elif verb == BehaviorType.FLEE:
                if entity and entity.alive:
                    target = params.get("target", "")
                    dx, dy = self.world.direction_to(entity_name, target)
                    entity.x -= dx * 0.5
                    entity.y -= dy * 0.5

            elif verb == BehaviorType.SHOOT:
                if entity and entity.alive:
                    dx, dy = params.get("dx", 1), params.get("dy", 0)
                    bullet_name = f"bullet_{self.world.tick}"
                    self.world.add_entity(bullet_name, "bullet", entity.x + dx, entity.y)
                    bullet = self.world.get_entity(bullet_name)
                    if bullet:
                        bullet.vx = dx * 2
                        bullet.vy = dy

            elif verb == BehaviorType.DIE:
                if entity:
                    entity.alive = False
                    self.world.messages.append(f"T{self.world.tick}: {entity_name} died")

            elif verb == BehaviorType.SAY:
                if entity and entity.alive:
                    text = params.get("text", "...")
                    entity.speech = text
                    self.world.messages.append(f"T{self.world.tick}: {entity_name}: '{text}'")

            elif verb == BehaviorType.FLAG:
                flag_name = params.get("name", "")
                self.world.flags.add(flag_name)
                self.world.messages.append(f"T{self.world.tick}: FLAG '{flag_name}' set")

        def execute_tick(self, tick_behaviors: Dict[str, Behavior]):
            """Execute all behaviors for one tick."""
            for entity_name, behavior in tick_behaviors.items():
                self.execute(entity_name, behavior)
            self.world.apply_physics()
            self.world.tick += 1

    return BehaviorInterpreter,


@app.cell
def create_demo_pattern(Pattern, Channel, spawn, move, jump, chase, shoot, say, nop, die, flag):
    """Create a demo pattern showing the system in action."""

    # 16-tick demo pattern with 4 channels
    demo = Pattern(name="chase_scene", length=16, channels=[
        Channel(name="player", entity_type="player", rows=[
            spawn(4, 14),    # T0: spawn player
            nop(),           # T1: wait
            move(1, 0),      # T2: move right
            move(1, 0),      # T3: move right
            jump(4),         # T4: jump!
            nop(),           # T5: in air
            nop(),           # T6: in air
            move(1, 0),      # T7: move right while falling
            nop(),           # T8: land
            say("uh oh"),    # T9: see enemy
            move(1, 0),      # T10: run!
            move(1, 0),      # T11: run!
            shoot(1, 0),     # T12: shoot right
            move(1, 0),      # T13: keep running
            move(1, 0),      # T14: keep running
            flag("escaped"), # T15: made it!
        ]),
        Channel(name="enemy", entity_type="enemy", rows=[
            nop(),           # T0: not yet
            nop(),           # T1: not yet
            nop(),           # T2: not yet
            spawn(28, 14),   # T3: enemy spawns
            nop(),           # T4: wait
            chase("player"), # T5: start chasing
            chase("player"), # T6: chase
            chase("player"), # T7: chase
            chase("player"), # T8: chase
            say("gotcha!"),  # T9: taunt
            chase("player"), # T10: chase faster
            chase("player"), # T11: chase
            die(),           # T12: hit by bullet!
            nop(),           # T13: dead
            nop(),           # T14: dead
            nop(),           # T15: dead
        ]),
        Channel(name="coin1", entity_type="item", rows=[
            spawn(12, 10),   # T0: coin floating
            nop(), nop(), nop(), nop(), nop(), nop(), nop(),
            nop(), nop(), nop(), nop(), nop(), nop(), nop(), nop(),
        ]),
        Channel(name="world", entity_type="world", rows=[
            nop(),           # T0: no gravity yet
            nop(),           # T1
            nop(),           # T2
            nop(),           # T3
            nop(),           # T4: gravity kicks in when player jumps
            nop(), nop(), nop(), nop(), nop(), nop(), nop(),
            nop(), nop(), nop(), nop(),
        ]),
    ])

    return demo,


@app.cell
def run_simulation(demo, World, BehaviorInterpreter):
    """Run the pattern and collect frames."""
    from dataclasses import dataclass
    from typing import List, Dict
    import copy

    @dataclass
    class Frame:
        tick: int
        entities: Dict[str, dict]
        messages: List[str]

    def run_pattern(pattern, gravity=0.3) -> List[Frame]:
        """Execute pattern and return list of frames."""
        world = World(width=32, height=16, gravity=gravity)
        interpreter = BehaviorInterpreter(world)
        frames = []

        for tick in range(pattern.length):
            # Get behaviors for this tick
            behaviors = pattern.get_tick(tick)

            # Capture frame before execution
            frame = Frame(
                tick=tick,
                entities={
                    name: {"x": e.x, "y": e.y, "alive": e.alive, "type": e.entity_type, "speech": e.speech}
                    for name, e in world.entities.items()
                },
                messages=list(world.messages)
            )
            frames.append(frame)
            world.messages.clear()

            # Clear speech bubbles from previous tick
            for e in world.entities.values():
                e.speech = ""

            # Execute this tick
            interpreter.execute_tick(behaviors)

        # Capture final frame
        frames.append(Frame(
            tick=pattern.length,
            entities={
                name: {"x": e.x, "y": e.y, "alive": e.alive, "type": e.entity_type, "speech": e.speech}
                for name, e in world.entities.items()
            },
            messages=list(world.messages)
        ))

        return frames

    frames = run_pattern(demo)

    return Frame, run_pattern, frames


@app.cell
def render_world(frames):
    """Render the world as ASCII for each frame."""

    def render_frame(frame, width=32, height=16) -> str:
        """Render a single frame as ASCII."""
        # Initialize empty grid
        grid = [['·' for _ in range(width)] for _ in range(height)]

        # Draw floor
        for x in range(width):
            grid[height-1][x] = '▀'

        # Draw entities
        symbols = {"player": "P", "enemy": "E", "item": "◆", "bullet": "→", "world": " "}
        speeches = []

        for name, e in frame.entities.items():
            if not e["alive"]:
                continue
            x, y = int(e["x"]), int(e["y"])
            if 0 <= x < width and 0 <= y < height:
                sym = symbols.get(e["type"], "?")
                grid[y][x] = sym
                if e.get("speech"):
                    speeches.append(f'{name}: "{e["speech"]}"')

        # Build output
        lines = ["".join(row) for row in grid]
        frame_str = "\n".join(lines)

        if speeches:
            frame_str += "\n" + " | ".join(speeches)

        return frame_str

    rendered_frames = [(f.tick, render_frame(f), f.messages) for f in frames]

    return render_frame, rendered_frames


@app.cell
def display_tracker_view(demo, nop):
    """Show the pattern in tracker notation."""
    import marimo as mo

    # Build tracker-style grid
    header = "Tick | " + " | ".join(f"{ch.name:12}" for ch in demo.channels)
    separator = "-" * len(header)

    rows = []
    for tick in range(demo.length):
        cells = []
        for ch in demo.channels:
            if tick < len(ch.rows):
                b = ch.rows[tick]
                cell = repr(b)[:12].ljust(12)
            else:
                cell = ".".ljust(12)
            cells.append(cell)
        rows.append(f" {tick:02} | " + " | ".join(cells))

    tracker_view = f"```\n{header}\n{separator}\n" + "\n".join(rows) + "\n```"

    tracker_output = mo.md(f"""
## Pattern: {demo.name}

{tracker_view}
""")

    return tracker_output,


@app.cell
def create_playback_ui(rendered_frames):
    """Create interactive playback."""
    import marimo as mo

    tick_slider = mo.ui.slider(
        start=0,
        stop=len(rendered_frames) - 1,
        value=0,
        label="Tick",
        show_value=True
    )

    return tick_slider,


@app.cell
def display_frame(tick_slider, rendered_frames):
    """Display the current frame."""
    import marimo as mo

    tick = tick_slider.value
    _, frame_art, messages = rendered_frames[tick]

    messages_md = "\n".join(f"- {m}" for m in messages) if messages else "*no events*"

    frame_output = mo.md(f"""
## World at Tick {tick}

```
{frame_art}
```

**Events:**
{messages_md}
""")

    return frame_output,


@app.cell
def display_all(tracker_output, tick_slider, frame_output):
    """Combine all displays."""
    import marimo as mo

    intro = mo.md("""
# Behavior Tracker

A tracker-style sequencer for game behaviors. Like ProTracker for music,
but for entity actions.

**Vocabulary**: spawn, move, jump, chase, flee, shoot, die, say, flag

**Grid**: 16 ticks × 4 channels (player, enemy, coin, world)

**Playback**: Use the slider to step through the simulation.

---
""")

    controls = mo.vstack([
        mo.md("### Playback"),
        tick_slider,
    ])

    layout = mo.vstack([
        intro,
        mo.hstack([tracker_output, mo.vstack([controls, frame_output])], justify="start"),
    ])

    return layout,


@app.cell
def reflection_layer(demo, frames):
    """What did we learn from building this?"""

    findings = [
        f"Built working tracker with {len(demo.channels)} channels × {demo.length} ticks",
        f"Simulation produced {len(frames)} frames of output",
        "Tracker notation makes behavior sequences scannable at a glance",
        "Pattern-based = easy to extend (just add more patterns)",
        "Constraint (16 ticks, verb vocabulary) forces design economy",
    ]

    insights = [
        "The tracker grid reveals RHYTHM in gameplay (spawn timings, chase patterns)",
        "Entity behaviors compose like musical voices - harmony of actions",
        "NOP/rest is as important in games as in music",
        "Speech bubbles work like tracker annotations",
        "This could work for cutscenes, tutorials, choreographed boss fights",
    ]

    next_steps = [
        "Add pattern chaining (song = sequence of patterns)",
        "Build visual editor with drag-drop behaviors",
        "Try making a real mini-game using only tracker patterns",
        "Add conditional behaviors (if flag set, do X)",
        "Export to actual game engine (Godot, Pygame)",
    ]

    return findings, insights, next_steps


if __name__ == "__main__":
    app.run()
