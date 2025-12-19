#!/usr/bin/env python3
"""Erstellt das Lesson.ipynb Notebook für Tag 14."""

from pathlib import Path

import nbformat as nbf


def build_notebook():
    nb = nbf.v4.new_notebook()

    story_md = """# 🎄 Tag 14 – Die GSAP-Rune erwacht

Felix, du findest mitten in einer Minecraft-Höhle eine schwebende Rune. Sie reagiert auf jede
Bewegung deiner Hand und will mit einer **GSAP-Timeline** zum Leben erweckt werden. Stell dir vor,
jedes Licht ist ein Redstone-Repeater – du bestimmst die Reihenfolge, das Tempo und sogar die
Extras wie ScrollTrigger. Heute baust du eine komplette Choreografie, damit die Rune leuchtet,
dreht und Partikel einsaugt wie ein Film-Intro.
"""

    learning_md = """## 📚 Was du heute lernst

- **GSAP Tweens & Timelines:** Wie `gsap.timeline()` in `Loesung/script.js` vier Animationsphasen
  verbindet, statt jede Bewegung einzeln zu verzögern.
- **Sequencing & Callbacks:** Die HUD-Elemente in `Loesung/index.html` werden über
  `timeline.call()` und `data-*` Attribute aktualisiert.
- **Plugins & ScrollTrigger:** Mit `ScrollTrigger` aus derselben JS-Datei blendest du Info-Karten
  erst ein, wenn Felix wirklich dort hinscrollt.
"""

    timeline_md = """### 🎬 Timelines statt Delay-Chaos verstehen

Im Code der Lösung steht:

```javascript
const runeTimeline = gsap.timeline({
  defaults: { duration: 1.1, ease: 'sine.inOut' },
  repeat: -1,
  repeatDelay: 0.4
});
```

- **Tweens stapeln:** Jeder `.to()` oder `.fromTo()` Block ist ein eigener Abschnitt.
- **Labels per `call()`:** Vor jeder Phase ruft die Timeline `updatePhase()` auf und setzt den Text in
  `data-phase` aus dem HUD.
- **Warum das hilft:** Wenn du später eine neue Bewegung einfügst, verschiebst du nur einen Block,
  statt 5 Delays neu zu rechnen – genau wie beim Umbauen einer Redstone-Uhr.
"""

    hud_md = """### 🛰️ HUD & Styling verbinden Theorie mit Praxis

In `Loesung/style.css` findest du die Panels rund um den Stage-Bereich. Besonders wichtig:

```css
/* Bühne für alle GSAP-gesteuerten Layer */
.rune-stage {
  border-radius: 24px;
  background: radial-gradient(circle at 20% 20%, rgba(248, 200, 111, 0.4), rgba(3, 9, 28, 0.95));
}
```

- **Glassmorphism:** Durch halbtransparente Hintergründe fühlt sich das HUD wie ein
  Kontrollpult an.
- **Datenbindung:** Elemente wie `<div class="progress-fill" data-progress-fill>` werden in JS
  angesprochen, um die Timeline sichtbar zu machen.
- **Aufgabe:** In `Aufgabe/style.css` fehlt absichtlich der aktive Zustand – du holst ihn gleich zurück.
"""

    plugin_md = """### ⚡ ScrollTrigger & Bonus Tweens

Der letzte Block in `Loesung/script.js` sammelt alle `.scroll-card` Elemente:

```javascript
gsap.utils.toArray('[data-scroll-card]').forEach((card, index) => {
  gsap.from(card, {
    opacity: 0,
    y: 60,
    duration: 0.8,
    ease: 'power3.out',
    delay: index * 0.04,
    scrollTrigger: {
      trigger: card,
      start: 'top 80%'
    }
  });
});
```

- **ScrollTrigger** ersetzt starre Delays und startet Animationen erst, wenn der Spieler den Bereich
  sieht.
- **Stagger** (`delay: index * 0.04`) sorgt für eine Welle aus Karten.
- **Mission:** In der Aufgabe musst du diesen Abschnitt wieder einsetzen, damit GSAP sein Plugin auch
  zeigt.
"""

    demo_intro = """## 🧪 Verstehen & Ausprobieren

Teste im Notebook, wie eine Mini-Rune mit Tweens reagiert. Drücke den Button, um die Timeline
umzuschalten – genau wie der Boost-Button im Projekt.
"""

    demo_code = """from IPython.core.display import HTML
HTML(\"\"\"
<div class=\"nb-demo\">
  <style>
    .nb-demo {
      font-family: 'Orbitron', sans-serif;
      color: #e2e8f0;
    }
    .demo-panel {
      background: linear-gradient(160deg, #0f172a, #134e4a);
      border-radius: 20px;
      padding: 24px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 20px 35px rgba(2, 6, 23, 0.6);
    }
    .demo-rune {
      width: 140px;
      height: 140px;
      border-radius: 50%;
      border: 3px solid rgba(248, 200, 111, 0.7);
      display: grid;
      place-items: center;
      margin: 0 auto;
      position: relative;
    }
    .demo-rune::before {
      content: '';
      position: absolute;
      inset: 18px;
      border-radius: 16px;
      border: 2px solid rgba(96, 165, 250, 0.5);
    }
    .demo-glyph {
      font-size: 1.8rem;
      letter-spacing: 0.3em;
    }
    .demo-progress {
      margin-top: 18px;
      height: 6px;
      width: 100%;
      background: rgba(148, 163, 184, 0.3);
      border-radius: 999px;
      overflow: hidden;
    }
    .demo-progress-fill {
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, #60a5fa, #59f6b7);
      transform-origin: left center;
      transform: scaleX(0);
    }
    .demo-actions {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 20px;
      gap: 12px;
    }
    .demo-actions button {
      flex: 1;
      border: none;
      border-radius: 999px;
      padding: 10px 14px;
      font-weight: 600;
      cursor: pointer;
      background: linear-gradient(120deg, #59f6b7, #60a5fa);
      color: #0f172a;
    }
    .demo-status {
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.3em;
    }
  </style>
  <div class=\"demo-panel\">
    <div class=\"demo-rune\" id=\"demoRune\">
      <span class=\"demo-glyph\">GS</span>
    </div>
    <div class=\"demo-progress\">
      <div class=\"demo-progress-fill\" id=\"demoProgress\"></div>
    </div>
    <div class=\"demo-actions\">
      <button id=\"demoToggle\">Pause</button>
      <span class=\"demo-status\" id=\"demoStatus\">Phase 1</span>
    </div>
  </div>
  <script src=\"https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js\"></script>
  <script>
    const rune = document.getElementById('demoRune');
    const progressFill = document.getElementById('demoProgress');
    const statusLabel = document.getElementById('demoStatus');
    const toggleBtn = document.getElementById('demoToggle');

    const miniTimeline = gsap.timeline({
      repeat: -1,
      repeatDelay: 0.3,
      defaults: { duration: 0.9, ease: 'sine.inOut' },
      onUpdate: function() {
        progressFill.style.transform = `scaleX(${this.progress().toFixed(2)})`;
      }
    })
      .call(() => statusLabel.textContent = 'Phase 1')
      .to(rune, { scale: 1.1 })
      .call(() => statusLabel.textContent = 'Phase 2')
      .to(rune, { rotation: '+=180', borderColor: 'rgba(248,200,111,0.9)' })
      .call(() => statusLabel.textContent = 'Phase 3')
      .to(rune, { scale: 0.95, rotation: '+=180' });

    toggleBtn.addEventListener('click', () => {
      if (miniTimeline.paused()) {
        miniTimeline.resume();
        toggleBtn.textContent = 'Pause';
      } else {
        miniTimeline.pause();
        toggleBtn.textContent = 'Abspielen';
      }
    });
  </script>
</div>
\"\"\")
"""

    task_md = """# 🚀 Deine Aufgabe – Rune perfektionieren

Im Ordner `Tag_14/Aufgabe/` wartet eine fast fertige Bühne. Drei TODOs fehlen, damit die Rune so
beeindruckend wie die Lösung aussieht.
"""

    todo1_md = """### 📝 TODO 1 – HTML: Fortschrittsbalken wieder einsetzen
- **Datei:** `Tag_14/Aufgabe/index.html`
- **Ort:** Im Block `<div class="hud-progress">` rund um Zeile 90.
- **Aufgabe:** Ersetze den Kommentar durch die beiden DIVs `progress-track` und
  `progress-fill` (inklusive `data-progress-fill`). Ohne sie kann das Skript keinen Fortschritt
  anzeigen.
- **Kontrolle:** Die Timeline sollte die Leiste von 0 bis 100% füllen.
"""

    todo2_md = """### 🎨 TODO 2 – CSS: Aktiven Timeline-Step hervorheben
- **Datei:** `Tag_14/Aufgabe/style.css`
- **Ort:** Bereich der `.phase-list` am Ende der Datei.
- **Aufgabe:** Füge wieder einen Stil für `.phase-list li.is-active` ein – grüner Rahmen und helle
  Fläche wie in der Lösung.
- **Warum:** `updatePhase()` setzt diese Klasse per JS. Ohne Stil merkst du nicht, welcher Abschnitt
  gerade läuft.
"""

    todo3_md = """### ⚡ TODO 3 – JavaScript: ScrollTrigger anwerfen
- **Datei:** `Tag_14/Aufgabe/script.js`
- **Ort:** Direkt über dem abschließenden `})();`.
- **Aufgabe:** Iteriere über alle `[data-scroll-card]` Elemente, animiere sie mit `gsap.from()` und
  verbinde alles mit `ScrollTrigger`, sodass die Karten beim Scrollen auftauchen.
- **Tipp:** Nutze denselben Aufbau wie in `Loesung/script.js` – so lernst du, Plugins modular
  einzubinden.
"""

    success_md = """## 🏆 Erfolgskontrolle
- HUD zeigt Fortschritt ohne Fehlermeldungen in der Konsole.
- Aktiver Schritt wird grün markiert, wenn sich `data-phase` ändert.
- Info-Karten blenden smooth ein, sobald du herunterscrollst.
"""

    test_md = """## 🌐 Test & Vergleich
- **Aufgabe testen:** `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_14/Aufgabe/`
- **Musterlösung ansehen:** `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_14/Loesung/`
- Prüfe im DevTools-Tab "Network", dass GSAP und ScrollTrigger sauber geladen werden.
"""

    outro_md = """## 🌟 Erfolg & Möglichkeiten
Du beherrschst jetzt GSAP Timelines, Live-Kontrollen und ScrollTrigger. Als nächstes könntest du:
- Ein zweites Objekt (z. B. schwebende Kristalle) zur Timeline hinzufügen.
- Mit `timeScale()` experimentieren und UI-Slider für Besucher einbauen.
- ScrollTrigger erweitern, sodass die Rune verschiedene Kapitel bei jedem Abschnitt zeigt.
"""

    nb.cells = [
        nbf.v4.new_markdown_cell(story_md),
        nbf.v4.new_markdown_cell(learning_md),
        nbf.v4.new_markdown_cell(timeline_md),
        nbf.v4.new_markdown_cell(hud_md),
        nbf.v4.new_markdown_cell(plugin_md),
        nbf.v4.new_markdown_cell(demo_intro),
        nbf.v4.new_code_cell(demo_code),
        nbf.v4.new_markdown_cell(task_md),
        nbf.v4.new_markdown_cell(todo1_md),
        nbf.v4.new_markdown_cell(todo2_md),
        nbf.v4.new_markdown_cell(todo3_md),
        nbf.v4.new_markdown_cell(success_md),
        nbf.v4.new_markdown_cell(test_md),
        nbf.v4.new_markdown_cell(outro_md),
    ]

    nbf.validate(nb)
    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    output_path = Path(__file__).resolve().parent / filename
    with open(output_path, "w", encoding="utf-8") as file:
        nbf.write(nb, file)
    return output_path


def main():
    notebook = build_notebook()
    path = save_notebook(notebook)
    print(f"✅ Lesson erstellt: {path}")


if __name__ == "__main__":
    main()
