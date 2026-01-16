"""convergence_algebra.py

Pushing deeper into reconciliation: what's the algebra of convergence?

Observations so far:
- Reconcilers compare desired vs actual, then act
- But what happens with MULTIPLE reconcilers? Conflicting desires?
- Distributed systems solved this (CRDTs, vector clocks, consensus)
- Can we steal those patterns for knowledge/research convergence?

This notebook explores: convergence as a formal system, not just a loop.

Provenance: Deepening reconciliation_patterns
Connects to: reconciliation_patterns, kubernetes_operators_exploration, notebook_mesh
"""

import marimo

__generated_with__ = "0.9.16"
app = marimo.App(width="medium")


@app.cell
def strategic_layer():
    """The deeper questions about convergence."""

    questions = [
        "What's the algebra of reconciliation? (compose, merge, conflict)",
        "How do CRDTs achieve convergence without coordination?",
        "Can research/learning state be modeled as a CRDT?",
        "What's the 'merge function' for knowledge?",
        "How do you detect when convergence is impossible?",
    ]

    key_insight = """
    Reconciliation isn't just a loop—it's a MERGE OPERATION.

    The interesting question isn't "how do I converge?"
    It's "what happens when two reconcilers disagree?"

    Distributed systems answers:
    - Last-write-wins (crude, loses data)
    - Vector clocks (track causality)
    - CRDTs (design data so merge is always valid)
    - Consensus (agree before acting)

    Can we apply these to notebooks, research, learning?
    """

    return questions, key_insight


@app.cell
def execution_layer():
    """Implement convergence primitives."""
    from dataclasses import dataclass, field
    from typing import Any, Callable, Dict, Set, List
    from abc import ABC, abstractmethod
    import time

    # ═══════════════════════════════════════════════════════════════
    # CRDT-inspired convergent data types
    # ═══════════════════════════════════════════════════════════════

    @dataclass
    class GCounter:
        """Grow-only counter - always converges via max()."""
        counts: Dict[str, int] = field(default_factory=dict)

        def increment(self, node_id: str):
            self.counts[node_id] = self.counts.get(node_id, 0) + 1

        def value(self) -> int:
            return sum(self.counts.values())

        def merge(self, other: 'GCounter') -> 'GCounter':
            """Merge two counters - take max of each node's count."""
            merged = GCounter()
            all_nodes = set(self.counts.keys()) | set(other.counts.keys())
            for node in all_nodes:
                merged.counts[node] = max(
                    self.counts.get(node, 0),
                    other.counts.get(node, 0)
                )
            return merged

    @dataclass
    class GSet:
        """Grow-only set - always converges via union."""
        items: Set[str] = field(default_factory=set)

        def add(self, item: str):
            self.items.add(item)

        def merge(self, other: 'GSet') -> 'GSet':
            return GSet(self.items | other.items)

    @dataclass
    class LWWRegister:
        """Last-writer-wins register - converges via timestamp."""
        value: Any = None
        timestamp: float = 0.0

        def set(self, value: Any):
            self.value = value
            self.timestamp = time.time()

        def merge(self, other: 'LWWRegister') -> 'LWWRegister':
            if other.timestamp > self.timestamp:
                return LWWRegister(other.value, other.timestamp)
            return LWWRegister(self.value, self.timestamp)

    # ═══════════════════════════════════════════════════════════════
    # Research state as CRDT
    # ═══════════════════════════════════════════════════════════════

    @dataclass
    class ResearchState:
        """
        Model research/learning as convergent data.

        - topics_explored: GSet (only grows, union merges)
        - insights: GSet (findings never removed)
        - current_focus: LWWRegister (latest focus wins)
        - depth_per_topic: Dict of GCounters (depth always increases)
        """
        topics_explored: GSet = field(default_factory=GSet)
        insights: GSet = field(default_factory=GSet)
        current_focus: LWWRegister = field(default_factory=LWWRegister)
        depth: Dict[str, GCounter] = field(default_factory=dict)

        def explore(self, topic: str, node_id: str = "local"):
            self.topics_explored.add(topic)
            if topic not in self.depth:
                self.depth[topic] = GCounter()
            self.depth[topic].increment(node_id)

        def record_insight(self, insight: str):
            self.insights.add(insight)

        def focus_on(self, topic: str):
            self.current_focus.set(topic)

        def merge(self, other: 'ResearchState') -> 'ResearchState':
            """Merge two research states - always converges."""
            merged = ResearchState()
            merged.topics_explored = self.topics_explored.merge(other.topics_explored)
            merged.insights = self.insights.merge(other.insights)
            merged.current_focus = self.current_focus.merge(other.current_focus)

            # Merge depth counters
            all_topics = set(self.depth.keys()) | set(other.depth.keys())
            for topic in all_topics:
                self_depth = self.depth.get(topic, GCounter())
                other_depth = other.depth.get(topic, GCounter())
                merged.depth[topic] = self_depth.merge(other_depth)

            return merged

    # Demo: two "researchers" working independently, then merging
    alice = ResearchState()
    alice.explore("reconciliation", "alice")
    alice.explore("reconciliation", "alice")  # deeper
    alice.explore("CRDTs", "alice")
    alice.record_insight("Merge functions must be commutative")
    alice.focus_on("CRDTs")

    bob = ResearchState()
    bob.explore("reconciliation", "bob")
    bob.explore("consensus", "bob")
    bob.record_insight("Consensus requires coordination")
    bob.record_insight("CRDTs avoid coordination")
    bob.focus_on("consensus")

    # Merge - no conflicts, always valid
    merged = alice.merge(bob)

    findings = [
        f"Alice explored: {alice.topics_explored.items}",
        f"Bob explored: {bob.topics_explored.items}",
        f"Merged topics: {merged.topics_explored.items}",
        f"Merged insights: {len(merged.insights.items)} total",
        f"Reconciliation depth: {merged.depth['reconciliation'].value()} (alice:2 + bob:1)",
        f"Focus after merge: {merged.current_focus.value} (last writer wins)",
        "Key: merge() is always valid, no coordination needed",
    ]

    return GCounter, GSet, LWWRegister, ResearchState, alice, bob, merged, findings


