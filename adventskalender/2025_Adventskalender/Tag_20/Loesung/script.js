// Tag 20 – Magische Crafting-Station
// -----------------------------------
// Dieser Code baut die komplette Drag-&-Drop-Crafting-UI aus JavaScript heraus auf.
// Alle Karten, Slots und Rezepte entstehen mit createElement – so lernst du, wie
// dynamische Interfaces ganz ohne statisches HTML funktionieren.

const inventoryBlueprint = [
  {
    id: 'scissors',
    name: 'Laser-Schere',
    emoji: '✂️',
    lore: 'Schneidet Sternenpapier millimetergenau.',
    rarity: 'episch',
    type: 'Werkzeug',
    accent: 'from-fuchsia-500 to-rose-400',
  },
  {
    id: 'paper',
    name: 'Polar-Papier',
    emoji: '📜',
    lore: 'Schimmert wie Eis, wenn Licht darauf fällt.',
    rarity: 'selten',
    type: 'Material',
    accent: 'from-cyan-400 to-sky-500',
  },
  {
    id: 'candle',
    name: 'Frostkerze',
    emoji: '🕯️',
    lore: 'Bringt sanftes Licht in jede Werkbank.',
    rarity: 'magisch',
    type: 'Deko',
    accent: 'from-amber-400 to-orange-500',
  },
  {
    id: 'holder',
    name: 'Schneeflocken-Halter',
    emoji: '🪔',
    lore: 'Hält Flammen ruhig – auch bei Nordwind.',
    rarity: 'magisch',
    type: 'Träger',
    accent: 'from-indigo-400 to-purple-500',
  },
  {
    id: 'bell',
    name: 'Rotguss-Glocke',
    emoji: '🔔',
    lore: 'Weckt jede Elfentruppe.',
    rarity: 'episch',
    type: 'Signal',
    accent: 'from-rose-400 to-red-500',
  },
  {
    id: 'redstone',
    name: 'Nordlicht-Redstone',
    emoji: '🧱',
    lore: 'Speichert elektrische Weihnachtsenergie.',
    rarity: 'legendär',
    type: 'Energie',
    accent: 'from-lime-400 to-emerald-500',
  },
];

const recipeBook = [
  {
    id: 'giftwrap',
    title: 'Leucht-Geschenkpapier',
    emoji: '🎁',
    description:
      'Wenn du Laser-Schere und Polar-Papier kombinierst, entsteht eine Folie, die Geschenke automatisch einpackt.',
    inputs: ['scissors', 'paper'],
    bonus: 'Tipp: Erst schneiden, dann falten!',
  },
  {
    id: 'lantern',
    title: 'Windlicht der Hoffnung',
    emoji: '🕯️',
    description:
      'Die Frostkerze sitzt perfekt im Schneeflocken-Halter. Zusammen ergibt das ein warmes Windlicht ohne Ruß.',
    inputs: ['candle', 'holder'],
    bonus: 'Platziere zuerst den Halter, dann die Kerze für stabile Flammen.',
  },
  {
    id: 'alarm',
    title: 'Alarm-Girlande',
    emoji: '🎐',
    description:
      'Verbinde Rotguss-Glocke mit Nordlicht-Redstone und du erhältst eine Girlande, die bei Magier-Alarm aufleuchtet.',
    inputs: ['bell', 'redstone'],
    bonus: 'Rufe die Elfen nur, wenn es wirklich wichtig ist!',
  },
];

// State-Management Objekt – hier merkt sich die Station, was in welchem Slot liegt.
const craftingState = {
  slots: {},
  history: [],
};

const slotIds = ['slot-1', 'slot-2', 'slot-3', 'slot-4'];
slotIds.forEach((id) => {
  craftingState.slots[id] = null;
});

// Haupt-Elemente greifen
const inventoryPanel = document.querySelector('[data-inventory-panel]');
const gridPanel = document.querySelector('[data-grid-panel]');
const recipePanel = document.querySelector('[data-recipe-book]');
const resultCard = document.querySelector('[data-result-card]');
const eventLog = document.querySelector('[data-event-log]');
const resetButton = document.querySelector('[data-reset-grid]');
const energyBar = document.querySelector('[data-energy-bar]');

// Sicherheitsnetz: Falls etwas fehlt, brechen wir früh ab.
if (!inventoryPanel || !gridPanel || !recipePanel || !resultCard) {
  throw new Error('Layout-Container fehlen – bitte HTML-Struktur prüfen.');
}

