# 🌸 Budding Guide: From Garden to Dedicated Repository

How to graduate successful experiments from the Literate Garden to production projects.

---

## Philosophy

The Literate Garden is for **rapid experimentation**. When a prototype proves:
1. **Playable** — Users can meaningfully interact
2. **Momentum** — Clear path for continued development
3. **Structure-ready** — Would benefit from formal specs, testing, or team coordination
4. **Garden-cramped** — Too complex for quick iteration

...it's time to **bud** into a dedicated repository with appropriate governance.

---

## Current Budding Candidates

### 🌟 High Priority

#### 1. Lighthouse Palimpsest
**Status:** Ready to bud
**Recommended Governance:** Spec-driven with narrative design docs
**Team:** 1 narrative designer + 1 technical artist + 1 programmer
**Timeline:** 12-week vertical slice
**Festival Target:** IGF Excellence in Narrative, Day of the Devs

**Budding Checklist:**
- [ ] Create `~/Documents/GitHub/lighthouse-palimpsest/`
- [ ] Extract `experiments/palimpsest/web/lighthouse-palimpsest.html` as foundation
- [ ] Set up spec-driven development (GitHub spec-kit integration)
- [ ] Create `CLAUDE.md` with narrative design authority domains
- [ ] Document shader research from `experiments/palimpsest/docs/`
- [ ] Establish timeline and milestone tracking

---

#### 2. Aurora Chord Pilgrimage
**Status:** Ready to bud
**Recommended Governance:** Scientific project with music theory validation
**Team:** 1 composer + 1 audio programmer + 1 game designer
**Timeline:** 10-week interactive prototype
**Festival Target:** IGF Nuovo, IndieCade Innovation

**Budding Checklist:**
- [ ] Create `~/Documents/GitHub/aurora-chord-pilgrimage/`
- [ ] Extract `experiments/clockwork/web/aurora_chord.html`
- [ ] Validate music theory mechanics with domain expert
- [ ] Set up audio middleware integration plan
- [ ] Create `CLAUDE.md` with composer collaboration protocols
- [ ] Coordinate with Python Toolbox for audio analysis utilities

---

#### 3. Bloom//Breaker
**Status:** High potential, needs networking R&D
**Recommended Governance:** Library project with comprehensive testing
**Team:** 2 gameplay programmers + 1 VFX artist + 1 network engineer
**Timeline:** 16-week networked prototype
**Festival Target:** SXSW Gaming Awards, MIX

**Budding Checklist:**
- [ ] Research deterministic netcode solutions (Photon Fusion vs bespoke)
- [ ] Prototype procedural foliage system
- [ ] Create `~/Documents/GitHub/bloom-breaker/`
- [ ] Set up testing infrastructure for networked gameplay
- [ ] Create `CLAUDE.md` with networking architecture constraints
- [ ] Evaluate Godot 4 GDExtension for foliage performance

---

## Budding Process Template

### Step 1: Create New Repository

```bash
cd ~/Documents/GitHub/
mkdir [project-name]
cd [project-name]
git init
```

### Step 2: Extract Garden Artifacts

```bash
# Copy relevant files from Literate Garden
cp ~/Documents/GitHub/Literate-Garden/experiments/[collection]/web/[demo].html ./prototype.html
cp ~/Documents/GitHub/Literate-Garden/experiments/[collection]/docs/* ./docs/

# Preserve provenance
echo "# Provenance

This project budded from the Literate Garden on $(date +%Y-%m-%d).

**Garden Origin:**
- Collection: [collection name]
- Concept Document: experiments/[collection]/docs/concepts.md
- Interactive Prototype: experiments/[collection]/web/[demo].html

**Reason for Budding:**
[Explain why this graduated from the garden]

**Literate Garden Commit:** $(cd ~/Documents/GitHub/Literate-Garden && git rev-parse HEAD)
" > PROVENANCE.md
```

### Step 3: Choose Governance Model

Select appropriate governance based on project type:

#### A. Spec-Driven Project
```bash
# For narrative-heavy or scientifically-validated projects
# Example: Lighthouse Palimpsest, Aurora Chord Pilgrimage

# Create CLAUDE.md inheriting meta-project + spec-kit patterns
cat > CLAUDE.md << 'EOF'
# Claude Agent Instructions - [Project Name]

**Context Level**: 3 (Sub-Project)
**Inherits From**: Meta-project spec-driven development framework
**Governance**: GitHub spec-kit for formal requirement management

## Authority Domains

### Human Domain
- Domain expertise validation (narrative/music theory/etc)
- Specification approval
- Quality gates for creative direction

### Code Agent Domain
- Technical implementation from approved specs
- Prototyping and vertical slice development

### Chat Agent Domain
- Specification drafting
- Pattern recognition from portfolio
EOF
```

