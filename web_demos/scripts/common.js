// COLLAB NOTE: Shared utilities for lightweight visualizations. Keep pure functions to simplify reuse.
export function lerp(start, end, t) {
  return start + (end - start) * t;
}

export function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

export function createTicker(callback) {
  let frameId = null;
  let lastTime = performance.now();

  function tick(now) {
    const delta = now - lastTime;
    lastTime = now;
    callback(delta);
    frameId = requestAnimationFrame(tick);
  }

  frameId = requestAnimationFrame(tick);

  return () => {
    if (frameId) {
      cancelAnimationFrame(frameId);
    }
  };
}

export function createElement(tag, className, text) {
  const el = document.createElement(tag);
  if (className) el.className = className;
  if (text) el.textContent = text;
  return el;
}

export function readableTimestamp() {
  const now = new Date();
  return `${now.toLocaleDateString()} ${now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`;
}
