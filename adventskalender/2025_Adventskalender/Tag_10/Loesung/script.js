/*
 * Tag 10 – Interaktives Dashboard für Formulare
 * Dieses Skript verbindet Navigation, Formularvalidierung, Vorschau und Listen-Management.
 */

const panelButtons = document.querySelectorAll('[data-panel-target]');
const panels = document.querySelectorAll('[data-panel]');
const orderList = document.querySelector('#order-list');
const counters = {
  total: document.querySelector('[data-counter="total"]'),
  urgent: document.querySelector('[data-counter="urgent"]'),
  ready: document.querySelector('[data-counter="ready"]')
};

const previewTitle = document.querySelector('.preview-title');
const previewPriority = document.querySelector('#preview-priority');
const previewType = document.querySelector('#preview-type');
const previewQuality = document.querySelector('#preview-quality');
const previewPanel = document.querySelector('#live-preview');

const orderForm = document.querySelector('#gift-order-form');
const priorityPills = document.querySelectorAll('.priority-pill');
const advancedToggle = document.querySelector('#advanced-toggle');
const advancedBlock = document.querySelector('#advanced-block');
const capacityRange = document.querySelector('#capacity-range');
const capacityLabel = document.querySelector('#capacity-label');
const timelineChips = document.querySelectorAll('.timeline-chip');
const timelineDescription = document.querySelector('#timeline-description');
const timelineProgress = document.querySelector('#timeline-progress');
const toast = document.querySelector('#toast');

let activePriority = 'Standard';

const demoOrders = [
  {
    kid: 'Mira (12) aus Dorf Frosttal',
    wish: 'Redstone-Drohne mit Sternenwerfer',
    category: 'Redstone',
    priority: 'Express',
    status: 'Lackierung läuft',
    elf: 'Silver'
  },
  {
    kid: 'Junis (10) aus Zuckerwald',
    wish: 'Selbstwärmender Schal',
    category: 'Dekoration',
    priority: 'Standard',
    status: 'Wartet auf Qualitätscheck',
    elf: 'Emba'
  },
  {
    kid: 'Nora (9) aus Schneehafen',
    wish: 'Mini-Schlitten mit LED-Spuren',
    category: 'Abenteuer',
    priority: 'Notfall',
    status: 'Versand wird vorbereitet',
    elf: 'Luka'
  }
];

function switchPanel(target) {
  panels.forEach((panel) => {
    panel.classList.toggle('hidden', panel.dataset.panel !== target);
  });
  panelButtons.forEach((button) => {
    button.classList.toggle('is-active', button.dataset.panelTarget === target);
  });
}

panelButtons.forEach((button) => {
  button.addEventListener('click', () => switchPanel(button.dataset.panelTarget));
});

function renderOrders() {
  const fragment = document.createDocumentFragment();

  demoOrders.forEach((order) => {
    const item = document.createElement('li');
    item.className = 'order-card';
    item.innerHTML = `
      <div class="order-card__meta">
        <strong>${order.kid}</strong>
        <span class="order-card__priority" data-priority="${order.priority}">${order.priority}</span>
      </div>
      <p>${order.wish}</p>
      <div class="order-card__meta">
        <span>${order.category}</span>
        <span class="order-card__status">Betreuender Elf: ${order.elf}</span>
      </div>
      <span class="order-card__status">Status: ${order.status}</span>
    `;
    fragment.appendChild(item);
  });

  orderList.innerHTML = '';
  orderList.appendChild(fragment);
  updateCounters();
}

function updateCounters() {
  const total = demoOrders.length;
  const urgent = demoOrders.filter((order) => order.priority === 'Express' || order.priority === 'Notfall').length;
  const ready = demoOrders.filter((order) => /Versand|bereit/i.test(order.status)).length;

  counters.total.textContent = total;
  counters.urgent.textContent = urgent;
  counters.ready.textContent = ready;
}