#### B. Library Project
```bash
# For technical utilities or reusable systems
# Example: Bloom//Breaker (if networking toolkit extracted)

# Create CLAUDE.md with testing + versioning focus
cat > CLAUDE.md << 'EOF'
# Claude Agent Instructions - [Project Name]

**Context Level**: 3 (Sub-Project)
**Inherits From**: Python Toolbox library patterns
**Governance**: Comprehensive testing + semantic versioning

## Quality Standards
- 90%+ test coverage
- Semantic versioning (SemVer)
- API stability guarantees
EOF
```

#### C. Scientific Project
```bash
# For domain-validated or curator-reviewed work
# Example: Aurora Chord Pilgrimage (music theory validation)

# Create CLAUDE.md with constitutional governance
cat > CLAUDE.md << 'EOF'
# Claude Agent Instructions - [Project Name]

**Context Level**: 3 (Sub-Project)
**Inherits From**: AAFC Herbarium scientific validation patterns
**Governance**: Domain expert validation, constitutional quality gates
EOF
```

### Step 4: Set Up Project Infrastructure

```bash
# Initialize project structure
mkdir -p {src,docs,tests,assets,prototypes}

# Create README with budding context
cat > README.md << 'EOF'
# [Project Name]

**Budded from:** [Literate Garden](https://github.com/devvyn/Literate-Garden)
**Collection:** [Collection Name]
**Status:** Vertical Slice Development

## Provenance

This project graduated from the Literate Garden experimental greenhouse on [date].
See PROVENANCE.md for full lineage.

## Getting Started

[Project-specific setup instructions]
EOF

# Set up git
git add .
git commit -m "Initial commit: budded from Literate Garden

Provenance: experiments/[collection]/web/[demo].html
Reason: [explanation of why this budded]
Garden commit: [hash]

$(cat PROVENANCE.md)"
```

### Step 5: Register with Meta-Project

```bash
# Coordinate through bridge system
cd ~/devvyn-meta-project

# Create budding notification
cat > /tmp/budding-notification.md << 'EOF'
# New Project Budded from Literate Garden

**Project:** [Project Name]
**Origin:** Literate Garden → [Collection] → [Concept]
**Governance:** [Spec-driven/Library/Scientific]
**Team:** [Team composition]
**Timeline:** [Development timeline]

## Coordination Needs

- [ ] Portfolio tracking update
- [ ] Bridge system registration
- [ ] Cross-project pattern library sync
- [ ] Festival submission coordination

## Next Steps

[Immediate next actions for the new project]
EOF

./scripts/bridge-send.sh code chat NORMAL "[Project Name] budded from Garden" /tmp/budding-notification.md
```

### Step 6: Update Garden Records

```bash
cd ~/Documents/GitHub/Literate-Garden

# Document the budding in garden
echo "
## Budded Projects

### [Project Name]
- **Budded:** $(date +%Y-%m-%d)
- **Collection:** [Collection]
- **New Repo:** ~/Documents/GitHub/[project-name]/
- **Reason:** [Brief explanation]
- **Status:** [Vertical Slice/Alpha/etc]
" >> experiments/BUDDING_LOG.md

# Update CLAUDE.md with budding record
# (Track graduated experiments for cross-pollination)
```

---

## Post-Budding: Garden Maintenance

### Option A: Archive in Garden
Keep the original experiment as reference:

```bash
# Mark as budded in experiments/README.md
# Add "🌸 BUDDED" badge to concept description
```

### Option B: Prune from Garden
Remove if no longer useful for reference:

```bash
# Move to experiments/archive/
mkdir -p experiments/archive
mv experiments/[collection]/web/[demo].html experiments/archive/

# Document in BUDDING_LOG.md why it was archived
```

---

## Integration with Portfolio

### Meta-Project Tracking
- Add to `~/devvyn-meta-project/status/current-project-state.json`
- Update portfolio capacity (Framework v2.1 tier management)
- Register with bridge system for coordination

### Cross-Project Patterns
- Extract reusable patterns to pattern library
- Coordinate with Python Toolbox for shared utilities
- Connect to AAFC Herbarium for scientific validation patterns (if applicable)

---

## Warning Signs: When NOT to Bud

❌ **Premature budding indicators:**
- Concept not yet playable/interactive
- No clear development path forward
- Would benefit from more rapid iteration in garden
- Uncertain about core mechanics or market fit
- Garden still provides value for experimentation

