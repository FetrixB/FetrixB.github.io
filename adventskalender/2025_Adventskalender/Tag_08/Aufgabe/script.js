const root = document.documentElement;
const windSlider = document.getElementById("wind-slider");
const statusText = document.getElementById("status-text");
const addWoodButton = document.getElementById("add-wood");
const toggleSnowButton = document.getElementById("toggle-snow");
const campfireScene = document.querySelector(".campfire-scene");
const snowLayer = document.querySelector(".snow-layer");

let heatLevel = 2;
const heatMessages = {
  1: "Nur kleine Flämmchen: Noch ist Zeit, Holz nachzulegen.",
  2: "Perfektes Kochfeuer – alle Marshmallows werden golden!",
  3: "Mega-Boost! Die Flammen ändern sogar ihre Farbe etwas."
};

function updateHeatLevel() {
  if (!campfireScene) return;
  // Speichert die Intensität als Data-Attribut, damit CSS sofort reagieren kann.
  campfireScene.dataset.heat = String(heatLevel);
  if (statusText) {
    statusText.textContent = heatMessages[heatLevel];
  }
}

if (windSlider) {
  windSlider.addEventListener("input", (event) => {
    // TODO 3: Nutze den Sliderwert, um die CSS-Variable "--wind-angle" zu setzen
    // und beschreibe im Status-Text, ob der Wind nach links oder rechts pustet.
  });
}

if (addWoodButton) {
  addWoodButton.addEventListener("click", () => {
    heatLevel = heatLevel === 3 ? 1 : heatLevel + 1;
    updateHeatLevel();
    addWoodButton.classList.add("btn-pulse");
    setTimeout(() => addWoodButton.classList.remove("btn-pulse"), 350);
  });
}

if (toggleSnowButton && snowLayer) {
  toggleSnowButton.addEventListener("click", () => {
    const paused = snowLayer.classList.toggle("paused");
    toggleSnowButton.textContent = paused ? "❄️ Schnee starten" : "❄️ Schnee pausieren";
    // Schnellere Animation vermittelt stärkeren Wind, langsamere wirkt ruhig.
    root.style.setProperty("--snow-speed", paused ? "999s" : "26s");
    if (statusText) {
      statusText.textContent = paused
        ? "Der Himmel cleart auf – der Schnee ruht kurz."
        : "Schneeflocken glitzern wieder über dem Feuer.";
    }
  });
}

updateHeatLevel();
