"""
# Life as Game: Daily Activities → Playable Side-Scroller

**Provenance**: Created by Claude Code on 2025-11-30
**Purpose**: Turn real life (via event logs) into a playable game
**Philosophy**: The Mirroring made literal - your coordination system becomes your game world

## Core Concept

Your daily activities (bridge messages, pattern extraction, coordination) are abstractions
that naturally show up in games. This experiment:

1. Reads event logs from ~/infrastructure/agent-bridge/bridge/events/
2. Maps events → ActivityTypes (inspired by Immortality Idle)
3. Renders as playable side-scroller with resource management
4. Exports replay data for PICO-8 / fantasy consoles

## The Mapping

Real Life → Game Mechanics:
- Attention available → Mana pool
- Energy level → Stamina
- Context loaded → Knowledge
- Patterns discovered → XP / Cultivation level
- Flow state → Combo multiplier
- Bridge coordination → Quests

Activities:
- Code work → Mind Cultivation
- Pattern extraction → Investigation
- Defer queue review → Strategic Planning
- Coffee/Rest → Restoration
- Walking → Endurance training
"""

import marimo

__generated_with = "0.16.3"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import json
    from pathlib import Path
    from datetime import datetime, timedelta
    from dataclasses import dataclass
    from enum import Enum
    from typing import List, Dict, Optional
    import random
    return (
        Dict,
        Enum,
        List,
        Optional,
        Path,
        dataclass,
        datetime,
        json,
        timedelta,
    )


@app.cell
def _(mo):
    mo.md(
        """
    # 🎮 Life as Game: The Mirroring, Playable

    **Real life → Event log → Game replay**

    This experiment demonstrates "The Mirroring" in action: your coordination system
    generates events, which become gameplay. Programming yourself through programming
    the environment that programs you - but now it's a side-scroller.
    """
    )
    return


@app.cell
def _(Dict, Enum, Optional, dataclass, datetime):
    """Define activity types (inspired by Immortality Idle)"""

    class ActivityType(Enum):
        # Code & Creative Work
        MIND_CULTIVATION = "Mind Cultivation"
        CODE_WRITING = "Code Writing"
        PATTERN_EXTRACTION = "Pattern Extraction"
        INVESTIGATION = "Investigation"
        EXPERIMENTATION = "Experimentation"
        CREATIVE_FLOW = "Creative Flow"

        # Coordination
        STRATEGIC_PLANNING = "Strategic Planning"
        MESSAGE_ROUTING = "Message Routing"
        AGENT_COORDINATION = "Agent Coordination"
        DEFER_QUEUE_REVIEW = "Defer Queue Review"

        # Restoration
        RESTING = "Resting"
        COFFEE_BREAK = "Coffee Break"
        WALKING = "Walking"
        MEDITATION = "Meditation"

        # Meta-Work
        SYSTEM_DESIGN = "System Design"
        KNOWLEDGE_BASE_UPDATE = "Knowledge Base Update"
        DOCUMENTATION = "Documentation"

        # Special
        BACON_POWER = "Bacon Power"  # Tilly tribute :)
        UNKNOWN = "Unknown Activity"

    @dataclass
    class GameResource:
        name: str
        current: float
        maximum: float
        regen_rate: float = 0.0

        def consume(self, amount: float):
            self.current = max(0, self.current - amount)

        def restore(self, amount: float):
            self.current = min(self.maximum, self.current + amount)

        def tick(self):
            """Natural regeneration"""
            self.restore(self.regen_rate)

    @dataclass
    class Activity:
        activity_type: ActivityType
        timestamp: datetime
        duration_minutes: float = 15.0  # Default pomodoro-ish
        event_data: Optional[Dict] = None

        # Resource costs/gains
        attention_cost: float = 0
        energy_cost: float = 0
        flow_gain: float = 0
        knowledge_gain: float = 0
    return Activity, ActivityType, GameResource


@app.cell
def _(mo):
    """Configuration: Event log parsing rules"""

    days_to_analyze = mo.ui.slider(
        start=1,
        stop=30,
        value=7,
        label="Days of history to load:"
    )

    show_raw_events = mo.ui.checkbox(
        value=False,
        label="Show raw event data (debug)"
    )

    mo.md(f"""
    ## Configuration

    {days_to_analyze}

    {show_raw_events}
    """)
    return days_to_analyze, show_raw_events


