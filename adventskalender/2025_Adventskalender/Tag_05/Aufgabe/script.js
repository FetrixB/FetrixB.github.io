const blueprintMessages = {
  foundation: {
    title: "Header-Dach stabilisieren",
    description: "Nutze <header>, damit Logo und Navigation zusammenbleiben.",
    code: "<header class='content-shell'>...</header>",
  },
  flow: {
    title: "Main-Fluss lenken",
    description: "Der <main>-Block bekommt mehrere <section>-Räume.",
    code: "<main>...</main>",
  },
  signal: {
    title: "Footer-Signal senden",
    description: "Im <footer> landen Kontakt und Credits.",
    code: "<footer>...</footer>",
  },
};

function initBlueprintLab() {
  const buttons = document.querySelectorAll("[data-blueprint]");
  const output = document.querySelector(".blueprint-output");
  const heading = output?.querySelector("h3");
  const paragraph = output?.querySelector("p");
  const codeBlock = output?.querySelector("pre code");

  const updateOutput = (key) => {
    const data = blueprintMessages[key];
    if (!data || !heading || !paragraph || !codeBlock) return;

    // TODO 3: Übernimm hier Titel, Beschreibung und Code in die Ausgabe und triggere einen kurzen Flash-Effekt.
  };

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      buttons.forEach((btn) => {
        btn.classList.remove("is-active");
        btn.setAttribute("aria-pressed", "false");
      });

      button.classList.add("is-active");
      button.setAttribute("aria-pressed", "true");

      updateOutput(button.dataset.blueprint);
    });
  });

  updateOutput("foundation");
}

function initTimeline() {
  const timelineSteps = document.querySelectorAll(".timeline-step");
  const rebuildButton = document.getElementById("rebuildButton");
  const statusIndicator = document.querySelector(".status-indicator");

  const playTimeline = () => {
    timelineSteps.forEach((step, index) => {
      setTimeout(() => {
        step.classList.add("is-complete");
        const label = step.querySelector("span");
        if (label) {
          label.textContent = "Fertig!";
        }
      }, index * 350);
    });
  };

  rebuildButton?.addEventListener("click", () => {
    rebuildButton.disabled = true;
    rebuildButton.textContent = "Wärme läuft...";

    statusIndicator?.classList.add("is-visible");
    playTimeline();

    setTimeout(() => {
      rebuildButton.disabled = false;
      rebuildButton.textContent = "Schneesturm stoppen";
    }, 2600);
  });

  statusIndicator?.classList.add("is-visible");
}

window.addEventListener("DOMContentLoaded", () => {
  initBlueprintLab();
  initTimeline();
});
