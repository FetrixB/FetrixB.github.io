document.addEventListener('DOMContentLoaded', () => {
  const stage = document.getElementById('parallax-stage');
  const layers = stage ? stage.querySelectorAll('[data-depth]') : [];
  const speedSlider = document.getElementById('speed-control');
  const speedValue = document.getElementById('speed-value');
  const depthReport = document.getElementById('depth-report');
  const scrollMeter = document.querySelector('[data-scroll-meter]');
  const dimensionToggle = document.getElementById('dimension-toggle');
  const dimensionLabel = document.getElementById('dimension-label');
  const treeRange = document.getElementById('tree-range');
  const treeOutput = document.getElementById('tree-output');
  const layerBadges = document.querySelectorAll('[data-layer-badge]');

  let speedFactor = speedSlider ? Number(speedSlider.value) : 70;
  let ticking = false;

  /**
   * Aktualisiert HUD-Texte für Scrolltiefe und Layeraktivierung.
   * @param {number} relativeScroll - Abstand, den der Nutzer durch den Wald gescrollt ist.
   */
  const updateDepthReport = (relativeScroll) => {
    if (!depthReport) return;
    depthReport.textContent =
      relativeScroll <= 0
        ? 'Starte einen Scroll, um den Wald zu bewegen.'
        : `Scrolltiefe: ${Math.round(relativeScroll)}px · Layer-Geschwindigkeit ${speedFactor}%`;
  };

  /**
   * Zeichnet den Fortschrittsbalken entsprechend der Scrolldistanz.
   * @param {number} progress - Prozentualer Fortschritt durch das Parallax-Fenster.
   */
  const updateMeter = (progress) => {
    if (!scrollMeter) return;
    const capped = Math.max(0, Math.min(100, Math.round(progress)));
    scrollMeter.style.setProperty('--scroll-progress', `${capped}%`);
    const strongNode = scrollMeter.querySelector('strong');
    if (strongNode) {
      strongNode.textContent = `${capped}%`;
    }
  };

  /**
   * TODO 3: Setze hier das Highlighting für die Layer-Liste um.
   * Tipp: Vergleiche progress mit badge.dataset.layerBadge und füge/entferne "is-active".
   */
  const highlightLayers = (progress) => {
    // TODO 3: Badges abhängig vom Scroll-Fortschritt aktivieren.
    // layerBadges.forEach((badge) => {
    //   const threshold = Number(badge.dataset.layerBadge || 0);
    //   if (progress >= threshold) {
    //     badge.classList.add('is-active');
    //   } else {
    //     badge.classList.remove('is-active');
    //   }
    // });
  };

  /**
   * Berechnet alle Transformationen für das Parallax-Fenster.
   */
  const animateLayers = () => {
    if (!stage) return;

    const stageTop = stage.offsetTop;
    const scrollY = window.scrollY || window.pageYOffset;
    const relativeScroll = Math.max(0, scrollY - stageTop);
    const stageHeight = stage.offsetHeight || 1;
    const progress = (relativeScroll / stageHeight) * 100;

    layers.forEach((layer) => {
      const depth = Number(layer.dataset.depth || 0);
      const translateY = (relativeScroll * depth * speedFactor) / 400;
      const zShift = depth * -120;
      const scale = 1 + depth * 0.08;
      layer.style.transform = `translate3d(0, ${translateY * -1}px, ${zShift}px) scale(${scale})`;
    });

    updateDepthReport(relativeScroll);
    updateMeter(progress);
    highlightLayers(progress);
    ticking = false;
  };

  const requestTick = () => {
    if (!ticking) {
      window.requestAnimationFrame(animateLayers);
      ticking = true;
    }
  };

  window.addEventListener('scroll', requestTick, { passive: true });
  window.addEventListener('resize', requestTick);

  if (speedSlider && speedValue) {
    speedValue.textContent = `${speedFactor}%`;
    speedSlider.addEventListener('input', (event) => {
      speedFactor = Number(event.target.value);
      speedValue.textContent = `${speedFactor}%`;
      requestTick();
    });
  }

  if (dimensionToggle && dimensionLabel) {
    dimensionToggle.addEventListener('click', () => {
      const toggled = document.body.classList.toggle('dimension-shift');
      dimensionToggle.setAttribute('aria-pressed', toggled ? 'true' : 'false');
      dimensionLabel.textContent = toggled ? 'Lumina-Ebene aktiv' : 'Frost-Ebene aktiv';
      requestTick();
    });
  }

  if (treeRange && treeOutput && stage) {
    const updateTreeDensity = (value) => {
      stage.style.setProperty('--tree-density', value);
      treeOutput.textContent = `Hintergrund-Bäume multipliziert: ${value}x`;
    };

    updateTreeDensity(treeRange.value);
    treeRange.addEventListener('input', (event) => {
      updateTreeDensity(event.target.value);
      requestTick();
    });
  }

  // Aktiviere simpleParallax.js für die Galerie-Bilder, falls das CDN geladen wurde.
  const tokens = document.querySelectorAll('.dimension-token');
  if (tokens.length && window.simpleParallax) {
    /* eslint-disable no-new */
    new simpleParallax(tokens, {
      orientation: 'up',
      scale: 1.35,
      delay: 0.15,
      transition: 'cubic-bezier(0.33, 1, 0.68, 1)'
    });
    /* eslint-enable no-new */
  }

  requestTick();
});
