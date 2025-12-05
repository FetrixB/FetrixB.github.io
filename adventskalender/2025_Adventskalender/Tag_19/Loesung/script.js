const creationField = document.getElementById("creationField");
const spellButtons = document.getElementById("spellButtons");
const spellLog = document.getElementById("spellLog");
const removeLastButton = document.getElementById("removeLast");
const clearAllButton = document.getElementById("clearAll");
const toggleGlowButton = document.getElementById("toggleGlow");
const cardTemplate = document.getElementById("spellCard");

// Blueprint fuer alle Zauber. So koennen wir spaeter neue Varianten leicht ergaenzen.
const spells = {
  wald: {
    title: "Moosiger Wald",
    text: "Erzeugt mehrere Mini-Baeume mit weichem Nebel.",
    icon: "🌲",
    badge: "Nature",
    flavorClass: "spell-card--forest"
  },
  quelle: {
    title: "Kuehle Quelle",
    text: "Laesst particles wabern und spendet Heilung.",
    icon: "💧",
    badge: "Water",
    flavorClass: "spell-card--water"
  },
  kristall: {
    title: "Kristallturm",
    text: "Baut tuerkis funkelnde Tuerme aus Licht.",
    icon: "💎",
    badge: "Crystal",
    flavorClass: "spell-card--crystal"
  },
  funken: {
    title: "Funkenregen",
    text: "Stylt bestehende Karten mit elektrischen Highlights.",
    icon: "⚡",
    badge: "Style",
    flavorClass: "spell-card--spark"
  }
};

function createSpellCard({ title, text, icon, badge, flavorClass }) {
  const fragment = cardTemplate.content.cloneNode(true);
  const card = fragment.querySelector(".spell-card");
  card.classList.add(flavorClass);
  fragment.querySelector(".spell-card__icon").textContent = icon;
  fragment.querySelector(".spell-card__title").textContent = title;
  fragment.querySelector(".spell-card__text").textContent = text;
  fragment.querySelector(".spell-card__badge").textContent = badge;
  return fragment;
}

function addLogEntry(message) {
  const entry = document.createElement("button");
  entry.type = "button";
  entry.className = "spell-log__entry";
  // textContent verhindert, dass ungewolltes HTML interpretiert wird
  entry.textContent = message;
  spellLog.prepend(entry);
}

function ensureFieldIsReady() {
  if (creationField.querySelector(".spell-card")) return;
  creationField.innerHTML = "";
}

function castSpell(name) {
  const config = spells[name];
  if (!config) {
    console.warn("Unbekannter Zauber:", name);
    return;
  }

  if (name === "funken") {
    document.querySelectorAll(".spell-card").forEach((card, index) => {
      card.style.setProperty("--spark", `${index * 0.2}s`);
      card.classList.toggle("is-charged");
    });
    addLogEntry("⚡ Funkenregen toggled alle Karten");
    return;
  }

  ensureFieldIsReady();
  const card = createSpellCard(config);
  creationField.appendChild(card);
  creationField.classList.add("glow");
  addLogEntry(`✨ ${config.title} wurde erschaffen`);
}

function removeLastElement() {
  const cards = creationField.querySelectorAll(".spell-card");
  if (!cards.length) return;
  cards[cards.length - 1].remove();
  addLogEntry("🌀 Letzte Projektion wurde geloescht");
  if (!creationField.querySelector(".spell-card")) {
    creationField.classList.remove("glow");
    creationField.innerHTML = "<p class='text-center text-slate-400'>Feld ist leer. Wir brauchen neue Energie!</p>";
  }
}

function clearField() {
  creationField.replaceChildren();
  creationField.classList.remove("glow");
  creationField.innerHTML = "<p class='text-center text-slate-400'>Sauberes Feld. Beschwoere etwas Neues!</p>";
  addLogEntry("🧼 Alle Projektionen wurden entfernt");
}

spellButtons.addEventListener("click", (event) => {
  const button = event.target.closest("[data-spell]");
  if (!button) return;
  castSpell(button.dataset.spell);
});

removeLastButton.addEventListener("click", removeLastElement);
clearAllButton.addEventListener("click", clearField);

toggleGlowButton.addEventListener("click", () => {
  creationField.classList.toggle("glow");
  const state = creationField.classList.contains("glow") ? "aktiv" : "aus";
  addLogEntry(`💡 Glow-Runen sind jetzt ${state}`);
});

spellLog.addEventListener("click", (event) => {
  if (!event.target.classList.contains("spell-log__entry")) return;
  spellLog.querySelectorAll(".spell-log__entry").forEach((entry) => entry.classList.remove("active"));
  event.target.classList.add("active");
});
