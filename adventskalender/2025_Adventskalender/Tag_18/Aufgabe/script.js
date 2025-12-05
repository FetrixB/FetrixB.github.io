// Referenzen auf alle wichtigen Bereiche der Bühne
const icicleWall = document.getElementById("icicleWall");
const arrayInspector = document.getElementById("arrayInspector");
const melodyMeter = document.getElementById("melodyMeter");
const avgLength = document.getElementById("avgLength");
const lengthBadge = document.getElementById("lengthBadge");
const loopNarration = document.getElementById("loopNarration");
const sparkleGrid = document.getElementById("sparkleGrid");
const patternDigest = document.getElementById("patternDigest");
const filterToggle = document.getElementById("filterToggle");

// Kleine Tonleiter, damit jeder Zapfen eine eigene Farbe bekommt
const tonePalette = [
  { note: "C#", accent: "#f472b6" },
  { note: "D", accent: "#facc15" },
  { note: "E", accent: "#34d399" },
  { note: "F#", accent: "#60a5fa" },
  { note: "G", accent: "#a5b4fc" },
  { note: "A", accent: "#fca5a5" },
  { note: "B", accent: "#bef264" }
];

// Start-Aufstellung des Vorhangs – dient als Referenz für Resets
const baseIcicles = [
  { id: "Polar Echo", length: 220, chill: 8, shimmer: "#67e8f9" },
  { id: "Snow Lyra", length: 170, chill: 6, shimmer: "#bae6fd" },
  { id: "Crystal Bass", length: 140, chill: 4, shimmer: "#c084fc" },
  { id: "Aurora Ping", length: 190, chill: 7, shimmer: "#f472b6" },
  { id: "Frost Spark", length: 120, chill: 3, shimmer: "#facc15" },
  { id: "Moon Drop", length: 200, chill: 7, shimmer: "#bef264" },
  { id: "Shard Alto", length: 160, chill: 5, shimmer: "#93c5fd" },
  { id: "Echo Spike", length: 210, chill: 9, shimmer: "#d946ef" }
];

let icicleData = cloneBlueprint(baseIcicles);
let filterLongOnly = false;
const loopLog = [];

// Kopiert Daten, damit wir das Original nie direkt verändern
function cloneBlueprint(blueprint) {
  return blueprint.map((item) => ({ ...item }));
}

// Schreibt erklärende Log-Zeilen ins Loop-Journal
function logLoop(message) {
  if (!loopNarration) return; // Ohne Loop-Narrator soll es trotzdem laufen
  const timestamp = new Date().toLocaleTimeString("de-DE", { minute: "2-digit", second: "2-digit" });
  loopLog.push(`<p class="text-slate-200"><span class="text-sky-300">${timestamp}</span> · ${message}</p>`);
  if (loopLog.length > 6) loopLog.shift();
  loopNarration.innerHTML = loopLog.join("");
}

// Malt die sichtbaren Zapfen, optional mit Filter
function renderIcicles() {
  const activeData = filterLongOnly ? icicleData.filter((item) => item.length >= 180) : icicleData;
  icicleWall.innerHTML = "";

  for (let index = 0; index < activeData.length; index++) {
    const icicleInfo = activeData[index];
    const column = document.createElement("div");
    column.className = "icicle transition-all duration-500 ease-out hover:-translate-y-2";
    column.style.height = `${icicleInfo.length}px`;
    column.style.background = `linear-gradient(180deg, rgba(147, 197, 253, 0.9), ${icicleInfo.shimmer})`;

    const label = document.createElement("span");
    label.className = "tag";
    label.textContent = `${icicleInfo.length} cm`;

    const note = document.createElement("span");
    note.className = "note-dot";
    note.style.color = icicleInfo.shimmer;

    column.append(label, note);
    column.setAttribute("aria-label", `${icicleInfo.id} misst ${icicleInfo.length} Zentimeter`);
    icicleWall.appendChild(column);
  }

  logLoop(`For-Loop hat ${activeData.length} Zapfen nacheinander positioniert.`);
}

// Berechnet Durchschnittswerte und schreibt sie in die UI
function updateStats() {
  if (!icicleData.length) {
    avgLength.textContent = "0 cm";
    melodyMeter.style.width = "0%";
    arrayInspector.textContent = "Keine Daten – starte den Kristallregen!";
    return;
  }

  let total = 0;
  for (const icicle of icicleData) {
    total += icicle.length;
  }
  const average = Math.round(total / icicleData.length);
  avgLength.textContent = `${average} cm`;
  melodyMeter.style.width = `${Math.min(100, average)}%`;
  lengthBadge.textContent = icicleData.length;

  const lines = [];
  for (const icicle of icicleData) {
    lines.push(`• ${icicle.id} → ${icicle.length} cm (Kühle-Stufe ${icicle.chill})`);
  }
  arrayInspector.innerHTML = `<p class="text-emerald-300 font-semibold">Array-Länge: ${icicleData.length}</p><p class="text-slate-300 whitespace-pre-line">${lines.join("\n")}</p>`;
}