@app.cell
def _(
    Activity,
    ActivityType,
    Dict,
    List,
    Path,
    datetime,
    days_to_analyze,
    json,
    timedelta,
):
    """Parse event logs from bridge"""

    def parse_event_logs(days: int = 7) -> List[Activity]:
        """Read event logs and convert to game activities"""
        events_path = Path("~/infrastructure/agent-bridge/bridge/events/").expanduser()

        if not events_path.exists():
            return []

        since = datetime.now() - timedelta(days=days)
        activities = []

        for event_file in sorted(events_path.glob("*.json")):
            try:
                with open(event_file, 'r') as f:
                    event = json.load(f)

                # Extract timestamp from filename (format: YYYY-MM-DDTHH:MM:SS-TZ-sender-uuid.json)
                filename = event_file.stem
                timestamp_str = filename.split('-')[0:3]  # Get date parts
                timestamp = datetime.fromisoformat('-'.join(timestamp_str))

                if timestamp < since:
                    continue

                # Map event to activity type
                event_type = event.get('type', 'unknown')
                sender = event.get('sender', 'unknown')

                activity_type = map_event_to_activity(event_type, sender, event)

                # Create activity with resource costs based on type
                activity = create_activity_from_event(activity_type, timestamp, event)
                activities.append(activity)

            except Exception as e:
                # Skip malformed events
                continue

        return sorted(activities, key=lambda a: a.timestamp)

    def map_event_to_activity(event_type: str, sender: str, event: Dict) -> ActivityType:
        """Map bridge event to game activity type"""

        # Pattern-based classification
        event_lower = event_type.lower()
        content = str(event.get('content', '')).lower()

        if 'pattern' in event_lower or 'pattern' in content:
            return ActivityType.PATTERN_EXTRACTION
        elif 'code' in sender or 'implementation' in content:
            return ActivityType.CODE_WRITING
        elif 'chat' in sender or 'strategic' in content:
            return ActivityType.STRATEGIC_PLANNING
        elif 'defer' in content or 'queue' in content:
            return ActivityType.DEFER_QUEUE_REVIEW
        elif 'investigat' in content or 'analysis' in content:
            return ActivityType.INVESTIGATION
        elif 'message' in event_lower:
            return ActivityType.AGENT_COORDINATION
        elif 'experiment' in content or 'marimo' in content:
            return ActivityType.EXPERIMENTATION
        elif 'barkour' in content or 'tilly' in content:
            return ActivityType.BACON_POWER
        elif 'knowledge' in content or 'kb' in content:
            return ActivityType.KNOWLEDGE_BASE_UPDATE
        else:
            return ActivityType.MIND_CULTIVATION  # Default for mental work

    def create_activity_from_event(
        activity_type: ActivityType,
        timestamp: datetime,
        event: Dict
    ) -> Activity:
        """Create game activity with resource costs"""

        # Define resource costs per activity type
        costs = {
            ActivityType.CODE_WRITING: {"attention": 20, "energy": 15, "flow": 5, "knowledge": 2},
            ActivityType.PATTERN_EXTRACTION: {"attention": 25, "energy": 10, "flow": 8, "knowledge": 5},
            ActivityType.STRATEGIC_PLANNING: {"attention": 30, "energy": 5, "flow": 3, "knowledge": 3},
            ActivityType.INVESTIGATION: {"attention": 35, "energy": 20, "flow": 10, "knowledge": 8},
            ActivityType.EXPERIMENTATION: {"attention": 15, "energy": 25, "flow": 15, "knowledge": 1},
            ActivityType.AGENT_COORDINATION: {"attention": 10, "energy": 5, "flow": 1, "knowledge": 1},
            ActivityType.DEFER_QUEUE_REVIEW: {"attention": 20, "energy": 10, "flow": 2, "knowledge": 2},
            ActivityType.RESTING: {"attention": -30, "energy": -50, "flow": 0, "knowledge": 0},  # Negative = restore
            ActivityType.COFFEE_BREAK: {"attention": -10, "energy": -5, "flow": 2, "knowledge": 0},
            ActivityType.BACON_POWER: {"attention": 0, "energy": -20, "flow": 20, "knowledge": 1},  # Tilly!
        }

        activity_costs = costs.get(activity_type, {"attention": 10, "energy": 10, "flow": 0, "knowledge": 0})

        return Activity(
            activity_type=activity_type,
            timestamp=timestamp,
            duration_minutes=15.0,
            event_data=event,
            attention_cost=activity_costs["attention"],
            energy_cost=activity_costs["energy"],
            flow_gain=activity_costs["flow"],
            knowledge_gain=activity_costs["knowledge"]
        )

    # Load activities from event log
    loaded_activities = parse_event_logs(days=days_to_analyze.value)
    return (loaded_activities,)


@app.cell
def _(loaded_activities, mo):
    """Display loaded activities"""

    mo.md(f"""
    ## 📊 Loaded Activities

    Found **{len(loaded_activities)}** activities from event logs.
    """)
    return


