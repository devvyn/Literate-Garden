// Version D: ritual planner with drag-drop interactions
const board = document.querySelector(".board");
const paletteButtons = document.querySelectorAll(".pylon");
const forecast = document.querySelector(".forecast");

const boardSize = 4;
const layout = [];

function createBoard() {
  for (let i = 0; i < boardSize * boardSize; i++) {
    const tile = document.createElement("div");
    tile.className = "tile";
    tile.dataset.element = "Mesa";
    tile.dataset.index = i;
    tile.addEventListener("dragover", (e) => e.preventDefault());
    tile.addEventListener("drop", handleDrop);
    board.appendChild(tile);
    layout.push(null);
  }
}

let draggedElement = null;

paletteButtons.forEach((btn) => {
  btn.draggable = true;
  btn.addEventListener("dragstart", (event) => {
    draggedElement = event.target.dataset.element;
    event.dataTransfer.setData("text/plain", draggedElement);
  });
});

function handleDrop(event) {
  event.preventDefault();
  const tile = event.currentTarget;
  const index = parseInt(tile.dataset.index, 10);
  const element = event.dataTransfer.getData("text/plain") || draggedElement;
  if (!element) return;

  layout[index] = element;
  tile.dataset.element = element;
  updateForecast();
}

function updateForecast() {
  const counts = layout.reduce(
    (acc, item) => {
      if (item) acc[item] = (acc[item] || 0) + 1;
      return acc;
    },
    { wind: 0, rain: 0, ember: 0 }
  );

  const patterns = [];
  if (counts.wind >= 3) patterns.push("Jetstream Corridor forming in east quadrant.");
  if (counts.rain >= 3) patterns.push("Cascade Veil prepping relief rains for villages.");
  if (counts.ember >= 3) patterns.push("Ember Shield heating trade winds for balloon convoys.");
  if (counts.wind && counts.rain && counts.ember) patterns.push("Grand Confluence ready — trigger co-op ritual!");

  forecast.textContent =
    patterns.join(" ") || "Place at least three pylons to stabilize the storm front.";
}

createBoard();
updateForecast();
