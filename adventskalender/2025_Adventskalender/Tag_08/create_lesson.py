#!/usr/bin/env python3
"""Erstellt das Lesson.ipynb für Tag 08."""

import nbformat as nbf
from pathlib import Path


def create_lesson():
    nb = nbf.v4.new_notebook()

    story_cell = nbf.v4.new_markdown_cell(
        """# 🎄 Tag 08 – Der Feuerwächter der Schneewildnis

Felix, mitten in der verschneiten Minecraft-Wildnis lodert ein Lagerfeuer, das allen Reisenden Hoffnung schenkt. Der Feuerwächter bittet dich: "Die Flammen brennen ungleichmäßig und der Schnee fällt kaum noch!" Deine Mission: Mit dem CSS-Boxmodell, leuchtenden Farbverläufen und Keyframe-Animationen bringst du das Feuer zurück ins Gleichgewicht.
"""
    )

    learning_cell = nbf.v4.new_markdown_cell(
        """## 📚 Lern-Kapitel – Baue ein lebendiges Lagerfeuer

### 🧱 Boxmodell verstehen
- **Content, Padding, Border, Margin** sind wie Block-Schichten. In `Loesung/index.html` sorgt der Container `.campfire-card` mit `padding: 2.5rem` dafür, dass das Feuer genügend Platz bekommt.
- `box-sizing: border-box;` (in `Loesung/style.css`) macht jede Breite berechenbar. Du addierst keine Padding-Werte mehr drauf – super für saubere Layouts.

### 🎨 Farben & Gradients
- Mit CSS-Variablen wie `--ember-light` oder `--sky-glow` (siehe `Loesung/style.css`) kannst du HSL-Werte zentral pflegen.
- Radial- und Linear-Gradients stapeln sich wie Biome: erst warme Glut, dann kalter Nachthimmel.

### 🔥 Keyframes & Timing
- Jede `.flame` besitzt eine eigene `@keyframes flicker` Animation. Unterschiedliche `animation-duration` Werte lassen die Flammen individuell tanzen.
- Transform-Funktionen (`rotate`, `scale`) nutzen eine CSS-Variable `--wind-angle`, die du mit JavaScript steuerst.

### 🧊 Schnee-Overlay
- Drei übereinanderliegende Radial-Gradients bilden die Flocken.
- Die Custom Property `--snow-speed` erlaubt, den Schneefall per Button zu pausieren.
"""
    )

    structure_cell = nbf.v4.new_markdown_cell(
        """## 🧪 Verstehen & Nachbauen

**So spielt alles zusammen:**
1. `Loesung/index.html` strukturiert den Inhalt in drei Abschnitte: Heldengeschichte, Campfire-Canvas und Wissens-Karten.
2. `Loesung/style.css` definiert Variablen und setzt das Boxmodell konsequent ein. Kommentare erklären einzelne Bereiche wie "Schnee Overlay".
3. `Loesung/script.js` reagiert auf Benutzeraktionen: Slider = Windrichtung, Button = Wärmelevel, Toggle = Schnee.

> Tipp: Öffne im Browser die DevTools, aktiviere das Boxmodell-Overlay und beobachte, wie sich Margin/Padding verändern, wenn du an den Werten drehst.
"""
    )

    demo_cell = nbf.v4.new_code_cell(
        '''from IPython.core.display import HTML

demo_html = """
<style>
  .demo-lab {
    font-family: \"Orbitron\", \"Trebuchet MS\", sans-serif;
    background: radial-gradient(circle at top, #0f4069, #050f1a);
    color: #e9f6ff;
    padding: 24px;
    border-radius: 22px;
    border: 2px solid rgba(255, 187, 122, 0.5);
    max-width: 620px;
    margin: 0 auto;
  }
  .demo-preview {
    position: relative;
    height: 200px;
    border-radius: 18px;
    border: 3px solid rgba(255, 174, 92, 0.7);
    background: linear-gradient(160deg, rgba(6, 67, 97, 0.9), rgba(3, 12, 25, 0.95));
    overflow: hidden;
    margin-bottom: 16px;
  }
  .demo-flame {
    position: absolute;
    left: 50%;
    bottom: 32px;
    width: 90px;
    height: 150px;
    border-radius: 60% 60% 45% 45%;
    background: radial-gradient(circle at 30% 20%, #ffd18d, #ff914d 55%, #d55c1f 90%);
    transform: translateX(-50%) rotate(var(--demo-angle, 0deg));
    animation: demo-flicker 2s ease-in-out infinite;
    box-shadow: 0 0 25px rgba(255, 145, 77, 0.8);
  }
  .demo-info {
    font-size: 0.9rem;
    line-height: 1.5;
    margin-bottom: 6px;
  }
  .demo-slider {
    width: 100%;
  }
  @keyframes demo-flicker {
    0% { transform: translateX(-50%) rotate(-4deg) scale(1); }
    50% { transform: translateX(-50%) rotate(4deg) scale(1.05); }
    100% { transform: translateX(-50%) rotate(0deg) scale(0.98); }
  }
</style>
<div class=\"demo-lab\">
  <div class=\"demo-preview\" id=\"demoFire\">
    <div class=\"demo-flame\"></div>
  </div>
  <p class=\"demo-info\"><strong>Ziehe den Slider:</strong> So kippt die Flamme über <code>transform: rotate()</code>.</p>
  <input type=\"range\" min=\"-12\" max=\"12\" value=\"0\" class=\"demo-slider\" id=\"demoSlider\" />
  <p class=\"demo-info\" id=\"demoText\">Windwinkel: 0° – neutrales Flackern.</p>
</div>
<script>
  const slider = document.getElementById('demoSlider');
  const preview = document.getElementById('demoFire');
  const text = document.getElementById('demoText');
  slider.addEventListener('input', (event) => {
    const value = Number(event.target.value);
    preview.style.setProperty('--demo-angle', value + 'deg');
    text.textContent = `Windwinkel: ${value}° – ${value === 0 ? 'ruhiges Feuer' : value > 0 ? 'Wind aus Westen' : 'Wind aus Osten'}.`;
  });
</script>
"""

HTML(demo_html)
'''
    )

    task_intro = nbf.v4.new_markdown_cell(
        """## 🚀 Deine Aufgabe – Drei TODOs bändigen
In `Tag_08/Aufgabe/` wartet bereits die fast fertige Version. Du vervollständigst genau drei Stellen, damit Schnee, Flammen und Wind wie in der Lösung zusammenspielen.
"""
    )

    todo1 = nbf.v4.new_markdown_cell(
        """### 📝 TODO 1 – HTML: Schnee-Overlay wieder einsetzen
**Datei:** `Aufgabe/index.html` (Bereich `.campfire-scene`)

- Suche den Kommentar `<!-- TODO 1: ... -->`.
- Füge direkt darunter wieder das `<div class="snow-layer" aria-hidden="true"></div>` ein.
- Dieses Element liegt über der Szene und sorgt dafür, dass das Boxmodell drei Ebenen stapelt: Himmel → Flamme → Schnee.

> Kontrolle: Wenn du in der Browser-Konsole `document.querySelector('.snow-layer')` eingibst, darf `null` **nicht** mehr zurückkommen.
"""
    )

    todo2 = nbf.v4.new_markdown_cell(
        """### 🎨 TODO 2 – CSS: Flammenanimation aktivieren
**Datei:** `Aufgabe/style.css` (Klasse `.flame`)

- Ersetze den Kommentar `/* TODO 2 ... */` durch `animation: flicker 1.8s ease-in-out infinite alternate;`.
- So nutzt jede Flamme wieder die bereits definierte `@keyframes flicker`-Sequenz.
- Beobachte anschließend, wie sich auch `.flame-secondary` und `.flame-triple` automatisch mit unterschiedlichen Geschwindigkeiten bewegen.
"""
    )

    todo3 = nbf.v4.new_markdown_cell(
        """### ⚡ TODO 3 – JavaScript: Wind-Slider anbinden
**Datei:** `Aufgabe/script.js` (Event-Listener auf `wind-slider`)

- Lies den Sliderwert mit `Number(event.target.value)` aus.
- Setze `document.documentElement.style.setProperty("--wind-angle", value + "deg")`.
- Aktualisiere `statusText.textContent`, z.B. "Der Wind pustet nach links" bei negativen Gradzahlen.

Damit steuerst du nicht nur den Text, sondern auch das CSS, weil `--wind-angle` direkt im `@keyframes flicker` genutzt wird.
"""
    )

    success_cell = nbf.v4.new_markdown_cell(
        """## 🏆 Erfolgskontrolle & Ausblick
- Öffne `https://web.tb-cloudlab.org/2025_Adventskalender/Tag_08/Aufgabe/` und vergleiche mit `.../Loesung/`.
- Drehe am Slider: Flammen kippen sofort.
- Klick auf "Holz nachlegen": Statusmeldungen wechseln zwischen drei Wärmeleveln.
- Schneeschalter pausiert die Animation sichtbar.

### 🌟 Was du jetzt kannst
- Du denkst in Boxmodell-Schichten wie beim Stapeln von Minecraft-Blöcken.
- Du nutzt HSL-Farbverläufe, um Atmosphäre zu steuern.
- Du verbindest CSS-Variablen mit JavaScript für echte Interaktivität.

### 🔭 Ideen zum Weiterbauen
1. Erweitere das Panel um einen Farb-Mischer für die Glut.
2. Gib jedem Funken (`.spark`) eine zufällige Flugbahn per JavaScript.
3. Lass den Schnee schneller werden, wenn der Slider extreme Werte erreicht.
"""
    )

    nb.cells.extend(
        [
            story_cell,
            learning_cell,
            structure_cell,
            demo_cell,
            task_intro,
            todo1,
            todo2,
            todo3,
            success_cell,
        ]
    )

    nbf.validate(nb)
    return nb


def save_notebook(nb, filename="Lesson.ipynb"):
    output_path = Path.cwd() / filename
    with open(output_path, "w", encoding="utf-8") as f:
        nbf.write(nb, f)
    return output_path


def main():
    print("🎄 Erstelle Lesson.ipynb für Tag 08...")
    nb = create_lesson()
    path = save_notebook(nb)
    print(f"✅ Fertig! Lesson gespeichert unter: {path}")


if __name__ == "__main__":
    main()
