document.addEventListener('DOMContentLoaded', () => {
  const overlay = document.getElementById('intro-overlay');
  const launchButton = document.getElementById('launch-btn');
  const progressFill = document.getElementById('progress-fill');
  const progressBar = document.getElementById('launch-progress');
  const progressLabel = document.getElementById('progress-label');
  const srStatus = document.getElementById('sr-status');
  const stepBoxes = document.querySelectorAll('[data-deploy-step]');
  const celebrateButton = document.getElementById('celebrate-btn');
  const toggleButtons = document.querySelectorAll('[data-toggle-class]');
  const timelineItems = document.querySelectorAll('[data-timeline]');
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let introPlayed = false;

  // Kleine Hilfsfunktion, um Timeline-Einträge zu finden
  const findTimelineItem = (stepId) => {
    return Array.from(timelineItems).find((item) => item.dataset.timeline === stepId);
  };

  // Aktualisiert Progress-Bar und Live-Region sobald eine Checkbox angeklickt wird
  const updateProgress = () => {
    const total = stepBoxes.length;
    const checked = Array.from(stepBoxes).filter((box) => box.checked).length;
    const percent = Math.round((checked / total) * 100);
    progressFill.style.width = `${percent}%`;
    progressBar.setAttribute('aria-valuenow', String(percent));
    progressLabel.textContent = `${percent}% fertig · ${percent === 100 ? 'Launch frei!' : 'Mission läuft'}`;
    if (srStatus) {
      srStatus.textContent = `Checkliste steht bei ${percent} Prozent.`;
    }

    // Markiere passende Timeline-Zeile, damit Felix sofort sieht, was erledigt ist
    stepBoxes.forEach((box) => {
      const target = findTimelineItem(box.dataset.deployStep);
      if (target) {
        // TODO 3: Aktiviere hier wieder das Umschalten der Timeline-Klasse, damit erledigte Steps leuchten
      }
    });
  };

  // Sorgt dafür, dass sich der Intro-Screen einmalig weg animiert
  const startIntro = () => {
    if (introPlayed || !overlay) return;
    introPlayed = true;

    const duration = prefersReducedMotion.matches ? 0.4 : 1.1;
    if (window.gsap) {
      const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });
      tl.to('.intro-screen', { opacity: 0, duration, pointerEvents: 'none' }).set('.intro-screen', { display: 'none' })
        .from('.hero-title', { y: 60, opacity: 0, duration }, '<')
        .from('[data-hero-animate]', { y: 30, opacity: 0, stagger: prefersReducedMotion.matches ? 0.05 : 0.18, duration: duration * 0.9 }, '-=0.5')
        .to('.portal-glow', { boxShadow: '0 0 60px rgba(61,214,140,0.85)', duration: duration * 0.6, repeat: 1, yoyo: true }, '<');
    } else {
      overlay.style.display = 'none';
    }

    overlay?.setAttribute('aria-hidden', 'true');
    overlay?.removeAttribute('aria-modal');
    overlay?.removeAttribute('role');
    if (srStatus) {
      srStatus.textContent = 'Intro-Screen geschlossen. Bühne frei!';
    }
  };

  // Tastatur & Klick-Handling für den Intro-Button
  launchButton?.addEventListener('click', startIntro);
  launchButton?.addEventListener('keyup', (event) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      startIntro();
    }
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && !introPlayed) {
      startIntro();
    }
  });

  // Animate On Scroll initialisieren, sobald die Bibliothek geladen ist
  if (window.AOS) {
    AOS.init({
      once: true,
      duration: prefersReducedMotion.matches ? 400 : 900,
      offset: 120
    });
  }

  // Jeder Toggle verändert eine visuelle Unterstützung (Kontrast, Schriftgröße ...)
  toggleButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const toggleClass = button.dataset.toggleClass;
      const active = document.body.classList.toggle(toggleClass);
      button.setAttribute('aria-pressed', String(active));
      if (srStatus) {
        srStatus.textContent = `${button.dataset.label} ${active ? 'aktiviert' : 'deaktiviert'}.`;
      }
    });
  });

  // Passt sich automatisch an, wenn das System "Bewegung reduzieren" bevorzugt
  const handleMotionPreference = (event) => {
    if (event.matches) {
      document.body.classList.add('calm-motion');
    } else {
      document.body.classList.remove('calm-motion');
    }
  };

  if (prefersReducedMotion.addEventListener) {
    prefersReducedMotion.addEventListener('change', handleMotionPreference);
  } else if (prefersReducedMotion.addListener) {
    prefersReducedMotion.addListener(handleMotionPreference);
  }

  handleMotionPreference(prefersReducedMotion);

  // Kleine Launch-Party mit GSAP-Sparkles
  celebrateButton?.addEventListener('click', () => {
    if (!window.gsap) return;
    Array.from({ length: 8 }).forEach(() => {
      const sparkle = document.createElement('span');
      sparkle.className = 'sparkle';
      sparkle.setAttribute('aria-hidden', 'true');
      document.body.appendChild(sparkle);
      const x = Math.random() * window.innerWidth;
      const y = Math.random() * window.innerHeight;
      sparkle.style.left = `${x}px`;
      sparkle.style.top = `${y}px`;
      gsap.fromTo(
        sparkle,
        { scale: 0, opacity: 1 },
        {
          scale: 1.6,
          opacity: 0,
          duration: 1.2,
          ease: 'power2.out',
          onComplete: () => sparkle.remove()
        }
      );
    });
    if (srStatus) {
      srStatus.textContent = 'Launch-Party gezündet!';
    }
  });

  // Sobald ein Deployment-Step fertig ist → Fortschritt berechnen
  stepBoxes.forEach((box) => {
    box.addEventListener('change', updateProgress);
  });

  updateProgress();
});
