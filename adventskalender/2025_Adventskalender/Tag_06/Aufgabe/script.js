'use strict';

(function () {
  const bookWrapper = document.querySelector('.book-wrapper');
  const fallbackSection = document.getElementById('static-article');
  const statusBadge = document.querySelector('[data-status-badge]');
  const progressLabel = document.querySelector('[data-progress-text]');
  const progressFill = document.querySelector('[data-progress-fill]');
  const sigil = document.querySelector('.floating-sigil');

  const tips = [
    'Magie bereit',
    'Blättere mit ← →',
    'Tippe auf eine Seite',
    'Probier eine Touch-Geste'
  ];
  let tipIndex = 0;

  function setStatus(text) {
    if (!statusBadge) return;
    statusBadge.textContent = `🔮 ${text}`;
  }

  function enableFallback(reason) {
    if (bookWrapper) {
      bookWrapper.setAttribute('data-disabled', 'true');
    }
    if (fallbackSection) {
      fallbackSection.hidden = false;
    }
    setStatus(reason);
  }

  function getBookSize(bookElement) {
    const width = Math.min(900, Math.max(420, Math.floor(bookElement.getBoundingClientRect().width || 720)));
    const height = Math.max(360, Math.floor(width * 0.66));
    return { width, height };
  }

  function formatStage(page, total) {
    if (!total) return 'Kapitel 1 / 1';
    if (page === 1) {
      return 'Deckblatt · Willkommen';
    }
    if (page === total) {
      return 'Epilog · Abschluss';
    }
    const logicalTotal = Math.max(1, total - 2);
    const logicalCurrent = Math.min(logicalTotal, Math.max(1, page - 1));
    return `Kapitel ${logicalCurrent} / ${logicalTotal}`;
  }

  function updateSigil(percent) {
    if (!sigil) return;
    const rotation = Math.round(percent * 360);
    sigil.style.transform = `rotate(${rotation}deg)`;
    sigil.style.opacity = 0.6 + percent * 0.4;
  }

  function updateProgress(page, total) {
    if (!progressLabel || !progressFill) {
      return;
    }
    progressLabel.textContent = formatStage(page, total);
    const safeTotal = Math.max(1, total - 1);
    const progress = Math.min(1, Math.max(0, (page - 1) / safeTotal));
    progressFill.style.width = `${(progress * 100).toFixed(0)}%`;
    updateSigil(progress);
    tipIndex = (tipIndex + 1) % tips.length;
    setStatus(tips[tipIndex]);
  }

  function createDebouncedResize(callback, delay = 200) {
    let timeoutId;
    return () => {
      window.clearTimeout(timeoutId);
      timeoutId = window.setTimeout(callback, delay);
    };
  }

  function bindButtons($book) {
    const buttons = document.querySelectorAll('[data-direction]');
    buttons.forEach((button) => {
      button.addEventListener('click', () => {
        if (button.dataset.direction === 'next') {
          $book.turn('next');
        } else {
          $book.turn('previous');
        }
      });
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'ArrowRight') {
        $book.turn('next');
      }
      if (event.key === 'ArrowLeft') {
        $book.turn('previous');
      }
    });
  }

  function initFlipbook() {
    const bookElement = document.getElementById('book');
    if (!bookElement) {
      return;
    }

    if (!window.jQuery || !window.jQuery.fn || typeof window.jQuery.fn.turn !== 'function') {
      enableFallback('Turn.js konnte nicht geladen werden');
      return;
    }

    const $book = window.jQuery(bookElement);
    const { width, height } = getBookSize(bookElement);

    $book.turn({
      width,
      height,
      autoCenter: true,
      gradients: true,
      duration: 900,
      elevation: 120,
      when: {
        turning: (event, page) => {
          updateProgress(page, $book.turn('pages'));
        },
        turned: (event, page) => {
          updateProgress(page, $book.turn('pages'));
        }
      }
    });

    const debouncedResize = createDebouncedResize(() => {
      const size = getBookSize(bookElement);
      $book.turn('size', size.width, size.height);
    }, 250);
    window.addEventListener('resize', debouncedResize, { passive: true });

    bindButtons($book);
    updateProgress($book.turn('page'), $book.turn('pages'));
    setStatus('Magie bereit');
  }

  document.addEventListener('DOMContentLoaded', initFlipbook);
})();
