// --- Datenbasis ------------------------------------------------------------
// Jede Kategorie besitzt Items mit Rarität, Gewicht (für die Wahrscheinlichkeit)
// sowie einem kleinen Satz für die Beschreibung.
const lootPools = {
  spielzeug: [
    { name: "Redstone Robo-Buddy", rarity: "epic", weight: 2, emoji: "🤖", description: "Hilft dir beim Farmen, wie ein automatischer Helfer." },
    { name: "Schnee-Boomerang", rarity: "rare", weight: 5, emoji: "🪃", description: "Fliegt wie ein Boomerang und hinterlässt Schneepartikel." },
    { name: "Creeper-Kuscheltier", rarity: "common", weight: 10, emoji: "🧸", description: "Kuschelig, aber ohne Explosion – versprochen!" },
    { name: "Pixel-Schlitten", rarity: "legendary", weight: 1, emoji: "🛷", description: "Hinterlässt leuchtende Partikel auf jeder Strecke." }
  ],
  buecher: [
    { name: "Zauberbuch der Koordinaten", rarity: "rare", weight: 5, emoji: "📘", description: "Führt dich zu geheimen Basen wie ein Kompass." },
    { name: "Redstone-Rezepte Band 7", rarity: "epic", weight: 2, emoji: "📕", description: "Vollgestopft mit Profi-Schaltungen." },
    { name: "Wintermärchen Pixel-Edition", rarity: "common", weight: 10, emoji: "📗", description: "Perfekt zum Einschlafen vor dem Kamin." },
    { name: "Nether-Grimoire", rarity: "legendary", weight: 1, emoji: "📙", description: "Nur für mutige Wizards mit Lava-Skill." }
  ],
  kleidung: [
    { name: "Frostschutz-Poncho", rarity: "common", weight: 9, emoji: "🧣", description: "Halte dich warm während Schneestürmen." },
    { name: "Glow-In-The-Dark Boots", rarity: "rare", weight: 5, emoji: "🥾", description: "Leuchten bei jedem Schritt." },
    { name: "Eis-Kristall Helm", rarity: "epic", weight: 3, emoji: "⛑️", description: "Verleiht +20 Coolness." },
    { name: "Aurora-Mantel", rarity: "legendary", weight: 1, emoji: "🧥", description: "Schimmert wie Nordlichter." }
  ],
  games: [
    { name: "PixelKart 8", rarity: "rare", weight: 4, emoji: "🎮", description: "Race durch Candy-Biome." },
    { name: "Skyblock Deluxe DLC", rarity: "epic", weight: 2, emoji: "🕹️", description: "Neue Inseln plus Pet-Fox." },
    { name: "Creeper Rhythm Game", rarity: "common", weight: 8, emoji: "🎵", description: "Tippe Beats, entschärfe TNT." },
    { name: "VR Nether Escape", rarity: "legendary", weight: 1, emoji: "🧯", description: "Überstehe Lava in Ultra-Realistik." }
  ],
  mischung: [] // wird dynamisch gefüllt, sobald wir mischen möchten
};

const statusList = document.getElementById("statusList");
const giftGrid = document.getElementById("giftGrid");
const boosterRange = document.getElementById("boosterRange");
const boosterValue = document.getElementById("boosterValue");
const form = document.getElementById("generatorForm");
const categorySelect = document.getElementById("categorySelect");
const amountInput = document.getElementById("amountInput");
const mysteryToggle = document.getElementById("mysteryToggle");

// Browser-sichere ID-Erstellung: funktioniert auch ohne HTTPS
const createId = () => {
  const cryptoObj = globalThis.crypto;
  if (cryptoObj && typeof cryptoObj.randomUUID === "function") {
    return cryptoObj.randomUUID();
  }
  return `loot-${Date.now()}-${Math.floor(Math.random() * 1e6)}`;
};

// Farben für Raritäten
const rarityClasses = {
  common: "badge badge--common",
  rare: "badge badge--rare",
  epic: "badge badge--epic",
  legendary: "badge badge--legendary"
};

// Function Declaration: klassischer Funktionsaufbau, sehr gut lesbar
function logStatus(message) {
  const listItem = document.createElement("li");
  listItem.textContent = message;
  statusList.prepend(listItem);
  // Nur die letzten fünf Nachrichten anzeigen, damit es übersichtlich bleibt
  while (statusList.children.length > 5) {
    statusList.removeChild(statusList.lastElementChild);
  }
}

