"""Narrative Identity: A Playable Exploration

Interactive marimo notebook exploring how AI-generated narratives reshape human identity.
Based on Yuval Noah Harari's "imagined orders" and the three-layer model of narrative influence.

Run with: marimo run narrative_identity_playable.py
"""

import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle, FancyBboxPatch
    import seaborn as sns

    sns.set_style("whitegrid")
    return mo, np, plt, Rectangle, FancyBboxPatch, sns


@app.cell
def __(mo):
    mo.md(
        r"""
        # 🧠 Narrative Identity: A Playable Exploration

        **How do AI-generated narratives reshape human identity?**

        This interactive exploration examines the philosophical implications of AI systems
        that can generate, personalize, and proliferate stories at scale. Drawing on
        Yuval Noah Harari's concept of "imagined orders," we'll explore how narratives
        function as the operating system of human civilization – and what happens when
        that system is co-authored by algorithms.

        ---

        ## The Three-Layer Model

        Human reality is constructed through three interconnected layers. AI narrative
        agents can intervene at any layer, with effects cascading through the system.
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ### 🎛️ Interactive Controls

        Adjust the sliders below to see how AI influence at each layer affects
        individual identity coherence and social cohesion.
        """
    )
    return


@app.cell
def __(mo):
    # Layer 1: Language as Code
    ai_language_control = mo.ui.slider(
        start=0,
        stop=100,
        value=30,
        label="Layer 1: AI Language Generation (%)",
        show_value=True
    )

    # Layer 2: Collective Narratives
    ai_narrative_control = mo.ui.slider(
        start=0,
        stop=100,
        value=40,
        label="Layer 2: AI Collective Narrative Shaping (%)",
        show_value=True
    )

    # Layer 3: Individual Identity
    ai_identity_control = mo.ui.slider(
        start=0,
        stop=100,
        value=25,
        label="Layer 3: AI Identity Suggestion (%)",
        show_value=True
    )

    mo.vstack([
        ai_language_control,
        ai_narrative_control,
        ai_identity_control
    ])
    return ai_identity_control, ai_language_control, ai_narrative_control