const getItem = (id) => inventoryBlueprint.find((item) => item.id === id);

const logEvent = (message, type = 'info') => {
  const entry = document.createElement('li');
  entry.className =
    type === 'success'
      ? 'border border-emerald-400/50 bg-emerald-950/40 rounded-xl px-3 py-2 text-emerald-100 text-sm'
      : 'text-slate-200 text-sm';
  entry.textContent = `${new Date().toLocaleTimeString()} · ${message}`;
  eventLog.prepend(entry);
  craftingState.history.push({ message, type });
  if (eventLog.children.length > 6) {
    eventLog.lastElementChild?.remove();
  }
};

const buildInventory = () => {
  inventoryBlueprint.forEach((item) => {
    const card = document.createElement('button');
    card.className = `inventory-card text-left bg-gradient-to-br ${item.accent}`;
    card.type = 'button';
    card.setAttribute('draggable', 'true');
    card.dataset.itemId = item.id;
    card.dataset.itemName = item.name;
    card.dataset.itemEmoji = item.emoji;
    card.dataset.itemType = item.type;
    card.innerHTML = `
      <span class="text-3xl">${item.emoji}</span>
      <h3>${item.name}</h3>
      <p>${item.lore}</p>
      <div class="text-xs uppercase tracking-[0.2em]">${item.rarity}</div>
    `;

    // Drag & Drop Ereignisse
    card.addEventListener('dragstart', (event) => {
      card.classList.add('opacity-80');
      event.dataTransfer.setData('text/plain', item.id);
      event.dataTransfer.effectAllowed = 'copy';
    });

    card.addEventListener('dragend', () => {
      card.classList.remove('opacity-80');
    });

    // Tastaturbedienung: ENTER legt Item auf den ersten freien Slot.
    card.addEventListener('keydown', (event) => {
      if (event.key === 'Enter') {
        const emptySlot = slotIds
          .map((id) => document.querySelector(`[data-slot-id="${id}"]`))
          .find((slot) => slot && !slot.dataset.itemId);
        if (emptySlot) {
          placeItemInSlot(emptySlot, item.id);
        }
      }
    });

    inventoryPanel.appendChild(card);
  });
};

const createSlot = (slotId, label) => {
  const slot = document.createElement('button');
  slot.className = 'crafting-slot text-white text-4xl flex items-center justify-center';
  slot.type = 'button';
  slot.setAttribute('data-slot-id', slotId);
  slot.dataset.slotId = slotId;
  slot.setAttribute('data-slot-label', label);
  slot.setAttribute('aria-label', `Crafting Slot ${label}`);
  slot.addEventListener('dragover', (event) => {
    event.preventDefault();
    slot.classList.add('ring-2', 'ring-emerald-300/60');
  });
  slot.addEventListener('dragleave', () => {
    slot.classList.remove('ring-2', 'ring-emerald-300/60');
  });
  slot.addEventListener('drop', (event) => {
    event.preventDefault();
    slot.classList.remove('ring-2', 'ring-emerald-300/60');
    const itemId = event.dataTransfer.getData('text/plain');
    if (!itemId) return;
    placeItemInSlot(slot, itemId);
  });
  slot.addEventListener('dblclick', () => clearSlot(slot));
  slot.addEventListener('keydown', (event) => {
    if (event.key === 'Delete') {
      clearSlot(slot);
    }
  });
  gridPanel.appendChild(slot);
};

const clearSlot = (slot) => {
  if (!slot.dataset.itemId) return;
  logEvent(`Slot ${slot.getAttribute('data-slot-label')} wurde geleert.`);
  slot.textContent = '';
  slot.removeAttribute('data-item-id');
  slot.removeAttribute('data-item-name');
  slot.removeAttribute('data-item-emoji');
  slot.dataset.filled = 'false';
  craftingState.slots[slot.dataset.slotId] = null;
  evaluateRecipe();
};

