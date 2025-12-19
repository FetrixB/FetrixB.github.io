#!/usr/bin/env python3
"""Generiert die Lesson.ipynb für Tag 21."""

from pathlib import Path
import sys
import nbformat as nbf

BASE_DIR = Path(__file__).parent


def build_cells():
    cells = []

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🎄 Tag 21 – Schneeball-Physik in Felixdorf

Die Kinder liefern sich eine chaotische Schneeballschlacht und schreien durcheinander: *"Wer hat wen getroffen?!"* Deine Mission: Baue eine Kontrollzentrale, die Würfe zählt, Treffer sichtbar macht und mit **Matter.js** echte Physik simuliert. Heute wirst du zum Game-Designer und Physik-Meister!"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🧭 Was du heute meisterst
- **Game Loop & `requestAnimationFrame`** als Herzschlag deines Mini-Games
- **Delta-Time** verstehen, damit Bewegungen auf jedem PC gleich schnell sind
- **Kollisionserkennung** nutzen, um Punkte nur bei echten Treffern zu vergeben
- **Matter.js Bodies & Forces** einsetzen, damit Schneebälle springen, rollen und abprallen"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## ⚙️ Game Loop + Delta-Time wie eine Redstone-Uhr
Stell dir vor, dein Spiel ist eine automatische Redstone-Farm: Sie läuft nur sauber, wenn die Ticks gleichmäßig passieren. `requestAnimationFrame` ruft deine Funktion ca. 60 Mal pro Sekunde auf. Mit *Delta-Time* misst du, wie viel Zeit wirklich zwischen zwei Aufrufen lag. So rechnen wir Bewegungen unabhängig von der echten FPS.

```javascript
let lastTimestamp = 0;
function gameLoop(timestamp) {
  if (!lastTimestamp) lastTimestamp = timestamp;
  const delta = (timestamp - lastTimestamp) / 1000;
  lastTimestamp = timestamp;

  scoreboard.clock += delta;
  windValue.textContent = `${(scoreboard.wind).toFixed(1)} km/h`;
  requestAnimationFrame(gameLoop);
}

requestAnimationFrame(gameLoop);
```

📌 *So nutzt es die Lösung:* In `Tag_21/Loesung/script.js` aktualisiert der Loop Uhrzeit, Windstärke, Combo-Balken und entfernt alte Schneebälle. Ohne Delta-Time würde ein langsamer Laptop den gesamten Flug verlangsamen."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🎯 Kollisionen zählen wie Treffer in Minecraft PvP
Jeder Schneeball ist ein Matter-Body. Sobald er ein Ziel berührt, feuert das Event `collisionStart`. Wir prüfen, ob eines der beiden Objekte das Label `target-...` trägt und ob der Schneeball dieses Ziel schon belohnt hat.

```javascript
Events.on(engine, "collisionStart", (event) => {
  for (const pair of event.pairs) {
    const target = [pair.bodyA, pair.bodyB].find((b) => b.plugin?.type === "target");
    const snowball = [pair.bodyA, pair.bodyB].find((b) => b.plugin?.type === "snowball");
    if (!target || !snowball) continue;

    snowball.plugin.scoredTargets.add(target.plugin.id);
    scoreboard.hits += 1;
    spawnFloatingText(`+${target.plugin.points}`, target.position.x, target.position.y);
  }
});
```

🧠 *Warum das wichtig ist:* In Minecraft stellst du auch sicher, dass ein Button nicht mehrfach auslöst. Hier verhinderst du Mehrfach-Punkte pro Aufprall und kannst Effekte wie die leuchtenden Ziel-Chips triggern."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🌌 Matter.js Crashkurs
- **Bodies.circle(...)** – erzeugt runde Ziele oder Schneebälle. Mit `render.fillStyle` gibst du ihnen Farbe.
- **World.add(world, body)** – platziert deine Objekte wie Blöcke in die Welt.
- **Body.applyForce(...)** – hier pustet der Wind! Schon kleine Werte wie `0.00002` verändern die Flugbahn.
- **Body.setVelocity(...)** – startet den Flug. Hier kombinierst du Winkel + Power (Trigonometrie). Genau das wirst du gleich in TODO 3 üben!