// Kleine Infokarten mit besonderen Messwerten
function updatePatternDigest() {
  if (!icicleData.length) {
    patternDigest.innerHTML = "<p>Keine Kristalle aktiv.</p>";
    return;
  }

  const longest = Math.max(...icicleData.map((item) => item.length));
  const shortest = Math.min(...icicleData.map((item) => item.length));
  const frosty = icicleData.filter((item) => item.chill >= 7).length;
  const warm = icicleData.filter((item) => item.chill <= 4).length;

  const metrics = [
    { label: "Höchster Zapfen", value: `${longest} cm` },
    { label: "Kürzester Zapfen", value: `${shortest} cm` },
    { label: "Super frostig", value: `${frosty}×` },
    { label: "Mild und weich", value: `${warm}×` }
  ];

  patternDigest.innerHTML = metrics
    .map(
      (metric) => `
        <div class="rounded-xl bg-white/5 border border-white/10 p-3">
          <p class="text-xs text-slate-400">${metric.label}</p>
          <p class="text-lg text-cyan-100 font-semibold">${metric.value}</p>
        </div>`
    )
    .join("");
}

// Erzeugt neue Zapfen mithilfe einer Kombination aus For- und For-of-Loops
function addCluster() {
  const clusterSize = Math.floor(Math.random() * 3) + 2; // 2-4 neue Kristalle
  const newCluster = [];

  for (let i = 0; i < clusterSize; i++) {
    const randomTone = tonePalette[Math.floor(Math.random() * tonePalette.length)];
    newCluster.push({
      id: `${randomTone.note}-Pulse ${Date.now().toString().slice(-3)}${i}`,
      length: Math.floor(Math.random() * 120) + 100,
      chill: Math.floor(Math.random() * 6) + 3,
      shimmer: randomTone.accent
    });
  }

  for (const crystal of newCluster) {
    icicleData.push(crystal);
  }

  logLoop(`For-of-Loop pushte ${newCluster.length} neue Zapfen ins Array.`);
  renderAll();
}

// Entfernt den letzten Eintrag – perfekt zum Zeigen von pop()
function removeLastIcicle() {
  if (!icicleData.length) return;
  const removed = icicleData.pop();
  logLoop(`Pop entfernte "${removed.id}" vom Ende – Array schrumpft.`);
  renderAll();
}

// Sortiert die Sammlung aufsteigend
function sortIcicles() {
  icicleData.sort((a, b) => a.length - b.length);
  logLoop("Sort() ordnete alles von kurz zu lang.");
  renderAll();
}

// Fisher-Yates sorgt für echte Zufallsreihenfolgen
function shuffleIcicles() {
  for (let i = icicleData.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [icicleData[i], icicleData[j]] = [icicleData[j], icicleData[i]];
  }
  logLoop("Fisher-Yates-Loop mischte die Melodie wie Schneewind.");
  renderAll();
}

// Aktiviert oder deaktiviert eine Filteransicht
function toggleFilter() {
  /* TODO 3: Lass den Button wirklich filtern! Schalte mit filterLongOnly zwischen beiden Zuständen
     um, aktualisiere die Button-Beschriftung und rufe danach renderAll() auf. Inspiriere dich gerne
     an der Lösung. */
}

// Stellt den Ausgangszustand wieder her
function resetWall() {
  icicleData = cloneBlueprint(baseIcicles);
  filterLongOnly = false;
  filterToggle.textContent = "Filter: Nur extra lange anzeigen";
  logLoop("Reset stellte das Urmuster mit Spread-Kopie wieder her.");
  renderAll();
}

// Verschachtelter Loop für funkelnde Deko im Hintergrund
function createSparkleGrid() {
  const dots = [];
  for (let row = 0; row < 8; row++) {
    for (let col = 0; col < 16; col++) {
      const delay = (row + col) * 0.12;
      dots.push(
        `<span class="sparkle-dot" style="position:absolute; top:${row * 12}%; left:${col * 6}%; animation-delay:${delay}s;"></span>`
      );
    }
  }
  sparkleGrid.innerHTML += dots.join("");
  logLoop(`Verschachtelter Loop platzierte ${dots.length} Lichtpunkte als Windpartikel.`);
}

function renderAll() {
  renderIcicles();
  updateStats();
  updatePatternDigest();
}

// Verkabelt alle Buttons mit den passenden Funktionen
function attachEventListeners() {
  document.getElementById("addCluster").addEventListener("click", addCluster);
  document.getElementById("removeLast").addEventListener("click", removeLastIcicle);
  document.getElementById("sortIcicles").addEventListener("click", sortIcicles);
  document.getElementById("shuffleIcicles").addEventListener("click", shuffleIcicles);
  filterToggle.addEventListener("click", toggleFilter);
  document.getElementById("resetWall").addEventListener("click", resetWall);
}

// Startsequenz für den gesamten Tag
function initCurtain() {
  createSparkleGrid();
  attachEventListeners();
  renderAll();
}

document.addEventListener("DOMContentLoaded", initCurtain);
