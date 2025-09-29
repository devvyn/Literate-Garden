const patterns = [
  {
    title: "Rhythmic Environmental Tuning",
    concept: "Clockwork Skylark",
    tagline: "Conduct the wind to reveal secret traversal lines.",
    mechanic:
      "Players sync button presses to gust patterns, letting them rewind currents and reposition floating habitats.",
    suitability:
      "Shines in showcases where tactile feedback is prized; the rhythmic loop is easy to demo in short sessions.",
    feasibility:
      "Needs spline authoring tools and a lightweight wind shader. Prototype pathing in Unity with Cinemachine to keep scope sane.",
    pulseColor: "var(--accent)",
  },
  {
    title: "Diegetic Journaling UI",
    concept: "Nocturne Cartographers",
    tagline: "Notebook pages morph into navigation glyphs as time ticks down.",
    mechanic:
      "Every menu interaction is a sketch stroke; the act of recording information unlocks dream doors.",
    suitability:
      "Narrative juries gravitate to playable journals. Works on touchscreens and controllers with minimal remapping.",
    feasibility:
      "Implementable via HTML Canvas or Unity UI Toolkit. Waiting on gesture dataset to finish stroke recognition layer.",
    pulseColor: "#70d6ff",
  },
  {
    title: "Procedural Growth Feedback",
    concept: "Bloom//Breaker",
    tagline: "Competitive arenas bloom in direct response to your deck choices.",
    mechanic:
      "Seeds are cast like spells; each victory pulse sprouts terrain that changes traversal and line-of-sight.",
    suitability:
      "Instantly readable for streaming audiences and booth spectators—high visual payoff.",
    feasibility:
      "Requires deterministic growth curves synced over the network. Explore Godot 4 + GDExtension for performant foliage instancing.",
    pulseColor: "#c77dff",
  },
];

const grid = document.querySelector("#pattern-grid");
const toggle = document.querySelector("#toggle-feasibility");

const renderCard = (pattern) => {
  const card = document.createElement("article");
  card.className = "card";
  card.setAttribute("role", "listitem");
  card.innerHTML = `
    <div class="pulse-bar" aria-hidden="true">
      <span style="animation-delay:0s;background:${pattern.pulseColor}"></span>
      <span style="background:${pattern.pulseColor}"></span>
      <span style="animation-delay:0.4s;background:${pattern.pulseColor}"></span>
    </div>
    <h3>${pattern.title}</h3>
    <p class="tagline">Anchor concept: <strong>${pattern.concept}</strong></p>
    <p class="mechanic">${pattern.mechanic}</p>
    <p class="suitability"><strong>Why juries care:</strong> ${pattern.suitability}</p>
    <p class="feasibility"><strong>Build notes:</strong> ${pattern.feasibility}</p>
  `;
  return card;
};

patterns.forEach((pattern) => {
  const card = renderCard(pattern);
  grid.append(card);
});

let showFeasibility = false;

const syncFeasibilityState = () => {
  grid.querySelectorAll(".card").forEach((card) => {
    card.dataset.showFeasibility = String(showFeasibility);
  });
  toggle.setAttribute("aria-pressed", showFeasibility.toString());
  toggle.textContent = showFeasibility
    ? "Hide Feasibility Notes"
    : "Show Feasibility Notes";
};

syncFeasibilityState();

// COLLAB NOTE: Extend this handler when wiring keyboard shortcuts for booth demos.
toggle.addEventListener("click", () => {
  showFeasibility = !showFeasibility;
  syncFeasibilityState();
});

// COLLAB NOTE: Attempted to add localStorage persistence but paused until UX confirms desired default state.