👍 Tipp: Schau dir im Lösungsskript an, wie Gravitation (`engine.world.gravity.y = 1`) und feste Mauern (`isStatic: true`) für Grenzen sorgen."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """# 🧪 Verstehen & ausprobieren
Im Mini-Demo unten kannst du Winkel & Power verändern. Du siehst sofort, wie sich die Flugbahn und die berechnete Geschwindigkeit ändern. Probier verrückte Kombinationen!"""
        )
    )

    demo_html_source = """<!DOCTYPE html>
<html lang="de">
  <head>
    <style>
      body {
        font-family: "Orbitron", sans-serif;
        background: #020b16;
        color: #e0f2fe;
      }
      .demo-card {
        max-width: 640px;
        margin: 0 auto;
        padding: 18px 22px;
        border-radius: 18px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.9), rgba(4, 47, 46, 0.7));
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
      }
      .demo-grid {
        display: grid;
        gap: 12px;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        margin-bottom: 18px;
      }
      label {
        font-size: 0.75rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
      }
      input[type="range"] {
        width: 100%;
      }
      .demo-area {
        position: relative;
        height: 180px;
        border-radius: 14px;
        border: 1px dashed rgba(148, 163, 184, 0.5);
        background: radial-gradient(circle at top, rgba(15, 118, 110, 0.2), rgba(2, 6, 23, 0.9));
        overflow: hidden;
      }
      .demo-dot {
        position: absolute;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: #f8fafc;
        border: 2px solid #38bdf8;
        box-shadow: 0 0 18px rgba(56, 189, 248, 0.65);
        transform: translate(16px, 140px);
      }
      .info-line {
        font-size: 0.85rem;
        letter-spacing: 0.04em;
      }
    </style>
  </head>
  <body>
    <section class="demo-card">
      <h3>Mini-Schneeball-Demo</h3>
      <div class="demo-grid">
        <label>Winkel
          <input id="demo-angle" type="range" min="25" max="75" value="45" />
        </label>
        <label>Power
          <input id="demo-power" type="range" min="12" max="24" value="18" />
        </label>
      </div>
      <p class="info-line" id="demo-velocity">vx = 0 | vy = 0</p>
      <div class="demo-area">
        <div class="demo-dot" id="demo-dot"></div>
      </div>
    </section>

    <script>
      const angleInput = document.getElementById("demo-angle");
      const powerInput = document.getElementById("demo-power");
      const dot = document.getElementById("demo-dot");
      const info = document.getElementById("demo-velocity");
      let frameId;

      function toRad(value) {
        return (value * Math.PI) / 180;
      }

      function animate(angle, power) {
        cancelAnimationFrame(frameId);
        const start = performance.now();
        const areaHeight = 160;
        const scale = 7;
        function frame(now) {
          const t = (now - start) / 1000;
          const vx = Math.cos(angle) * power * scale;
          const vy = Math.sin(angle) * power * scale;
          const gravity = 9.81 * scale * 3;
          const x = Math.min(560, 20 + vx * t);
          const y = Math.min(areaHeight, areaHeight - (vy * t) + 0.5 * gravity * t * t);
          dot.style.transform = `translate(${x}px, ${y}px)`;
          if (y >= areaHeight) return;
          frameId = requestAnimationFrame(frame);
        }
        frameId = requestAnimationFrame(frame);
      }

      function update() {
        const angle = Number(angleInput.value);
        const power = Number(powerInput.value);
        const vx = (Math.cos(toRad(angle)) * power).toFixed(2);
        const vy = (Math.sin(toRad(angle)) * power).toFixed(2);
        info.textContent = `vx = ${vx}, vy = ${vy}`;
        animate(toRad(angle), power / 2);
      }

      angleInput.addEventListener("input", update);
      powerInput.addEventListener("input", update);
      update();
    </script>
  </body>
</html>"""
    safe_demo_html = demo_html_source.replace('"', '\\"')
    demo_html = f"""from IPython.core.display import HTML