const placeItemInSlot = (slot, itemId) => {
  const item = getItem(itemId);
  if (!item) {
    logEvent('Dieses Item existiert nicht (mehr) im Inventar.', 'error');
    return;
  }
  if (slot.hasAttribute('data-item-id')) {
    logEvent(`Slot ${slot.getAttribute('data-slot-label')} wurde überschrieben.`);
  }
  slot.dataset.itemId = item.id;
  slot.dataset.itemName = item.name;
  slot.dataset.itemEmoji = item.emoji;
  slot.dataset.filled = 'true';
  slot.textContent = item.emoji;
  craftingState.slots[slot.dataset.slotId] = item.id;
  logEvent(`${item.name} liegt jetzt im Slot ${slot.getAttribute('data-slot-label')}.`);
  evaluateRecipe();
};

const evaluateRecipe = () => {
  const filledItems = Object.values(craftingState.slots).filter(Boolean);
  updateEnergyBar(filledItems.length);

  if (!filledItems.length) {
    updateResultCard();
    return;
  }

  const key = filledItems
    .slice()
    .sort()
    .join('|');

  const match = recipeBook.find((recipe) => {
    return recipe.inputs.slice().sort().join('|') === key;
  });

  if (match) {
    updateResultCard(match, true);
    logEvent(`Rezept entdeckt: ${match.title}!`, 'success');
  } else if (filledItems.length >= 2) {
    updateResultCard({
      title: 'Hmm... kein Rezept',
      emoji: '❓',
      description: 'Diese Mischung gibt noch keinen Sinn. Probier eine andere Kombination!',
    });
  } else {
    updateResultCard();
  }
};

const updateResultCard = (recipe = null, success = false) => {
  resultCard.innerHTML = '';
  if (!recipe) {
    resultCard.innerHTML = '<p class="text-sm text-slate-400">Lege Items ab, um das Rezept zu entdecken.</p>';
    return;
  }

  const title = document.createElement('h3');
  title.className = 'title flex items-center gap-2';
  title.innerHTML = `<span class="text-3xl">${recipe.emoji}</span> ${recipe.title}`;

  const description = document.createElement('p');
  description.className = 'description';
  description.textContent = recipe.description;

  resultCard.appendChild(title);
  resultCard.appendChild(description);

  if (success && recipe.bonus) {
    const bonus = document.createElement('p');
    bonus.className = 'text-xs uppercase tracking-[0.3em] text-emerald-200';
    bonus.textContent = recipe.bonus;
    resultCard.appendChild(bonus);
  }
};

const renderRecipeBook = () => {
  recipeBook.forEach((recipe) => {
    const entry = document.createElement('article');
    entry.className = 'recipe-entry';

    const heading = document.createElement('strong');
    heading.innerHTML = `${recipe.emoji} ${recipe.title}`;
    entry.appendChild(heading);

    const combo = document.createElement('div');
    combo.className = 'flex items-center gap-2 text-xl';
    combo.innerHTML = recipe.inputs
      .map((id) => getItem(id)?.emoji || '❔')
      .join('<span class="text-base text-slate-500">＋</span>');
    entry.appendChild(combo);

    const description = document.createElement('p');
    description.textContent = recipe.description;
    entry.appendChild(description);

    if (recipe.bonus) {
      const bonus = document.createElement('p');
      bonus.className = 'text-xs text-emerald-200';
      bonus.textContent = recipe.bonus;
      entry.appendChild(bonus);
    }

    recipePanel.appendChild(entry);
  });
};

const resetGrid = () => {
  document.querySelectorAll('[data-slot-id]').forEach((slot) => {
    slot.textContent = '';
    slot.removeAttribute('data-item-id');
    slot.removeAttribute('data-item-name');
    slot.removeAttribute('data-item-emoji');
    slot.dataset.filled = 'false';
    craftingState.slots[slot.dataset.slotId] = null;
  });
  updateEnergyBar(0);
  updateResultCard();
  logEvent('Alle Slots wurden zurückgesetzt.');
};

const updateEnergyBar = (filledCount) => {
  const percent = Math.round((filledCount / slotIds.length) * 100);
  energyBar.style.width = `${percent}%`;
  energyBar.setAttribute('aria-valuenow', String(percent));
  energyBar.setAttribute('aria-valuemin', '0');
  energyBar.setAttribute('aria-valuemax', '100');
};

const init = () => {
  buildInventory();
  slotIds.forEach((id, index) => {
    const label = `Slot ${index + 1}`;
    createSlot(id, label);
  });
  renderRecipeBook();
  logEvent('Die Crafting-Station ist bereit. Ziehe Items auf das Gitter!');
};

resetButton?.addEventListener('click', resetGrid);

init();
