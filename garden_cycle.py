"""garden_cycle.py

Harvests insights from all notebooks and displays them for review.

Run this to see what's been learned across experiments, then ask Claude Code
to propose new experiments based on the aggregated insights.

Run: marimo run garden_cycle.py
"""

import marimo

__generated_with__ = "0.9.16"
app = marimo.App(width="medium")


@app.cell
def discover_notebooks():
    """Find all marimo notebooks in the garden."""
    from pathlib import Path

    garden = Path(__file__).parent
    excluded = {"garden_cycle.py", "__init__.py"}

    notebooks = []
    for p in garden.glob("*.py"):
        if p.name in excluded:
            continue
        content = p.read_text()
        if not content.startswith('"""'):
            continue

        # Extract description from docstring
        lines = content.split('\n')
        desc = ""
        for line in lines[1:10]:
            line = line.strip()
            if line and not line.startswith('"""'):
                desc = line[:80]
                break

        notebooks.append({
            "path": p,
            "name": p.stem,
            "description": desc or p.stem
        })

    return Path, garden, notebooks


@app.cell
def harvest_insights(notebooks):
    """Extract findings and next_steps from each notebook."""
    import re

    def extract_findings(path):
        content = path.read_text()
        findings = []

        # From findings=[ ] blocks
        for block in re.findall(r'findings\s*[=:]\s*\[(.*?)\]', content, re.DOTALL):
            findings.extend(re.findall(r'"([^"]{20,200})"', block))

        # From summary= strings
        findings.extend(re.findall(r'summary\s*[=:]\s*f?"([^"]{20,200})"', content))

        # Filter code-like strings
        findings = [f for f in findings if not any(x in f for x in ['=', 'import', 'def ', 'class '])]
        return list(set(findings))[:8]

    def extract_next_steps(path):
        content = path.read_text()
        steps = []
        for block in re.findall(r'next_steps\s*[=:]\s*\[(.*?)\]', content, re.DOTALL):
            steps.extend(re.findall(r'"([^"]+)"', block))
        return list(set(steps))[:5]

    harvested = []
    for nb in notebooks:
        findings = extract_findings(nb["path"])
        next_steps = extract_next_steps(nb["path"])
        harvested.append({
            "name": nb["name"],
            "description": nb["description"],
            "findings": findings,
            "next_steps": next_steps
        })

    return extract_findings, extract_next_steps, harvested


@app.cell
def display_overview(notebooks, harvested):
    """Display garden overview."""
    import marimo as mo

    total_findings = sum(len(h["findings"]) for h in harvested)
    total_next_steps = sum(len(h["next_steps"]) for h in harvested)

    output = mo.md(f"""
# Garden Cycle

**{len(notebooks)}** notebooks | **{total_findings}** findings | **{total_next_steps}** proposed directions

---
""")
    return output,


@app.cell
def display_notebooks(harvested):
    """Display each notebook's harvest."""
    import marimo as mo

    sections = []
    for h in harvested:
        if not h["findings"] and not h["next_steps"]:
            sections.append(f"### {h['name']}\n_{h['description']}_\n\n*No structured findings yet.*\n")
            continue

        section = f"### {h['name']}\n_{h['description']}_\n\n"

        if h["findings"]:
            section += "**Findings:**\n"
            for f in h["findings"]:
                section += f"- {f}\n"
            section += "\n"

        if h["next_steps"]:
            section += "**Next steps:**\n"
            for s in h["next_steps"]:
                section += f"- {s}\n"

        sections.append(section)

    output = mo.md("\n---\n".join(sections))
    return output,


@app.cell
def display_aggregate(harvested):
    """Aggregate all next_steps as potential new experiments."""
    import marimo as mo

    all_steps = []
    for h in harvested:
        for step in h["next_steps"]:
            all_steps.append(f"- {step} *(from {h['name']})*")

    if not all_steps:
        steps_md = "*No next steps harvested yet. Add findings to your notebooks.*"
    else:
        steps_md = "\n".join(all_steps)

    output = mo.md(f"""
---

## Potential New Experiments

These directions emerged from existing notebooks:

{steps_md}

---

**To generate new experiments**: Copy this output and ask Claude Code:
> "Based on these garden insights, propose 3 new experiments."

""")
    return output,


@app.cell
def scaffold():
    """Minimal scaffold for new experiments."""
    import marimo as mo

    template = '''"""new_experiment.py

[Description of what you're exploring]

Provenance: Inspired by garden_cycle harvest
"""

import marimo
app = marimo.App(width="medium")


@app.cell
def explore():
    """What are we investigating?"""
    questions = [
        "Question 1?",
        "Question 2?",
    ]
    return questions,


@app.cell
def findings(questions):
    """What did we discover?"""
    findings = [
        # Add findings as you explore
    ]
    next_steps = [
        # What should come next?
    ]
    return findings, next_steps,


if __name__ == "__main__":
    app.run()
'''

    output = mo.md(f"""
## Scaffold

When creating a new experiment:

```python
{template}
```
""")
    return output, template


if __name__ == "__main__":
    app.run()