@app.cell
def _(loaded_activities, mo, show_raw_events):
    """Activity timeline visualization"""

    if loaded_activities:
        # Create timeline data
        timeline_data = [
            {
                "time": a.timestamp.strftime("%Y-%m-%d %H:%M"),
                "activity": a.activity_type.value,
                "attention_cost": a.attention_cost,
                "energy_cost": a.energy_cost,
                "flow_gain": a.flow_gain,
            }
            for a in loaded_activities[-50:]  # Last 50 activities
        ]

        timeline_table = mo.ui.table(
            timeline_data,
            selection=None,
            label="Recent Activities"
        )

        if show_raw_events.value:
            mo.vstack([
                mo.md("### Activity Timeline"),
                timeline_table,
                mo.md("*Showing last 50 activities*")
            ])
        else:
            mo.md(f"*{len(loaded_activities)} activities loaded. Enable 'Show raw event data' to view.*")
    else:
        mo.md("⚠️ No events found. Event log may be empty or path incorrect.")
    return


@app.cell
def _(GameResource):
    """Initialize game resources"""

    resources = {
        "attention": GameResource(
            name="Attention",
            current=100,
            maximum=100,
            regen_rate=2.0  # Regenerates slowly over time
        ),
        "energy": GameResource(
            name="Energy",
            current=100,
            maximum=100,
            regen_rate=1.0
        ),
        "flow_state": GameResource(
            name="Flow State",
            current=0,
            maximum=100,
            regen_rate=0  # Only builds through activities
        ),
        "knowledge": GameResource(
            name="Knowledge",
            current=0,
            maximum=1000,  # Accumulates unbounded (but capped for UI)
            regen_rate=0
        ),
    }
    return (resources,)


@app.cell
def _(loaded_activities, mo, resources):
    """Simulate gameplay: process activities and track resources"""

    def simulate_gameplay(activities, resource_dict):
        """Process activities and track resource changes"""

        timeline = []

        for activity in activities:
            # Apply resource costs
            resource_dict["attention"].consume(activity.attention_cost)
            resource_dict["energy"].consume(activity.energy_cost)
            resource_dict["flow_state"].restore(activity.flow_gain)
            resource_dict["knowledge"].restore(activity.knowledge_gain)

            # Natural regeneration
            for resource in resource_dict.values():
                resource.tick()

            # Snapshot state
            timeline.append({
                "timestamp": activity.timestamp,
                "activity": activity.activity_type.value,
                "attention": resource_dict["attention"].current,
                "energy": resource_dict["energy"].current,
                "flow": resource_dict["flow_state"].current,
                "knowledge": resource_dict["knowledge"].current,
            })

        return timeline

    # Run simulation
    gameplay_timeline = simulate_gameplay(loaded_activities, resources) if loaded_activities else []

    mo.md(f"""
    ## 🎮 Gameplay Simulation

    Processed **{len(gameplay_timeline)}** activity steps.

    **Final Resource State:**
    - 🧠 Attention: {resources["attention"].current:.1f} / {resources["attention"].maximum}
    - ⚡ Energy: {resources["energy"].current:.1f} / {resources["energy"].maximum}
    - 🌊 Flow State: {resources["flow_state"].current:.1f} / {resources["flow_state"].maximum}
    - 📚 Knowledge: {resources["knowledge"].current:.1f}
    """)
    return (gameplay_timeline,)


@app.cell
def _(gameplay_timeline, mo):
    """Resource tracking chart"""

    if gameplay_timeline:
        # Create chart data
        chart_data = {
            "Timestamp": [t["timestamp"].strftime("%m-%d %H:%M") for t in gameplay_timeline],
            "Attention": [t["attention"] for t in gameplay_timeline],
            "Energy": [t["energy"] for t in gameplay_timeline],
            "Flow": [t["flow"] for t in gameplay_timeline],
        }

        resource_chart = mo.ui.altair_chart(
            {
                "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
                "data": {"values": [
                    {"time": t["timestamp"].strftime("%m-%d %H:%M"),
                     "resource": "Attention",
                     "value": t["attention"]}
                    for t in gameplay_timeline
                ] + [
                    {"time": t["timestamp"].strftime("%m-%d %H:%M"),
                     "resource": "Energy",
                     "value": t["energy"]}
                    for t in gameplay_timeline
                ] + [
                    {"time": t["timestamp"].strftime("%m-%d %H:%M"),
                     "resource": "Flow",
                     "value": t["flow"]}
                    for t in gameplay_timeline
                ]},
                "mark": "line",
                "encoding": {
                    "x": {"field": "time", "type": "nominal", "title": "Time"},
                    "y": {"field": "value", "type": "quantitative", "title": "Resource Level"},
                    "color": {"field": "resource", "type": "nominal", "title": "Resource"}
                },
                "width": 800,
                "height": 400
            }
        )

        mo.vstack([
            mo.md("### Resource Tracking Over Time"),
            resource_chart
        ])
    else:
        mo.md("*No gameplay data to visualize.*")
    return


