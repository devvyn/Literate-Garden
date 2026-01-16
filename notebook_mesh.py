"""notebook_mesh.py

Exploring cross-notebook coordination.

Agent_strata asks: "Can agents coordinate across notebooks?"
Garden_cycle harvests but doesn't enable notebook-to-notebook communication.

Can we build a simple mesh where notebooks talk to each other?

Provenance: Inspired by garden_cycle harvest
Connects to: agent_strata (open question), garden_cycle
"""

import marimo

__generated_with__ = "0.9.16"
app = marimo.App(width="medium")


@app.cell
def strategic_layer():
    """What are we trying to understand?"""
    questions = [
        "What's the minimal coordination protocol between notebooks?",
        "Can notebook A's reflection trigger notebook B's execution?",
        "How do you avoid circular dependencies?",
        "Can the mesh be self-organizing (notebooks discover each other)?",
    ]

    hypothesis = """
    Simple file-based IPC could work:
    - Each notebook writes to .mesh/{notebook_name}.json
    - Contains: findings, next_steps, requests_for_others
    - Other notebooks read on startup, act on relevant requests

    No daemon needed - coordination happens when notebooks run.
    """

    return questions, hypothesis


@app.cell
def execution_layer(questions):
    """Build minimal mesh infrastructure."""
    from dataclasses import dataclass, asdict
    from typing import List, Dict, Any
    from pathlib import Path
    import json
    import datetime

    MESH_DIR = Path(__file__).parent / ".mesh"

    @dataclass
    class MeshMessage:
        """Message from one notebook to the mesh."""
        from_notebook: str
        timestamp: str
        findings: List[str]
        next_steps: List[str]
        requests: List[Dict[str, Any]]  # {to: "notebook", action: "...", params: {...}}

    class NotebookMesh:
        """Simple file-based mesh coordination."""

        def __init__(self, notebook_name: str):
            self.name = notebook_name
            self.mesh_dir = MESH_DIR
            self.mesh_dir.mkdir(exist_ok=True)

        def broadcast(self, findings: List[str], next_steps: List[str],
                     requests: List[Dict] = None) -> Path:
            """Write this notebook's state to the mesh."""
            msg = MeshMessage(
                from_notebook=self.name,
                timestamp=datetime.datetime.utcnow().isoformat(),
                findings=findings,
                next_steps=next_steps,
                requests=requests or []
            )
            path = self.mesh_dir / f"{self.name}.json"
            path.write_text(json.dumps(asdict(msg), indent=2))
            return path

        def receive(self) -> Dict[str, MeshMessage]:
            """Read all messages from other notebooks."""
            messages = {}
            for f in self.mesh_dir.glob("*.json"):
                if f.stem == self.name:
                    continue  # skip own message
                try:
                    data = json.loads(f.read_text())
                    messages[f.stem] = MeshMessage(**data)
                except Exception:
                    pass  # ignore malformed
            return messages

        def get_requests_for_me(self) -> List[Dict]:
            """Get requests addressed to this notebook."""
            requests = []
            for name, msg in self.receive().items():
                for req in msg.requests:
                    if req.get("to") == self.name:
                        req["from"] = name
                        requests.append(req)
            return requests

    # Demo: create mesh and broadcast
    mesh = NotebookMesh("notebook_mesh")

    # Broadcast our findings
    broadcast_path = mesh.broadcast(
        findings=[
            "File-based IPC is simple and works",
            "No daemon needed - lazy coordination",
            "JSON is human-readable for debugging",
        ],
        next_steps=[
            "Test with multiple notebooks writing/reading",
            "Add request/response pattern",
            "Handle stale messages (TTL?)",
        ],
        requests=[
            {"to": "kubernetes_operators_exploration",
             "action": "explore",
             "params": {"topic": "operator-to-operator communication"}}
        ]
    )

    # Check what others have broadcast
    other_messages = mesh.receive()
    requests_for_us = mesh.get_requests_for_me()

    findings = [
        f"Broadcast to: {broadcast_path}",
        f"Found {len(other_messages)} messages from other notebooks",
        f"Requests for us: {len(requests_for_us)}",
        "Mesh protocol: broadcast + poll (no push)",
    ]

    return NotebookMesh, MeshMessage, mesh, findings, other_messages


@app.cell
def mesh_protocol_sketch(findings):
    """Sketch the full mesh protocol."""

    protocol = """
    ## Mesh Protocol v0.1

    ### Broadcast (write)
    ```python
    mesh.broadcast(
        findings=["what I learned"],
        next_steps=["what I'll explore next"],
        requests=[
            {"to": "other_notebook", "action": "...", "params": {...}}
        ]
    )
    ```

    ### Receive (read)
    ```python
    messages = mesh.receive()  # all other notebooks' broadcasts
    requests = mesh.get_requests_for_me()  # filtered to my name
    ```

    ### Request Actions (extensible)
    - `explore`: ask another notebook to research something
    - `validate`: ask for review of findings
    - `spawn`: suggest creating a new notebook
    - `merge`: suggest consolidating findings

    ### Conflict Resolution
    - Last-write-wins for broadcast (simple)
    - Requests are append-only until acknowledged
    - Circular deps: detect via request chain, refuse after N hops
    """

    return protocol,


@app.cell
def reflection_layer(findings, other_messages):
    """What did we learn?"""

    insights = [
        "File-based mesh is ~50 lines of code",
        "Lazy coordination (poll, not push) fits marimo's run-on-demand model",
        "Requests create a simple task queue between notebooks",
        "Self-organization: notebooks discover each other by scanning .mesh/",
    ]

    next_steps = [
        "Have kubernetes_operators_exploration broadcast its findings",
        "Test request handling - can one notebook trigger another?",
        "Add TTL to messages (expire after N hours)",
        "Build mesh dashboard showing all notebook states",
    ]

    return insights, next_steps


@app.cell
def display(hypothesis, protocol, findings, other_messages, insights, next_steps):
    """Display exploration results."""
    import marimo as mo

    others_md = "\n".join(f"- **{name}**: {len(msg.findings)} findings, {len(msg.requests)} requests"
                         for name, msg in other_messages.items()) or "*No other notebooks in mesh yet*"

    output = mo.md(f"""
# Notebook Mesh

## Hypothesis

{hypothesis}

## Protocol Sketch

{protocol}

## Current Mesh State

{others_md}

## Findings

{chr(10).join(f"- {f}" for f in findings)}

## Insights

{chr(10).join(f"- {i}" for i in insights)}

## Next Steps

{chr(10).join(f"- {s}" for s in next_steps)}
""")

    return output,


if __name__ == "__main__":
    app.run()