✅ **Keep iterating in garden if:**
- Still exploring multiple variations
- Rapid prototyping velocity is valuable
- Not yet ready for team coordination overhead
- Uncertain about long-term viability

---

## Example: Lighthouse Palimpsest Budding Walkthrough

```bash
# 1. Create repository
cd ~/Documents/GitHub/
mkdir lighthouse-palimpsest
cd lighthouse-palimpsest
git init

# 2. Extract from garden
cp ~/Documents/GitHub/Literate-Garden/experiments/palimpsest/web/lighthouse-palimpsest.html ./prototype-demo.html
cp ~/Documents/GitHub/Literate-Garden/experiments/palimpsest/docs/concepts.md ./docs/narrative-design.md

# 3. Create PROVENANCE.md
cat > PROVENANCE.md << 'EOF'
# Provenance: Lighthouse Palimpsest

**Budded from:** Literate Garden
**Date:** 2025-09-29
**Collection:** Palimpsest (Narrative Layering & Memory Themes)
**Garden Commit:** [hash]

## Reason for Budding

- ⭐⭐⭐⭐ Festival suitability (IGF Excellence in Narrative, Day of the Devs)
- Clear, compelling narrative hook: "Rotate a lighthouse to change the past"
- Moderate technical complexity (shader layering achievable in 12 weeks)
- Strong atmospheric visuals for marketing materials

## Original Garden Artifacts

- Concept document: experiments/palimpsest/docs/concepts.md
- Interactive demo: experiments/palimpsest/web/lighthouse-palimpsest.html
- Design philosophy: Narrative-forward with memory/timeline themes

## Development Path

**Governance:** Spec-driven with narrative design docs
**Team:** 1 narrative designer + 1 technical artist + 1 programmer
**Timeline:** 12-week vertical slice
**Festival Deadline:** IGF 2026 submission (October 2025)
EOF

# 4. Set up spec-driven structure
mkdir -p {specs,src,assets,docs,tests}

# 5. Create CLAUDE.md
cat > CLAUDE.md << 'EOF'
# Claude Agent Instructions - Lighthouse Palimpsest

**Context Level**: 3 (Sub-Project)
**Inherits From**: Meta-project spec-driven development
**Project Type**: Narrative puzzle game with timeline manipulation
**Governance**: GitHub spec-kit + narrative design validation

## Authority Domains

### Human Domain
- Narrative design validation
- Timeline puzzle coherence
- Emotional impact of story beats
- Festival pitch materials

### Code Agent Domain
- Shader implementation for timeline layering
- Timeline state management
- Input handling for lighthouse rotation

### Chat Agent Domain
- Specification drafting for narrative beats
- Pattern recognition from narrative games
- Festival submission coordination
EOF

# 6. Initial commit
git add .
git commit -m "Initial commit: budded from Literate Garden

Budded 'Lighthouse Palimpsest' from Literate Garden Palimpsest Collection.

Provenance: experiments/palimpsest/web/lighthouse-palimpsest.html
Reason: ⭐⭐⭐⭐ festival suitability, clear narrative hook, ready for
vertical slice development with narrative design specs.

Target: IGF Excellence in Narrative, Day of the Devs showcase"

# 7. Notify meta-project
cd ~/devvyn-meta-project
cat > /tmp/lighthouse-budding.md << 'EOF'
# Lighthouse Palimpsest Budded from Garden

**Status:** Vertical Slice Development
**Timeline:** 12 weeks
**Team:** 1 narrative designer + 1 technical artist + 1 programmer
**Festival Target:** IGF 2026 Excellence in Narrative

## Coordination Needs

- Narrative designer recruitment or collaboration
- Technical artist for shader timeline layering
- Festival submission timeline tracking
- Portfolio capacity allocation (Framework v2.1)
EOF
./scripts/bridge-send.sh code chat HIGH "Lighthouse Palimpsest budded" /tmp/lighthouse-budding.md
```

---

## Success Metrics

### For Budded Projects
- **Vertical slice completed** within projected timeline
- **Festival submission** successfully submitted
- **Team coordination** smooth with clear authority domains
- **Technical debt** manageable, not accumulating

### For Garden Health
- **Active experiments** remain playable and documented
- **Budding rate** indicates healthy experimentation → production pipeline
- **Pattern extraction** from successful buds enriches garden
- **Failed experiments** properly documented before pruning

---

**Generated:** 2025-09-29
**Purpose:** Guide successful experiment graduation from garden to production
**Status:** Active template for budding decisions