#!/usr/bin/env python3
"""
Erstellt das Lesson.ipynb Notebook für Tag 13.
Das Notebook folgt der Struktur aus agenten_kontext.md und füllt alle Inhalte
für den Pixel-Eisbär-Tag mit Story, Theorie, Aufgaben und einer HTML Demo.
"""

from pathlib import Path
import nbformat as nbf


def build_notebook():
    nb = nbf.v4.new_notebook()

    story = """# 🎄 Tag 13 – Der flauschige Pixel-Eisbär sprintet los!

Felix, heute rennt ein riesiger, flauschiger Eisbär durch das Weihnachtsdorf. Die Bewohner
bitten dich, ihn als Pixel-Kunst nachzubauen **und** ihm mit Animationen ein echtes Leben einzuhauchen.
Deine Bühne ist eine frostige Rennstrecke – genau wie eine frisch gebaute Schiene in Minecraft,
auf der ein Minecart ohne Ruckler rollen muss. Wir kombinieren heute CSS-Keyframes für den
Laufzyklus, Anime.js für Profi-Bewegungen und Performance-Hacks, damit nichts ruckelt.
"""

    learning_goals = """## 📚 Was du heute lernst

- **CSS Keyframes mit `steps()`**: einzelne Frames springen lassen wie bei einer Sprite-Animation.
- **Anime.js Timelines**: mehrere Bewegungen choreografieren und Callbacks nutzen.
- **Performance-Booster**: `transform`, `will-change` und `requestAnimationFrame`, damit der Bär nie laggt.
"""

    css_section = """### 🧱 Keyframes & Pixel-Sprites verstehen

In `Loesung/style.css` steuern Keyframes die Mini-Sprünge des Bären:

```css
.pixel-bear__sprite {
  position: relative;
  width: 100%;
  height: 100%;
  animation: sprite-bob 0.6s steps(2) infinite;
  animation-fill-mode: both;
}

@keyframes sprite-bob {
  0% { transform: translateY(calc(var(--pixel-size) * -0.2)); }
  100% { transform: translateY(calc(var(--pixel-size) * 0.15)); }
}
```

`steps(2)` lässt das Sprite nicht weich gleiten, sondern zwischen zwei Positionen springen –
wie wenn du in Minecraft schnell zwischen zwei Rüstungs-Skins wechselst. `animation-fill-mode: both`
hält die aktuelle Pose, damit der Lauf realistisch startet und landet.
"""

    anime_section = """### 🎬 Anime.js Timeline mit Easing & Callbacks

Die Datei `Loesung/script.js` zeigt eine Timeline, die mehrere Bewegungen verbindet:

```javascript
const timeline = anime.timeline({
  loop: true,
  duration: 5200,
  easing: 'easeInOutSine',
  begin: () => status.textContent = 'Der Pixel-Bär tänzelt an die Startlinie…',
  update: (anim) => {
    const progress = anim.progress / 100;
    progressFill.style.transform = `scaleX(${Math.min(progress, 1)})`;
  }
});

timeline
  .add({ targets: bear, translateX: ['-10%', '78%'], rotate: [{ value: -2 }, { value: 2 }] }, 0)
  .add({ targets: shadow, scaleX: [0.8, 1.5], opacity: [0.35, 0.7, 0.4] }, 0);
```

- **Timeline**: mehrere `.add()` Blöcke teilen sich denselben Takt.
- **Easing**: `easeInOutSine` macht das Loslaufen und Abbremsen weich.
- **Callbacks**: `begin`, `update`, `loopComplete` kümmern sich um Texte und Fortschrittsbalken.
"""

    performance_section = """### ⚡ Performance-Optimierung wie ein Redstone-Ingenieur

Ein schneller Eisbär braucht clevere Optimierungen:

```css
.pixel-bear { will-change: transform; }
```

```javascript
const monitorFrames = () => {
  const { fps } = stageElements;
  if (!fps) return;

  let lastTimestamp = performance.now();
  const update = (timestamp) => {
    const delta = timestamp - lastTimestamp || 16;
    lastTimestamp = timestamp;
    const currentFps = Math.max(1, Math.min(120, Math.round(1000 / delta)));
    fps.textContent = `${currentFps} fps`;
    requestAnimationFrame(update);
  };

  requestAnimationFrame(update);
};
```

- `transform` statt `left/top` verhindert, dass der Browser das Layout neu berechnet.
- `will-change` bittet die GPU höflich um Vorbereitung.
- `requestAnimationFrame` hängt den FPS-Monitor an den echten Bildschirm-Takt.
"""

    demo_intro = """## 🧪 Verstehen & Ausprobieren

Teste hier im Notebook, wie `steps()` und Anime.js zusammenspielen. Die Mini-Demo zeigt
zwei Pixelblöcke, die wie Fußstapfen alternieren. Nutze den Button, um eine Timeline per Callback
schneller zu machen – genau wie in `script.js`.
"""

    demo_code = """from IPython.core.display import HTML
HTML(\"\"\"
<div class=\"demo-wrapper\">
  <style>
    .demo-wrapper {
      font-family: 'Orbitron', sans-serif;
      color: #0f172a;
    }
    .demo-stage {
      background: linear-gradient(135deg, #0f172a, #134e4a);
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 25px 40px rgba(2, 6, 23, 0.45);
      position: relative;
      overflow: hidden;
      min-height: 180px;
    }
    .demo-track {
      position: relative;
      width: 100%;
      height: 90px;
      background: rgba(15, 23, 42, 0.4);
      border-radius: 12px;
      border: 1px solid rgba(148, 163, 184, 0.4);
      margin-top: 16px;
    }
    .demo-track::before {
      content: '';
      position: absolute;
      inset: 0;
      background-image: repeating-linear-gradient(90deg, rgba(59, 130, 246, 0.3) 0 40px, transparent 40px 80px);
      animation: stripes 8s linear infinite;
      animation-fill-mode: both;
    }
    .pixel-runner {
      position: absolute;
      top: 16px;
      left: 16px;
      width: 120px;
      height: 60px;
      display: flex;
      justify-content: space-between;
    }
    .pixel-foot {
      width: 50px;
      height: 50px;
      background: #fefce8;
      border: 4px solid #f472b6;
      border-radius: 8px;
      animation: footSteps 0.6s steps(2) infinite;
      animation-fill-mode: both;
    }
    .pixel-foot:nth-child(2) {
      animation-delay: 0.3s;
    }
    @keyframes footSteps {
      0% { transform: translateY(-6px) skewX(-6deg); }
      100% { transform: translateY(6px) skewX(6deg); }
    }
    @keyframes stripes {
      0% { background-position: 0 0; }
      100% { background-position: 400px 0; }
    }
    .demo-hud {
      margin-top: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: #f8fafc;
    }
    .demo-hud button {
      border: none;
      background: linear-gradient(120deg, #22d3ee, #f472b6);
      color: #0f172a;
      padding: 10px 18px;
      border-radius: 999px;
      font-weight: 700;
      cursor: pointer;
    }
  </style>
  <div class=\"demo-stage\">
    <div class=\"demo-info\">Mini-Sprite mit steps(2) + Anime.js Timeline</div>
    <div class=\"demo-track\">
      <div class=\"pixel-runner\" id=\"demoRunner\">
        <div class=\"pixel-foot\"></div>
        <div class=\"pixel-foot\"></div>
      </div>
    </div>
    <div class=\"demo-hud\">
      <div id=\"demoStatus\">Tempo: 1x</div>
      <button id=\"demoBoost\">Turbo aktivieren</button>
    </div>
  </div>
  <script src=\"https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js\"></script>
  <script>
    const runner = document.getElementById('demoRunner');
    const statusLabel = document.getElementById('demoStatus');
    const boostBtn = document.getElementById('demoBoost');
    let turbo = false;

    const runnerTimeline = anime.timeline({
      targets: runner,
      loop: true,
      duration: 4000,
      easing: 'easeInOutSine'
    }).add({ translateX: [0, 260] }).add({ translateX: [260, 0] });

    boostBtn.addEventListener('click', () => {
      turbo = !turbo;
      runnerTimeline.playbackRate = turbo ? 1.5 : 1;
      boostBtn.textContent = turbo ? 'Turbo stoppen' : 'Turbo aktivieren';
      statusLabel.textContent = `Tempo: ${turbo ? '1.5x' : '1x'}`;
    });
  </script>
</div>
\"\"\")
"""

    task_intro = """# 🚀 Deine Aufgabe – Pixel-Bär wieder flott machen

In `Tag_13/Aufgabe/` wartet bereits eine fast fertige Bühne. Drei TODOs fehlen, damit der Lauf
so beeindruckend wird wie die Musterlösung. Arbeite sie der Reihe nach durch.
"""

    todo1 = """### 📝 TODO 1: HTML – Fortschrittsbalken ergänzen
- **Datei:** `Aufgabe/index.html`
- **Ort:** Im `<div class="runway">` Block rund um Zeile 70.
- **Mission:** Ersetze den Kommentar `<!-- TODO 1 ... -->` durch den `<div class="trail-meter">` mit dem inneren `<div class="trail-meter__fill" data-progress-fill>` so wie er in `Loesung/index.html` steht.
- **Warum:** Das Anime.js `update`-Callback versucht, den Balken zu skalieren. Ohne Element siehst du nicht, wie weit der Sprint gerade ist.
"""

    todo2 = """### 🎨 TODO 2: CSS – Sprite-Animation wieder aktivieren
- **Datei:** `Aufgabe/style.css`
- **Ort:** Selektor `.pixel-bear__sprite` (Zeile ~168).
- **Mission:** Ersetze den Kommentar durch die Zeile `animation: spriteBob 0.6s steps(2) infinite;`.
- **Warum:** `steps(2)` macht die Beine pixelig. Ohne diese Zeile schwebt der Bär zu glatt über die Bahn und du verpasst das Frame-by-Frame Gefühl.
"""

    todo3 = """### ⚡ TODO 3: JavaScript – Turbo-Callback vervollständigen
- **Datei:** `Aufgabe/script.js`
- **Ort:** Funktion `bindBoostButton`, innerhalb des `click`-Handlers.
- **Mission:** Nutze `timeline.playbackRate`, `classList.toggle`, Button-Text und Status-Ausgabe, um den Turbo an- und auszuschalten wie in `Loesung/script.js`.
- **Warum:** Hier lernst du, Anime.js Callbacks mit UI-Elementen zu verbinden. Das ist der Moment, wo Theorie zur Action wird.
"""

    success = """## 🏆 Erfolgskontrolle
Wenn alle TODOs erledigt sind, solltest du sehen:
- Einen leuchtenden Fortschrittsbalken, der synchron mit dem Lauf wächst.
- Treppenartige Schritte der Pixel-Pfoten dank `steps(2)`.
- Den Turbo-Button, der Text, Farbe und Laufgeschwindigkeit ändert.
- Status-Text, der auf Callbacks reagiert (Start, Loop, Turbo).
"""

    testing = """## 🌐 Testen & Vergleichen
- **Aufgabe öffnen:** `http://192.168.0.20:8000/2025_Adventskalender/Tag_13/Aufgabe/`
- **Musterlösung ansehen:** `http://192.168.0.20:8000/2025_Adventskalender/Tag_13/Loesung/`
- Nutze die Browser-Konsole, um zu sehen, dass keine Fehler auftauchen, wenn du den Turbo spamst.
"""

    outro = """## 🌟 Erfolg & Möglichkeiten
Glückwunsch! Du hast gelernt, wie man eine Sprite-Animation mit Keyframes aufbaut, wie Anime.js
Timeline-Events auslöst und wie Performance-Tricks Aussetzer verhindern.

Als nächstes könntest du:
- Mehr Frames zeichnen und `steps(4)` testen.
- Einen `anime.stagger()`-Effekt für mehrere Tiere ergänzen.
- Die FPS-Anzeige erweitern, indem du Durchschnittswerte speicherst.
"""

    nb.cells = [
        nbf.v4.new_markdown_cell(story),
        nbf.v4.new_markdown_cell(learning_goals),
        nbf.v4.new_markdown_cell(css_section),
        nbf.v4.new_markdown_cell(anime_section),
        nbf.v4.new_markdown_cell(performance_section),
        nbf.v4.new_markdown_cell(demo_intro),
        nbf.v4.new_code_cell(demo_code),
        nbf.v4.new_markdown_cell(task_intro),
        nbf.v4.new_markdown_cell(todo1),
        nbf.v4.new_markdown_cell(todo2),
        nbf.v4.new_markdown_cell(todo3),
        nbf.v4.new_markdown_cell(success),
        nbf.v4.new_markdown_cell(testing),
        nbf.v4.new_markdown_cell(outro),
    ]

    nbf.validate(nb)
    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    output_path = Path(__file__).resolve().parent / filename
    with open(output_path, "w", encoding="utf-8") as f:
        nbf.write(nb, f)
    return output_path


def main():
    notebook = build_notebook()
    path = save_notebook(notebook)
    print(f"✅ Lesson erstellt: {path}")


if __name__ == "__main__":
    main()
