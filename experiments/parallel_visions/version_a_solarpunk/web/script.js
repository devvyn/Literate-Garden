// Version A interactive sketch
const canvas = document.getElementById("garden");
const ctx = canvas.getContext("2d");
const sunSlider = document.getElementById("sun");
const windSlider = document.getElementById("wind");
const motifReadout = document.getElementById("motifReadout");

const gradients = [
  "Aurora Sweep",
  "Prism Bloom",
  "Chorus Canopy",
  "Zephyr Loop",
  "Bloomwave",
  "Harmonic Drift",
  "Lattice Resonance",
];

function drawGarden() {
  const sunAngle = parseFloat(sunSlider.value);
  const wind = parseInt(windSlider.value, 10);

  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Background glow
  const radial = ctx.createRadialGradient(
    canvas.width / 2 + Math.cos((sunAngle * Math.PI) / 180) * 80,
    canvas.height / 4,
    30,
    canvas.width / 2,
    canvas.height / 2,
    240
  );
  radial.addColorStop(0, `hsla(${sunAngle}, 70%, 80%, 0.9)`);
  radial.addColorStop(1, `hsla(${(sunAngle + 180) % 360}, 60%, 25%, 0.4)`);
  ctx.fillStyle = radial;
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Plant stems inspired by wind pulse
  const stems = 5 + wind;
  for (let i = 0; i < stems; i++) {
    const x = (canvas.width / (stems + 1)) * (i + 1);
    const sway = Math.sin((sunAngle / 45 + i) * Math.PI) * (10 + wind * 2);

    ctx.beginPath();
    ctx.moveTo(x, canvas.height - 20);
    ctx.quadraticCurveTo(
      x + sway,
      canvas.height / 2,
      x + sway * 1.2,
      canvas.height / 4
    );
    ctx.strokeStyle = `hsla(${(sunAngle + i * 30) % 360}, 80%, 60%, 0.8)`;
    ctx.lineWidth = 6 - Math.min(4, Math.abs(wind - 3));
    ctx.lineCap = "round";
    ctx.stroke();

    // Plant nodes
    for (let node = 0; node < wind + 2; node++) {
      const t = node / (wind + 1);
      const px = x + sway * t * 1.1;
      const py = canvas.height - 20 - t * (canvas.height - 60);
      ctx.beginPath();
      ctx.fillStyle = `hsla(${(sunAngle + node * 45) % 360}, 85%, 70%, 0.85)`;
      ctx.arc(px, py, 10 + Math.sin(wind + node) * 4, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  // Motif readout to narrate state
  const motif = gradients[(wind + Math.round(sunAngle / 45)) % gradients.length];
  motifReadout.textContent = `Current motif: ${motif} · Sun ${sunAngle.toFixed(
    0
  )}° · Wind Pulse ${wind}`;
}

sunSlider.addEventListener("input", drawGarden);
windSlider.addEventListener("input", drawGarden);

drawGarden();
