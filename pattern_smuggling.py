"""pattern_smuggling.py

Pushing deeper into cross-domain translation: systematic pattern theft.

Observations so far:
- Tracker → Game DSL worked (tracker_as_dsl)
- K8s operators → Marimo reconcilers worked (reconciliation_patterns)
- But these were ad-hoc. Can we systematize?

This notebook explores: a method for finding and translating patterns.

Provenance: Deepening cross-domain observations
Connects to: tracker_as_dsl, reconciliation_patterns, all notebooks
"""

import marimo

__generated_with__ = "0.9.16"
app = marimo.App(width="medium")


@app.cell
def strategic_layer():
    """The deeper questions about pattern translation."""

    questions = [
        "What makes a pattern 'portable' across domains?",
        "How do you recognize isomorphisms between fields?",
        "What gets lost in translation? What's preserved?",
        "Can we build a 'pattern thesaurus' for systematic smuggling?",
        "Why do some transplants thrive and others fail?",
    ]

    hypothesis = """
    Portable patterns share abstract structure:

    1. ROLES: abstract participants (producer, consumer, mediator)
    2. INTERACTIONS: how roles relate (request, respond, observe)
    3. INVARIANTS: what must be true (ordering, consistency, termination)
    4. FORCES: tensions the pattern resolves (speed vs safety)

    The domain-specific parts are:
    - Vocabulary (what we call things)
    - Mechanics (how interactions happen)
    - Constraints (what's possible in this domain)

    Successful smuggling: keep structure, replace vocabulary + mechanics.
    """

    return questions, hypothesis


@app.cell
def execution_layer():
    """Build a pattern translation framework."""
    from dataclasses import dataclass
    from typing import List, Dict, Set

    @dataclass
    class AbstractPattern:
        """Domain-independent pattern structure."""
        name: str
        roles: List[str]
        interactions: List[str]
        invariants: List[str]
        forces: List[str]  # tensions it resolves

    @dataclass
    class DomainMapping:
        """How a pattern maps to a specific domain."""
        domain: str
        pattern: str
        role_bindings: Dict[str, str]  # abstract role → domain term
        mechanic_bindings: Dict[str, str]  # abstract interaction → domain mechanic
        vocabulary: Dict[str, str]  # abstract term → domain term

    @dataclass
    class PatternTranslation:
        """A documented cross-domain translation."""
        source_domain: str
        target_domain: str
        pattern: str
        what_transferred: List[str]
        what_adapted: List[str]
        what_lost: List[str]
        success_rating: str  # "thrived", "worked", "struggled", "failed"

    # Extract abstract patterns from garden notebooks
    patterns = [
        AbstractPattern(
            name="Reconciliation Loop",
            roles=["desired_state_holder", "actual_state_observer", "reconciler"],
            interactions=["observe", "compare", "act", "repeat"],
            invariants=["eventually converges", "idempotent actions"],
            forces=["consistency vs availability", "automation vs control"]
        ),
        AbstractPattern(
            name="Grid Composition",
            roles=["cell", "pattern", "composer", "player"],
            interactions=["define_cell", "group_pattern", "arrange", "playback"],
            invariants=["cells independent", "patterns reusable", "deterministic playback"],
            forces=["expressiveness vs simplicity", "flexibility vs structure"]
        ),
        AbstractPattern(
            name="Layered Processing",
            roles=["layer", "input", "output", "stack"],
            interactions=["receive", "transform", "emit", "propagate"],
            invariants=["layers isolated", "flow direction", "composition"],
            forces=["modularity vs performance", "abstraction vs visibility"]
        ),
        AbstractPattern(
            name="Effect Commands",
            roles=["command", "target", "interpreter", "state"],
            interactions=["parse", "apply", "modify_state"],
            invariants=["commands atomic", "state explicit", "reversible"],
            forces=["power vs simplicity", "flexibility vs predictability"]
        ),
    ]

    # Document translations already made in the garden
    translations = [
        PatternTranslation(
            source_domain="Kubernetes Operators",
            target_domain="Research Management",
            pattern="Reconciliation Loop",
            what_transferred=["observe/compare/act cycle", "desired vs actual model", "idempotent operations"],
            what_adapted=["CRD → research goals", "cluster state → learning state", "kubectl → notebook execution"],
            what_lost=["distributed consensus", "high availability", "formal API"],
            success_rating="thrived"
        ),
        PatternTranslation(
            source_domain="ProTracker",
            target_domain="Game Behaviors",
            pattern="Grid Composition",
            what_transferred=["row-based sequencing", "pattern reuse", "channel parallelism"],
            what_adapted=["notes → actions", "effects → modifiers", "samples → entities"],
            what_lost=["audio-specific effects", "frequency tables", "sample memory"],
            success_rating="worked"
        ),
        PatternTranslation(
            source_domain="Distributed Systems",
            target_domain="Notebook Coordination",
            pattern="Reconciliation Loop",
            what_transferred=["eventual consistency", "message passing", "state merging"],
            what_adapted=["network → filesystem", "nodes → notebooks", "protocols → JSON"],
            what_lost=["real-time guarantees", "Byzantine fault tolerance", "formal verification"],
            success_rating="worked"
        ),
    ]

    # Find potential new translations
    def suggest_translations(pattern: AbstractPattern,
                            known_domains: Set[str],
                            target_domain: str) -> List[str]:
        """Suggest how a pattern might apply to new domain."""
        suggestions = []
        for role in pattern.roles:
            suggestions.append(f"What plays the '{role}' role in {target_domain}?")
        for interaction in pattern.interactions:
            suggestions.append(f"How does '{interaction}' happen in {target_domain}?")
        return suggestions

    # Example: apply Grid Composition to new domains
    new_domain_ideas = [
        ("Dialogue Writing", "Grid Composition", [
            "cell → line of dialogue",
            "pattern → conversation template",
            "channel → character voice",
            "Could: write branching dialogue as patterns"
        ]),
        ("Learning/Spaced Repetition", "Reconciliation Loop", [
            "desired_state → knowledge target",
            "actual_state → current recall",
            "reconcile → study session",
            "Could: auto-generate study plans"
        ]),
        ("Animation", "Effect Commands", [
            "command → keyframe modifier",
            "target → sprite/property",
            "state → frame",
            "Could: tracker-style animation editor"
        ]),
    ]

    findings = [
        f"Extracted {len(patterns)} abstract patterns from garden",
        f"Documented {len(translations)} successful translations",
        f"Generated {len(new_domain_ideas)} new translation ideas",
        "Key insight: keep roles + interactions, adapt vocabulary + mechanics",
        "Translations 'thrive' when invariants match domain constraints",
    ]

    return AbstractPattern, PatternTranslation, patterns, translations, new_domain_ideas, findings