function updatePreview() {
  const kidName = orderForm.kidName.value.trim() || 'Noch kein Wunsch eingetragen';
  const wish = orderForm.wishItem.value.trim();
  const quality = orderForm.qualityCheck.checked ? 'Ja' : 'Nein';

  previewTitle.textContent = wish ? `${kidName} wünscht sich ${wish}` : kidName;
  previewPriority.textContent = activePriority;
  previewType.textContent = orderForm.wishType.value;
  previewQuality.textContent = quality;

  previewPanel.style.background = `linear-gradient(135deg, rgba(158,248,255,${wish ? 0.18 : 0.05}), rgba(255,92,141,${wish ? 0.18 : 0.05}))`;
}

function markFieldState(field) {
  const wrapper = field.closest('.elf-field');
  if (!wrapper) return;
  if (!field.value && field.hasAttribute('required')) {
    wrapper.dataset.state = 'error';
  } else if (field.value) {
    wrapper.dataset.state = 'ok';
  } else {
    wrapper.dataset.state = 'idle';
  }
}

function setPriority(value) {
  activePriority = value;
  priorityPills.forEach((pill) => pill.classList.toggle('is-active', pill.dataset.priority === value));
  previewPriority.textContent = value;
}

priorityPills.forEach((pill) => {
  pill.addEventListener('click', () => setPriority(pill.dataset.priority));
});

if (advancedToggle) {
  advancedToggle.addEventListener('click', () => {
    advancedBlock.classList.toggle('hidden');
    advancedToggle.textContent = advancedBlock.classList.contains('hidden')
      ? '✨ Geheime Elfenoptionen anzeigen'
      : '🔐 Optionen verstecken';
  });
}

if (capacityRange) {
  capacityRange.addEventListener('input', (event) => {
    const value = Number(event.target.value);
    capacityLabel.textContent = `${value}% Werkbank-Energie`;
    document.querySelector('#material-meter').style.width = `${Math.min(value, 120)}%`;
  });
}

timelineChips.forEach((chip, index) => {
  chip.addEventListener('click', () => {
    timelineChips.forEach((c) => c.classList.remove('is-active'));
    chip.classList.add('is-active');
    timelineDescription.textContent = getStageHint(chip.dataset.stage);
    const progress = ((index + 1) / timelineChips.length) * 100;
    timelineProgress.style.width = `${progress}%`;
  });
});

function getStageHint(stage) {
  const hints = {
    Scannen: 'Du digitalisierst Wunschzettel wie ein Kartenleser – Fokus auf saubere Daten!',
    Planen: 'Die UI sortiert alles in Panels, damit keine Info verloren geht.',
    Montage: 'Buttons triggern Maschinenabläufe – nur korrekte Formulare starten sie.',
    QA: 'Validierungsanzeigen zeigen, welche Inputs noch Feinschliff brauchen.'
  };
  return hints[stage] || 'Tippe auf einen Schritt, um mehr zu erfahren.';
}

function showToast(message) {
  if (!toast) return;
  toast.textContent = message;
  toast.classList.add('is-visible');
  setTimeout(() => {
    toast.classList.remove('is-visible');
  }, 2200);
}

function resetFormState() {
  orderForm.reset();
  setPriority('Standard');
  document.querySelectorAll('.elf-field').forEach((field) => {
    field.dataset.state = 'idle';
  });
  updatePreview();
}

function handleSubmit(event) {
  event.preventDefault();
  const data = new FormData(orderForm);

  if (!orderForm.checkValidity()) {
    orderForm.reportValidity();
    return;
  }

  const newOrder = {
    kid: `${data.get('kidName')} (${data.get('elfName') || 'unbekannter Elf'})`,
    wish: data.get('wishItem'),
    category: data.get('wishType'),
    priority: activePriority,
    status: data.get('qualityCheck') ? 'Qualitätscheck geplant' : 'Direkt zur Maschine',
    elf: data.get('elfName') || 'unbekannt'
  };

  demoOrders.unshift(newOrder);
  renderOrders();
  showToast('Neuer Wunsch wurde an die Maschinen gesendet ✨');
  resetFormState();
}

if (orderForm) {
  orderForm.addEventListener('submit', handleSubmit);
  orderForm.addEventListener('input', (event) => {
    if (event.target.matches('input, textarea')) {
      markFieldState(event.target);
    }
    updatePreview();
  });
  orderForm.addEventListener('change', updatePreview);
}

switchPanel('orders');
setPriority('Standard');
renderOrders();
updatePreview();
