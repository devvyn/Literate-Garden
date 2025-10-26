const timelineMarkers = document.querySelectorAll('.timeline__marker');
const weaveButton = document.getElementById('weaveButton');
const constellationCanvas = document.getElementById('constellationCanvas');
const routeButton = document.getElementById('routeButton');
const routeStatus = document.getElementById('routeStatus');

// Collaboration Note: Extend presets here when adding new starfield layouts.
const CONSTELLATION_PRESETS = [
  { points: [[60, 260], [140, 180], [220, 220], [300, 140], [380, 200]], color: '#88a4ff' },
  { points: [[40, 240], [120, 200], [200, 120], [280, 200], [360, 160]], color: '#ffd166' },
  { points: [[80, 220], [180, 160], [260, 220], [340, 180], [420, 240]], color: '#f78da7' }
];

// Collaboration Note: ROUTE graph powers Emberwake's status updates. Append nodes as needed.
const ROUTE_STATES = [
  { label: 'Momentum Chain: Stable', color: 'var(--accent)' },
  { label: 'Momentum Chain: Thriving', color: '#ffd166' },
  { label: 'Momentum Chain: Critical! Maintain Flow', color: '#ff5f5f' }
];

if (timelineMarkers.length) {
  let activeIndex = 1;
  setInterval(() => {
    timelineMarkers[activeIndex].classList.remove('timeline__marker--active');
    activeIndex = (activeIndex + 1) % timelineMarkers.length;
    timelineMarkers[activeIndex].classList.add('timeline__marker--active');
  }, 2600);
}

if (constellationCanvas && weaveButton) {
  const ctx = constellationCanvas.getContext('2d');
  const width = constellationCanvas.width;
  const height = constellationCanvas.height;

  const drawConstellation = (preset) => {
    ctx.clearRect(0, 0, width, height);
    ctx.fillStyle = 'rgba(15, 17, 23, 0.9)';
    ctx.fillRect(0, 0, width, height);

    ctx.strokeStyle = preset.color;
    ctx.lineWidth = 3;
    ctx.lineJoin = 'round';
    ctx.shadowColor = preset.color;
    ctx.shadowBlur = 18;

    ctx.beginPath();
    preset.points.forEach(([x, y], index) => {
      if (index === 0) {
        ctx.moveTo(x, y);
      } else {
        ctx.lineTo(x, y);
      }
    });
    ctx.stroke();

    preset.points.forEach(([x, y]) => {
      ctx.beginPath();
      ctx.arc(x, y, 6, 0, Math.PI * 2);
      ctx.fillStyle = '#ffffff';
      ctx.fill();
    });
  };

  let presetIndex = 0;
  drawConstellation(CONSTELLATION_PRESETS[presetIndex]);

  weaveButton.addEventListener('click', () => {
    presetIndex = (presetIndex + 1) % CONSTELLATION_PRESETS.length;
    drawConstellation(CONSTELLATION_PRESETS[presetIndex]);
    weaveButton.textContent = 'Weave Intensity +1';
    setTimeout(() => (weaveButton.textContent = 'Trigger Star Weave'), 1600);
  });
}

if (routeButton && routeStatus) {
  let routeIndex = 0;
  routeButton.addEventListener('click', () => {
    routeIndex = (routeIndex + 1) % ROUTE_STATES.length;
    const state = ROUTE_STATES[routeIndex];
    routeStatus.textContent = state.label;
    routeStatus.style.color = state.color;
    routeButton.textContent = 'Boost Chain +1';
    setTimeout(() => (routeButton.textContent = 'Ignite Delivery Boost'), 1500);
  });
}
