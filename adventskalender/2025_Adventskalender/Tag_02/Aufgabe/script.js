const portalButton = document.getElementById("portalButton");
const portalEnergy = document.getElementById("portalEnergy");
const portalStatus = document.getElementById("portalStatus");
const portalSection = document.querySelector(".portal-section");
const crystals = document.querySelectorAll(".portal-crystal");

let portalActive = false;
let sparkleIntervalId = null;

/**
 * Aktualisiert die Statusanzeige und sorgt für ermutigenden Text.
 * @param {string} message - Neue Meldung für Felix.
 */
function updateStatus(message) {
  portalStatus.textContent = message;
}

/**
 * Erstellt ein glitzerndes Partikel und lässt es nach oben schweben.
 */
function createSparkle() {
  const sparkle = document.createElement("span");
  sparkle.className = "sparkle";
  sparkle.style.left = `${Math.random() * 90 + 5}%`;
  sparkle.style.bottom = "20px";
  sparkle.style.animationDuration = `${Math.random() * 1 + 1}s`;
  portalSection.appendChild(sparkle);

  setTimeout(() => {
    sparkle.remove();
  }, 2000);
}

function startSparkles() {
  createSparkle();
  sparkleIntervalId = setInterval(createSparkle, 450);
}

function stopSparkles() {
  clearInterval(sparkleIntervalId);
  sparkleIntervalId = null;
}

function togglePortal() {
  portalActive = !portalActive;
  portalEnergy.classList.toggle("portal-energy-active", portalActive);

  if (portalActive) {
    updateStatus("Portal aktiv! Die Energie pulsiert gleichmäßig.");
    portalButton.textContent = "Portal beruhigen 💤";
    portalButton.setAttribute("aria-pressed", "true");
    startSparkles();
  } else {
    updateStatus("Das Portal ruht wieder. Klicke zum erneuten Aktivieren.");
    portalButton.textContent = "Portal starten ✨";
    portalButton.setAttribute("aria-pressed", "false");
    stopSparkles();
  }
}

portalButton.addEventListener("click", togglePortal);

crystals.forEach((crystal, index) => {
  crystal.style.animationDelay = `${index * 0.08}s`;
  crystal.addEventListener("mouseenter", () => {
    const message = crystal.dataset.message || "Kristall meldet stabile Energie";
    updateStatus(message);
  });
});

updateStatus("Das Portal schläft noch. Tappe auf einen Kristall für Infos!");
