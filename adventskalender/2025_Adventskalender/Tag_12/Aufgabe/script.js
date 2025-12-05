const root = document.documentElement;
const blurSlider = document.getElementById("blurRange");
const blurValue = document.getElementById("blurValue");
const glowToggle = document.getElementById("glowToggle");
const transparencyBar = document.getElementById("transparencyBar");
const contrastBadge = document.getElementById("contrastBadge");
const themeButtons = document.querySelectorAll("[data-theme]");

const themes = {
  aurora: {
    hue: 185,
    glow: "185 92% 72%",
    skyTop: "#030611",
    skyBottom: "#051729",
    focus: "rgba(108, 253, 255, 0.22)",
    accents: ["#5df1ff", "#fee3a8"],
  },
  moonstone: {
    hue: 215,
    glow: "215 94% 76%",
    skyTop: "#050d19",
    skyBottom: "#0a1f3a",
    focus: "rgba(148, 196, 255, 0.22)",
    accents: ["#94c4ff", "#e1f0ff"],
  },
  ember: {
    hue: 15,
    glow: "15 96% 64%",
    skyTop: "#120306",
    skyBottom: "#250a1c",
    focus: "rgba(255, 140, 102, 0.24)",
    accents: ["#ff8c66", "#ffd6a0"],
  },
};

const clamp = (value, min, max) => Math.min(Math.max(value, min), max);

const updateBlur = (value) => {
  // TODO 3: Nutze den Slider-Wert, um --frost-blur zu setzen und sowohl den Text (#blurValue) als auch die Anzeige-Leiste + Kontrast-Badge zu aktualisieren.
};

const toggleGlow = () => {
  const isActive = glowToggle.getAttribute("aria-pressed") === "true";
  const nextState = !isActive;
  glowToggle.setAttribute("aria-pressed", String(nextState));
  glowToggle.textContent = nextState ? "Glow aktiv ✨" : "Glow deaktiviert";
  document.documentElement.classList.toggle("glow-muted", !nextState);
};

const applyTheme = (themeKey) => {
  const data = themes[themeKey];
  if (!data) return;
  root.style.setProperty("--panel-hue", data.hue);
  root.style.setProperty(
    "--glow-strength",
    document.documentElement.classList.contains("glow-muted") ? "0.12" : "0.55"
  );
  root.style.setProperty("--sky-top", data.skyTop);
  root.style.setProperty("--sky-bottom", data.skyBottom);
  root.style.setProperty("--aurora-focus", data.focus);
  root.style.setProperty("--accent-1", data.accents[0]);
  root.style.setProperty("--accent-2", data.accents[1]);
  themeButtons.forEach((button) => {
    const isCurrent = button.dataset.theme === themeKey;
    button.classList.toggle("is-active", isCurrent);
    button.setAttribute("aria-pressed", String(isCurrent));
  });
};

blurSlider?.addEventListener("input", (event) => {
  updateBlur(Number(event.target.value));
});

glowToggle?.addEventListener("click", () => {
  toggleGlow();
  const activeTheme = document.querySelector("[data-theme].is-active");
  if (activeTheme) {
    applyTheme(activeTheme.dataset.theme);
  }
});

themeButtons.forEach((button) => {
  button.addEventListener("click", () => {
    applyTheme(button.dataset.theme);
  });
});

// Initial paint
updateBlur(Number(blurSlider?.value || 26));
applyTheme("aurora");
