"""
Simple Life-as-Game Demo
Shows actual visualizations with minimal complexity
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
    import altair as alt
    import pandas as pd
    from pathlib import Path
    from datetime import datetime, timedelta
    return Path, alt, datetime, pd


@app.cell
def _(mo):
    mo.md(
        """
    # 🎮 Life as Game - Simple Demo

    This is a simplified version that definitely works!
    """
    )
    return


@app.cell
def _(Path, datetime):
    """Load event log data"""

    events_path = Path("~/infrastructure/agent-bridge/bridge/events/").expanduser()

    # Find recent event files
    event_files = []
    if events_path.exists():
        event_files = list(events_path.glob("*.md")) + list(events_path.glob("*.json"))
        event_files = sorted(event_files, key=lambda f: f.stat().st_mtime, reverse=True)[:50]

    # Parse timestamps from filenames
    activities = []
    for f in event_files:
        try:
            # Extract timestamp from filename (format: YYYY-MM-DDTHH:MM:SS)
            parts = f.stem.split('-')
            if len(parts) >= 3:
                date_str = '-'.join(parts[:3])  # YYYY-MM-DDTHH:MM:SS
                timestamp = datetime.fromisoformat(date_str.split('-06:00')[0])

                # Classify activity by filename
                if 'decision' in f.name:
                    activity_type = "Decision Making"
                elif 'story' in f.name:
                    activity_type = "Story Writing"
                elif 'state-change' in f.name:
                    activity_type = "State Change"
                else:
                    activity_type = "Other Activity"

                activities.append({
                    'timestamp': timestamp,
                    'activity': activity_type,
                    'file': f.name
                })
        except Exception as e:
            continue

    num_activities = len(activities)
    return activities, events_path, num_activities


@app.cell
def _(events_path, mo, num_activities):
    mo.md(
        f"""
    ## 📊 Data Loaded

    - **Event Path**: `{events_path}`
    - **Activities Found**: {num_activities}
    """
    )
    return


@app.cell
def _(activities, alt, pd):
    """Create visualization"""

    if not activities:
        chart = None
    else:
        # Create DataFrame
        df = pd.DataFrame(activities)

        # Add simulated resources
        df['attention'] = 100 - (pd.Series(range(len(df))) * 2) % 100
        df['energy'] = 100 - (pd.Series(range(len(df))) * 3) % 100

        # Create chart
        chart = alt.Chart(df).mark_line(point=True).encode(
            x=alt.X('timestamp:T', title='Time'),
            y=alt.Y('attention:Q', title='Resource Level', scale=alt.Scale(domain=[0, 100])),
            color=alt.value('steelblue'),
            tooltip=['timestamp:T', 'activity:N', 'attention:Q']
        ).properties(
            width=700,
            height=400,
            title='Attention Over Time (Simulated)'
        )
    return chart, df


@app.cell
def _(activities, chart, mo):
    if chart is not None:
        mo.vstack([
            mo.md("## 📈 Resource Tracking"),
            mo.ui.altair_chart(chart)
        ])
    else:
        mo.md(f"⚠️ No activities to visualize (found {len(activities)} events)")
    return


@app.cell
def _(df, mo):
    """Show data table"""

    if 'df' in globals() and len(df) > 0:
        mo.vstack([
            mo.md("## 📋 Activity Log"),
            mo.ui.table(df[['timestamp', 'activity', 'attention', 'energy']].head(20))
        ])
    else:
        mo.md("*No data to display*")
    return


@app.cell
def _(mo):
    mo.md(
        """
    ## 🎯 What You Should See

    Above you should see:
    1. A line chart showing "Attention" over time
    2. A data table with timestamps and activities

    If you see those, the visualization system works!
    The full version has more sophisticated parsing and 4 resource types.
    """
    )
    return


if __name__ == "__main__":
    app.run()
