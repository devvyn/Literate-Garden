// Version C: memory web interaction sketch
const canvas = document.getElementById("web");
const ctx = canvas.getContext("2d");
const log = document.getElementById("log");

const nodes = [];
const memories = [
  "Echo-lanterns hum lullabies from evacuated rooftops.",
  "Steam archivists trade fingerprints for choir notes.",
  "A child sketches transit lines that bloom into moss.",
  "The city council dissolves into spores mid-argument.",
  "Rain translates forgotten names into ultraviolet chords.",
  "Derailed trains become subterranean amphitheaters.",
];

const center = { x: canvas.width / 2, y: canvas.height / 2 };
const radius = 140;

for (let i = 0; i < memories.length; i++) {
  const angle = (i / memories.length) * Math.PI * 2;
  nodes.push({
    x: center.x + Math.cos(angle) * radius,
    y: center.y + Math.sin(angle) * radius,
    memory: memories[i],
    energy: Math.random() * 0.5 + 0.5,
  });
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // TODO_LIGHTING: dynamic bloom overlay once shader pipeline lands
  ctx.strokeStyle = "rgba(143, 247, 207, 0.35)";
  ctx.lineWidth = 1.6;
  ctx.beginPath();
  nodes.forEach((node) => {
    ctx.moveTo(center.x, center.y);
    ctx.lineTo(node.x, node.y);
  });
  ctx.stroke();

  nodes.forEach((node) => {
    ctx.beginPath();
    const gradient = ctx.createRadialGradient(
      node.x,
      node.y,
      2,
      node.x,
      node.y,
      16
    );
    gradient.addColorStop(0, "rgba(143, 247, 207, 0.9)");
    gradient.addColorStop(1, "rgba(143, 247, 207, 0)");
    ctx.fillStyle = gradient;
    ctx.arc(node.x, node.y, 12 + node.energy * 6, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = "rgba(244, 249, 255, 0.85)";
    ctx.font = "600 12px 'IBM Plex Sans', sans-serif";
    ctx.textAlign = "center";
    ctx.fillText("Resonance", node.x, node.y + 28);
  });
}

function handleClick(event) {
  const rect = canvas.getBoundingClientRect();
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;

  let activated = null;
  nodes.forEach((node) => {
    const distance = Math.hypot(node.x - x, node.y - y);
    if (distance < 24) {
      activated = node;
    }
  });

  if (activated) {
    activated.energy = Math.min(1.5, activated.energy + 0.2);
    const item = document.createElement("li");
    item.textContent = activated.memory;
    log.prepend(item);
    if (log.children.length > 5) {
      log.removeChild(log.lastChild);
    }
    draw();
  }
}

canvas.addEventListener("click", handleClick);

draw();
