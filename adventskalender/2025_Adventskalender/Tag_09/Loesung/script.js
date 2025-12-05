// Banner-Datensätze bilden die Grundlage für die wiederverwendbaren Karten.
const banners = [
  {
    id: 'aurora-loom',
    title: 'Aurora Loom',
    biome: 'Frosttal',
    mood: 'frostig',
    rarity: 'Episch',
    description:
      'Schickt milchige Nordlichter über den Marktplatz. Perfekt für den Eis-Stand der Schneegnome.',
    features: ['Schimmernder Header mit Icon', 'Frost-Badge + XP-Label', 'Gradient-Overlay mit Glow'],
    level: 12,
    reward: 'Leuchtfaden x3',
    gradient: 'linear-gradient(135deg, #7dd3fc, #c4b5fd)',
    icon: '❄️',
    glow: ['rgba(125, 211, 252, 0.9)', 'rgba(196, 181, 253, 0.7)'],
  },
  {
    id: 'ember-crest',
    title: 'Ember Crest',
    biome: 'Kaminhalle',
    mood: 'feurig',
    rarity: 'Legendär',
    description:
      'Feurige Rot- und Goldtöne für alle Banner, die Mut und Wärme ausstrahlen sollen.',
    features: ['Twin-Badges für Siedlungen', 'Highlight für anstehende Events', 'Button mit Glut-Glow'],
    level: 20,
    reward: 'Funkenkern',
    gradient: 'linear-gradient(135deg, #fb7185, #f97316)',
    icon: '🔥',
    glow: ['rgba(251, 113, 133, 0.9)', 'rgba(249, 115, 22, 0.7)'],
  },
  {
    id: 'candy-pulse',
    title: 'Candy Pulse',
    biome: 'Zuckerwald',
    mood: 'festlich',
    rarity: 'Selten',
    description:
      'Süße Pastelllinien für Geschenke, Spenden und alles, was glänzen soll.',
    features: ['Gestreifte Kopfleiste', 'Badge-Stack für Missionen', 'Candy-Icon mit Glow'],
    level: 9,
    reward: 'Zuckerstab Stack',
    gradient: 'linear-gradient(135deg, #f472b6, #fb7185)',
    icon: '🍭',
    glow: ['rgba(244, 114, 182, 0.9)', 'rgba(251, 113, 133, 0.7)'],
  },
  {
    id: 'ivy-shield',
    title: 'Ivy Shield',
    biome: 'Moosige Lichtung',
    mood: 'festlich',
    rarity: 'Episch',
    description:
      'Gewebte Blätterkarten, die das Dorf wie einen schützenden Gürtel umgeben.',
    features: ['Gradient aus Moos und Gold', 'Biome-Badge', 'List-Layout mit Questpunkten'],
    level: 15,
    reward: 'Moosmedaille',
    gradient: 'linear-gradient(135deg, #34d399, #10b981)',
    icon: '🌿',
    glow: ['rgba(52, 211, 153, 0.9)', 'rgba(16, 185, 129, 0.7)'],
  },
  {
    id: 'midnight-bell',
    title: 'Midnight Bell',
    biome: 'Ender-Himmel',
    mood: 'mystisch',
    rarity: 'Legendär',
    description:
      'Flüsternde Glocken aus dem End, die bei jedem Blick kleine Partikel versprühen.',
    features: ['Dunkles Headline-Board', 'Mystische XP-Anzeige', 'Hover-Schatten mit Violett'],
    level: 22,
    reward: 'Enderfunke',
    gradient: 'linear-gradient(135deg, #6366f1, #c084fc)',
    icon: '🔮',
    glow: ['rgba(99, 102, 241, 0.9)', 'rgba(192, 132, 252, 0.7)'],
  },
  {
    id: 'glacier-note',
    title: 'Glacier Note',
    biome: 'Kristallhöhle',
    mood: 'frostig',
    rarity: 'Selten',
    description:
      'Kühle Blau-Schichten, die Nachrichten glasklar machen und trotzdem freundlich wirken.',
    features: ['Farbige Progress-Bar', 'Liste für Aufgaben', 'Sekundärer Button für Details'],
    level: 10,
    reward: 'Eisprisma',
    gradient: 'linear-gradient(135deg, #38bdf8, #6366f1)',
    icon: '🧊',
    glow: ['rgba(56, 189, 248, 0.9)', 'rgba(99, 102, 241, 0.6)'],
  },
  {
    id: 'lantern-loop',
    title: 'Lantern Loop',
    biome: 'Basar der Lichter',
    mood: 'festlich',
    rarity: 'Selten',
    description:
      'Goldene Laternenketten zeigen neue Shops an und geben sofortige Good-Vibes.',
    features: ['Icon-Ring', 'Footer mit Team-Badges', 'Zwei Buttons für Aktionen'],
    level: 7,
    reward: 'Laternenöl',
    gradient: 'linear-gradient(135deg, #fbbf24, #f97316)',
    icon: '🏮',
    glow: ['rgba(251, 191, 36, 0.9)', 'rgba(249, 115, 22, 0.6)'],
  },
  {
    id: 'prism-drift',
    title: 'Prism Drift',
    biome: 'Polarhafen',
    mood: 'mystisch',
    rarity: 'Episch',
    description:
      'Dreifarbiger Verlauf, der beim Scrollen wie Polarlicht wirkt und Nachrichten elegant einrahmt.',
    features: ['Stat-Stack im Header', 'Ziel-Liste', 'CTA mit Icon'],
    level: 18,
    reward: 'Prismensplitter',
    gradient: 'linear-gradient(135deg, #a855f7, #ec4899, #f97316)',
    icon: '💠',
    glow: ['rgba(168, 85, 247, 0.9)', 'rgba(236, 72, 153, 0.7)'],
  },
  {
    id: 'ember-leaf',
    title: 'Cedar Ember',
    biome: 'Tannenkronen',
    mood: 'feurig',
    rarity: 'Selten',
    description:
      'Mischung aus Holztextur und Funkenregen. Perfekt für Quest-Boards.',
    features: ['Badge-Stack', 'Checkliste', 'Glühender Footer'],
    level: 11,
    reward: 'Tannenharz',
    gradient: 'linear-gradient(135deg, #0f766e, #f97316)',
    icon: '🎄',
    glow: ['rgba(15, 118, 110, 0.9)', 'rgba(249, 115, 22, 0.6)'],
  },
];