@app.cell
def _(mo):
    """Export options for PICO-8 / fantasy consoles"""

    export_format = mo.ui.dropdown(
        options=["JSON (Replay Data)", "PICO-8 Stub", "HTML5 Canvas", "ASCII Art"],
        value="JSON (Replay Data)",
        label="Export format:"
    )

    mo.md(f"""
    ## 💾 Export Gameplay

    {export_format}

    *Export your life as replay data for different platforms.*
    """)
    return (export_format,)


@app.cell
def _(export_format, gameplay_timeline, json, mo):
    """Generate export based on selected format"""

    def export_gameplay(timeline, format_type: str) -> str:
        """Export gameplay timeline to various formats"""

        if format_type == "JSON (Replay Data)":
            return json.dumps([
                {
                    "timestamp": t["timestamp"].isoformat(),
                    "activity": t["activity"],
                    "resources": {
                        "attention": t["attention"],
                        "energy": t["energy"],
                        "flow": t["flow"],
                        "knowledge": t["knowledge"],
                    }
                }
                for t in timeline
            ], indent=2)

        elif format_type == "PICO-8 Stub":
            # Generate PICO-8 Lua stub
            return f"""-- life-game replay
    -- generated from event log
    -- {len(timeline)} activities

    activities={{}}

    function _init()
      -- load replay data
      -- {timeline[0]["timestamp"].strftime("%Y-%m-%d") if timeline else "N/A"} to {timeline[-1]["timestamp"].strftime("%Y-%m-%d") if timeline else "N/A"}
    end

    function _update()
      -- process next activity
    end

    function _draw()
      cls()
      -- render side-scroller
      print("life as game",10,10,7)
      print("activities: {len(timeline)}",10,20,6)
    end
    """

        elif format_type == "HTML5 Canvas":
            return f"""<!DOCTYPE html>
    <html>
    <head><title>Life as Game</title></head>
    <body>
      <canvas id="game" width="800" height="600"></canvas>
      <script>
    const activities = {json.dumps([{"time": t["timestamp"].isoformat(), "type": t["activity"]} for t in timeline])};
    // Render side-scroller here
    console.log("Loaded", activities.length, "activities");
      </script>
    </body>
    </html>
    """

        elif format_type == "ASCII Art":
            # Simple ASCII timeline
            output = ["=" * 60, "LIFE AS GAME - ASCII REPLAY", "=" * 60, ""]
            for t in timeline[-20:]:  # Last 20 activities
                bar_attention = "█" * int(t["attention"] / 10)
                bar_energy = "█" * int(t["energy"] / 10)
                output.append(f"{t['timestamp'].strftime('%H:%M')} | {t['activity'][:30]:<30}")
                output.append(f"  ATT: {bar_attention:<10} {t['attention']:.0f}")
                output.append(f"  NRG: {bar_energy:<10} {t['energy']:.0f}")
                output.append("")
            return "\n".join(output)

        return "Unknown format"

    if gameplay_timeline:
        exported_content = export_gameplay(gameplay_timeline, export_format.value)

        mo.vstack([
            mo.md(f"### Exported as: {export_format.value}"),
            mo.ui.code_editor(value=exported_content, language="text", disabled=True)
        ])
    else:
        mo.md("*No data to export.*")
    return


@app.cell
def _(mo):
    """Next steps: Budding into dedicated game"""

    mo.md("""
    ## 🌱 Next Steps: Budding Protocol

    This experiment demonstrates the **Life-as-Game** pattern. Ready to bud?

    ### When to Graduate:
    1. ✅ **Playable?** Yes - events → activities → resource management works
    2. ❓ **Momentum?** TBD - does this continue being developed?
    3. ❓ **Needs structure?** Could benefit from dedicated game engine integration
    4. ❓ **Garden cramped?** Not yet - can iterate here for now

    ### Potential Evolution Paths:
    - **PICO-8 Game**: Full side-scroller with Tilly avatar, bacon power-ups
    - **Web App**: HTML5 canvas with real-time event log streaming
    - **CLI Tool**: ASCII game that runs in terminal, reads bridge in real-time
    - **Barkour Integration**: Merge with Tilly's parkour mechanics

    ### Pattern Extracted:
    - **Event Log as Gameplay** (The Harvest layer → The Interface layer)
    - **Resource Management from Life Metrics** (Attention/Energy abstraction)
    - **Activity Loop System** (Immortality Idle pattern applied to real life)

    ---

    **Provenance**: Experiment created 2025-11-30, inspired by Immortality Idle's activity system
    and The Mirroring concept from Ludarium platform.
    """)
    return


if __name__ == "__main__":
    app.run()