HTML(\"\"\"{safe_demo_html}\"\"\")
"""

    cells.append(nbf.v4.new_code_cell(demo_html))

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🚀 Deine Aufgabe – bring Ordnung in die Schneeballschlacht
Im Ordner `Tag_21/Aufgabe/` wartet eine fast fertige Version auf dich. Dir fehlen nur noch **3 Schlüsselstellen**, um die gleiche Erfahrung wie in der Lösung zu bauen."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 📝 TODO 1 – HTML: Zielchips sichtbar machen
**Datei:** `Tag_21/Aufgabe/index.html` (unterhalb der Arena-Überschrift)

Dort findest du diesen Kommentar:
```html
<!-- TODO 1: Füge hier die drei Zielchips mit Namen & Punktwerten ein, damit Felix sofort sieht, welches Ziel wie viele Punkte bringt. -->
```
Ersetze ihn durch drei `<span>`-Elemente wie in der Lösung (`data-chip="ember"`, `data-chip="mint"`, `data-chip="aqua"`). Schreibe die passenden Punktwerte dazu, damit die Kinder sofort sehen, wofür sie zielen."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### 🎨 TODO 2 – CSS: Zielchips leuchten lassen
**Datei:** `Tag_21/Aufgabe/style.css`

Suche nach:
```css
/* TODO 2: Gestalte hier .target-chip und .target-chip--hit, damit die Zielchips wieder wie in der Lösung leuchten und Treffer anzeigen. */
```
Definiere dort wieder die Styles aus der Lösung:
- runde Badges mit Pixel-Glow
- Hover- oder Treffer-Effekte (`.target-chip--hit` erhält goldenen Rand)
- gleiche Schrift wie im Kontrollpanel

So lernen die Kinder sofort, welche Ziele aktiv reagiert haben."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """### ⚡ TODO 3 – JavaScript: Schneeball-Startgeschwindigkeit
**Datei:** `Tag_21/Aufgabe/script.js`

Im `launchSnowball()`-Block steht:
```javascript
const velocityScale = 0.55;
// TODO 3: Nutze Winkel & Power, um Body.setVelocity(...) aufzurufen. Du brauchst eine X- und eine Y-Komponente, damit der Schneeball wirklich fliegt.
Body.setAngularVelocity(snowball, 0.3);
```
Berechne hier wie in der Lösung zwei Komponenten:
- `Math.cos(angleRad) * power * velocityScale` für `x`
- `Math.sin(angleRad) * -power * velocityScale` für `y`

Nur dann verlassen die Schneebälle den Launcher und treffen die Ziele – genau wie in der echten Schneeballschlacht!"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🏆 Erfolgskontrolle
Nach allen TODOs solltest du sehen:
- ✅ Zielchips zeigen Punkte & blinken nach Treffern
- ✅ Combo-Balken füllt sich während der Game Loop
- ✅ Schneebälle fliegen in Bögen und lösen Treffer-Feeds aus
- ✅ Windanzeige, Uhrzeit und Trefferquote aktualisieren sich sauber"""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🌐 Teste deine Seite
- Aufgabe öffnen: <https://web.tb-cloudlab.org/2025_Adventskalender/Tag_21/Aufgabe/>
- Lösung vergleichen: <https://web.tb-cloudlab.org/2025_Adventskalender/Tag_21/Loesung/>
- Notebook-Datei liegt direkt unter `Tag_21/Lesson.ipynb` – alle Pfade in den Texten zeigen auf echte Dateien."""
        )
    )

    cells.append(
        nbf.v4.new_markdown_cell(
            """## 🌟 Level-Up-Ideen (ohne Spoiler)
- Lass getroffene Ziele für ein paar Sekunden rotieren
- Baue unterschiedliche Schwerkraft-Zonen (wie Slime-Blöcke)
- Ergänze Soundeffekte mit dem `<audio>`-Element
- Zeichne Flugbahnen mit Canvas oder SVG, um Physik sichtbar zu machen"""
        )
    )

    return cells


def create_lesson():
    nb = nbf.v4.new_notebook()
    nb["cells"] = build_cells()

    try:
        nbf.validate(nb)
    except nbf.ValidationError as error:  # pragma: no cover
        print(f"❌ Notebook-Validierung fehlgeschlagen: {error}")
        sys.exit(1)

    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    path = BASE_DIR / filename
    with path.open("w", encoding="utf-8") as handle:
        nbf.write(nb, handle)
    print(f"✅ Lesson erstellt: {path}")
    return path


def main():
    print("🎄 Erstelle Lesson.ipynb für Tag 21 ...")
    notebook = create_lesson()
    save_notebook(notebook)


if __name__ == "__main__":
    main()