const cardGrid = document.getElementById('card-grid');
const detailList = document.getElementById('detailList');
const bannerDetail = document.getElementById('bannerDetail');
const filterButtons = document.querySelectorAll('[data-filter]');
const floatRange = document.getElementById('floatRange');
const floatHint = document.getElementById('floatHint');
const layoutToggle = document.getElementById('layoutToggle');
const themeButtons = document.querySelectorAll('[data-theme-choice]');

let currentFilter = 'alle';
let listMode = false;
let activeCardId = null;

const themeMap = {
  winter: 'winter',
  forest: 'forest',
  candy: 'cupcake',
  ember: 'sunset',
};

// DaisyUI + Tailwind Template für eine einzelne Bannerkarte.
function createCardTemplate(banner) {
  return `
    <article class="card bg-base-100/90 border border-white/10 card-floating" data-id="${banner.id}" style="--glow-primary:${banner.glow[0]}; --glow-secondary:${banner.glow[1]};">
      <figure class="relative h-40">
        <div class="absolute inset-0" style="background:${banner.gradient};"></div>
        <div class="banner-glow"></div>
        <div class="absolute inset-0 flex flex-col justify-between p-4 text-white">
          <div class="flex justify-between text-sm">
            <span class="badge badge-outline text-white border-white/60 bg-white/10">${banner.biome}</span>
            <span class="badge badge-primary banner-mood">${banner.mood}</span>
          </div>
          <div class="flex items-center justify-between text-3xl font-orbitron">
            <span>${banner.icon}</span>
            <span class="text-sm tracking-widest">Lvl ${banner.level}</span>
          </div>
        </div>
      </figure>
      <div class="card-body gap-4">
        <div class="flex items-start justify-between gap-2">
          <div>
            <h3 class="card-title text-lg font-orbitron">${banner.title}</h3>
            <p class="text-sm text-base-content/70">${banner.description}</p>
          </div>
          <span class="badge badge-accent">${banner.rarity}</span>
        </div>
        <ul class="list-disc list-inside text-sm text-base-content/80 space-y-1">
          ${banner.features.map((feature) => `<li>${feature}</li>`).join('')}
        </ul>
        <div class="card-actions justify-between items-center">
          <span class="text-xs uppercase tracking-wide text-base-content/60">Belohnung: ${banner.reward}</span>
          <button class="btn btn-primary btn-sm" data-banner="${banner.id}">Zum Dorf schicken</button>
        </div>
      </div>
    </article>
  `;
}

