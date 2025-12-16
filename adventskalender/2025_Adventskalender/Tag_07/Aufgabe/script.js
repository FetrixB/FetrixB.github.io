// Boilerplate für Tag 07 – vervollständige die TODO-Stellen.

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
      const threshold = ((index + 1) / Math.max(runeNodes.length, 1)) * 100;
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

  // Kleines Extra bleibt bereits fertig, damit du direkt testen kannst.
  sparkToggle?.addEventListener('click', () => {
    document.body.classList.toggle('spark-active');
  });

  updateProgress();
};

window.addEventListener('DOMContentLoaded', () => {
  AOS.init({ once: false, easing: 'ease-out-quart', offset: 160 });
  initScrollStory();
});