@app.cell
def smuggling_method():
    """A systematic method for pattern smuggling."""

    method = """
    ## Pattern Smuggling Method

    ### Step 1: Extract Abstract Pattern

    From source domain, identify:
    - **Roles**: Who/what participates? (not specific names)
    - **Interactions**: How do they relate? (verbs, not implementations)
    - **Invariants**: What must always be true?
    - **Forces**: What tensions does this pattern resolve?

    ### Step 2: Survey Target Domain

    In target domain, ask:
    - What entities exist? (candidate role bindings)
    - What operations exist? (candidate interaction bindings)
    - What constraints exist? (compatibility check with invariants)
    - What problems need solving? (force alignment)

    ### Step 3: Attempt Mapping

    For each role in abstract pattern:
    - Find target domain entity that could play this role
    - Check: does it have required capabilities?

    For each interaction:
    - Find target domain operation that achieves same effect
    - Check: does it preserve invariants?

    ### Step 4: Evaluate Fit

    Rate translation by:
    - **Structure match**: Do roles/interactions map cleanly?
    - **Invariant preservation**: Do domain constraints support invariants?
    - **Force alignment**: Does the pattern solve a real tension here?
    - **Vocabulary naturalness**: Does the mapping feel forced or natural?

    ### Step 5: Adapt and Test

    - Build minimal prototype in target domain
    - Note what transferred, adapted, lost
    - Iterate on mapping based on what works

    ### Red Flags (translation likely to fail)

    - Invariants conflict with domain physics
    - Key role has no natural binding
    - Forces don't exist in target domain (solving non-problem)
    - Vocabulary feels extremely forced
    """

    return method,


@app.cell
def reflection_layer(findings, new_domain_ideas):
    """What did we learn about pattern smuggling?"""

    insights = [
        "Patterns are portable when structure (roles/interactions) is preserved",
        "Vocabulary and mechanics are domain-specific wrappers",
        "Invariants must be compatible with target domain physics",
        "Best translations solve a tension that actually exists in target",
        "Failed translations often force vocabulary onto unwilling domains",
    ]

    next_steps = [
        "Try 'Dialogue as Grid Composition' translation for real",
        "Build pattern thesaurus with 10+ documented patterns",
        "Study failed translations: what went wrong?",
        "Apply method to import patterns FROM garden TO other projects",
        "Create 'pattern smuggling' skill for systematic cross-pollination",
    ]

    return insights, next_steps


@app.cell
def display(hypothesis, method, findings, new_domain_ideas, insights, next_steps):
    """Render exploration."""
    import marimo as mo

    ideas_md = "\n".join(
        f"### {domain} ← {pattern}\n" + "\n".join(f"- {m}" for m in mappings)
        for domain, pattern, mappings in new_domain_ideas
    )

    output = mo.md(f"""
# Pattern Smuggling

## Hypothesis

{hypothesis}

{method}

## New Translation Ideas

{ideas_md}

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