// Rendert gefilterte Banner neu und verbindet Events.
function renderCards() {
  const filteredBanners =
    currentFilter === 'alle' ? banners : banners.filter((banner) => banner.mood === currentFilter);
  if (!filteredBanners.length) {
    cardGrid.innerHTML =
      '<p class="text-center text-base-content/60 col-span-full">Keine Banner in dieser Stimmung. Versuche einen anderen Filter.</p>';
    activeCardId = null;
    return;
  }
  cardGrid.innerHTML = filteredBanners.map((banner) => createCardTemplate(banner)).join('');
  attachCardEvents();
  if (activeCardId) {
    highlightCard(activeCardId);
  }
}

function attachCardEvents() {
  const buttons = cardGrid.querySelectorAll('[data-banner]');
  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      const id = button.dataset.banner;
      const banner = banners.find((entry) => entry.id === id);
      if (banner) {
        highlightCard(id);
        updateDetailPanel(banner);
      }
    });
  });
}

function highlightCard(id) {
  const cards = cardGrid.querySelectorAll('[data-id]');
  cards.forEach((card) => {
    card.classList.toggle('ring', card.dataset.id === id);
    card.classList.toggle('ring-offset-2', card.dataset.id === id);
    card.classList.toggle('ring-primary', card.dataset.id === id);
  });
  activeCardId = id;
}

function updateDetailPanel(banner) {
  bannerDetail.querySelector('h3').textContent = banner.title;
  detailList.innerHTML = `
    <li><strong>Biome:</strong> ${banner.biome}</li>
    <li><strong>Stimmung:</strong> ${banner.mood}</li>
    <li><strong>Seltenheit:</strong> ${banner.rarity}</li>
    <li><strong>Belohnung:</strong> ${banner.reward}</li>
    <li><strong>Features:</strong>
      <ul class="list-disc list-inside mt-1 space-y-1">
        ${banner.features.map((feature) => `<li>${feature}</li>`).join('')}
      </ul>
    </li>
  `;
}

function setFilter(filter) {
  currentFilter = filter;
  filterButtons.forEach((btn) => btn.classList.toggle('active', btn.dataset.filter === filter));
  renderCards();
}

function initFilters() {
  filterButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      setFilter(btn.dataset.filter);
    });
  });
  setFilter('alle');
}

// Steuert die Hover-Schwebe über eine CSS-Variable.
function initFloatControl() {
  if (!floatRange) return;
  const updateFloat = (value) => {
    document.documentElement.style.setProperty('--float-range', `${value}px`);
    floatHint.textContent = `${value}px`;
  };
  floatRange.addEventListener('input', (event) => updateFloat(event.target.value));
  updateFloat(floatRange.value);
}

function initLayoutToggle() {
  if (!layoutToggle) return;
  layoutToggle.addEventListener('click', () => {
    listMode = !listMode;
    layoutToggle.setAttribute('aria-pressed', String(listMode));
    layoutToggle.textContent = listMode ? '🧊 Raster anzeigen' : '📐 Listenmodus aktivieren';
    cardGrid.classList.toggle('list-view', listMode);
  });
}

// Aktiviert thematische DaisyUI-Skins.
function initThemeButtons() {
  themeButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      const choice = btn.dataset.themeChoice;
      const theme = themeMap[choice] || 'winter';
      document.documentElement.setAttribute('data-theme', theme);
      themeButtons.forEach((innerBtn) => innerBtn.classList.remove('btn-active'));
      btn.classList.add('btn-active');
    });
  });
}

renderCards();
initFilters();
initFloatControl();
initLayoutToggle();
initThemeButtons();
