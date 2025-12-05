const MAX_SNOWFLAKES = 22;

const stageElements = {
  snowLayer: document.querySelector('[data-snow]'),
  status: document.querySelector('[data-status]'),
  speed: document.querySelector('[data-speed-readout]'),
  fps: document.querySelector('[data-fps]'),
  boostButton: document.getElementById('boostButton'),
  progressFill: document.querySelector('[data-progress-fill]'),
  bear: document.getElementById('pixelBear'),
  shadow: document.querySelector('[data-shadow]'),
  loopHint: document.querySelector('[data-loop-hint]')
};

const createSnow = () => {
  const { snowLayer } = stageElements;
  if (!snowLayer) return;
  snowLayer.innerHTML = '';

  Array.from({ length: MAX_SNOWFLAKES }).forEach((_, index) => {
    const flake = document.createElement('span');
    flake.className = 'snowflake';
    flake.style.left = `${Math.random() * 100}%`;
    flake.style.animationDelay = `${index * 0.2}s`;
    flake.style.animationDuration = `${4 + Math.random() * 3}s`;
    snowLayer.appendChild(flake);
  });
};

const initTimeline = () => {
  const { bear, shadow, status, speed, progressFill } = stageElements;
  if (!bear || !shadow) return null;

  const timeline = anime.timeline({
    direction: 'normal',
    loop: true,
    autoplay: true,
    duration: 5200,
    easing: 'easeInOutSine',
    begin: () => {
      if (status) {
        status.textContent = 'Der Pixel-Bär tänzelt an die Startlinie…';
      }
    },
    update: (anim) => {
      const progress = anim.progress / 100;
      if (progressFill) {
        progressFill.style.transform = `scaleX(${Math.min(progress, 1)})`;
      }
      const baseSpeed = 12 + progress * 48;
      const turboBonus = timeline.playbackRate > 1 ? 12 : 0;
      if (speed) {
        speed.textContent = `${Math.round(baseSpeed + turboBonus)} km/h`;
      }
    },
    loopComplete: () => {
      if (status) {
        status.textContent = 'Applaus! Noch eine Runde?';
      }
    }
  });

  timeline
    .add(
      {
        targets: bear,
        translateX: ['-10%', '78%'],
        translateY: [
          { value: -18, duration: 1000, easing: 'easeOutQuad' },
          { value: 6, duration: 1500, easing: 'easeInOutQuad' }
        ],
        rotate: [
          { value: -2, duration: 1000, easing: 'easeInOutSine' },
          { value: 2, duration: 1400, easing: 'easeInOutSine' }
        ],
        scale: [1, 1.04]
      },
      0
    )
    .add(
      {
        targets: shadow,
        scaleX: [0.8, 1.5],
        opacity: [0.35, 0.7, 0.4],
        easing: 'easeOutQuad'
      },
      0
    )
    .add(
      {
        targets: bear,
        translateX: ['78%', '-5%'],
        duration: 1500,
        easing: 'easeInOutExpo'
      },
      '-=600'
    );

  return timeline;
};

const monitorFrames = () => {
  const { fps } = stageElements;
  if (!fps) return;

  let lastTimestamp = performance.now();

  const update = (timestamp) => {
    const delta = timestamp - lastTimestamp || 16;
    lastTimestamp = timestamp;
    const currentFps = Math.max(1, Math.min(120, Math.round(1000 / delta)));
    fps.textContent = `${currentFps} fps`;
    requestAnimationFrame(update);
  };

  requestAnimationFrame(update);
};

const bindBoostButton = (timeline) => {
  const { boostButton, status, loopHint } = stageElements;
  if (!boostButton || !timeline) return;

  let turboEnabled = false;

  boostButton.addEventListener('click', () => {
    // TODO 3: Nutze hier timeline.playbackRate und UI-Updates, um den Turbo-Button lebendig zu machen.
  });
};

const init = () => {
  createSnow();
  const timeline = initTimeline();
  bindBoostButton(timeline);
  monitorFrames();
};

window.addEventListener('DOMContentLoaded', init);
