// Tag 07 – Scroll-Schlitten Interaktionen
// In diesem Skript kombinieren wir die Intersection Observer API mit AOS-Animationen
// und einigen kleinen UI-Extras, damit Felix live verfolgen kann, wie viel Magie
// bereits freigeschaltet wurde.

const initScrollStory = () => {
  const cards = document.querySelectorAll('.story-card');
  const runeFill = document.querySelector('.rune-progress-fill');
  const runeLabel = document.querySelector('#rune-label');
  const runeNodes = document.querySelectorAll('[data-rune]');
  const scrollHint = document.querySelector('#scroll-hint');
  const sparkToggle = document.querySelector('#spark-toggle');
  const storyContainer = document.querySelector('#story-scroll');

  if (!cards.length || !runeFill || !storyContainer) {
    return;
  }

  const activated = new Set();

  const updateProgress = () => {
    const percent = (activated.size / cards.length) * 100;
    runeFill.style.width = `${percent}%`;
    runeLabel.textContent = `${Math.round(percent)}% Magie`;

    runeNodes.forEach((node, index) => {
      const threshold = ((index + 1) / runeNodes.length) * 100;
      node.classList.toggle('active', percent >= threshold - 1);
    });
  };

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const cardIndex = Number(entry.target.dataset.index);
        if (entry.isIntersecting) {
          activated.add(cardIndex);
          entry.target.classList.add('story-card-active');
        } else {
          activated.delete(cardIndex);
          entry.target.classList.remove('story-card-active');
        }
      });
      updateProgress();
    },
    {
      threshold: 0.55,
    }
  );

  cards.forEach((card) => observer.observe(card));

  scrollHint?.addEventListener('click', () => {
    storyContainer.scrollIntoView({ behavior: 'smooth' });
  });

  const toggleSparkles = () => {
    document.body.classList.toggle('spark-active');
    let sparkleLayer = document.querySelector('.sparkle-container');
    if (document.body.classList.contains('spark-active')) {
      if (!sparkleLayer) {
        sparkleLayer = document.createElement('div');
        sparkleLayer.className = 'sparkle-container';
        for (let i = 0; i < 22; i += 1) {
          const sparkle = document.createElement('span');
          sparkle.textContent = '✦';
          sparkle.style.left = `${Math.random() * 100}%`;
          sparkle.style.animationDelay = `${Math.random() * 5}s`;
          sparkle.style.fontSize = `${0.4 + Math.random() * 1.1}rem`;
          sparkleLayer.appendChild(sparkle);
        }
        document.body.appendChild(sparkleLayer);
      }
      sparkToggle.textContent = '🌠 Sternenfunken stoppen';
    } else {
      sparkleLayer?.remove();
      sparkToggle.textContent = '❄️ Sternenfunken umschalten';
    }
  };

  sparkToggle?.addEventListener('click', toggleSparkles);

  updateProgress();
};

window.addEventListener('DOMContentLoaded', () => {
  AOS.init({
    once: false,
    easing: 'ease-out-quart',
    offset: 160,
  });
  initScrollStory();
});
