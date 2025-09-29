// Version B: simple dual-state puzzle illustrating quantum overlap
const gridEl = document.querySelector(".grid");
const statusEl = document.querySelector(".status");
const resetBtn = document.getElementById("reset");

const size = 5;
const states = [];

function initGrid() {
  gridEl.innerHTML = "";
  states.length = 0;
  for (let row = 0; row < size; row++) {
    const rowStates = [];
    for (let col = 0; col < size; col++) {
      const tile = document.createElement("button");
      tile.className = "tile";
      tile.type = "button";
      tile.dataset.state = "0";
      tile.dataset.label = `${row + 1}-${col + 1}`;
      tile.setAttribute("role", "gridcell");
      tile.addEventListener("click", () => cycleState(tile, row, col));
      gridEl.appendChild(tile);
      rowStates.push(0);
    }
    states.push(rowStates);
  }
  updateStatus();
}

function cycleState(tile, row, col) {
  const nextState = (states[row][col] + 1) % 3; // 0 = idle, 1 = timeline A, 2 = timeline B
  states[row][col] = nextState;
  tile.dataset.state = String(nextState);
  updateStatus();
}

function checkWin(stateValue) {
  // Win when a full row is filled with the same non-zero state
  return states.some((row) => row.every((cell) => cell === stateValue));
}

function updateStatus() {
  const timelineAWins = checkWin(1);
  const timelineBWins = checkWin(2);

  if (timelineAWins && timelineBWins) {
    statusEl.textContent = "Clean extraction! Both timelines achieved synchronized infiltration.";
  } else if (timelineAWins || timelineBWins) {
    statusEl.textContent = "Partial alignment achieved. Mirror timeline still vulnerable.";
  } else {
    statusEl.textContent = "Stage operatives on matching rows in both timelines.";
  }
}

resetBtn.addEventListener("click", initGrid);

initGrid();
