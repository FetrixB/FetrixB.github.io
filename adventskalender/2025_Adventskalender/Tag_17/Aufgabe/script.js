const lootPools = {
  spielzeug: [
    { name: "Redstone Robo-Buddy", rarity: "epic", weight: 2, emoji: "🤖", description: "Automatischer Helfer wie ein Mini-Golem." },
    { name: "Schnee-Boomerang", rarity: "rare", weight: 5, emoji: "🪃", description: "Hinterlässt Winterpartikel." },
    { name: "Creeper-Kuscheltier", rarity: "common", weight: 10, emoji: "🧸", description: "Weicher als jeder Creeper." },
    { name: "Pixel-Schlitten", rarity: "legendary", weight: 1, emoji: "🛷", description: "Lässt Funkenregeln zurück." }
  ],
  buecher: [
    { name: "Zauberbuch der Koordinaten", rarity: "rare", weight: 5, emoji: "📘", description: "Findet Basen wie ein Kompass." },
    { name: "Redstone-Rezepte Band 7", rarity: "epic", weight: 2, emoji: "📕", description: "Voller Profi-Schaltungen." },
    { name: "Wintermärchen Pixel-Edition", rarity: "common", weight: 10, emoji: "📗", description: "Perfekt neben dem Kamin." },
    { name: "Nether-Grimoire", rarity: "legendary", weight: 1, emoji: "📙", description: "Nur für Lava-Profis." }
  ],
  kleidung: [
    { name: "Frostschutz-Poncho", rarity: "common", weight: 9, emoji: "🧣", description: "Hält dich warm." },
    { name: "Glow-In-The-Dark Boots", rarity: "rare", weight: 5, emoji: "🥾", description: "Leuchten bei jedem Schritt." },
    { name: "Eis-Kristall Helm", rarity: "epic", weight: 3, emoji: "⛑️", description: "Verleiht Coolness." },
    { name: "Aurora-Mantel", rarity: "legendary", weight: 1, emoji: "🧥", description: "Schimmert wie Nordlichter." }
  ],
  games: [
    { name: "PixelKart 8", rarity: "rare", weight: 4, emoji: "🎮", description: "Rase durch Candy-Biome." },
    { name: "Skyblock Deluxe DLC", rarity: "epic", weight: 2, emoji: "🕹️", description: "Neue Inseln!" },
    { name: "Creeper Rhythm Game", rarity: "common", weight: 8, emoji: "🎵", description: "Tippe Beats, entschärfe TNT." },
    { name: "VR Nether Escape", rarity: "legendary", weight: 1, emoji: "🧯", description: "Überlebe Lava in VR." }
  ],
  mischung: []
};

const statusList = document.getElementById("statusList");
const giftGrid = document.getElementById("giftGrid");
const boosterRange = document.getElementById("boosterRange");
const boosterValue = document.getElementById("boosterValue");
const form = document.getElementById("generatorForm");
const categorySelect = document.getElementById("categorySelect");
const amountInput = document.getElementById("amountInput");
const mysteryToggle = document.getElementById("mysteryToggle");

const createId = () => {
  const cryptoObj = globalThis.crypto;
  if (cryptoObj && typeof cryptoObj.randomUUID === "function") {
    return cryptoObj.randomUUID();
  }
  return `loot-${Date.now()}-${Math.floor(Math.random() * 1e6)}`;
};

const rarityClasses = {
  common: "badge badge--common",
  rare: "badge badge--rare",
  epic: "badge badge--epic",
  legendary: "badge badge--legendary"
};

function logStatus(message) {
  const listItem = document.createElement("li");
  listItem.textContent = message;
  statusList.prepend(listItem);
  while (statusList.children.length > 5) {
    statusList.removeChild(statusList.lastElementChild);
  }
}

const pickRandomFromArray = (items) => {
  if (!items.length) return null;
  const index = Math.floor(Math.random() * items.length);
  return items[index];
};

function clampAmount(value, min = 1, max = 5) {
  return Math.min(Math.max(value, min), max);
}

// TODO 3: Vervollständige hier die gewichtete Loot-Berechnung (inkl. Booster) wie in der Lösung, damit legendäre Items bei höherem Booster wahrscheinlicher auftauchen.
function buildWeightedPool(pool, rarityBoost = 1) {
  return pool;
}

function rollItem(category, rarityBoost = 1) {
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
    description: "Verdoppelt ein Item deiner Liste."
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
    giftGrid.innerHTML = "<p>Keine Items gefunden.</p>";
    return;
  }

  giftGrid.innerHTML = gifts
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

  const starterLoot = generateGiftBatch("spielzeug", 2, { rarityBoost: 1 });
  renderGiftCards(starterLoot);
  logStatus("Starter-Loot erzeugt. Passe die Parameter an!");
}

init();