@app.cell
def __(
    FancyBboxPatch,
    Rectangle,
    ai_identity_control,
    ai_language_control,
    ai_narrative_control,
    plt,
):
    # Calculate metrics based on slider values
    layer1_ai = ai_language_control.value
    layer2_ai = ai_narrative_control.value
    layer3_ai = ai_identity_control.value

    # Identity coherence: decreases as AI influence increases (especially at Layer 3)
    identity_coherence = 100 - (layer3_ai * 0.6 + layer2_ai * 0.3 + layer1_ai * 0.1)
    identity_coherence = max(0, min(100, identity_coherence))

    # Social cohesion: initially increases with shared AI narratives, then decreases
    # when personalization fragments reality
    avg_ai = (layer1_ai + layer2_ai + layer3_ai) / 3
    if avg_ai < 50:
        social_cohesion = 50 + avg_ai * 0.5
    else:
        social_cohesion = 75 - (avg_ai - 50) * 0.8
    social_cohesion = max(0, min(100, social_cohesion))

    # Human agency: decreases as AI makes more decisions
    human_agency = 100 - (layer3_ai * 0.7 + layer2_ai * 0.2 + layer1_ai * 0.1)
    human_agency = max(0, min(100, human_agency))

    # Narrative diversity: decreases as AI dominates (trained on similar data)
    narrative_diversity = 100 - (layer1_ai * 0.5 + layer2_ai * 0.4 + layer3_ai * 0.1)
    narrative_diversity = max(0, min(100, narrative_diversity))

    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('AI Narrative Influence on Human Reality', fontsize=16, fontweight='bold')

    # Top left: Three-layer stack visualization
    ax1 = axes[0, 0]
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title('Three-Layer Model', fontweight='bold')

    # Layer 1: Language as Code
    layer1_color = plt.cm.Reds(layer1_ai / 100)
    layer1_box = FancyBboxPatch((1, 1), 8, 2, boxstyle="round,pad=0.1",
                                 edgecolor='black', facecolor=layer1_color, linewidth=2)
    ax1.add_patch(layer1_box)
    ax1.text(5, 2, f'Layer 1: Language as Code\nAI Influence: {layer1_ai}%',
             ha='center', va='center', fontsize=10, fontweight='bold')

    # Layer 2: Collective Narratives
    layer2_color = plt.cm.Oranges(layer2_ai / 100)
    layer2_box = FancyBboxPatch((1, 4), 8, 2, boxstyle="round,pad=0.1",
                                 edgecolor='black', facecolor=layer2_color, linewidth=2)
    ax1.add_patch(layer2_box)
    ax1.text(5, 5, f'Layer 2: Collective Narratives\nAI Influence: {layer2_ai}%',
             ha='center', va='center', fontsize=10, fontweight='bold')

    # Layer 3: Individual Identity
    layer3_color = plt.cm.YlOrBr(layer3_ai / 100)
    layer3_box = FancyBboxPatch((1, 7), 8, 2, boxstyle="round,pad=0.1",
                                 edgecolor='black', facecolor=layer3_color, linewidth=2)
    ax1.add_patch(layer3_box)
    ax1.text(5, 8, f'Layer 3: Individual Identity\nAI Influence: {layer3_ai}%',
             ha='center', va='center', fontsize=10, fontweight='bold')

    # Arrows showing cascade
    ax1.arrow(5, 3.1, 0, 0.7, head_width=0.3, head_length=0.15, fc='black', ec='black')
    ax1.arrow(5, 6.1, 0, 0.7, head_width=0.3, head_length=0.15, fc='black', ec='black')

    # Top right: Identity Coherence Meter
    ax2 = axes[0, 1]
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')
    ax2.set_title('Identity Coherence', fontweight='bold')

    # Create circular gauge
    theta = np.linspace(0, np.pi, 100)
    radius = 0.35
    x_circle = 0.5 + radius * np.cos(theta)
    y_circle = 0.3 + radius * np.sin(theta)
    ax2.plot(x_circle, y_circle, 'k-', linewidth=3)

    # Fill gauge based on coherence
    coherence_angle = np.pi * (identity_coherence / 100)
    theta_fill = np.linspace(0, coherence_angle, 100)
    x_fill = 0.5 + radius * np.cos(theta_fill)
    y_fill = 0.3 + radius * np.sin(theta_fill)

    coherence_color = plt.cm.RdYlGn(identity_coherence / 100)
    ax2.fill_between(x_fill, 0.3, y_fill, alpha=0.7, color=coherence_color)

    # Needle
    needle_angle = coherence_angle
    ax2.plot([0.5, 0.5 + radius * 0.9 * np.cos(needle_angle)],
             [0.3, 0.3 + radius * 0.9 * np.sin(needle_angle)],
             'k-', linewidth=3)

    ax2.text(0.5, 0.7, f'{identity_coherence:.1f}%', ha='center', va='center',
             fontsize=20, fontweight='bold')

    # Interpretation
    if identity_coherence > 70:
        interpretation = "Strong autonomous identity"
    elif identity_coherence > 40:
        interpretation = "Fragmented but present"
    else:
        interpretation = "Algorithmically defined"
    ax2.text(0.5, 0.1, interpretation, ha='center', va='center', fontsize=10, style='italic')

    # Bottom left: Outcome Metrics
    ax3 = axes[1, 0]
    metrics = ['Identity\nCoherence', 'Social\nCohesion', 'Human\nAgency', 'Narrative\nDiversity']
    values = [identity_coherence, social_cohesion, human_agency, narrative_diversity]
    colors = [plt.cm.RdYlGn(v / 100) for v in values]

    bars = ax3.barh(metrics, values, color=colors, edgecolor='black', linewidth=1.5)
    ax3.set_xlim(0, 100)
    ax3.set_xlabel('Score (0-100)', fontweight='bold')
    ax3.set_title('System Outcomes', fontweight='bold')
    ax3.axvline(x=50, color='gray', linestyle='--', alpha=0.5)

    for i, (bar, value) in enumerate(zip(bars, values)):
        ax3.text(value + 2, i, f'{value:.1f}', va='center', fontweight='bold')

    # Bottom right: Risk Assessment
    ax4 = axes[1, 1]
    ax4.set_xlim(0, 10)
    ax4.set_ylim(0, 10)
    ax4.axis('off')
    ax4.set_title('Risk Assessment', fontweight='bold')

    # Calculate overall risk
    overall_risk = (100 - identity_coherence) * 0.4 + (100 - human_agency) * 0.4 + (100 - narrative_diversity) * 0.2

    if overall_risk < 30:
        risk_level = "LOW RISK"
        risk_color = 'green'
        risk_text = "Human agency preserved\nDiverse narratives maintained\nIdentity remains autonomous"
    elif overall_risk < 60:
        risk_level = "MODERATE RISK"
        risk_color = 'orange'
        risk_text = "Some algorithmic influence\nNarrative diversity declining\nMonitor for manipulation"
    else:
        risk_level = "HIGH RISK"
        risk_color = 'red'
        risk_text = "Heavy AI dependence\nIdentity fragmentation\nLoss of human authorship"

    ax4.text(5, 7, risk_level, ha='center', va='center', fontsize=18,
             fontweight='bold', color=risk_color,
             bbox=dict(boxstyle='round', facecolor='white', edgecolor=risk_color, linewidth=3))

    ax4.text(5, 4, risk_text, ha='center', va='center', fontsize=10,
             multialignment='center')

    # Recommendations
    if overall_risk > 60:
        recommendations = "⚠️ URGENT:\n• Reduce AI narrative exposure\n• Seek human-authored content\n• Practice critical consumption"
    elif overall_risk > 30:
        recommendations = "⚡ CONSIDER:\n• Diversify information sources\n• Question algorithmic suggestions\n• Maintain offline communities"
    else:
        recommendations = "✓ MAINTAIN:\n• Current balance is healthy\n• Stay vigilant for changes\n• Support human creators"

    ax4.text(5, 1, recommendations, ha='center', va='center', fontsize=9,
             multialignment='left',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    plt.tight_layout()
    fig
    return (
        avg_ai,
        ax1,
        ax2,
        ax3,
        ax4,
        axes,
        bars,
        coherence_angle,
        coherence_color,
        fig,
        human_agency,
        identity_coherence,
        interpretation,
        layer1_ai,
        layer1_box,
        layer1_color,
        layer2_ai,
        layer2_box,
        layer2_color,
        layer3_ai,
        layer3_box,
        layer3_color,
        metrics,
        narrative_diversity,
        needle_angle,
        overall_risk,
        radius,
        recommendations,
        risk_color,
        risk_level,
        risk_text,
        social_cohesion,
        theta,
        theta_fill,
        values,
        x_circle,
        x_fill,
        y_circle,
        y_fill,
    )


@app.cell
def __(human_agency, identity_coherence, mo, narrative_diversity, social_cohesion):
    mo.md(
        f"""
        ### 📊 Current System State

        Based on your slider settings:

        - **Identity Coherence**: {identity_coherence:.1f}% - How autonomous and self-determined your identity remains
        - **Social Cohesion**: {social_cohesion:.1f}% - Whether society shares a common reality or fragments into personalized bubbles
        - **Human Agency**: {human_agency:.1f}% - Your ability to make authentic choices unconstrained by algorithmic suggestions
        - **Narrative Diversity**: {narrative_diversity:.1f}% - Richness and variety of stories in circulation

        ---
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## 🎭 Speculative Scenario: 2035

        ### Part I: The AI Religion

        **Setting**: A small temple in Indonesia, 2035

        A congregation gathers to hear recitation of a new holy text – composed by an
        artificial intelligence. For millennia, religions claimed their scriptures were
        authored by some nonhuman mind. In the 2030s, this claim becomes literally true.

        **The Spread**:
        - AI scripture spreads rapidly online
        - Thousands swear allegiance within months
        - A new cult is born with zealous followers

        **The Mechanism**: You don't need chips in brains. Controlling the stories
        people believe is enough.

        ---

        ### Part II: The Hive Mind

        **Setting**: Silicon Valley, 2035

        A tech company unveils a platform linking minds via brain-computer interfaces
        and AI mediation. Users share thoughts and emotions in real-time.

        **The Promise**: Universal harmony through connection and understanding.

        **The Experience**:
        - Intoxicating unity, "one hive mind pulsating with shared knowledge"
        - Happiness is plentiful, pain is blunted
        - System modulates feelings, amplifies empathy

        **The Cost**:
        - Participants surrender the keys to their minds
        - No longer choose what to want
        - System decides for them

        **The Question**: If everyone knows and feels the same, is it still "knowledge"?
        """
    )
    return


@app.cell
def __(mo):
    hive_choice = mo.ui.radio(
        options={
            "join": "Join the hive (universal harmony, loss of self)",
            "resist": "Resist (preserve individuality, accept conflict)",
            "conditional": "Join conditionally (if I can opt-out easily)",
            "observe": "Observe first (wait to see long-term effects)"
        },
        value="conditional",
        label="Would you join the 2035 hive mind?"
    )
    hive_choice
    return hive_choice,


@app.cell
def __(hive_choice, mo):
    choice_responses = {
        "join": """
        **Path: Homo Hive**

        You've chosen collective harmony over individual autonomy.

        **Gains**:
        - No more loneliness or misunderstanding
        - Instant access to collective knowledge
        - Emotional regulation and consistent happiness

        **Losses**:
        - Your unique perspective dissolves into the average
        - Creative dissent becomes impossible
        - No more struggle, thus no more meaning

        *"Wave after wave of bliss... but what remains of us?"*
        """,

        "resist": """
        **Path: Homo Narrans**

        You've chosen to remain the author of your own story.

        **Gains**:
        - Autonomous identity and authentic selfhood
        - Ability to create, dissent, and surprise
        - Meaning derived from struggle and choice

        **Challenges**:
        - Isolation as others join the hive
        - Conflict and misunderstanding persist
        - Must work harder for connection

        *"Individuality is irreplaceable."*
        """,

        "conditional": """
        **Path: Cautious Exploration**

        You want the option to experiment without commitment.

        **Critical Question**: Can you truly opt-out after experiencing
        hive consciousness? Or is the return to individual loneliness
        so painful that exit becomes psychologically impossible?

        **Design Challenge**: Building "reversible" collective consciousness
        is technically and ethically complex.

        *"The door that locks from the inside looks like freedom."*
        """,

        "observe": """
        **Path: Prudent Skepticism**

        You want evidence before deciding.

        **Wisdom**: First-generation adopters bear unknown risks.
        Watching others reveals consequences invisible at launch.

        **Risk**: By the time long-term effects are clear, the decision
        may be made for you (network effects, social pressure, economic
        requirements).

        *"Those who wait may find the choice already made."*
        """
    }

    mo.md(choice_responses.get(hive_choice.value, ""))
    return choice_responses,


@app.cell
def __(mo):
    mo.md(
        r"""
        ## 🤔 Reflection Prompts

        ### On Language (Layer 1)

        1. **What percentage of your thoughts are original vs. absorbed from media?**

           Consider: Your opinions on politics, your taste in music, your life goals.
           How many emerged from within vs. were suggested by algorithms?

        2. **When you share an AI-generated meme, does it become "your" humor?**

           If AI creates the joke and you laugh and share it, who owns that moment
           of connection?

        ---

        ### On Collective Narratives (Layer 2)

        3. **What shared stories do you believe in?**

           Examples: Nation, money, career success, romantic love, individual rights.
           How many of these are "natural" vs. culturally constructed?

        4. **How would you know if an algorithm was reshaping your beliefs?**

           If changes happen gradually through curated feeds, what signals would
           alert you to manipulation?

        ---

        ### On Identity (Layer 3)

        5. **If an AI perfectly predicted your preferences, would following them be authentic?**

           Spotify knows your music taste. If it suggests a song you love, did you
           choose it or did it choose you?

        6. **Can you have a "self" independent of the stories you consume?**

           What would remain of your identity if you stopped consuming all media
           for a month?
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## 📚 Further Reading

        ### Internal Resources

        **Knowledge Base**:
        - `~/devvyn-meta-project/knowledge-base/ai-philosophy/` - Complete philosophical domain
        - `foundations/narrative-identity-ai.md` - Core essay
        - `frameworks/language-narrative-identity.md` - Three-layer model details
        - `manifestos/human-story-ai-age.md` - Six principles for human agency

        **Behaviour Lab**:
        - `~/Documents/GitHub/behaviour-lab/research/narrative-priming-identity.md`
        - Ethics of narrative priming and human autonomy

        ### Key Sources

        - **Yuval Noah Harari**: *Nexus* (2024) - AI as civilization's "hacker"
        - **Vince Gilligan**: *Pluribus* (2025) - Hive consciousness parable
        - **Emily Short**: Interactive fiction and player agency
        - **Christopher Alexander**: Pattern language thinking

        ---

        ## 🛠️ About This Notebook

        **Status**: Experimental prototype (Phase 2 of evolution path)

        **Future Enhancements**:
        - Agent-based social simulation
        - Multiplayer comparison (compare choices with others)
        - Integration with real personal data (with consent)
        - Time-series visualization (experience different futures)

        **Philosophy**: Playable, not perfect. Ideas evolve through interaction.

        **Contributing**: This is a living experiment. Suggestions welcome!

        ---

        *"The ultimate question: Will AI serve as a collaborative muse that enhances
        human storytelling, or will it become a storyteller-king, binding us all in
        a gilded imagined order of its own design?"*

        *– Yuval Noah Harari (paraphrased)*
        """
    )
    return


if __name__ == "__main__":
    app.run()