@app.cell
def algebra_sketch():
    """Formalize the algebra of convergence."""

    algebra = """
    ## Convergence Algebra

    A convergent data type (CRDT) satisfies:

    1. **Associative**: (a ⊔ b) ⊔ c = a ⊔ (b ⊔ c)
    2. **Commutative**: a ⊔ b = b ⊔ a
    3. **Idempotent**: a ⊔ a = a

    Where ⊔ is the merge operation.

    These properties guarantee:
    - Order of merges doesn't matter
    - Duplicate merges are harmless
    - All replicas eventually converge

    ## Merge Strategies

    | Strategy | Merge ⊔ | Loses Data? | Needs Coordination? |
    |----------|---------|-------------|---------------------|
    | GSet | union | No | No |
    | GCounter | max per node | No | No |
    | LWW | latest timestamp | Yes | No |
    | 2P-Set | add wins over remove | Subtle | No |
    | Consensus | agree first | No | Yes |

    ## Application to Research

    Research state modeled as CRDTs:
    - **Topics explored** → GSet (only grows)
    - **Insights gained** → GSet (never lose insights)
    - **Current focus** → LWW (latest context wins)
    - **Depth per topic** → GCounter (effort accumulates)

    Multiple agents can research independently, merge anytime.
    No coordination overhead. No merge conflicts. Always valid.
    """

    return algebra,


@app.cell
def reflection_layer(findings):
    """What did we learn about convergence?"""

    insights = [
        "CRDTs turn merge conflicts into non-problems by design",
        "The trick: choose data structures where merge is always valid",
        "Research state CAN be modeled as convergent data",
        "GSet for knowledge (grows), LWW for attention (latest focus)",
        "This could enable truly parallel notebook exploration",
    ]

    next_steps = [
        "Implement ResearchState in notebook_mesh for real",
        "Explore 2P-Set for 'pruned' insights (add + remove)",
        "Study Automerge/Yjs for richer CRDT implementations",
        "Apply to garden_cycle: merge harvests from parallel runs",
        "Design 'knowledge CRDT' that captures learning, not just facts",
    ]

    return insights, next_steps


@app.cell
def display(key_insight, algebra, findings, insights, next_steps):
    """Render exploration."""
    import marimo as mo

    output = mo.md(f"""
# Convergence Algebra

## Key Insight

{key_insight}

{algebra}

## Demo Findings

{chr(10).join(f"- {f}" for f in findings)}

## Insights

{chr(10).join(f"- {i}" for i in insights)}

## Next Steps

{chr(10).join(f"- {s}" for s in next_steps)}
""")

    return output,


if __name__ == "__main__":
    app.run()