// Function Expression: kompakte Schreibweise, wir speichern sie in einer Konstanten
const pickRandomFromArray = (items) => {
  if (!items.length) return null;
  const index = Math.floor(Math.random() * items.length);
  return items[index];
};

// Hilfsfunktion mit Default-Parameter: wenn nichts übergeben wird, nutzen wir den Standard
function clampAmount(value, min = 1, max = 5) {
  return Math.min(Math.max(value, min), max);
}

// Gewichtete Auswahl: wir multiplizieren seltene Items mit dem Booster
function buildWeightedPool(pool, rarityBoost = 1) {
  const weighted = [];
  pool.forEach((item) => {
    const boostMultiplier = item.rarity === "legendary" ? rarityBoost : 1;
    const copies = Math.max(1, Math.round(item.weight / boostMultiplier));
    for (let i = 0; i < copies; i += 1) {
      weighted.push(item);
    }
  });
  return weighted;
}

function rollItem(category, rarityBoost = 1) {
  // Misch-Kategorie nimmt zufällig eine Basis-Kategorie
  const actualCategory =
    category === "mischung"
      ? pickRandomFromArray(Object.keys(lootPools).filter((key) => key !== "mischung"))
      : category;

  const pool = lootPools[actualCategory];
  if (!pool) return null;
  const weightedPool = buildWeightedPool(pool, rarityBoost);
  return pickRandomFromArray(weightedPool);
}

function createMysteryCube() {
  return {
    name: "Überraschungswürfel",
    rarity: "epic",
    weight: 0,
    emoji: "🎲",
    description: "Verdoppelt beim Öffnen eines Items deiner Liste."
  };
}

function generateGiftBatch(category, amount = 3, options = {}) {
  const { includeMystery = false, rarityBoost = 1 } = options;
  const safeAmount = clampAmount(amount);
  const gifts = [];

  for (let i = 0; i < safeAmount; i += 1) {
    const gift = rollItem(category, rarityBoost);
    if (gift) {
      gifts.push({ ...gift, id: createId(), category });
    }
  }

  if (includeMystery) {
    gifts.push({ ...createMysteryCube(), id: createId(), category: "mystery" });
  }

  return gifts;
}

function renderGiftCards(gifts) {
  if (!gifts.length) {
    giftGrid.innerHTML = "<p>Keine Items gefunden. Stell sicher, dass die Kategorie existiert.</p>";
    return;
  }

  const cards = gifts
    .map((gift) => {
      const rarityClass = rarityClasses[gift.rarity] ?? "badge badge--common";
      const categoryLabel = gift.category === "mischung" ? "Mix" : gift.category;
      const extraBadge = gift.category === "mystery" ? '<span class="badge badge--mystery">mystery</span>' : "";

      return `
        <article class="gift-card" data-rarity="${gift.rarity}">
          <span class="gift-card__emoji">${gift.emoji}</span>
          <h3 class="gift-card__name">${gift.name}</h3>
          <p class="gift-card__rarity">${categoryLabel.toUpperCase()}</p>
          <p class="gift-card__desc">${gift.description}</p>
          <span class="${rarityClass}">${gift.rarity}</span>
          ${extraBadge}
        </article>
      `;
    })
    .join("");

  giftGrid.innerHTML = cards;
}

function updateSummary({ category, amount, booster, mystery }) {
  const summary = `Kategorie: ${category} | Menge: ${amount} | Booster: x${booster}${mystery ? " | plus Überraschung" : ""}`;
  logStatus(summary);
}

function handleGeneration(event) {
  event.preventDefault();

  const category = categorySelect.value;
  const amount = Number(amountInput.value);
  const booster = Number(boosterRange.value);
  const includeMystery = mysteryToggle.checked;

  const gifts = generateGiftBatch(category, amount, {
    includeMystery,
    rarityBoost: booster
  });

  renderGiftCards(gifts);
  updateSummary({ category, amount, booster, mystery: includeMystery });
}

function init() {
  form.addEventListener("submit", handleGeneration);
  boosterRange.addEventListener("input", () => {
    boosterValue.textContent = `x${boosterRange.value}`;
  });

  // Leicht verständliche Default-Generierung, damit die Seite nicht leer wirkt
  const starterLoot = generateGiftBatch("spielzeug", 3, { rarityBoost: 1 });
  renderGiftCards(starterLoot);
  logStatus("Starter-Loot erzeugt. Passe die Parameter an!");
}

init();
