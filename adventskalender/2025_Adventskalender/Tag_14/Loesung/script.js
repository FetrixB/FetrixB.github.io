'use strict';

(() => {
  if (typeof window === 'undefined') {
    return;
  }

  const stage = document.querySelector('[data-stage]');
  if (!stage || typeof gsap === 'undefined') {
    return;
  }

  gsap.registerPlugin(ScrollTrigger);

  const ui = {
    core: document.querySelector('[data-rune-core]'),
    ring: document.querySelector('[data-rune-ring]'),
    glow: document.querySelector('[data-rune-glow]'),
    glyph: document.querySelector('[data-rune-glyph]'),
    orbit: document.querySelector('.rune-orbit'),
    orbs: gsap.utils.toArray('[data-spark]'),
    shards: gsap.utils.toArray('[data-shard]'),
    phase: document.querySelector('[data-phase]'),
    phaseDetail: document.querySelector('[data-phase-detail]'),
    loopCount: document.querySelector('[data-loop-count]'),
    progressFill: document.querySelector('[data-progress-fill]'),
    steps: gsap.utils.toArray('[data-phase-step]'),
    toggleBtn: document.querySelector('[data-action="toggle"]'),
    reverseBtn: document.querySelector('[data-action="reverse"]'),
    burstBtn: document.querySelector('[data-action="burst"]'),
    speedSlider: document.querySelector('[data-speed]'),
    speedValue: document.querySelector('[data-speed-value]')
  };

  const phaseMessages = [
    {
      title: 'Aufladen der Rune',
      detail: 'Der Kern sammelt Licht, Tweens nutzen fromTo um Energie sichtbar zu machen.'
    },
    {
      title: 'Orbit in Bewegung',
      detail: 'RotationX und RotationY kippen den Ring, ein Timeline-Abschnitt bewegt mehrere Teile synchron.'
    },
    {
      title: 'Pulsierende Glyphen',
      detail: 'Farben springen per ease "expo" und verstärken das Ritual.'
    },
    {
      title: 'Cine Wrap',
      detail: 'Partikel werden eingesogen, bevor der Loop sauber schließt.'
    }
  ];

  const randomBetween = (min, max) => Math.random() * (max - min) + min;

  const placeShards = () => {
    ui.shards.forEach((shard) => {
      shard.style.left = `${randomBetween(0, 100)}%`;
      shard.style.top = `${randomBetween(0, 100)}%`;
      shard.style.animationDelay = `${randomBetween(0, 2)}s`;
    });
  };

  placeShards();

  let loopCounter = 0;

  const highlightStep = (index) => {
    ui.steps.forEach((step, stepIndex) => {
      step.classList.toggle('is-active', stepIndex === index);
    });
  };

  const updatePhase = (index) => {
    const message = phaseMessages[index] ?? phaseMessages[0];
    ui.phase.textContent = message.title;
    ui.phaseDetail.textContent = message.detail;
    highlightStep(index);
  };

  const updateLoopLabel = () => {
    ui.loopCount.textContent = loopCounter.toString();
  };

  const updateProgress = (progress) => {
    if (!ui.progressFill) {
      return;
    }
    const clamped = Math.max(0, Math.min(1, progress));
    ui.progressFill.style.transform = `scaleX(${clamped})`;
  };

  // Haupttimeline mit vier klaren Abschnitten
  const runeTimeline = gsap.timeline({
    defaults: { duration: 1.1, ease: 'sine.inOut' },
    repeat: -1,
    repeatDelay: 0.4,
    onUpdate: function onUpdate() {
      updateProgress(this.progress());
    },
    onRepeat: () => {
      loopCounter += 1;
      updateLoopLabel();
    }
  });

  runeTimeline
    .call(() => updatePhase(0))
    .fromTo(
      ui.core,
      { scale: 0.9, boxShadow: 'inset 0 0 12px rgba(96,165,250,0.3)' },
      { scale: 1.08, boxShadow: '0 0 35px rgba(89,246,183,0.65)' }
    )
    .to(ui.glow, { opacity: 1, duration: 0.8 }, '<')
    .to(ui.ring, { rotateZ: 180, borderColor: 'rgba(248,200,111,0.85)' }, '<')
    .call(() => updatePhase(1))
    .to(ui.ring, { rotationX: 35, rotationY: -25, transformOrigin: 'center', duration: 1.2 })
    .to(ui.orbs, { rotation: 360, duration: 1.5, ease: 'power2.inOut', stagger: 0.08 }, '<')
    .call(() => updatePhase(2))
    .to(ui.glyph, { color: 'var(--accent-gold)', scale: 1.18, ease: 'expo.out', duration: 0.8 })
    .to(ui.core, { borderColor: 'rgba(248,200,111,0.4)', duration: 0.8 }, '<')
    .to(ui.orbit, { scale: 1.08, duration: 0.8 }, '<')
    .call(() => updatePhase(3))
    .to(ui.shards, { opacity: 0.85, yPercent: -40, stagger: 0.05, duration: 0.7 }, '<0.1')
    .to(ui.glow, { opacity: 0.25, duration: 0.6 }, '-=0.1')
    .to(ui.core, { scale: 0.96, duration: 0.5 }, '-=0.2');

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (reduceMotion.matches) {
    runeTimeline.timeScale(0.8);
  }

  const toggleTimeline = () => {
    if (runeTimeline.isActive() && !runeTimeline.paused()) {
      runeTimeline.pause();
      ui.toggleBtn.textContent = 'Abspielen';
    } else {
      runeTimeline.resume();
      ui.toggleBtn.textContent = 'Pause';
    }
  };

  const handleReverse = () => {
    runeTimeline.reversed(!runeTimeline.reversed());
    ui.reverseBtn.classList.toggle('control-button--ghost');
  };

  const handleBurst = () => {
    // Extra Tween für eine Mini-Explosion
    gsap.fromTo(
      ui.ring,
      { filter: 'drop-shadow(0 0 0 rgba(89,246,183,0.2))' },
      { filter: 'drop-shadow(0 0 35px rgba(89,246,183,0.8))', duration: 0.6, yoyo: true, repeat: 1 }
    );
    gsap.fromTo(
      ui.glow,
      { opacity: 0.4 },
      { opacity: 1, duration: 0.4, yoyo: true, repeat: 1, ease: 'power1.in' }
    );
  };

  const updateSpeed = () => {
    const speed = parseFloat(ui.speedSlider.value);
    runeTimeline.timeScale(speed);
    ui.speedValue.textContent = `${speed.toFixed(1)}x`;
  };

  ui.toggleBtn?.addEventListener('click', toggleTimeline);
  ui.reverseBtn?.addEventListener('click', handleReverse);
  ui.burstBtn?.addEventListener('click', handleBurst);
  ui.speedSlider?.addEventListener('input', updateSpeed);

  // ScrollTrigger animiert erklärende Karten
  gsap.utils.toArray('[data-scroll-card]').forEach((card, index) => {
    gsap.from(card, {
      opacity: 0,
      y: 60,
      duration: 0.8,
      ease: 'power3.out',
      delay: index * 0.04,
      scrollTrigger: {
        trigger: card,
        start: 'top 80%'
      }
    });
  });
})();
